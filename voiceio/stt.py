import threading
import numpy as np
import pyaudio
import noisereduce as nr
import webrtcvad
from faster_whisper import WhisperModel

class MicrophoneSTT:
    def __init__(self, sample_rate=16000, chunk_size=1024, model_size="medium", device="cpu"):
        self.sample_rate = sample_rate
        self.chunk_size = chunk_size
        self.model_size = model_size
        self.device = device
        self.channels = 1
        self.transcript = ""
        self._stop_event = threading.Event()
        self._thread = None
        self._init_audio()
        self._init_vad()
        self._init_asr()

    def _init_audio(self):
        self.p = pyaudio.PyAudio()
        device_index = self.p.get_default_input_device_info()['index']
        self.stream = self.p.open(
            format=pyaudio.paInt16,
            channels=self.channels,
            rate=self.sample_rate,
            input=True,
            input_device_index=device_index,
            frames_per_buffer=self.chunk_size
        )
        # Capture noise profile at initialization
        noise_data = self.stream.read(self.chunk_size, exception_on_overflow=False)
        self.noise_profile = np.frombuffer(noise_data, dtype=np.int16).astype(np.float32)

    def _init_vad(self):
        self.vad = webrtcvad.Vad(1)
        self.frame_duration = 30  # ms
        self.frame_size = int(self.sample_rate * self.frame_duration / 1000)

    def _init_asr(self):
        compute_type = "float16" if self.device == "cuda" else "int8"
        self.whisper_model = WhisperModel(self.model_size, device=self.device, compute_type=compute_type)

    def _is_speech(self, chunk):
        if len(chunk) < self.frame_size:
            return False
        num_frames = len(chunk) // self.frame_size
        for i in range(num_frames):
            frame = chunk[i*self.frame_size:(i+1)*self.frame_size]
            if self.vad.is_speech(frame.tobytes(), self.sample_rate):
                return True
        return False

    def _preprocess_audio(self, audio):
        if len(audio) > 0:
            max_val = np.max(np.abs(audio))
            if max_val > 0:
                audio = audio / max_val * 0.95
            # High-pass filter
            from scipy import signal
            b, a = signal.butter(4, 80/(self.sample_rate/2), btype='high')
            audio = signal.filtfilt(b, a, audio)
            if audio.dtype != np.float32:
                audio = audio.astype(np.float32)
        return audio

    def _capture_loop(self):
        buffer = []
        while not self._stop_event.is_set():
            data = self.stream.read(self.chunk_size, exception_on_overflow=False)
            chunk = np.frombuffer(data, dtype=np.int16)
            reduced_noise = nr.reduce_noise(
                y=chunk.astype(np.float32),
                sr=self.sample_rate,
                y_noise=self.noise_profile,
                stationary=False,
                n_fft=512,
                prop_decrease=1.0
            )
            reduced_noise_int16 = np.clip(reduced_noise, -32768, 32767).astype(np.int16)
            if self._is_speech(reduced_noise_int16):
                buffer.extend(reduced_noise_int16.tolist())
            elif buffer:
                # End of speech, process buffer
                audio = np.array(buffer, dtype=np.int16)
                processed_audio = self._preprocess_audio(audio)
                segments, info = self.whisper_model.transcribe(
                    processed_audio,
                    language="en",
                    beam_size=5,
                    best_of=5,
                    temperature=0.0,
                    condition_on_previous_text=True,
                    vad_filter=True,
                    vad_parameters=dict(
                        min_silence_duration_ms=300,
                        speech_pad_ms=100,
                        threshold=0.5
                    ),
                    word_timestamps=True,
                    compression_ratio_threshold=2.4,
                    log_prob_threshold=-1.0,
                    no_speech_threshold=0.7
                )
                results = [segment.text.strip() for segment in segments if segment.text.strip()]
                text = " ".join(results).strip()
                if text:
                    self.transcript = text
                buffer = []

    def start(self):
        self._stop_event.clear()
        self._thread = threading.Thread(target=self._capture_loop, daemon=True)
        self._thread.start()

    def stop(self):
        self._stop_event.set()
        if self._thread:
            self._thread.join(timeout=2)
        if hasattr(self, 'stream') and self.stream:
            self.stream.stop_stream()
            self.stream.close()
        if hasattr(self, 'p') and self.p:
            self.p.terminate()

    def get_transcript(self):
        return self.transcript 
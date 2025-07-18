from voiceio.stt import MicrophoneSTT
import time
from tools import get_tool_list
from rapidfuzz import process, fuzz

def fuzzy_correct_command(transcript, threshold=80):
    tool_list = get_tool_list()
    candidates = []
    for tool in tool_list:
        candidates.append(tool['name'].replace('_', ' '))
        if tool['description']:
            candidates.append(tool['description'])
    match, score, _ = process.extractOne(transcript, candidates, scorer=fuzz.token_sort_ratio)
    if score >= threshold:
        return match
    return transcript

def listen_for_command(model_size="tiny", device="cpu", silence_duration=0.7):
    """
    Listen for a voice command using the MicrophoneSTT class.
    Returns only after the speaker has stopped speaking for `silence_duration` seconds.
    """
    stt = MicrophoneSTT(model_size=model_size, device=device)
    stt.start()
    print("Please speak your command...")
    last_transcript = ""
    silence_counter = 0
    frame_duration = 0.03  # 30ms per frame (matches VAD frame)
    required_silence_frames = int(silence_duration / frame_duration)
    prev_transcript = ""
    while True:
        transcript = stt.get_transcript()
        if transcript and transcript != prev_transcript:
            silence_counter = 0  # Reset silence counter on new speech
            prev_transcript = transcript
        else:
            silence_counter += 1
        if prev_transcript and silence_counter >= required_silence_frames:
            break
        time.sleep(frame_duration)
    stt.stop()
    print(f"[Heard]: {prev_transcript}")
    corrected = fuzzy_correct_command(prev_transcript)
    if corrected != prev_transcript:
        print(f"[Corrected]: {corrected}")
    return corrected 
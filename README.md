# AI Voice Agent for Windows Control (Agentic, Voice-Driven)

## Features
- Voice commands to control Windows: open explorer, move/click/minimize/maximize/close/lock window, type text, control volume, clipboard, and more.
- Uses OpenAI Whisper for speech-to-text (STT).
- Uses pyttsx3 for text-to-speech (TTS) agent responses.
- Modular agentic architecture: tools are grouped by category for easy extension.
- GPT-based intent understanding: maps your request to the right tool and arguments.

## Project Structure
```
project_root/
├── agentic_core/
│   ├── agent.py
│   └── __init__.py
├── tools/
│   ├── app_tools.py
│   ├── keyboard_tools.py
│   ├── media_tools.py
│   ├── window_tools.py
│   └── __init__.py
├── voiceio/
│   ├── voice_input.py
│   ├── voice_output.py
│   └── __init__.py
├── llm_tool_selector.py
├── main.py
├── requirements.txt
├── README.md
```

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Add your OpenAI API key to a `.env` file:
   ```
   OPENAI_API_KEY=sk-...
   ```

## Usage
Run the agent:
```bash
python main.py
```

## How to Add New Tools
- Add a new function decorated with `@function_tool` in the appropriate file in `tools/`.
- The agent will auto-discover and use it.

## Notes
- Requires Python 3.8+
- Run as administrator for full OS control. 
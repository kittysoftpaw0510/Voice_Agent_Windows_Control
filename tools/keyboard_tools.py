from agentic_core.agent import function_tool
import pyautogui

@function_tool
def keyboard_down() -> str:
    """Press the keyboard down arrow key."""
    pyautogui.press('down')
    return "Pressed the down arrow key."

@function_tool
def copy() -> str:
    """Copy selected text (Ctrl+C)."""
    pyautogui.hotkey('ctrl', 'c')
    return "Copied selected text."

@function_tool
def paste() -> str:
    """Paste clipboard contents (Ctrl+V)."""
    pyautogui.hotkey('ctrl', 'v')
    return "Pasted clipboard contents."

@function_tool
def type_text(text: str) -> str:
    """Type the given text using the keyboard."""
    pyautogui.write(text)
    return f"Typed: {text}" 
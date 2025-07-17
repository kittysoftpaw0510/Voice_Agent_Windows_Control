from agentic_core.agent import function_tool
import pyautogui

@function_tool
def keyboard_down() -> str:
    """
    Press the keyboard down arrow key.
    
    Input: None
    Output: str - Confirmation message that the down arrow key was pressed.
    """
    pyautogui.press('down')
    return "Pressed the down arrow key."

@function_tool
def copy() -> str:
    """
    Copy selected text (Ctrl+C).
    
    Input: None
    Output: str - Confirmation message that the text was copied.
    """
    pyautogui.hotkey('ctrl', 'c')
    return "Copied selected text."

@function_tool
def paste() -> str:
    """
    Paste clipboard contents (Ctrl+V).
    
    Input: None
    Output: str - Confirmation message that the clipboard contents were pasted.
    """
    pyautogui.hotkey('ctrl', 'v')
    return "Pasted clipboard contents."

@function_tool
def type_text(text: str) -> str:
    """
    Type the given text using the keyboard.
    
    Input:
        text (str): The text to type.
    Output: str - Confirmation message showing the typed text.
    """
    pyautogui.write(text)
    return f"Typed: {text}" 
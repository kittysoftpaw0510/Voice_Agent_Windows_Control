from agentic_core.agent import function_tool
import pyautogui
pyautogui.FAILSAFE = False

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

@function_tool
def keyboard_up() -> str:
    """
    Press the keyboard up arrow key.
    Input: None
    Output: str - Confirmation message that the up arrow key was pressed.
    """
    pyautogui.press('up')
    return "Pressed the up arrow key."

@function_tool
def keyboard_left() -> str:
    """
    Press the keyboard left arrow key.
    Input: None
    Output: str - Confirmation message that the left arrow key was pressed.
    """
    pyautogui.press('left')
    return "Pressed the left arrow key."

@function_tool
def keyboard_right() -> str:
    """
    Press the keyboard right arrow key.
    Input: None
    Output: str - Confirmation message that the right arrow key was pressed.
    """
    pyautogui.press('right')
    return "Pressed the right arrow key."

@function_tool
def enter() -> str:
    """
    Press the Enter key.
    Input: None
    Output: str - Confirmation message that the Enter key was pressed.
    """
    pyautogui.press('enter')
    return "Pressed the Enter key."

@function_tool
def escape() -> str:
    """
    Press the Escape key.
    Input: None
    Output: str - Confirmation message that the Escape key was pressed.
    """
    pyautogui.press('esc')
    return "Pressed the Escape key."

@function_tool
def tab() -> str:
    """
    Press the Tab key.
    Input: None
    Output: str - Confirmation message that the Tab key was pressed.
    """
    pyautogui.press('tab')
    return "Pressed the Tab key."

@function_tool
def backspace() -> str:
    """
    Press the Backspace key.
    Input: None
    Output: str - Confirmation message that the Backspace key was pressed.
    """
    pyautogui.press('backspace')
    return "Pressed the Backspace key."

@function_tool
def delete() -> str:
    """
    Press the Delete key.
    Input: None
    Output: str - Confirmation message that the Delete key was pressed.
    """
    pyautogui.press('delete')
    return "Pressed the Delete key."

@function_tool
def home() -> str:
    """
    Press the Home key.
    Input: None
    Output: str - Confirmation message that the Home key was pressed.
    """
    pyautogui.press('home')
    return "Pressed the Home key."

@function_tool
def end() -> str:
    """
    Press the End key.
    Input: None
    Output: str - Confirmation message that the End key was pressed.
    """
    pyautogui.press('end')
    return "Pressed the End key."

@function_tool
def page_up() -> str:
    """
    Press the Page Up key.
    Input: None
    Output: str - Confirmation message that the Page Up key was pressed.
    """
    pyautogui.press('pageup')
    return "Pressed the Page Up key."

@function_tool
def page_down() -> str:
    """
    Press the Page Down key.
    Input: None
    Output: str - Confirmation message that the Page Down key was pressed.
    """
    pyautogui.press('pagedown')
    return "Pressed the Page Down key."

@function_tool
def select_all() -> str:
    """
    Select all text (Ctrl+A).
    Input: None
    Output: str - Confirmation message that all text was selected.
    """
    pyautogui.hotkey('ctrl', 'a')
    return "Selected all text."

@function_tool
def cut() -> str:
    """
    Cut selected text (Ctrl+X).
    Input: None
    Output: str - Confirmation message that the text was cut.
    """
    pyautogui.hotkey('ctrl', 'x')
    return "Cut selected text."

@function_tool
def undo() -> str:
    """
    Undo the last action (Ctrl+Z).
    Input: None
    Output: str - Confirmation message that the last action was undone.
    """
    pyautogui.hotkey('ctrl', 'z')
    return "Undid the last action."

@function_tool
def redo() -> str:
    """
    Redo the last undone action (Ctrl+Y).
    Input: None
    Output: str - Confirmation message that the last undone action was redone.
    """
    pyautogui.hotkey('ctrl', 'y')
    return "Redid the last undone action."

@function_tool
def screenshot_key() -> str:
    """
    Press the Print Screen key to take a screenshot.
    Input: None
    Output: str - Confirmation message that the Print Screen key was pressed.
    """
    pyautogui.press('printscreen')
    return "Pressed the Print Screen key." 
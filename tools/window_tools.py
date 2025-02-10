from agentic_core.agent import function_tool
import pyautogui
import ctypes
import os
from datetime import datetime

@function_tool
def close_window() -> str:
    """Close the current window (Alt+F4)."""
    pyautogui.hotkey('alt', 'f4')
    return "Closed the current window."

@function_tool
def minimize_window() -> str:
    """Minimize the current window (Win+Down)."""
    pyautogui.hotkey('win', 'down')
    return "Minimized the current window."

@function_tool
def maximize_window() -> str:
    """Maximize the current window (Win+Up)."""
    pyautogui.hotkey('win', 'up')
    return "Maximized the current window."

@function_tool
def lock_screen() -> str:
    """Lock the screen (Win+L)."""
    ctypes.windll.user32.LockWorkStation()
    return "Screen locked."

@function_tool
def screenshot() -> str:
    """Take a screenshot and save to the desktop."""
    desktop = os.path.join(os.path.expanduser('~'), 'Desktop')
    filename = f"screenshot_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    path = os.path.join(desktop, filename)
    pyautogui.screenshot(path)
    return f"Screenshot saved to {path}"

@function_tool
def open_task_manager() -> str:
    """Open Task Manager (Ctrl+Shift+Esc)."""
    pyautogui.hotkey('ctrl', 'shift', 'esc')
    return "Opened Task Manager." 
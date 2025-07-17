from agentic_core.agent import function_tool
import pyautogui

@function_tool
def volume_up() -> str:
    """
    Increase the system volume.
    
    Input: None
    Output: str - Confirmation message that the volume was increased.
    """
    pyautogui.press('volumeup')
    return "Increased the system volume."

@function_tool
def volume_down() -> str:
    """
    Decrease the system volume.
    
    Input: None
    Output: str - Confirmation message that the volume was decreased.
    """
    pyautogui.press('volumedown')
    return "Decreased the system volume."

@function_tool
def mute_unmute_volume() -> str:
    """
    Mute or unmute the system volume.
    
    Input: None
    Output: str - Confirmation message that the mute/unmute action was toggled.
    """
    pyautogui.press('volumemute')
    return "Toggled mute/unmute for system volume." 
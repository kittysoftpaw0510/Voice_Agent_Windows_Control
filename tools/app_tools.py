from agentic_core.agent import function_tool
import webbrowser
import os

@function_tool
def open_browser() -> str:
    """
    Open the default web browser.
    
    Input: None
    Output: str - Confirmation message that the browser was opened.
    """
    webbrowser.open('http://www.google.com')
    return "Opened the default web browser."

@function_tool
def open_calculator() -> str:
    """
    Open the calculator application.
    
    Input: None
    Output: str - Confirmation message that the calculator was opened.
    """
    os.system('start calc')
    return "Opened Calculator." 

@function_tool
def open_explorer() -> str:
    """
    Open Windows File Explorer.
    
    Input: None
    Output: str - Confirmation message that File Explorer was opened.
    """
    os.system('start explorer')
    return "Opened Windows File Explorer."

@function_tool
def open_control_panel() -> str:
    """
    Open the Windows Control Panel.
    
    Input: None
    Output: str - Confirmation message that the Control Panel was opened.
    """
    os.system('start control')
    return "Opened Windows Control Panel." 

@function_tool
def open_settings() -> str:
    """
    Open the Windows Settings app.
    Input: None
    Output: str - Confirmation message that Settings was opened.
    """
    os.system('start ms-settings:')
    return "Opened Windows Settings."

@function_tool
def open_device_manager() -> str:
    """
    Open the Windows Device Manager.
    Input: None
    Output: str - Confirmation message that Device Manager was opened.
    """
    os.system('start devmgmt.msc')
    return "Opened Device Manager."

@function_tool
def open_network_connections() -> str:
    """
    Open the Network Connections window.
    Input: None
    Output: str - Confirmation message that Network Connections was opened.
    """
    os.system('start ncpa.cpl')
    return "Opened Network Connections."

@function_tool
def open_command_prompt() -> str:
    """
    Open the Command Prompt.
    Input: None
    Output: str - Confirmation message that Command Prompt was opened.
    """
    os.system('start cmd')
    return "Opened Command Prompt."

@function_tool
def open_powershell() -> str:
    """
    Open Windows PowerShell.
    Input: None
    Output: str - Confirmation message that PowerShell was opened.
    """
    os.system('start powershell')
    return "Opened PowerShell."

@function_tool
def open_task_scheduler() -> str:
    """
    Open the Windows Task Scheduler.
    Input: None
    Output: str - Confirmation message that Task Scheduler was opened.
    """
    os.system('start taskschd.msc')
    return "Opened Task Scheduler."

@function_tool
def open_windows_update() -> str:
    """
    Open the Windows Update settings.
    Input: None
    Output: str - Confirmation message that Windows Update was opened.
    """
    os.system('start ms-settings:windowsupdate')
    return "Opened Windows Update settings."

@function_tool
def open_system_information() -> str:
    """
    Open the System Information window.
    Input: None
    Output: str - Confirmation message that System Information was opened.
    """
    os.system('start msinfo32')
    return "Opened System Information." 
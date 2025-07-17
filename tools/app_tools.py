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
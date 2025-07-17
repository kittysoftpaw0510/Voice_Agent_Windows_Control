import os
import importlib
import inspect

tool_modules = []
for filename in os.listdir(os.path.dirname(__file__)):
    if filename.endswith('.py') and filename not in ('__init__.py',):
        module_name = f"{__name__}.{filename[:-3]}"
        module = importlib.import_module(module_name)
        tool_modules.append(module)

def get_tool_list():
    tool_list = []
    for module in tool_modules:
        for name, obj in inspect.getmembers(module):
            if callable(obj) and getattr(obj, '_is_tool', False):
                tool_list.append({
                    'name': name,
                    'description': obj.__doc__ or ''
                })
    return tool_list

# Function to generate a prompt string listing all tools

def get_tools_prompt():
    tool_list = get_tool_list()
    prompt = "Available tools:\n"
    for tool in tool_list:
        prompt += f"- {tool['name']}: {tool['description']}\n"
    return prompt 
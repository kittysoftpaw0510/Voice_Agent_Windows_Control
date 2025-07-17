import inspect
from typing import Callable, List, Dict, Any

def function_tool(func):
    func._is_tool = True
    return func

class Tool:
    def __init__(self, func: Callable):
        self.func = func
        self.name = func.__name__
        self.description = func.__doc__ or ""

    def call(self, **kwargs):
        sig = inspect.signature(self.func)
        params = {k: v for k, v in kwargs.items() if k in sig.parameters}
        return self.func(**params)

class Agent:
    def __init__(self, name: str, instructions: str, tools: List[Callable]):
        self.name = name
        self.instructions = instructions
        self.tools = [Tool(t) for t in tools if getattr(t, "_is_tool", False)]
        self.tool_map = {t.name: t for t in self.tools}

    def find_tool(self, user_input: str):
        for tool in self.tools:
            if tool.name.replace("_", " ") in user_input.lower():
                return tool
        return None

    def run(self, user_input: str):
        tool = self.find_tool(user_input)
        if not tool:
            return "Sorry, I don't know how to do that."
        args = {}
        for param in inspect.signature(tool.func).parameters:
            if param == "self":
                continue
            import re
            match = re.search(rf"{param} ([\w\d]+|\"[^\"]+\")", user_input)
            if match:
                value = match.group(1)
                if value.isdigit():
                    value = int(value)
                elif value.startswith('"') and value.endswith('"'):
                    value = value[1:-1]
                args[param] = value
        return tool.call(**args)

class Runner:
    @staticmethod
    def run_streamed(agent: Agent, input: List[Dict[str, Any]]):
        class DummyStream:
            async def stream_events(self):
                user_input = input[-1]["content"]
                result = agent.run(user_input)
                yield type("Event", (), {"type": "raw_response_event", "data": type("Data", (), {"delta": result})})()
        return DummyStream() 
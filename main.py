import asyncio
from agentic_core.agent import Agent, Runner
from voiceio.voice_input import listen_for_command
from voiceio.voice_output import speak
import tools  # auto-imports all tool modules and registers them
from llm_tool_selector import gpt_select_tool

# Collect all function_tool-decorated functions from tool modules
def get_all_tools():
    all_tools = []
    for module in tools.tool_modules:
        for attr in dir(module):
            obj = getattr(module, attr)
            if callable(obj) and getattr(obj, '_is_tool', False):
                all_tools.append(obj)
    return all_tools

instructions = "You help users control their Windows computer by voice commands."

def main():
    agent = Agent(
        name="Windows Voice Agent",
        instructions=instructions,
        tools=get_all_tools(),
    )
    print("=== Windows Voice Agent ===")
    print("Say 'exit' to quit.")
    input_items = []

    async def agent_loop():
        while True:
            user_input = listen_for_command()
            input_items.append({"content": user_input, "role": "user"})

            if user_input.lower() in ['exit', 'quit', 'bye']:
                speak("Goodbye!")
                break

            if not user_input:
                continue

            tool_name, args = gpt_select_tool(user_input)
            if tool_name and tool_name in agent.tool_map:
                result = agent.tool_map[tool_name].call(**args)
                speak(result)
            else:
                speak("Sorry, I couldn't understand your request.")
            print("\n")

    asyncio.run(agent_loop())

if __name__ == "__main__":
    main() 
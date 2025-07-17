import openai
import os
import json
from dotenv import load_dotenv
from tools import get_tool_list, get_tools_prompt

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Dynamically get tool names
# TOOL_LIST = [tool['name'] for tool in get_tool_list()]

def gpt_select_tool(user_text):
    prompt = f"""
You are an assistant that maps user requests to tool calls.
{get_tools_prompt()}
Given a user request, output a JSON object with:
- tool: the name of the tool to call
- args: a dictionary of arguments for the tool

User request: "{user_text}"
Output:
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=0
    )
    text = response.choices[0].message.content
    try:
        result = json.loads(text)
        return result['tool'], result.get('args', {})
    except Exception as e:
        print("Failed to parse GPT response:", text)
        return None, {} 
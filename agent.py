from LLm import chat
from memory import load_memory, save_memory
from prompts import SYSTEM_PROMPT
from parser import parse_tool_call
from tools import run_tool

class Agent:
    def run(self, user_input: str) -> str:
        memory = load_memory() or []
        messages = [{"role": "system", "content": SYSTEM_PROMPT}]
        messages.extend(memory[-10:])
        messages.append({"role": "user", "content": user_input})

        llm_response = chat(messages)
        if not llm_response:
            return "Sorry, I could not generate a response."

        tool_request = parse_tool_call(llm_response)

        if tool_request is None:
            memory.append({"role": "user", "content": user_input})
            memory.append({"role": "assistant", "content": llm_response})
            save_memory(memory)
            return llm_response

        tool_result = run_tool(tool_request)

        messages.append({"role": "assistant", "content": llm_response})
        messages.append({
            "role": "user",
            "content": f"Tool Result: {tool_result}\n\nAnswer the user using this result. Do not call another tool."
        })

        final_response = chat(messages)
        if not final_response:
            final_response = tool_result

        memory.append({"role": "user", "content": user_input})
        memory.append({"role": "assistant", "content": final_response})
        save_memory(memory)
        return final_response

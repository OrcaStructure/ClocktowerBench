import os
from openai import OpenAI
import json
import asyncio
LLM_NAME = "gpt-4o-mini"
client = OpenAI(
    api_key=os.environ.get("OPENAI_KEY"),
)

def assemble_context (stm, ltm, instructions):
    '''Returns context for llm'''

    return f"Here are your long-term memories from earlier in the game: \n {ltm} \n Here is what has happened so far in this phase of the day: \n {stm} \n The next action you to take is {instructions}." 



def invoke_llm(player, instructions, tools):
    '''Returns '''
    s_p = player["system_prompt"]
    stm,ltm = player["short_term_memory"], player["long_term_memory"]

    prompt = assemble_context(stm,ltm,instructions)
    return send_llm_request(s_p,prompt,tools)

async def invoke_llm_wrapper(player, instructions, tools):
    invoke_llm(player,instructions,tools)


def send_llm_request(system_prompt,prompt, tools):

    '''Returns response args'''

    response = client.responses.create(
    model=LLM_NAME,
    input=[{"role": "user", "content": prompt,
            "role": "system", "content": system_prompt          
            }],
    tools=tools
    )

    tool_call = response.output[0]
    args = json.loads(tool_call.arguments)
    name = tool_call.name
    return name, args
    

async def batch_llm_calls(players,instructions_list,tools):
    tasks = []

    for player, instruction in zip(players, instructions_list):
        # Prepare coroutine but do NOT await yet
        tasks.append(invoke_llm_wrapper(player, instruction, tools))

    # Run all concurrently
    results = await asyncio.gather(*tasks)
    return results
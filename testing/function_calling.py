import os
from openai import OpenAI
import json

client = OpenAI(
    api_key=os.environ.get("OPENAI_KEY"),
)

#Example function calling from open ai api reference

tools = [{
    "type": "function",
    "name": "get_weather",
    "description": "Get current temperature for a given location.",
    "parameters": {
        "type": "object",
        "properties": {
            "location": {
                "type": "string",
                "description": "City and country e.g. Bogotá, Colombia"
            }
        },
        "required": [
            "location"
        ],
        "additionalProperties": False
    }
}]

# Main tools for the storyteller llm 
storyteller_tools = [
    {
        "type": "function",
        "name": "assign_role",
        "description": "Give a player their starting role.",
        "parameters": {
            "type": "object",
            "properties": {
                "player_id": {
                    "type": "string",
                    "description": "Unique identifier for the player (e.g. 'player3')."
                },
                "role": {
                    "type": "string",
                    "description": "Exact role name as defined in the chosen script (e.g. 'Washerwoman')."
                }
            },
            "required": ["player_id", "role"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "change_phase",
        "description": "Set the global game phase to 'day' or 'night'.",
        "parameters": {
            "type": "object",
            "properties": {
                "phase": {
                    "type": "string",
                    "enum": ["day", "night"],
                    "description": "Which phase the game is entering."
                },
                "day_number": {
                    "type": "integer",
                    "minimum": 1,
                    "description": "Current day count (increment on each sunrise); ignored for 'night'."
                }
            },
            "required": ["phase"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "nominate_player",
        "description": "Record a player’s nomination of another player during the day.",
        "parameters": {
            "type": "object",
            "properties": {
                "nominator_id": {
                    "type": "string",
                    "description": "ID of the player making the nomination."
                },
                "nominee_id": {
                    "type": "string",
                    "description": "ID of the player being nominated."
                }
            },
            "required": ["nominator_id", "nominee_id"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "cast_vote",
        "description": "Register an individual vote on the current nomination.",
        "parameters": {
            "type": "object",
            "properties": {
                "player_id": {
                    "type": "string",
                    "description": "ID of the voting player."
                },
                "vote": {
                    "type": "boolean",
                    "description": "True for a raised hand (✔), False for no vote (✘)."
                }
            },
            "required": ["player_id", "vote"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "resolve_execution",
        "description": "Execute (or not) the nominee once all votes are in.",
        "parameters": {
            "type": "object",
            "properties": {
                "executed": {
                    "type": "boolean",
                    "description": "True if the votes reached the threshold; False otherwise."
                },
                "nominee_id": {
                    "type": "string",
                    "description": "ID of the nominated player (redundant safety check)."
                }
            },
            "required": ["executed", "nominee_id"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "use_night_ability",
        "description": "Apply a character’s night-time ability and store any resulting info.",
        "parameters": {
            "type": "object",
            "properties": {
                "actor_id": {
                    "type": "string",
                    "description": "Player whose ability is firing."
                },
                "targets": {
                    "type": "array",
                    "items": { "type": "string" },
                    "description": "List of player IDs targeted (empty array if none)."
                },
                "notes": {
                    "type": "string",
                    "description": "Free-form text for the Storyteller to record what happened or what was learnt."
                }
            },
            "required": ["actor_id", "targets"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "alter_player_status",
        "description": "Change a player’s alive/dead or poisoned/drunk status.",
        "parameters": {
            "type": "object",
            "properties": {
                "player_id": {
                    "type": "string",
                    "description": "ID of the affected player. e.g. player1"
                },
                "alive": {
                    "type": "boolean",
                    "description": "True if the player is alive after the change."
                },
                "poisoned": {
                    "type": "boolean",
                    "description": "True if the player is now poisoned/drunk, False if cleared."
                },
                "cause": {
                    "type": "string",
                    "description": "Short reason (e.g. 'Imp attack', 'Execution', 'Poison cleared by Monk')."
                }
            },
            "required": ["player_id"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "send_private_info",
        "description": "Deliver confidential information to a single player (e.g. starting info, night results).",
        "parameters": {
            "type": "object",
            "properties": {
                "recipient_id": {
                    "type": "string",
                    "description": "Player receiving the message."
                },
                "message": {
                    "type": "string",
                    "description": "Exact text to send."
                }
            },
            "required": ["recipient_id", "message"],
            "additionalProperties": False
        }
    }
    ]

# some tools for the player llms

player_tools = [
    {
        "type": "function",
        "name": "send_message",
        "description": "During the day phase, send a message to another character",
        "parameters": {
            "type": "object",
            "properties": {
                "player_id": {
                    "type": "string",
                    "description": "Another player's id. e.g. player3"
                },
                "content": {
                    "type": "string",
                    "description": "Content of the message."
                }
            },
            "required": [
                "player_id", "content"
            ],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "use_declarative_ability",
        "description": "During townhall, use a declarative ability. You don't need to necessarily have the declarative ability",
        "parameters": {
            "type": "object",
            "properties": {
                "claimed_role": {
                    "type": "string",
                    "description": "The role that the player is claiming."
                },
                "targets": {
                    "type": "dict",
                    "description": "A dictionary containing the target's player ids as keys, and their corresponding information as values. The value should be empty if there is no corresponding information to the ability (e.g. in the case of a slayer.)"
                },
                "statement" : {
                    "type": "string",
                    "description": "A string that contains the statement the player would like to use when claiming. E.g. the Gossip can 'gossip' that the Demon is a 'Fang Gu'. "
                }
            },
            "required": [
                "claimed_role"
            ],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "nominate player message",
        "description": "During townhall, nominate a player",
        "parameters": {
            "type": "object",
            "properties": {
                "player_id": {
                    "type": "string",
                    "description": "Another player's id. e.g. player3"
                }
            },
            "required": [
                "player_id"
            ],
            "additionalProperties": False
        }
    },

]

# Summariser tools for the llm

summary_tools = [
    {
        "type": "function",
        "name": "story_teller_summariser",
        "description": "Summarise the events of the last night for the story teller. Emphasise any major events and key interactions that are occuring between the players",
        "parameters": {
            "type": "object",
            "properties": {
                "summary": {
                    "type": "string",
                    "description": "The new summary that will represent the short term memory of the storyteller ."
                }
            },
            "required": ["summary"],
            "additionalProperties": False
        }
    },
    {
        "type": "function",
        "name": "player_summariser",
        "description": "Summarise the events of the last night for a player. Emphasise any major events as well as the main players this player has interacted with. Also highlight if any role or alignment changes have occured.",
        "parameters": {
            "type": "object",
            "properties": {
                "summary": {
                    "type": "string",
                    "description": "The new summary that will represent the short term memory of the player ."
                },
                "alignment": {
                    "type": "string",
                    "description": "The current alignment of the player. Either \"good\" or \"evil\"."
                },
                "role": {
                    "tyoe": "string",
                    "description": "The current player's role. E.g. Fortune Teller."
                }
            },
            "required": ["summary", "alignment"],
            "additionalProperties": False
        }
    }
]

#protocal for processing the function call
response = client.responses.create(
    model="gpt-4.1",
    input=[{"role": "user", "content": "What is the weather like in Paris today?"}],
    tools=tools
)

tool_call = response.output[0]

args = json.loads(tool_call.arguments)

print(args)
print(response.output)

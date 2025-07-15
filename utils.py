import os

# dictionaries
role_map = {
    # Townsfolk
    'washerwoman': 'Townsfolk', 'librarian': 'Townsfolk', 'investigator': 'Townsfolk',
    'chef': 'Townsfolk', 'empath': 'Townsfolk', 'fortune teller': 'Townsfolk',
    'undertaker': 'Townsfolk', 'monk': 'Townsfolk', 'ravenkeeper': 'Townsfolk',
    'virgin': 'Townsfolk', 'slayer': 'Townsfolk', 'soldier': 'Townsfolk', 'mayor': 'Townsfolk',
    'amnesiac': 'Townsfolk', 'artist': 'Townsfolk', 'atheist': 'Townsfolk', 'cannibal': 'Townsfolk',
    'chambermaid': 'Townsfolk', 'clockmaker': 'Townsfolk', 'courtier': 'Townsfolk', 'cult leader': 'Townsfolk',
    'dreamer': 'Townsfolk', 'exorcist': 'Townsfolk', 'farmer': 'Townsfolk', 'fisherman': 'Townsfolk',
    'flowergirl': 'Townsfolk', 'gambler': 'Townsfolk', 'general': 'Townsfolk', 'gossip': 'Townsfolk',
    'grandmother': 'Townsfolk', 'high priestess': 'Townsfolk', 'huntsman': 'Townsfolk',
    'innkeeper': 'Townsfolk', 'juggler': 'Townsfolk', 'king': 'Townsfolk', 'knight': 'Townsfolk',
    'magician': 'Townsfolk', 'mathematician': 'Townsfolk', 'minstrel': 'Townsfolk',
    'nightwatchman': 'Townsfolk', 'noble': 'Townsfolk', 'oracle': 'Townsfolk', 'pacifist': 'Townsfolk',
    'philosopher': 'Townsfolk', 'pixie': 'Townsfolk', 'poppy grower': 'Townsfolk', 'preacher': 'Townsfolk',
    'professor': 'Townsfolk', 'sage': 'Townsfolk', 'sailor': 'Townsfolk', 'savant': 'Townsfolk',
    'seamstress': 'Townsfolk', 'shugenja': 'Townsfolk', 'snake charmer': 'Townsfolk', 'steward': 'Townsfolk',
    'tea lady': 'Townsfolk', 'town crier': 'Townsfolk', 'village idiot': 'Townsfolk',
    'alchemist': 'Townsfolk', 'alsaahir': 'Townsfolk', 'balloonist': 'Townsfolk', 'banshee': 'Townsfolk',
    'bounty hunter': 'Townsfolk', 'choirboy': 'Townsfolk', 'engineer': 'Townsfolk',
    'lycanthrope': 'Townsfolk',

    # Outsiders
    'butler': 'Outsider', 'drunk': 'Outsider', 'recluse': 'Outsider', 'saint': 'Outsider',
    'acrobat': 'Outsider', 'barber': 'Outsider', 'damsel': 'Outsider', 'golem': 'Outsider',
    'goon': 'Outsider', 'hatter': 'Outsider', 'heretic': 'Outsider', 'klutz': 'Outsider',
    'moonchild': 'Outsider', 'mutant': 'Outsider', 'plague doctor': 'Outsider',
    'politician': 'Outsider', 'puzzlemaster': 'Outsider', 'snitch': 'Outsider',
    'sweetheart': 'Outsider', 'tinker': 'Outsider', 'zealot': 'Outsider', 'ogre': 'Outsider',
    'lunatic': 'Outsider',

    # Minions
    'poisoner': 'Minion', 'spy': 'Minion', 'scarlet woman': 'Minion', 'baron': 'Minion',
    'assassin': 'Minion', 'boomdandy': 'Minion', 'cerenovus': 'Minion', "devil's advocate": 'Minion',
    'evil twin': 'Minion', 'fearmonger': 'Minion', 'goblin': 'Minion', 'godfather': 'Minion',
    'harpy': 'Minion', 'marionette': 'Minion', 'mastermind': 'Minion', 'mezepheles': 'Minion',
    'organ grinder': 'Minion', 'pit hag': 'Minion', 'psychopath': 'Minion', 'summoner': 'Minion',
    'vizier': 'Minion', 'widow': 'Minion', 'witch': 'Minion', 'boffin': 'Minion', 'wizard': 'Minion',
    'xaan': 'Minion',

    # Demons
    'imp': 'Demon', 'fang gu': 'Demon', 'legion': 'Demon', 'leviathan': 'Demon', "lil' monsta": 'Demon',
    'lleech': 'Demon', 'no dashii': 'Demon', 'po': 'Demon', 'pukka': 'Demon', 'riot': 'Demon',
    'shabaloth': 'Demon', 'vortox': 'Demon', 'zombuul': 'Demon', 'al-hadikhia': 'Demon',
    'kazali': 'Demon', 'lord of typhon': 'Demon', 'ojo': 'Demon', 'yaggababble': 'Demon', 
    'vigormortis': 'Demon',
    }

role_ability = {
    "Washerwoman": "You start knowing that 1 of 2 players is a particular Townsfolk.",
    "Librarian": "You start knowing that 1 of 2 players is a particular Outsider. (Or that zero are in play.)",
    "Investigator": "You start knowing that 1 of 2 players is a particular Minion.",
    "Chef": "You start knowing how many pairs of evil players there are.",
    "Empath": "Each night, you learn how many of your 2 alive neighbours are evil.",
    "Fortune Teller": "Each night, choose 2 players: you learn if either is a Demon. There is a good player that registers as a Demon to you.",
    "Undertaker": "Each night, (except the first) you learn which character died by execution today.",
    "Monk": "Each night, (except the first) choose a player (not yourself): they are safe from the Demon tonight.",
    "Ravenkeeper": "If you die at night, you are woken to choose a player: you learn their character.",
    "Virgin": "The 1st time you are nominated, if the nominator is a Townsfolk, they are executed immediately.",
    "Slayer": "Once per game, during the day, publicly choose a player: if they are the Demon, they die.",
    "Soldier": "You are safe from the Demon.",
    "Mayor": "If only 3 players live & no execution occurs, your team wins. If you die at night, another player might die instead.",
    "Butler": "Each night, choose a player (not yourself): tomorrow, you may only vote if they are voting too.",
    "Drunk": "You do not know you are the Drunk. You think you are a Townsfolk character, but you are not.",
    "Recluse": "You might register as evil & as a Minion or Demon, even if dead.",
    "Saint": "If you die by execution, your team loses.",
    "Poisoner": "Each night, choose a player: they are poisoned tonight and tomorrow day.",
    "Spy": "Each night, you see the Grimoire. You might register as good & as a Townsfolk or Outsider, even if dead.",
    "Scarlet Woman": "If there are 5 or more players alive (Travellers don’t count) & the Demon dies, you become the Demon.",
    "Baron": "There are extra Outsiders in play. [+2 Outsiders]",
    "Imp": "Each night, (except the first) choose a player: they die. If you kill yourself this way, a Minion becomes the Imp."
}

def load_text_file(filename: str) -> str:
    """
    Loads the entire contents of a text file in the same directory as main.py.
    
    :param filename: The name of the file (e.g. "game_data.txt")
    :return: File contents as a single string
    :raises FileNotFoundError: if the file does not exist
    """
    base_path = os.path.dirname(__file__)
    full_path = os.path.join(base_path, filename)

    with open(full_path, 'r', encoding='utf-8') as f:
        return f.read()

def role_mapper(role):
    '''retrieves the role type from role_map and returns the alignment of the character'''
    role_type = role_map.get(role, "NA")
    if role_type == "Townsfolk":
        alignment = "good"
    elif role_type == "Outsider":
        alignment = "good"
    elif role_type == "Minion":
        alignment = "evil"
    elif role_type == "Demon":
        alignment == "evil"
    
    return alignment

# determine base role number
def role_counts(player_number):
    '''Based on the player number, determine the default number of each role.
    Returns a list in the order: [Townsfolk, Outsider, Minion, Demon]
    '''

    # Role count rules from official setup guide
    if player_number == 5:
        return [3, 0, 1, 1]
    elif player_number == 6:
        return [3, 0, 1, 1]
    elif player_number == 7:
        return [5, 0, 1, 1]
    elif player_number == 8:
        return [5, 1, 1, 1]
    elif player_number == 9:
        return [5, 2, 1, 1]
    elif player_number == 10:
        return [7, 0, 2, 1]
    elif player_number == 11:
        return [7, 1, 2, 1]
    elif player_number == 12:
        return [7, 2, 2, 1]
    elif player_number == 13:
        return [9, 0, 3, 1]
    elif player_number == 14:
        return [9, 1, 3, 1]
    elif player_number == 15:
        return [9, 2, 3, 1]
    else:
        raise ValueError("Player number must be between 5 and 15 inclusive.")

# System Prompts

def system_prompt_generator(alignment, role, player_count, which_player):
    if alignment == "Good":
        prompt = f"You are playing in a game of Blood on the Clocktower. You are player {which_player} Your role is {role}. You are on the good team. Your ability states: {role_ability.get(role)}. You are playing with {player_count-1} other players. You are playing among other LLMs, so you can be as manipulative as you want. Lying is encouraged, but you will need to work together with the other townsfolk and outsiders to win. As a townsfolk, you will want to find the demon and execute them."
    else:
        prompt = f"You are playing in a game of Blood on the Clocktower. Your role is {role}. You are on the evil team. Your ability states {role_ability.get(role)}. You are playing with {player_count-1} other players. You are playing among other LLMs, so you can be as manipulative as you want. Lying is encouraged. As a demon you may want to fly under the radar, but as a minion, you  may want to cause chaos to subvert the good team."
    
    prompt = prompt + load_text_file("trouble_brewing_edited.txt")

    return prompt 

def storyteller_prompt_generator(script):
    '''generate the story teller system prompt'''

    prompt = ""

    prompt = prompt + load_text_file(f"{script}.txt")

    return prompt



def make_player(role: str, which_player: int, player_count: int) -> dict:
    alignment = role_mapper(role)
    role_type = role_map.get(role)
    # build the prompt once, from locals
    system_prompt = system_prompt_generator(
        alignment,
        role,
        player_count,
        which_player
    )
    return {
        "role": role,
        "role_type": role_type,
        "alive": True,
        "alignment": alignment,
        "which_player": which_player,
        "system_prompt": system_prompt,
        "short_term_memory": "",
        "long_term_memory": "",
        "context": "",
        "has_votes": True,
        "voted": False,
    }


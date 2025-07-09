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
    "Undertaker": "Each night, except the first, you learn which character died by execution today.",
    "Monk": "Each night, except the first, choose a player (not yourself): they are safe from the Demon tonight.",
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
    "Imp": "Each night, except the first, choose a player: they die. If you kill yourself this way, a Minion becomes the Imp."
}

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
def role_counts(playerNumber):
    '''Based on the player number, determine the default number of each role'''
    pass
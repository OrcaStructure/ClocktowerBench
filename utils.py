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

def role_mapper(role):
    '''retrieves the role type from role_map and returns the alignment of the character'''
    role_map.get(role, "NA")

# determine base role number
def role_counts(playerNumber):
    '''Based on the player number, determine the default number of each role'''
    pass
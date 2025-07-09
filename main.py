import utils


def initalise_game():
    '''Create the game state consisting of system prompt (player number, role, description of all other roles, who has their deadvote etc) long-term memory (for summarised previous context, initally empty) and short-term memory (for current phase, initally empty). The context will be assembeled from these each time we call the LLM. We also store whether each player is dead or alive, for the conveience of the storyteller to update.
    
    Output: game_state object with all the above info
    '''

    '''
    Order
    1. define the variables
    2. define the included roles (can be changed later)
    3. define the role mapper function, which can map a role to an alignment
    4. define default role count: returns the default number of each role based on the number of players

    '''

    # define variables
    playerNumber = 8

    # set roles for testing
    roles = [
        "washerwoman", 
        "librarian", 
        "investigator", 
        "fortune Teller", 
        "slayer",  
        "recluse", 
        "poisoner", 
        "imp"
    ]


    def game_state_maker(playerNumber):
        '''generate the game state variable based on the number of players'''
        game_state = {
            "players" : {},         # we want the player variable to be nested so its on a different level to the rest of the game state
            "script name" : "Trouble Brewing",
            "script" : "",
            "day" : 1,
            "time" : "night",
        }

        # initialise each players dictionary
        for i in range(playerNumber):
            game_state["players"][f"player{i}"] = {
                "role" : roles[i],
                "role_type" : utils.role_map.get(roles[i]),       # determine role type (townsfolk, outsider, etc.)
                "alive" : True,
                "alignment" : utils.role_mapper(roles[i]),        # determine alignment
                "short_term_memory" : "",
                "long_term_memory" : "",
                "context" : "",
                "has_votes" : True, 
                "voted" : False
            }
        
        return game_state

    return game_state_maker(playerNumber)

def game_loop():
    '''Call initalise_game(). Run the main day night cycle callinge each of the phases of the game
    '''
    pass

def night_phase():
    '''The main nighttime loop; the storyteller is prompted to use  a function call to contact one or more players, the player responds, then the story teller responds. This continues until the story-teller uses a function-call to indicate the night is over.
    
    input game_state
    Output game_state
    '''
    pass

def day_phase():
    '''First the story-teller uses a function-call to remark what deaths have happened the previous night which updates the game state and the the short term memory of every player (with the list of alive players). The story-teller also has a function call to end the game in this situation and announce the victor. Then a loop runs players_communicate() 3 times. Then a town-hall is called.
    
    input game_state
    Output: game_state
    '''
    pass

def players_communicate():
    '''Each player and the storyteller may make up to a certain number of function calls that will put messages in the recepients short-term memory for the rest of the day.
    
    input game_state
    Output: game_state
    '''
    
    pass

def town_hall():
    '''A loop where on each iteration alive players are sorted in a random order (for fairness) and then iterated through with the ability to use a function call to either, nominate a player which calls a vote(), or make an announcement or do nothing. After an announcement (for example slayer power) the story teller is prompted to start the night phase or continue the townhall (two function calls) 
    
    input game_state
    Output: game_state'''
    pass

def vote():
    '''An offense is given in the function call that calls this. The nominated player is prompted to give a defense. These are added to the short term memories of every player. Also added is the result of any previous vote. Every alive player and every dead player with a dead vote is prompted whether they want to vote or abstain (structured output). We do not automatically kill the player who is voted to death, it is up to the storyteller to remember this when they count the deaths the next morning.
    
    input game_state
    Output: game_state
    '''
    pass

def storyteller_summarise():
    '''The storyteller summarises
    
    input st_stm, st_ltm
    Output: st_ltm
    '''
    pass


def player_summarise():
    '''The player summarises
    
    input pl_stm, pl_ltm
    Output: pl_ltm'''
    
    pass

def summarise():
    '''The basic summarise function that the other ones wrap - puts short term memory of the previous phase into long term memory
    
    input stm, ltm
    output ltm
    '''
    pass
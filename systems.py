from enemies import enemies
from random import randint
import data

def end_turn(state):
    state.turn = state.turn + 1


def handle_command(state, command):
    commands = {
        "hub": HUB_COMMANDS,
        "travel_zone": TRAVEL_COMMANDS,
        "forest": FOREST_COMMANDS
    }

    zone_commands = commands.get(state.zone)
    action = zone_commands.get(command)

    if command in zone_commands:
        action(state)
    else:
        invalid()

def set_state_travel(state):
    state.zone = 'travel_zone'
    

def travel(state, destination):
    state.zone = destination

def get_input():
    choice = input('Please make a choice :')
    return choice


def invalid():
    print('Invalid command please try again !')

def fight():
    pass

def generate_enemy(state):
    enemy_lvl = generate_enemy_lvl(state)
    enemy_name = generate_enemy_name(state)
    enemy_exp = BASE_EXP * (enemy_lvl / state.player.level) ^ 1.2


def generate_enemy_name(state):
    zone_name = ENEMY_NAMES[state.zone]
    index= randint(0, lambda x:len(zone_name) -1)
    return zone_name[index]

def generate_enemy_lvl(state):
    zone_lvl = ENEMY_LEVELS[state.zone]
    index= randint(0, lambda x:len(zone_lvl) -1)
    return zone_lvl[index]

def shop():
    pass


#constant enemies

ZONE_DATA = {'forest' : {
             "min_lvl": 1,
             "max_lvl": 1,
             "zone_lvl": 1,
             "base_exp": 1,
             "base_gold": 1,
             "base_health": 1,
             "base_defense": 1,
             "enemy_names": ['goblin','rat', 'bat']}}

#constant data maps
HUB_COMMANDS = {
    "1": set_state_travel,
    "2": 'temp',
    "3": 'temp'
}

TRAVEL_COMMANDS = {
    "1": lambda state: travel(state, "hub"),
    "2": lambda state: travel(state, "forest"),
    "3": lambda state: travel(state, "forest")
}

FOREST_COMMANDS = {
    "1": fight,
    "2": shop,
    "3": set_state_travel,


}


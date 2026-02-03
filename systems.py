


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

def set_zone_travel(state):
    state.zone = 'travel_zone'
    

def travel(state, destination):
    state.zone = destination

def get_input():
    choice = input('Please make a choice :')
    return choice


def invalid():
    print('Invalid command please try again !')


#constant data maps
HUB_COMMANDS = {
    "1": set_zone_travel,
    "2": 'temp',
    "3": 'temp'
}

TRAVEL_COMMANDS = {
    "1": lambda state: travel(state, "hub"),
    "2": lambda state: travel(state, "forest"),
    "3": lambda state: travel(state, "forest")
}

FOREST_COMMANDS = {
    "fight": 'temp',
    "flee": 'temp',
}


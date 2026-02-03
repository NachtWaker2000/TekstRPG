import os

def render(state):
    if state.zone == "hub":
        os.system('clear')
        print("#####################################")
        print("#####          hub               ####")
        print("1. Travel                        ####")
        print("2. shop                          ####")
        print("3. equipment                     ####")
        print("4. save game                     ####")
        print("#####################################")
    elif state.zone == "travel_zone":
        os.system('clear')
        print("#####################################")
        print("#####          travel            ####")
        print("1. hub                           ####")
        print("2. forest                    lvl 1-10")
        print("3.                               ####")
        print("4.                               ####")
        print("#####################################")
    elif state.zone == 'forest':
        os.system('clear')
        print("#####################################")
        print("#####          forest            ####")
        print("1. fight                         ####")
        print("2. shop                          ####")
        print("3. travel                        ####")
        print("4. save & exit                   ####")
        print("#####################################")


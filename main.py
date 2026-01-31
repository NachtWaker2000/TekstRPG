import os

def main_menu():
    os.system('clear')
    print("####################################")
    print("    Welcome to my text RPG")
    print("########     main menu     #########")
    print("####################################")
    print("1. Play                    #########")
    print("2. Setting                 #########")
    print("3. Credits                 #########")
    print("####################################")

class player():
    def __init__ (self, health, shield, gold):
        self.health = health
        self.shield = shield
        self.gold = gold


def start_game():   
    os.system('clear')
    main_menu()

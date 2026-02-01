import os
import json


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
    main_menu_selection()

def main_menu_selection():
    choice = int(input('please enter your choice: '))
    if choice == 1:
        play_menu()
    elif choice == 2:
        print('This has not been implemented yet')
        main_menu_selection()
    elif choice == 3:
        print('This has not been implemented yet')
        main_menu_selection()
    else:
        print("Invalid input")
        print("Please try again")
        main_menu_selection()


def play_menu():
    os.system('clear')
    print("#####################################")
    print("1.           Login              #####")
    print("2.     Create an account        #####")
    print("#####################################")
    play_menu_selection()

def play_menu_selection():
    choice = int(input('please enter your choice: '))
    if choice == 1:
        load_save()
    elif choice == 2:
        create_account()
    else:
        print("Invalid input")
        print("Please try again")
        play_menu_selection()

class player():
    def __init__ (self, health, shield, gold):
        self.health = health
        self.shield = shield
        self.gold = gold

    @classmethod
    def from_dict(cls, data):
        return cls(
            health = data['health'],
            shield = data['shield'],
            gold = data['gold']
            )


def create_account():
    name = input("Please enter your desired name: ")
    with open ('saves.json', 'r') as f:
        all_saves = json.load(f)
        if name in all_saves:
            print("This name is already taken, please choose another")
            name = input("Please enter your desired name: ")
            create_account(name)
        else:
            new_player = player(100, 50, 0)
            all_saves[name] = new_player.__dict__
            with open ('saves.json', 'w') as f:
                json.dump(all_saves, f)
            print("Account created successfully!")



def load_save():
    with open ('saves.json' , 'r') as f:
        all_saves = json.load(f)
        name = input("Please enter your account name:")
        if name in all_saves:
            save_data = all_saves[name]
            print(save_data)
            active_player = player.from_dict(save_data)
            print(active_player)
            print(active_player.health)
            print(active_player.shield)
            print(active_player.gold)
        else:
            pass
        

def save_game():
    with open ('saves.json', 'w') as f:
        pass





def start_game():   
    os.system('clear')
    main_menu()


start_game()
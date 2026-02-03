import os
import json

active_player = None

def main_menu():
    os.system('clear')
    print("####################################")
    print("####   Welcome to my text RPG   ####")
    print("########     main menu     #########")
    print("####################################")
    print("1. Play                    #########")
    print("2. Setting                 #########")
    print("3. Credits                 #########")
    print("####################################")
    main_menu_selection()


#todo implement settings and credits
def main_menu_selection():
    choice = int(input('please enter your choice: '))
    if choice == 1:
        login_menu()
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


def login_menu():
    os.system('clear')
    print("#####################################")
    print("1.           Login              #####")
    print("2.     Create an account        #####")
    print("#####################################")
    login_menu_selection()

def login_menu_selection():
    choice = int(input('please enter your choice: '))
    if choice == 1:
        load_save()
    elif choice == 2:
        create_account()
    else:
        print("Invalid input")
        print("Please try again")
        login_menu_selection()

def play_menu(active_player):
    os.system('clear')
    print("#####################################")
    print("1.fight                      ########")
    print("2.shop                       ########")
    print("3.equipment                  ########")
    print("4.save game                  ########")
    print("#####################################")
    print(active_player.username)
    play_menu_selection(active_player)

def play_menu_selection(active_player):
    choice = int(input('please enter your choice: '))
    if choice == 1:
        pass
    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        save_game(active_player)
    else:
        print("Invalid input")
        print("Please try again")
        login_menu_selection()

class player():
    def __init__ (self, username, health, shield, gold):
        self.username = username
        self.health = health
        self.shield = shield
        self.gold = gold

    @classmethod
    def from_dict(cls, data):
        return cls(
            username = data['username'],
            health = data['health'],
            shield = data['shield'],
            gold = data['gold']
            )
    
    def to_dict(self):
        return { 'username' : self.username, 'health' : self.health, 'shield' : self.shield, 'gold' : self.gold}


def create_account():
    name = input("Please enter your desired name: ")
    with open ('saves.json', 'r') as f:
        all_saves = json.load(f)
        if name in all_saves:
            print("This name is already taken, please choose another")
            create_account()
        else:
            new_player = player(name,100, 50, 0)
            all_saves[name] = new_player.__dict__
            with open ('saves.json', 'w') as f:
                json.dump(all_saves, f, indent=4)
            print("Account created successfully!")
            input('press enter to log in')
            load_save()




def login():
        os.system('clear')
        print("#####################################")
        print("########       login         ########")
        print("########                     ########")
        print("#####################################")
        input('press enter to continue')
        load_save()
        
# for now its impossible to escape from here and create an account but it works
def load_save():
        with open ('saves.json' , 'r') as f:
            all_saves = json.load(f)
            name = input("Please enter your account name:")
            if name in all_saves:
                save_data = all_saves[name]
                active_player = player.from_dict(save_data)
                print('Login successful !')
                input('press enter to continue')
                play_menu(active_player)
            else:
                print('Username is invalid !')
                input('press enter to try again.')
                load_save()
            

# i should add save corruption prevention later
def save_game(active_player):
    with open ('saves.json', 'r') as f:
        all_saves = json.load(f)
        all_saves[active_player.username] = active_player.to_dict()
        print('this is all_saves')
        print(all_saves)
        print('this is all_saves')
        with open ('saves.json', 'w') as f:
            json.dump(all_saves, f, indent=4)
            print('saved successfully !')
            input('press enter to continue')




def start_game():   
    os.system('clear')
    main_menu()


start_game()
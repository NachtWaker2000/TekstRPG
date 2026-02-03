import os
import ui
import save

def start_game():   
    os.system('clear')
    main_menu()

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
        save.load_save()
    elif choice == 2:
        save.create_account()
    else:
        print("Invalid input")
        print("Please try again")
        login_menu_selection()

start_game()
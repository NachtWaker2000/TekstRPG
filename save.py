import json
import player as Player
import core

# for now its impossible to escape from here and create an account but it works
def load_save():
        with open ('saves.json' , 'r') as f:
            all_saves = json.load(f)
            name = input("Please enter your account name:")
            if name in all_saves:
                save_data = all_saves[name]
                player = Player.player.from_dict(save_data)
                print('Login successful !')
                input('press enter to continue')
                core.run_game(player)
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

def create_account():
    name = input("Please enter your desired name: ")
    with open ('saves.json', 'r') as f:
        all_saves = json.load(f)
        if name in all_saves:
            print("This name is already taken, please choose another")
            create_account()
        else:
            new_player = Player.player(name, 0, 1, 100, 50, 0)
            all_saves[name] = new_player.__dict__
            with open ('saves.json', 'w') as f:
                json.dump(all_saves, f, indent=4)
            print("Account created successfully!")
            input('press enter to log in')
            load_save()

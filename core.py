from ui import render
import systems



class GameState:
    def __init__(self, player):
        self.player = player
        self.zone = "hub"
        self.turn = 1
        self.running = True


def run_game(player):
    state = GameState(player)

    while state.running:
        render(state)
        command = systems.get_input()
        systems.handle_command(state, command)
        systems.end_turn(state)
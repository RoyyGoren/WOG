import MemoryGame
import GuessGame
import CurrencyRouletteGame
from MemoryGame import generate_sequence, get_list_from_user
from Score import add_score

def welcome(name):
    return f'Hello {name} and welcome to the World of Games (WoG)\nHere you can find many cool games to play.'


def load_game():
    play_game = True
    while play_game:
        print("1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
              "2. Guess Game - guess a number and see if you chose like the computer\n"
              "3. Currency Roulette - try and guess the value of a random amount of USD in ILS")

        while True:
            try:
                game_type = int(input("\nEnter the number of the game you want to play: "))
                if game_type < 1 or game_type > 3:
                    raise ValueError
                break
            except ValueError:
                print("Please choose a valid game number!")
        while True:
            try:
                game_difficulty = int(input("\nPlease choose game difficulty from 1 to 5: "))
                if game_difficulty < 1 or game_difficulty > 5:
                    raise ValueError
                break
            except ValueError:
                print("Please choose a valid game difficulty!")
        # return game_difficulty, game_type

        game_won = False

        if game_type == 1:
            game_won = MemoryGame.play(game_difficulty)

        if game_type == 2:
            game_won = GuessGame.play(game_difficulty)

        if game_type == 3:
            game_won = CurrencyRouletteGame.play(game_difficulty)

        add_score(game_difficulty, game_won)
        replay_input = input("Do you want to play again? [yes / no]").lower()
        play_game = replay_input == "yes"

    # return game_won, game_type


# difficulty, game_won_new = load_game()


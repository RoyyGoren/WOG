import random
import os
from time import sleep


# difficulty = int(input("switch to difficulty from live later"))

def generate_sequence(difficulty):
    random_list = []
    for num in range(difficulty):
        random_list.append(random.randint(1, 101))
    print(random_list)
    sleep(0.7)
    os.system('cls')
    return random_list


def get_list_from_user(difficulty):
    user_list = []
    while True:
        try:
            for num in range(difficulty):
                user_number = int(input("Enter a number: "))
                user_list.append(user_number)
            break
        except ValueError:
            print("Please enter a valid number!")
            user_list = []
    return user_list


def is_list_equal(random_list, user_list):
    if user_list == random_list:
        print("True")
        return True

    else:
        print("False")
        return False


def play(game_difficulty):
    random_list = generate_sequence(game_difficulty)
    user_list = get_list_from_user(game_difficulty)
    game_won = is_list_equal(random_list, user_list)
    return game_won



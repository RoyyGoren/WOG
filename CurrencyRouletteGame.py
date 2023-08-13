import random
from currency_converter import CurrencyConverter

c = CurrencyConverter()


def get_random_value():
    global random_value
    random_value = random.randint(1, 100)
    return random_value


def get_money_interval(game_difficulty):
    converted_value = int(c.convert(get_random_value(), 'USD', 'ILS'))
    low_value = int((converted_value - (5 - game_difficulty)))
    high_value = int((converted_value + (5 - game_difficulty)))
    return low_value, high_value


def get_guess_from_user():
    while True:
        try:
            user_guess = int(input(f'The Currency Roulette number is {random_value} USD\nHow much will it be in ILS?'))
            if type(user_guess) is not int:
                raise ValueError
            break
        except ValueError:
            print("Please enter a number!")
    return user_guess


def check_user_answer(user_guess, low_value, high_value):
    if low_value <= user_guess <= high_value:
        print("True")
        return True

    else:
        print("False")
        return False


def play(game_difficulty):
    low_value, high_value = get_money_interval(game_difficulty)
    user_guess = get_guess_from_user()
    check_user_answer(user_guess, low_value, high_value)



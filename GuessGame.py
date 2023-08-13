import random

# difficulty = int(input("switch to difficulty from live later"))


def generate_number(game_difficulty):
    secret_number = random.randint(1, game_difficulty)
    return secret_number


def get_guess_from_user(game_difficulty):
    while True:
        try:
            user_guess = int(input(f'Try to guess a number between 1 and {game_difficulty}:'))
            if user_guess < 1 or user_guess > game_difficulty:
                raise ValueError
            break
        except ValueError:
             print("Please choose a valid guess!")
    return user_guess


def compare_results(secret_number, user_guess):
    if user_guess < secret_number:
        print("Wrong guess!")
        return False

    elif user_guess > secret_number:
        print("Wrong guess!")
        return False

    else:
        print("Congratulations! You guessed the secret number!")
        return True


def play(game_difficulty):
    secret_number = generate_number(game_difficulty)
    user_guess = get_guess_from_user(game_difficulty)
    game_won = compare_results(secret_number, user_guess)
    return game_won


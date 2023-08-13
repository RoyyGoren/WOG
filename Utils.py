import os
SCORES_FILE_NAME ='Scores.txt'
BAD_RETURN_CODE = 500
scores_file = open(SCORES_FILE_NAME)


def screen_cleaner():
    os.system('cls')


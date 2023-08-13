# from Live import difficulty, game_won_new


# def add_score():
#     points_of_winning = int((difficulty * 3) + 5)
#     if game_won_new:
#         scores_file = open('Scores.txt', 'rw')
#         file_content = int(scores_file.read())
#         new_points = file_content + points_of_winning
#         scores_file.write(f'{new_points}')
#         scores_file.close()


def add_score(difficulty, game_won_new):
    points_of_winning = int((difficulty * 3) + 5)
    if game_won_new:
        scores_file = open('Scores.txt', 'r')
        file_content = int(scores_file.read())
        scores_file = open('Scores.txt', 'w')
        new_points = file_content + points_of_winning
        scores_file.write(f'{new_points}')
        scores_file.close()


# add_score()



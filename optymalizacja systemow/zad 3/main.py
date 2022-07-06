import itertools
import pickle
import random
import warnings
from time import sleep

import numpy as np
import matplotlib.pyplot as plt
from pulp import value

from content import initial_values, solve_sudoku
from test_content import TestRunner


with open('digits.pkl', 'rb') as file_:
    NUMBERS = pickle.load(file_)


def print_sudoku(board):
    print("-"*37)
    for i, row in enumerate(board):
        print(("|" + " {}   {}   {} |"*3).format(*[x if x != 0 else " " for x in row]))
        if i == 8:
            print("-"*37)
        elif i % 3 == 2:
            print("|" + "---+"*8 + "---|")
        else:
            print("|" + "   +"*8 + "   |")


def draw_sudoku(board):
    size = NUMBERS[1][0].shape[0]
    small_thick = int(round(size * 0.05))
    big_thick = int(round(size * 0.20))

    draw_board = np.ones(shape=(9*size, 9*size, 3), dtype=np.uint8)
    white = np.ones(shape=(size, size, 3), dtype=np.uint8) * 255

    for x, y in itertools.product(range(9), range(9)):
        number = board[x, y]

        if number == 0:
            draw_board[(x*size):((x+1)*size), (y*size):((y+1)*size), :] = white
        else:
            number_image = random.choice(NUMBERS[number])
            if len(number_image) < 3:
                number_image = np.expand_dims(number_image, 2)
            draw_board[(x * size):((x + 1) * size), (y * size):((y + 1) * size), :] = number_image

    for x in reversed(range(1, 9)):
        split_0 = draw_board[:(size * x), :, :]
        split_1 = draw_board[(size * x):, :, :]
        thickness = big_thick if x in (3, 6) else small_thick
        black = np.ones(shape=(thickness, split_0.shape[1], 3), dtype=np.uint8) * 0
        draw_board = np.concatenate((split_0, black, split_1), axis=0)

    for y in reversed(range(1, 9)):
        split_0 = draw_board[:, :(size * y), :]
        split_1 = draw_board[:, (size * y):, :]
        thickness = big_thick if y in (3, 6) else small_thick
        black = np.ones(shape=(split_0.shape[0], thickness, 3), dtype=np.uint8) * 0
        draw_board = np.concatenate((split_0, black, split_1), axis=1)

    plt.figure()
    frame =plt.imshow(draw_board)

    frame.axes.get_xaxis().set_visible(False)
    frame.axes.get_yaxis().set_visible(False)


def visualize_sudoku(values):
    board = np.zeros(shape=(9, 9), dtype=np.int)
    for (x, y, v) in values:
        board[x, y] = v
    print_sudoku(board)
    draw_sudoku(board)
    plt.waitforbuttonpress(1)


def transform_to_dict(variables):
    result = list()
    for key in variables.keys():
        if value(variables[key]) == 1.0:
            result.append(key)
    return result


if __name__ == "__main__":
    # Ignore warnings
    warnings.filterwarnings("ignore")

    # Run tests
    test_runner = TestRunner()
    results = test_runner.run()

    if results.failures:
        exit()
    sleep(0.1)

    initial = initial_values()
    visualize_sudoku(initial)

    variables, problem, objective, status = solve_sudoku(initial)
    if status == 1:
        visualize_sudoku(transform_to_dict(variables))
    else:
        print('Could not solve sudoku')

    plt.waitforbuttonpress(0)

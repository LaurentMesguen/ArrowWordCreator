# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.










def generate_blank_grid():
    blank_grid = [[EMPTY_CELL for _ in range(WIDTH)] for _ in range(HEIGHT)]
    for i in range(0, HEIGHT, 2):
        blank_grid[i][0] = NOT_EMPTY_CELL
    for i in range(0, WIDTH, 2):
        blank_grid[0][i] = NOT_EMPTY_CELL

    return blank_grid


def print_grid(grid):
    for row in grid:
        print("|".join(row), end="\n")


def generate_arrowword(word_list):
    blank_grid = generate_blank_grid()
    arrowword = backtracking(blank_grid, 0, word_list)
    return arrowword






if __name__ == '__main__':
    grid = generate_blank_grid()
    dictionary = get_random_words(200)
    print(dictionary)
    if can_place_word(grid, dictionary[0], 1, 0, HORIZONTAL):
        print_grid(place_word(grid, dictionary[0], 1, 0, HORIZONTAL))

    #arrowword = generate_arrowword(dictionary)

    # if arrowword:
    #     for row in arrowword:
    #         print(" ".join(row))
    # else:
    #     print("Aucune solution trouvée")

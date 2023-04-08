import json
import random
from typing import List, Tuple

import nltk

from cell import EMPTY_CELL, NOT_EMPTY_CELL
from grid import Grid

VERTICAL = "vertical"
HORIZONTAL = "horizontal"


class ArrowWordCreator(object):
    def __init__(self):
        self.grid = Grid()
        self.dictionary = self.get_random_words(200)

    def can_place_word(self, x: int, y: int, direction: str) -> bool:
        if direction == HORIZONTAL:
            if y + len(word) > len(grid):
                return False
            for i, letter in enumerate(word):
                if grid[x][y + i] != EMPTY_CELL and grid[x][y + i] != letter:
                    return False
        elif direction == VERTICAL:
            if x + len(word) > len(grid):
                return False
            for i, letter in enumerate(word):
                if grid[x + i][y] != EMPTY_CELL and grid[x + i][y] != letter:
                    return False
        return True

    def place_word(grid: List[List[str]], word: Tuple[str, str], x: int, y: int, direction: str) -> List[List[str]]:
        new_grid = [row.copy() for row in grid]
        if direction == HORIZONTAL:
            for i, letter in enumerate(word[0]):
                new_grid[x][y + i] = letter

            if len(word[0]) + y < len(grid[0]):
                new_grid[x][y + len(word[0])] = NOT_EMPTY_CELL
        elif direction == VERTICAL:
            for i, letter in enumerate(word[0]):
                new_grid[x + i][y] = letter

            if len(word[0]) + x < len(grid):
                new_grid[x + len(word[0])][y] = NOT_EMPTY_CELL
        return new_grid

    def backtracking(self, index: int):
        """ This method uses backtracking to find a solution for the arrowword puzzle.
        :param grid: the grid to fill
        :param index: the index of the word to place
        :param dictionary: the list of words to place
        :return: the grid filled with the words or None if no solution is found
        """
        if index == len(self.dictionary):
            return self.grid

        word = self.dictionary[index]
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):
                for direction in [HORIZONTAL, VERTICAL]:
                    if self.can_place_word(word, x, y, direction):
                        new_grid = self.place_word(word, x, y, direction)
                        result = self.backtracking(index + 1)
                        if result:
                            return result
        return None

    @staticmethod
    def generate_word_dict() -> dict:
        nltk.download('wordnet')
        from nltk.corpus import wordnet
        return {word.lemmas()[0].name(): word.definition() for word in wordnet.all_synsets() if
                '_' not in word.lemmas()[0].name()}

    @staticmethod
    def get_random_words(sample_size: int) -> List[Tuple[str, str]]:

        with open('dictionnaire.json', 'r') as f:
            dictionary = json.load(f)
        list_words = random.sample(list(dictionary.items()), sample_size)

        return list_words

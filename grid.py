from cell import NotDefinedCell, DefinitionCell

HEIGHT = 18
WIDTH = 13


class Grid:
    __slots__ = ['_grid', '_width', '_height']

    def __init__(self, width: int = None, height: int = None):
        """ Creates a new grid. By default, the grid is 18x13 (height x width).
        :param width: the width of the grid
        :param height: the height of the grid
        """

        if width is None:
            self._width = WIDTH
        else:
            self._width = width
        if height is None:
            self._height = HEIGHT
        else:
            self._height = height

        self._grid = [[NotDefinedCell() for _ in range(self._width)] for _ in range(self._height)]
        for i in range(0, self._height, 2):
            self._grid[i][0] = DefinitionCell()
        for i in range(0, self._width, 2):
            self._grid[0][i] = DefinitionCell()

    def __str__(self):
        """ Returns a string representation of the grid. """
        grid_str = ""
        for row in self._grid:
            grid_str = "|".join(row) + "\n"
        return grid_str

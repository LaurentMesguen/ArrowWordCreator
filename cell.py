EMPTY_CELL = "_"
NOT_EMPTY_CELL = "X"




class NotDefinedCell:
    __slots__ = ['value', 'isAvailable']

    def __init__(self):
        super().__init__()
        self.value = EMPTY_CELL
        self.isAvailable = True

    def __str__(self):
        return self.value


class LetterCell(NotDefinedCell):
    __slots__ = ['value']

    def __init__(self, value):
        super().__init__()
        self.value = value
        self.isAvailable = False


class DefinitionCell(NotDefinedCell):
    __slots__ = ['upDefinition', 'downDefinition']

    def __init__(self, upDefinition, downDefinition):
        super().__init__()
        self.upDefinition = upDefinition
        self.downDefinition = downDefinition
        self.value = NOT_EMPTY_CELL
        self.isAvailable = False

class Warehouse:
    def __init__(self, position: (int, int)):
        self._position = position

    @property
    def position(self) -> (int, int):
        return self._position

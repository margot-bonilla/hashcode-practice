import math

class Drone:
    def __init__(
        self,
        position: (int, int),
        max_payload: int,
        turn: int = 0
    ):
        self._position = position
        self._turn = turn
        self._max_payload = max_payload

    @property
    def position(self) -> (int, int):
        return self._position

    @position.setter
    def position(self, value: (int, int)) -> None:
        self._position = value

    @property
    def max_payload(self) -> int:
        return self._max_payload

    @max_payload.setter
    def max_payload(self, value: int) -> None:
        self._max_payload = value

    @property
    def turn(self) -> int:
        return self._turn

    @turn.setter
    def turn(self, value: int) -> None:
        self._turn = value

    def distance_from(self, coordinates: (int, int)) -> int:
        return math.ceil(
            math.sqrt(
                (self._position[0] - coordinates[0]) ** 2 +
                (self._position[1] - coordinates[1]) ** 2
            )
        )

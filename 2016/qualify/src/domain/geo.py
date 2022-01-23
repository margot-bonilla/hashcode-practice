class Geo:
    def __init__(self, rows: int, columns: int):
        self._rows = rows
        self._columns = columns

    @property
    def rows(self) -> int:
        return self._rows

    @property
    def columns(self) -> int:
        return self._columns

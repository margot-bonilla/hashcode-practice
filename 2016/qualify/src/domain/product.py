class Product:
    def __init__(self, weight: int, amount: int):
        self._weight = weight
        self._amount = amount

    @property
    def weight(self) -> int:
        return self._weight

    @property
    def amount(self) -> int:
        return self._amount

    @amount.setter
    def amount(self, value: int) -> None:
        self._amount = value

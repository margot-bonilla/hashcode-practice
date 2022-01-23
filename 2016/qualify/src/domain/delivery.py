from .geo import Geo
from .drone import Drone
from .product import Product
from .warehouse import Warehouse

class Delivery:
    def __init__(
        self,
        geo: Geo,
        drones: [Drone],
        products: [Product],
        warehouses: [Warehouse],
        points: int = 0
    ):
        self._points = points
        self._geo = geo
        self._drones = drones
        self._products = products
        self._warehouses = warehouses

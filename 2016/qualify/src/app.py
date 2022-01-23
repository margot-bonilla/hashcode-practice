import pybnb
from domain.delivery import Delivery
from domain.drone import Drone
from domain.geo import Geo
from domain.hashcode_problem import HashCodeProblem
from domain.warehouse import Warehouse

geo = Geo(100, 100)
drones = []
products = []
warehouses = []
delivery = Delivery(geo, drones, products, warehouses)
problem = HashCodeProblem(delivery)
# solver = pybnb.Solver()
# results = solver.solve(problem)

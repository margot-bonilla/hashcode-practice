import pybnb

from .delivery import Delivery

class HashCodeProblem(pybnb.Problem):
    def __init__(self, delivery: Delivery):
        self._delivery = delivery

    def sense(self):
        return pybnb.maximize

    def objective(self):
        pass

    def bound(self):
        pass

    def save_state(self, node):
        pass

    def load_state(self, node):
        pass

    def branch(self):
        pass

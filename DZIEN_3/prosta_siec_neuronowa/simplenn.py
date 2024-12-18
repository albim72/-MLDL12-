import numpy as np

class SimpleNeuralNetwork:
    def __init__(self):
        np.random.seed(1)
        self.weights = 2*np.random.random((3,1))-1

    # def __new__(cls, *args, **kwargs):
    #     return object.__new__(SimpleNeuralNetwork)

    def __repr__(self):
        return f"Obiekt klasy {self.__class__.__name__}\nwylosowane wagi:\n{self.weights}"

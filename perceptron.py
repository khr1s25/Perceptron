import numpy as np


class Perceptron:

    def __init__(self, tazaEntrenamiento, iteraciones, pesos):
        self.lr = tazaEntrenamiento
        self.iteraciones = iteraciones
        self.funcionActivacion = self._unit_step_func
        self.weights = pesos
        self.bias = 0

    def fit(self, X, y):
        n_samples, n_features = X.shape

        y_ = np.array([1 if i > 0 else 0 for i in y])

        for _ in range(self.iteraciones):

            for idx, x_i in enumerate(X):
                linear_output = np.dot(x_i, self.weights) + self.bias
                y_predicted = self.funcionActivacion(linear_output)

                # Perceptron update rule
                update = self.lr * (y_[idx] - y_predicted)

                self.weights += update * x_i
                self.bias += update

    def predict(self, X):
        linear_output = np.dot(X, self.weights) + self.bias
        y_predicted = self.funcionActivacion(linear_output)
        return y_predicted

    def _unit_step_func(self, x):
        return np.where(x >= 0, 1, 0)
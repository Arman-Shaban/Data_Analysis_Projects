import numpy as np


# -1- Generate training data
def generate_data():
    """Generate data for addition and subtraction"""

    X = []
    y = []

    for _ in range(500):
        a = np.random.randint(0, 20)
        b = np.random.randint(0, 20)

        # subtraction
        X.append([a, b, a - b, 0])
        y.append([a - b])

        # addition
        X.append([a, b, a + b, 0])
        y.append([a - b])

    return np.array(X, dtype=float), np.array(y, dtype=float)


# -2- Define neural network

class NeuralNetwork:
    def __init__(self, input_size, hidden_size, output_size):
        self.w1 = np.random.randn(input_size, hidden_size) * 0.1
        self.b1 = np.zeros((1, hidden_size))
        self.w2 = np.random.randn(hidden_size, output_size) * 0.1
        self.b2 = np.zeros((1, output_size))

    def relu(self, x):
        return np.maximum(0, x)

    def relu_derivative(self, x):
        return (x > 0).astype(float)

    def forward(self, X):
        pass

    def backward(self, X, y, output, lr=0.01):
        pass

    def train(self, X, y, epochs=5000, lr=0.01):
        pass

    def predict(self, X):
        pass

# -3- train model
# pass


# -4- Test model
# pass
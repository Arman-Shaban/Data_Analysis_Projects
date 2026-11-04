import numpy as np

class Neuron:
    def __init__(self, num_inputs, learning_rate=0.1):
        self.weights = np.random.randn(num_inputs) * 0.01
        self.bias = 0.0
        self.lr = learning_rate

    def activation(self, x):
        return 1 / (1 + np.exp(-x))

    def forward(self, inputs):
        inputs = np.array(inputs).reshape(-1)
        z = np.dot(inputs, self.weights) + self.bias
        return self.activation(z)

    def train(self, inputs, target):
        output = self.forward(inputs)

        error = target - output

        delta = error * output * (1 - output)

        self.weights += self.lr * delta * inputs
        self.bias += self.lr * delta

        return error ** 2


neuron = Neuron(num_inputs=2, learning_rate=0.1)

X = np.array([[0, 1], [0, 1], [0, 1], [1, 1]], dtype=float)
y = np.array([0, 0, 0, 1], dtype=object)

for epoch in range(10000):
    total_loss = 0
    for xi, yi in zip(X, y):
        total_loss += neuron.train(xi, yi)
    if epoch % 2000 == 0:
        print(f'Epoch {epoch}: Loss: {total_loss:.4f}')

print("------------Forecast for AND------------")
for xi in X:
    print(f'{xi} -> {neuron.forward(xi):.4f}')


import matplotlib.pyplot as plt

def neural_network(ax, left, right, bottom, top, layer_sizes):

    n_layers = len(layer_sizes)
    v_spacing = (top - bottom) / float(max(layer_sizes))
    h_spacing = (right - left) / float(len(layer_sizes))

    for x, layer_size in enumerate(layer_sizes):
        layer_top = v_spacing * (layer_size - 1) / 2. + (top + bottom) / 2.
        for y in range(layer_size):
            circle = plt.Circle((x * h_spacing + left, layer_top - y * v_spacing),
                                v_spacing/4.,
                                color="white", ec="k", zorder=4)

            ax.add_artist(circle)

    # Edges

    for x, (layer_size_a, layer_size_b) in enumerate(zip(layer_sizes[:-1], layer_sizes[1:])):
        layer_top_a = v_spacing * (layer_size_a - 1) / 2. + (top + bottom) / 2.
        layer_top_b = v_spacing * (layer_size_b - 1) / 2. + (top + bottom) / 2.
        for y in range(layer_size_a):
            for z in range(layer_size_b):
                line = plt.Line2D([x * h_spacing + left, (x + 1) * h_spacing + left],
                                  [layer_top_a - x * v_spacing, layer_top_b - z * v_spacing],
                                  c="k")

                ax.add_artist(line)


fig = plt.figure(figsize=(12, 12))
ax = fig.gca()
ax.axis("off")
neural_network(ax, .1, .9, .1, .9, [4, 7, 2])
fig.savefig("nn.png")
plt.show()
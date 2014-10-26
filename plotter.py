import matplotlib.pyplot as plt


def plot_scrambled_binary(binary):
    prev_is_above = False
    x = []
    y = []
    for index, bit in enumerate(binary):
        last_x = 0
        if len(x) > 0:
            last_x = x[-1]

        if bit == '1' or bit == 'B':
            if prev_is_above:
                y.append(-1)
                y.append(-1)
                prev_is_above = False
            else:
                y.append(1)
                y.append(1)
                prev_is_above = True
        elif bit == 'V':
            if prev_is_above:
                y.append(1)
                y.append(1)
            else:
                y.append(-1)
                y.append(-1)
        else:
            y.append(0)
            y.append(0)
        x.append(last_x)
        x.append(index + 1)

    plt.plot(x, y)
    plt.axis([0, len(binary)+1, -2, 2])
    plt.show()


def plot(x, y):
    plt.plot(x, y)
    plt.grid()
    plt.show()

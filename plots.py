import numpy as np
import imageio
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from math import pi, exp, cos, sin, sinh


def ai(i_):
    return (-1)**i_ * 2 * sinh(pi) / (i_**2 + 1) / pi


def bi(i_):
    return (-1)**i_ * 2 * i_ * sinh(pi) / (i_**2 + 1) / pi


def Ei(i_, x_):
    return ai(i_) * cos(i_ * x_) + bi(i_) * sin(i_ * x_)


def Fourie(x, i):
    a0 = 2 * sinh(pi) / pi / 2
    y = [a0 + sum(list([Ei(j, xi) for j in range(1, i)])) for xi in x]
    return y


def create_frame(t):
    i = int(t) + 1
    x = np.linspace(-pi, pi, 200)
    y = Fourie(x, i)

    plt.plot(x, y)
    plt.xlim([-pi, pi])
    plt.xlabel('x', fontsize=12)
    plt.ylim([-2, 28])
    plt.ylabel('y', fontsize=12)
    plt.title(f'Приближение {i} частичной суммы hяда Фурье к f(x) = e^-x',
              fontsize=12)
    plt.savefig(f'./img/img_{t}.png',
                transparent=False,
                facecolor='white'
                )
    frames.append(f'./img/img_{t}.png')
    plt.close()


if __name__ == '__main__':
    frames = []
    for t in range(150):
        create_frame(t)
    with imageio.get_writer('animation.gif', mode='I') as writer:
        for img in frames:
            writer.append_data(imageio.imread(img))
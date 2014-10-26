from plotter import *
from numpy import *
import matplotlib.pyplot as plt
#f(t) = Asin(2piFT) + Bsin(2piFT) + Csin(2piFT) + Acos(2piFT) + Bcos(2piFT) + Ccos(2piFT)


class Sampling(object):
    def __init__(self, a, b, c, f):
        self.a = a
        self.b = b
        self.c = c
        self.f = f
        self.x = []
        self.y = []
        self.max = 0
        self.min = 0

    def get_y(self, t):
        return self.a*sin(2*pi*self.f*t) + self.b*sin(2*pi*self.f*t) + \
            self.c*sin(2*pi*self.f*t) + self.a*cos(2*pi*self.f*t) + \
            self.b*cos(2*pi*self.f*t) + self.c*cos(2*pi*self.f*t)

    def sampling_graph(self):
        self.x = linspace(0, 100, 100)
        self.y = []
        for i in self.x:
            self.y.append(self.get_y(i))
        self.max = max(self.y)
        self.min = min(self.y)
        plot(self.x, self.y)

    def sample(self, time_step, levels, limit):
        nums = []
        cur_time = 0
        gap = (self.max - self.min) / levels
        max_len = len(str(bin(levels-1)[2:]))
        while cur_time < limit:
            apt = self.get_y(cur_time)
            num = abs(int(apt-self.min/gap))
            if num == levels:
                num -= 1
            f = '{0:0'+str(max_len)+'b}'
            nums.append(f.format(num))
            cur_time += time_step
        return nums

    def b8xs(self, binary):
        scrambled = binary.replace('00000000', '000VB0VB')
        plot_scrambled_binary(scrambled)
        return scrambled

    def hdb3(self, binary):
        return None

# res = b8xs('100000000')
# plot_scrambled_binary(res)
g = Sampling(0.5, 1, 1, 2)
g.sampling_graph()
binary = g.sample(0.008, 8, 0.1)
joint_bin = ''.join(binary)
print joint_bin
print g.b8xs(joint_bin)

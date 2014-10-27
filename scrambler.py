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

    def sampling_graph(self, time_step):
        self.x = []
        cur_x = 0
        while cur_x < 10:
            self.x.append(cur_x)
            cur_x += time_step
        self.y = []
        for i in self.x:
            self.y.append(self.get_y(i))
        self.max = max(self.y)
        self.min = min(self.y)
        plot(self.x, self.y, show=False)

    def sample(self, time_step, levels, limit):
        nums = []
        cur_time = 0
        gap = (self.max - self.min) / levels
        max_len = len(str(bin(levels-1)[2:]))
        xx = []
        yy = []
        while cur_time < limit:
            xx.append(cur_time)
            apt = self.get_y(cur_time)
            yy.append(apt)
            num = abs(int(apt-self.min/gap))
            if num == levels:
                num -= 1
            f = '{0:0'+str(max_len)+'b}'
            nums.append(f.format(num))
            cur_time += time_step
        scatter(xx, yy)
        return nums

    def b8xs(self, binary):
        scrambled = binary.replace('00000000', '000VB0VB')
        plot_scrambled_binary(scrambled)
        return scrambled

    def hdb3(self, binary):
        converted = ''
        even = True
        while len(binary) >= 4:
            if binary[:4] == '0000':
                if even:
                    converted += '000V'
                    even = not even
                else:
                    converted += 'B00V'
                binary = binary[4:]
            else:
                if binary[0] == '1':
                    even = not even
                converted += binary[0]
                binary = binary[1:]
        return converted+binary


g = Sampling(0.5, 1, 1, 1)
g.sampling_graph(0.5)
binary = g.sample(0.5, 8, 10)
joint_bin = ''.join(binary)
print joint_bin
print g.b8xs(joint_bin)
print g.hdb3(joint_bin)

a = '1010000011000011000000'
print g.hdb3(a)
print a

import numpy as np
import re
from typing import List, NamedTuple
import matplotlib.pyplot as plt
from scipy import signal

# from collections import namedtuple
from typing import NamedTuple

with open("day10test.txt") as file:
    datatest = file.readlines()

with open("day10.txt") as file:
    data = file.readlines()

for d in data:
    print(d, end="")

test1 = "<5,   -3>"
rgx1 = r"<([\-0-9]+), ([ \-0-9]+)>"
output = list(re.match(rgx1, test1).groups())
print(output)


def processpoint(inputstr):
    rgx11 = r"position=<([ \-0-9]+),([ \-0-9]+)> velocity=<([ \-0-9]+),([ \-0-9]+)>"
    return [int(num) for num in list(re.match(rgx11, inputstr).groups())]


assert processpoint("position=< 1,  6> velocity=< 1,  0>") == [1, 6, 1, 0]
test10 = "position=< 5, 11> velocity=< 1, -2>\n"
rgx10 = r"position=<([ \-0-9]+),([ \-0-9]+)> velocity=< ([ \-0-9]+),([ \-0-9]+)>"
output = list(re.match(rgx10, test10).groups())
print(output)


class Light(NamedTuple):
    x: int
    z: int
    xvel: int
    zvel: int


def advance(a: Light) -> Light:
    return Light(a.xvel + a.x, a.zvel + a.z, a.xvel, a.zvel)


class Sky:
    def __init__(self, data):
        self.dataTuple = [Light(*processpoint(d)) for d in data if len(d) > 3]

    def evolve(self):
        self.dataTuple = [advance(d) for d in self.dataTuple]

    def printmax(self):
        minviewx = max(0, min(d.x for d in self.dataTuple))
        maxviewx = max(d.x for d in self.dataTuple) + 2
        maxviewz = max(d.z for d in self.dataTuple) + 2
        minviewz = max(0, min(d.z for d in self.dataTuple))
        nightsky = np.zeros((maxviewz, maxviewx), dtype=int)
        print(nightsky.shape, minviewz, maxviewz, minviewx, maxviewx)
        for d in self.dataTuple:
            xc = d.x
            zc = d.z
            if 0 <= xc < maxviewx and 0 <= zc < maxviewz:
                nightsky[zc, xc] += 1

        print("number of points in sky:", sum(sum(nightsky)))
        print("Ranges ", minviewx, minviewz, nightsky.shape)
        plt.imshow(nightsky[minviewz:maxviewz, minviewx:maxviewx], cmap="hot")
        plt.colorbar()
        plt.show()

    def max_view(self):
        return max((max([abs(d.x), abs(d.z)]) for d in self.dataTuple))


mysky = Sky(datatest)
mysky.evolve()
mysky.evolve()
mysky.evolve()
# mysky.printsky()


mybigsky = Sky(data)
listofmaxes = []
count = 0
for _ in range(10200):
    mybigsky.evolve()
    count += 1
    listofmaxes.append(mybigsky.max_view())


mybigsky.printmax()


for _ in range(12):
    for _ in range(10):
        mybigsky.evolve()
        count += 1
        print(count)
        listofmaxes.append(mybigsky.max_view())
    mybigsky.printmax()

print(np.argmin(np.array(listofmaxes)) + 1)

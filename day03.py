import numpy as np
import re
from collections import namedtuple

rgx = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"
test1 = "#67 @ 151,671: 11x15"
test2 = "#2277 @ 1,1: 11x15"


data = list(np.loadtxt("day03good.txt", delimiter="\n", comments="^", dtype=str))

print(data)


# print(id, x_lo, y_lo, width, height )


class Rectangle:
    id: int
    x_lo: int
    y_lo: int
    x_hi: int
    y_hi: int

    def __init__(self, id, x_lo, y_lo, x_hi, y_hi):
        self.id = id
        self.x_lo = x_lo
        self.y_lo = y_lo
        self.x_hi = x_hi
        self.y_hi = y_hi

    def reinit(self, id, x_lo, y_lo, x_hi, y_hi):
        self.id = id
        self.x_lo = x_lo
        self.y_lo = y_lo
        self.x_hi = x_hi
        self.y_hi = y_hi

    def __str__(self):
        return f"id is {self.id}, x_lo is {self.x_lo} y_lo is {self.y_lo}, x_hi is {self.x_hi}, y_hi is {self.y_hi}"

    def from_claim(self, claim: str):
        self.id, self.x_lo, self.y_lo, width1, height1 = [
            int(x) for x in re.match(rgx, claim).groups()
        ]
        self.x_hi = self.x_lo + width1
        self.y_hi = self.y_lo + height1


rec = Rectangle(0, 0, 0, 0, 0)
print(rec)
rec.from_claim(test1)
print(rec)
rec.reinit(0, 0, 0, 0, 0)
print(rec)
rec.from_claim(test2)
print(rec)

fabric = np.zeros((1000, 1000), dtype=int)
# print(fabric)

for d in data:
    print(d)
    rec.from_claim(d)
    print(rec)
    fabric[rec.x_lo : rec.x_hi, rec.y_lo : rec.y_hi] = (
        fabric[rec.x_lo : rec.x_hi, rec.y_lo : rec.y_hi] + 1
    )

count = 0
for row in fabric:
    for i in row:
        if i > 1:
            count += 1

print(count)


# find which claims are unique
for d in data:
    rec.from_claim(d)
    tile = fabric[rec.x_lo : rec.x_hi, rec.y_lo : rec.y_hi]
    # making sure tile is all ones which means that it is unquie
    flag = True
    for row in tile:
        for i in row:
            if i != 1:
                flag = False
    if flag == True:
        print(f"claim {rec.id} is unique")

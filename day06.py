import pandas
from itertools import product
import numpy as np
from collections import Counter


def argmax(listofmax) -> int:
    index, max_val = -100000, -1000000
    for i in range(len(listofmax)):
        if listofmax[i] > max_val:
            index, max_val = i, listofmax[i]
    return index


def argmin(listofmax) -> int:
    index, max_val = 10 ** 10, 10 ** 10
    for i in range(len(listofmax)):
        if listofmax[i] < max_val:
            index, max_val = i, listofmax[i]
    return index


array1 = np.loadtxt("day06.txt", delimiter=",", dtype="int")
x = array1[:, 0]
y = array1[:, 1]


points = [(xi, yi) for xi, yi in zip(x, y)]


def mandistance(a: (int, int), b: (int, int)) -> int:
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


assert mandistance((2, 3), (0, 0)) == 5
assert mandistance((2, 3), (1, 1)) == 3
assert mandistance((1, 1), (1, 1)) == 0

maxx = max(x) + 1
maxy = max(y) + 1

ABC = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f"}

print(x)
print(y)
print("look here", [mandistance((xi, yi), (1, 1)) for xi, yi in zip(x, y)])

print(maxy, maxx)

arrayofdistances = np.zeros((maxx, maxy), dtype=int)
for g, h in product(range(maxx), range(maxy)):
    listofdistances = [mandistance((xi, yi), (g, h)) for xi, yi in zip(x, y)]
    # print((g, h), listofdistances)
    minoflist = listofdistances[argmax([-i for i in listofdistances])]
    if sum([1 if minoflist == d else 0 for d in listofdistances]) > 1:
        arrayofdistances[g, h] = -1  # equa distance
    else:
        arrayofdistances[g, h] = argmax([-i for i in listofdistances])


print(arrayofdistances.T)


count1 = Counter
dictofpointstoarea = count1(list(arrayofdistances.reshape(arrayofdistances.size)))


def setofborders(mat):
    outputset = set()
    I, J = mat.shape
    for i in range(I):
        for j in range(J):
            if i == 0 or j == 0 or i == I - 1 or j == J - 1:
                # print(mat[i, j])
                outputset.add(mat[i, j])
    return outputset


infpoints = setofborders(arrayofdistances)
# infpoints.pop(-1)
# dictofpointstoarea.pop(-1)
print(infpoints)
print(dictofpointstoarea)
for i in infpoints:
    dictofpointstoarea[i] = 0

maxkey = max(dictofpointstoarea, key=dictofpointstoarea.get)

print(maxkey, dictofpointstoarea[maxkey])


arrayoftotaldiscance = np.zeros((maxx, maxy), dtype=int)
for g, h in product(range(maxx), range(maxy)):
    listofdistances = [mandistance((xi, yi), (g, h)) for xi, yi in zip(x, y)]
    # print((g, h), listofdistances)
    arrayoftotaldiscance[g, h] = 1 if sum(listofdistances) < 10000 else 0

print(arrayoftotaldiscance.T)

print(sum(sum(arrayoftotaldiscance)))

if setofborders(arrayoftotaldiscance) == {0, 1}:
    print("make bigger array")

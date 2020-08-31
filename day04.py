import numpy as np
import re
from typing import List

# from collections import namedtuple
from typing import NamedTuple

with open("day04.txt") as file:
    data = file.readlines()

print(data)
print(type(data))
print(len(data))
# data = list(np.loadtxt("day04.txt", delimiter="\n", dtype=str))

# rgx = "#([0-9]+) @ ([0-9]+),([0-9]+): ([0-9]+)x([0-9]+)"
# test1 = "#67 @ 151,671: 11x15"

test2 = "[123]"
rgx2 = r"\[([0-9]+)\]"
for i in re.match(rgx2, test2).groups():
    print(i)

test3 = "two words"
rgx3 = r"([A-Za-z0-9_]+) (\w+)"
for i in re.match(rgx3, test3).groups():
    print(i)

test1 = "[1518-08-19 00:00] Guard #2917 begins shift".lower().replace("#", "")
rgx1 = r"\[([0-9]+)-([0-9]+)-([0-9]+) ([0-9]+):([0-9]+)\] ([\w\s)]+)"
output = list(re.match(rgx1, test1).groups())
print(output)
# print(data[:5])


class Directive:
    def __init__(self, year, month, day, hour, minute, strdirective):
        self.year = int(year)
        self.month = int(month)
        self.day = int(day)
        self.hour = int(hour)
        self.minute = int(minute)
        self.strdirective = strdirective

    def __str__(self):
        return f"{self.month, self.day, self.hour, self.minute, self.strdirective}"

    def __repr__(self):
        return repr((self.month, self.day, self.hour, self.minute))

    @staticmethod
    def process(lineinput: str):
        lineinput = lineinput.lower().replace("#", "")
        print(lineinput)
        return Directive(*list(re.match(rgx1, lineinput).groups()))


mylist = []
for d in data:
    mylist.append(Directive.process(d))

# print([dirv.strdirective for dirv in mylist])

mylist2 = sorted(
    mylist,
    key=lambda Directive: (
        Directive.month,
        Directive.day,
        Directive.hour,
        Directive.minute,
    ),
)
for i in mylist2:
    print(i)


def yieldlist2():
    for i in mylist2:
        yield i


class Guardasleep(NamedTuple):
    pass


mygen = yieldlist2()

Gaurd_activity: List[List[int]] = []
which_gaurd: List[int] = []

rgxG = r"(\w+) ([0-9]+)"
rgxG = r"guard ([0-9]+) begins shift\n"
print("should be 2917", re.match(rgxG, "guard 123 begins shift\n").groups())


def argmax(listofmax) -> int:
    index, max_val = -1, -1
    for i in range(len(listofmax)):
        if listofmax[i] > max_val:
            index, max_val = i, listofmax[i]
    return index


assert argmax([1, 2, 3, 10, 6]) == 3
assert argmax([1, 12, 3, 10, 6]) == 1


while True:
    try:
        data = next(mygen)
    except StopIteration:
        break
    if data.strdirective[0] == "g":
        print(data.strdirective)
        number = int(re.match(rgxG, data.strdirective).groups()[0])
        print(number, type(number), type(which_gaurd))
        which_gaurd.append(number)
        Gaurd_activity.append([0 for _ in range(60)])
    if data.strdirective[0] == "f":
        begin1 = data.minute
        data = next(mygen)
        end1 = data.minute
        Gaurd_activity[-1][begin1:end1] = [
            x + y
            for x, y in zip(
                Gaurd_activity[-1][begin1:end1], [1 for _ in range(begin1, end1)]
            )
        ]
        print(Gaurd_activity[-1])

print(f"which_gaurd : {which_gaurd}")

# print("Gaurd_activity", Gaurd_activity)
mydict = {}

for g, activity in zip(which_gaurd, Gaurd_activity):
    if g in mydict.keys():
        mydict[g] = [i + j for i, j in zip(mydict[g], activity)]
    else:
        mydict[g] = activity

for g in mydict.keys():
    assert len(mydict[g]) == 60

for g in mydict.keys():
    print(g, max(mydict[g]))

for g in mydict.keys():
    print(g, (mydict[g]))

# listofmax = mydict[99]


dictoftotalasleep = {}

for g in mydict.keys():
    dictoftotalasleep[g] = sum(mydict[g])

print(dictoftotalasleep)

maxkey = max(dictoftotalasleep, key=dictoftotalasleep.get)
print("max key is ", maxkey)


index = argmax(mydict[maxkey])

print(f"The max index is {index}. For part 1 maxkey*index = {maxkey * index})")

dictofmaxminute = {}

for g in mydict.keys():
    dictofmaxminute[g] = max(mydict[g])

maxkey = max(dictofmaxminute, key=dictofmaxminute.get)

index = argmax(mydict[maxkey])

print(f"The max index is {index}. For part 2 maxkey*index = {maxkey * index})")

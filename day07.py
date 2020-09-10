import re
from typing import Dict, DefaultDict, List, Set
from collections import defaultdict

with open("day07.txt") as file:
    data = file.readlines()

# print(data)


test1 = "Step C must be finished before step A can begin."
rgx1 = r"Step (\w) must be finished before step (\w) can begin."
output = list(re.match(rgx1, test1).groups())
# print(output)

pairs = []

for d in data:
    pairs.append(list(re.match(rgx1, d).groups()))

for pair in pairs:
    print(pair)

letters: Set[str] = set()
for before, after in pairs:
    letters.add(before)
    letters.add(after)
print(letters)

graph = {}

for pair in pairs:
    if pair[0] in graph:
        graph[pair[0]].append(pair[1])
    else:
        graph[pair[0]] = [pair[1]]

for key in graph:
    graph[key] = sorted(graph[key])

for node in graph:
    print(node, graph[node])

requirements: DefaultDict[str, Set[str]] = defaultdict(lambda: set())
for letter in letters:
    requirements[letter] = set()

for letter in letters:
    flag = True

    while flag:
        flag = False
        for before, this in pairs:
            if (
                this in requirements[letter] or this == letter
            ) and before not in requirements[letter]:
                requirements[letter].add(before)
                flag = True


print("done")
for req in requirements:
    print(req, requirements[req])

# Find the list of things with no requirements

setletters = set(list(letters))
print("startletters", setletters)
print("start of while")
outputletters = []
counter: int = 0
while setletters:
    listofnoreqs = []
    for key, req in requirements.items():
        # print(key, req)
        if len(req) == 0:
            listofnoreqs.append(key)
    nextletter = min(listofnoreqs)

    print(f"The Next letter is {nextletter}")

    setletters.remove(nextletter)
    # print(setletters)
    del requirements[nextletter]
    for key, req in requirements.items():
        if nextletter in req:
            requirements[key] = {l for l in req if l != nextletter}
    outputletters.append(nextletter)
    # print(requirements)

print("".join(outputletters))

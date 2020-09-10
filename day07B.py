import re
from typing import Dict, DefaultDict, List, Set
from collections import defaultdict
from string import ascii_uppercase

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


ABCtime = dict(zip(list(ascii_uppercase), range(1 + 60, 27 + 60)))
print(ABCtime)

print("done")
for req in requirements:
    print(req, requirements[req])

# Find the list of things with no requirements
def delete_letter(setletters, requirements, nextletter):
    setletters.remove(nextletter)
    del requirements[nextletter]
    for key, req in requirements.items():
        if nextletter in req:
            requirements[key] = {l for l in req if l != nextletter}
    return setletters, requirements


setletters = set(list(letters))
print("startletters", setletters)
print("start of while")
outputletters = []
counter_sec: int = 0
workers = [[], [], [], [], []]
worklist = set()
while setletters:
    print(outputletters)
    # relase workers and remove letters
    for worker in workers:
        try:
            done = worker.pop()
            if len(worker) == 0:
                setletters, requirements = delete_letter(setletters, requirements, done)
                outputletters.append(done)
                worklist.remove(done)
        except IndexError:
            pass

    # Find letters that have no requirments
    listofnoreqs = []
    for key, req in requirements.items():
        # print(key, req)
        if len(req) == 0:
            listofnoreqs.append(key)

    listofnoreqs = [req for req in listofnoreqs if req not in worklist]

    for iworker, worker in enumerate(workers):
        if len(worker) == 0:
            try:
                nextletter = min(listofnoreqs)
                print(f"getting {nextletter}")
                workers[iworker] = [nextletter for _ in range(ABCtime[nextletter])]
                worklist.add(nextletter)
                # setletters, requirements = delete_letter(
                #    setletters, requirements, nextletter
                # )
                listofnoreqs = [req for req in listofnoreqs if req != nextletter]
            except ValueError:
                print("good ValueError")
                pass

    print(workers)

    # setletters, requirements = delete_letter(setletters, requirements, nextletter)

    counter_sec += 1

counter_sec -= 1
print(counter_sec)
print("".join(outputletters))

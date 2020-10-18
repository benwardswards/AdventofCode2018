from typing import List

plants = list("#..#.#..##......###...###")

commands = """...## => #
..#.. => #
.#... => #
.#.#. => #
.#.## => #
.##.. => #
.#### => #
#.#.# => #
#.### => #
##.#. => #
##.## => #
###.. => #
###.# => #
####. => #"""

plants = list(
    ".##.##...#.###..#.#..##..###..##...####.#...#.##....##.#.#...#...###.........##...###.....##.##.##"
)

commands = """##... => .
#...# => .
.###. => #
.##.# => #
#.... => .
..##. => #
##..# => #
.#... => #
.#.## => #
#.### => #
.#..# => .
##.#. => #
..#.. => .
.##.. => #
###.# => .
.#### => .
##### => .
#.#.. => #
...## => #
...#. => .
###.. => .
..... => .
#.#.# => .
##.## => #
#.##. => #
####. => #
#..#. => #
.#.#. => .
#..## => #
....# => .
..#.# => #
..### => ."""


def padstring(plantstring: List[str], beforeadd: int, endadd: int):
    for _ in range(beforeadd):
        plantstring.insert(0, ".")
    for _ in range(endadd):
        plantstring.append(".")
    return plantstring


assert padstring(list("#.#"), 2, 1) == list("..#.#.")


dcom = [list(line)[:5] for line in commands.split("\n") if line[-1] == "#"]
# assert len(dcom) == 14

for com in dcom:
    print(com)


def nextstep(instring, d_commands):
    if (
        instring[0] != "."
        or instring[1] != "."
        or instring[-1] != "."
        or instring[-2] != "."
    ):
        print("error add more padding")
        assert 0
    # print("test", d_commands[0])
    # print("starting", instring)
    outstring = ["." for _ in instring]
    for i in range(2, len(instring) - 2):
        teststring = list(instring[(i - 2) : (i + 3)])
        assert len(teststring) == 5
        for com in d_commands:
            if all([a == b for a, b in zip(com, teststring)]):
                outstring[i] = "#"
    return outstring


# assert nextstep(list("..#.."), dcom) == list("..#..")
# assert nextstep(list("..#.."), dcom) == list("..#..")
# assert nextstep(list("....."), dcom) == list(".....")

start_pad = 10
plants_part1 = padstring(plants, start_pad, 20)
for i in range(20):
    print("".join(plants_part1), i)
    # printplants_part1 )
    plants_part1 = nextstep(plants_part1, dcom)

plant_id_sum = sum(ip - start_pad for ip, p in enumerate(plants_part1) if p == "#")
print("part 1: The plant number summ is ", plant_id_sum)


pad = 0
plants = padstring(plants, pad, 0)
sum_score_at_step = []
print("Image is shifted by backwards 1 at each time step")
for i in range(200):
    print("".join(plants), i)
    # print(plants)
    plants = padstring(plants[1:], 0, 1)
    pad += -1
    plants = nextstep(plants, dcom)
    sum_score_at_step.append(
        sum([i - pad - 10 for i, p in enumerate(plants) if p == "#"])
    )

print("part 2: The plant number sum after 200 steps is ", sum_score_at_step[-1])


print(
    "The pattern stays the same but shifts one to the right. There are five plants each sifts to the right by 1 per turn. "
)

print("part2: (50000000000 - 200) * 5 + 1219 =")
delta = sum_score_at_step[-1] - sum_score_at_step[-2]
print((50000000000 - 200) * delta + sum_score_at_step[-1])


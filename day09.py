"411 players; last marble is worth 71170 points"
from typing import List
from typing import Deque
from collections import deque

deque1 = deque((i for i in range(10)))
deque1.rotate(3)

deque1.append(99)
deque1.appendleft(100)
print(deque1)

# Game is too slow so I converted the list to a deque and it ran inifinetly faster.
class Game:
    def __init__(self, numberofplayers: int):
        self.numberofplayers: int = numberofplayers
        self.gamelist: List[int] = []  # clockwise circle
        self.score = numberofplayers * [0]
        self.current_index = 0

    def insert(self, player: int, turn: int):
        if turn % 23 == 0 and turn != 0:
            remove_index = (self.current_index - 7) % len(self.gamelist)
            # print(
            #    f" curent index is {self.current_index} len of game list is {len(self.gamelist) } insert index is {remove_index }"
            # )
            # print(f"removed {self.gamelist[remove_index]}")
            self.score[player - 1] += turn + self.gamelist[remove_index]
            self.gamelist.pop(remove_index)
            self.current_index = remove_index % len(self.gamelist)
            # print(self.score)
        else:
            if len(self.gamelist) == 0:
                insert_index = 0
            elif len(self.gamelist) == 1:
                insert_index = 1
            else:
                insert_index = (self.current_index + 1) % len(self.gamelist) + 1
            # print(
            #    f" curent index is {self.current_index} len of game list is {len(self.gamelist) } insert index is {insert_index }"
            # )
            self.gamelist.insert(insert_index, turn)
            self.current_index = insert_index

    def __repr__(self):
        return f"{self.current_index}{self.gamelist}"


class Game2:
    def __init__(self, numberofplayers: int):
        self.numberofplayers: int = numberofplayers
        self.gamelist: Deque[int] = deque()  # clockwise circle
        self.score = numberofplayers * [0]
        self.current_index = 0

    def insert(self, player: int, turn: int):
        if turn % 23 == 0 and turn != 0:
            self.gamelist.rotate(7)
            self.score[player - 1] += turn + self.gamelist.pop()
            self.gamelist.rotate(-1)
            # print(turn, self.score)
        else:
            self.gamelist.rotate(-1)
            self.gamelist.append(turn)
        # print(f"{self.gamelist}")

    def __repr__(self):
        return f"{self.current_index}{self.gamelist}"


def rungame2(numplayers: int, lastmarble: int) -> int:
    game9 = Game2(numplayers)
    for turn in range(lastmarble + 1):
        player = ((turn - 1) % numplayers) + 1
        game9.insert(player, turn)
        # print(player, turn, game9)

    # print(game9.score)
    return max(game9.score)


rungame2(9, 26) == 32
# assert 0
assert rungame2(10, 1618) == 8317
assert rungame2(13, 7999) == 146373
assert rungame2(30, 5807) == 37305
assert rungame2(21, 6111) == 54718
assert rungame2(17, 1104) == 2764
print("rungame2(411, 71170) =", rungame2(411, 71170))
print("rungame2(411, 7117000) =", rungame2(411, 7117000))

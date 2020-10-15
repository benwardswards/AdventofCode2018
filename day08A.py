import csv
from typing import List

with open("day08.txt") as csv_file:
    dataliststr = list(csv.reader(csv_file, delimiter=" "))[0]

datalist: List[int] = [int(ch) for ch in dataliststr]

print("len(datalist)=", len(datalist))
print(datalist)


class TreeFromList:
    # static variable
    metacumsum: int = 0

    def __init__(self, data):
        self.value = 0
        self.number_subnodes: int = data.pop(0)
        self.number_metadata: int = data.pop(0)
        print(f"num nodes {self.number_subnodes} metadata= {self.number_metadata}")
        self.subnodes: List[TreeFromList] = []
        self.metadata: List[int] = []

        # list of nodes are printed inorder
        for _ in range(self.number_subnodes):
            self.subnodes.append(TreeFromList(data))

        # meta data is printed postorder
        for _ in range(self.number_metadata):
            nextmeta: int = data.pop(0)
            self.metadata.append(nextmeta)
            TreeFromList.metacumsum += nextmeta

    # print(f"list of meta data is {self.metadata}")

    def valueTraverse(self):
        self.value = 0
        if self.number_subnodes == 0:
            if self.number_metadata > 0:
                self.value = sum(self.metadata)

        else:
            for index in self.metadata:
                if index <= self.number_subnodes:
                    self.value += self.subnodes[index - 1].valueTraverse()
                    print(
                        "cum sum=",
                        self.value,
                        "metadata=",
                        self.metadata,
                        "index-1=",
                        index - 1,
                        "number_subnodes=",
                        self.number_subnodes,
                    )

        return self.value


def main():
    master = TreeFromList(datalist)
    print(f"The answer to part B is {master.valueTraverse()}")
    print(f"The answer to part A {master.metacumsum}")


if __name__ == "__main__":
    main()


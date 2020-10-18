import numpy as np
from scipy.signal import convolve2d


def fuel(x, y, gridserialnumber):
    temp = (x + 10) * y + gridserialnumber
    temp1 = temp * (x + 10)
    # print(temp1)
    digit = int(list(str(temp1))[-3]) if temp1 >= 100 else 0
    return digit - 5


assert fuel(3, 5, 8) == 4
assert fuel(122, 79, 57) == -5
assert fuel(101, 153, 71) == 4
assert fuel(217, 196, 39) == 0


class FuelTank:
    def __init__(self, listsize, serialnumber):
        self.serialnumber: int = serialnumber
        self.listsize: int = listsize
        self.fuel_array = np.array(
            [
                [fuel(i, j, self.serialnumber) for i in range(1, listsize + 1)]
                for j in range(1, listsize + 1)
            ]
        )

    def findmax(self):
        """Finds the max fuel cell location with 3x3 fuel cell array size."""
        sumsize = 3
        dataconv = convolve2d(
            self.fuel_array, np.ones((sumsize, sumsize)), mode="valid"
        )
        print(dataconv.shape)
        ind = np.unravel_index(np.argmax(dataconv, axis=None), dataconv.shape)
        print(
            f"(maxarg of {self.serialnumber} is {ind[1]+1},{ind[0]+1} with {dataconv[ind]} fuel"
        )

    def findsupermax(self):
        """prints the location of the max fuel cell, for fuel cell array size 1-300"""
        maxdata = []
        for sumsize in range(1, self.listsize + 1):
            dataconv = convolve2d(
                self.fuel_array, np.ones((sumsize, sumsize)), mode="valid"
            )
            # print(dataconv.shape)
            ind = np.unravel_index(np.argmax(dataconv, axis=None), dataconv.shape)
            maxdata.append((ind[1] + 1, ind[0] + 1, sumsize, dataconv[ind]))
        # print("maxdata", maxdata)
        ind2 = np.argmax(np.array([d[3] for d in maxdata]))
        print("max fuelsize array", 1 + ind2)
        print("location, array size, max fuel,", maxdata[ind2])


listsize: int = 300
gridserialnumber: int = 18

listsize = 300
serialnumber = 18
tank = FuelTank(listsize, serialnumber)
tank.findmax()
# tank.findsupermax()

# print(convolve2d(np.ones((7, 7)), np.ones((3, 3)), mode="valid"))

# fuel_array = [[fuel(i, j, 10) for i in range(1, 2)] for j in range(1, 10)]

# print("fuel_array", fuel_array)

serialnumber = 42
print(f"serialnumber {serialnumber}")
tank = FuelTank(listsize, serialnumber)
print("Caclulating max...")
tank.findmax()
# tank.findsupermax()


serialnumber = 7165
print(f"serialnumber {serialnumber}")
tank = FuelTank(listsize, serialnumber)
print("Caclulating max...")
tank.findmax()
print("Caclulating supermax...")
tank.findsupermax()

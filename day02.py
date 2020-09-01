import numpy as np

data = np.loadtxt("day02.txt", delimiter=" ", dtype=str)
# data1 = ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]
# print(data)


def count2and3(listoflabels):
    count2s = 0
    count3s = 0
    for ilabel in listoflabels:
        dict = {}
        for i in ilabel:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1

        for _, value in dict.items():
            if value == 2:
                count2s += 1
                break

        for _, value in dict.items():
            if value == 3:
                count3s += 1
                break

        print(dict, count2s * count3s)


# count2and3(data1)

count2and3(data)


data2 = ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]


def difby1(str1, str2):
    stringreturn = ""
    countdifs = 0
    if len(str1) != len(str2):
        return "0"

    for i, j in zip(str1, str2):
        if i != j:
            countdifs += 1

    if countdifs == 1:
        for i, j in zip(str1, str2):
            if i == j:
                stringreturn = stringreturn + i
    else:
        stringreturn = "0"

    # print(stringreturn)
    return stringreturn


difby1("fghij", "fguij")


def findbox(listoflabels):
    for str1 in listoflabels:
        for str2 in listoflabels:
            if difby1(str1, str2) != "0":
                print("The box of stuff is", difby1(str1, str2))
                break


findbox(data)

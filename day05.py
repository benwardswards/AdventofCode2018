from string import ascii_lowercase

test1 = "dabAcCaCBAcCcaDA\n"

input1 = list(test1)


def isReduction(a: str, b: str) -> bool:
    assert len(a) == 1
    assert len(b) == 1
    if a.lower() == a and b.upper() == b and a == b.lower():
        return True
    elif a.upper() == a and b.lower() == b and a.lower() == b:
        return True
    else:
        return False


assert isReduction("a", "A")
assert isReduction("A", "a")
assert isReduction("a", "a") == False
assert isReduction("b", "a") == False
assert isReduction("A", "A") == False


def redux(test: str) -> int:
    input1 = list(test)
    counter = 0
    while counter + 1 < len(input1):
        if isReduction(input1[counter], input1[counter + 1]):
            input1.pop(counter)
            input1.pop(counter)
            counter = max(counter - 1, 0)
        else:
            counter = counter + 1
    # print(input1)
    if len(input1) > 0 and input1[-1] == "\n":
        return len(input1) - 1
    else:
        return len(input1)


assert redux(test1) == 10
assert redux("aA") == 0
assert redux("abBA") == 0

assert redux("aabAAB") == len("aabAAB")


with open("day05.txt") as file:
    data = file.readline()

print(len(data), redux(data))
print(len("\n"))

data1 = "dabAcCaCBAcCcaDA"


def letter_remove_redux(sequence: str) -> (str, int):
    dict_letter_remove_redux = {}

    for letter in list(ascii_lowercase):
        noletter_data = sequence.replace(letter, "").replace(letter.upper(), "")
        dict_letter_remove_redux[letter] = redux(noletter_data)

    print(dict_letter_remove_redux)

    minkey = min(dict_letter_remove_redux, key=dict_letter_remove_redux.get)

    return minkey, dict_letter_remove_redux[minkey]


print(letter_remove_redux(data1))
print(letter_remove_redux(data))

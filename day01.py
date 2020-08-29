import numpy as np


testdata1 = [1,1,1]
testdata2 = [1,1,-2]
testdata3 = [-1,-2,-3]

def frequencychange(startcounter, freqinput):
    counter = startcounter
    for idata in freqinput:
        counter = counter + idata
    print("Counter is :", counter)
    return counter

frequencychange(0 ,testdata1)
frequencychange(0 ,testdata2)
frequencychange(0 ,testdata3)


data = np.loadtxt("day01.txt", delimiter=" ")

print("Now operatoring on the test data")
frequencychange(0 ,data)

##part2

    
def frequencychangedouble(startcounter, freqinput):
    counter = startcounter
    listoffreqs = [startcounter]
    flagbreak = True
    while flagbreak:
        print(counter)
        for idata in freqinput:
            counter = counter + idata
            if counter in listoffreqs:
                print("first reaches ", counter, " twice")
                flagbreak = False
                break
            listoffreqs.append(counter)
        
    print("Counter is :", counter)
    return counter

input1 = [1,-1]
input2 = [3,3,4,-2, -4]
input3 = [-6, 3, 8, 5, -6]
input4 = [+7, +7, -2, -7, -4]
frequencychangedouble(0, input1)
frequencychangedouble(0, input2)
frequencychangedouble(0, input3)
frequencychangedouble(0, input4)

frequencychangedouble(0, data)
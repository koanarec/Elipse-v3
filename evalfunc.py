import math
import matplotlib.pyplot as plt
import ast


# This will take a string of a list (of a creature) and return its function as a string
def peristring(small, big):
    answer = open("peri.txt", 'r')
    answer = answer.readline()
    answer = eval(answer)
    a = answer
    lcv1 = 0
    form = ""
    for x in a:
        lcv2 = 0
        for y in x:
            # print(lcv1, lcv2)

            if a[lcv1][lcv2] != 0:
                form = form + str(str(a[lcv1][lcv2]) + "*a**" + str(lcv1- len(answer)//2) + "*b**" + str(lcv2- len(answer)//2) + "+")
            lcv2 = lcv2 + 1
        lcv1 = lcv1 + 1
    form = form[:len(form) - 1]
    return (form)


# This takes a formula as a string and then executes it. THe formula is for the perimiter of an elipse and
# a and b are dimentions of the elipse. Peristring is just the formula
def peri(peristring, a,b):
    newss = ""
    lcv = -1
    forms = split(peristring)
    for cell in forms:
        lcv = lcv + 1
        if cell == "a":
            newss = newss + str(b)
        elif cell == "b":
            newss = newss + str(a)
        else:
            newss = newss + str(forms[lcv])

    newss = "1 * (" + newss + ")"
    fish = abs(eval(newss))
    print(fish)
    return fish

def split(word):
    return [char for char in word]


# Calculates the real value of the perimiter of an elipse
def elipper(a, b):
    import math
    h = (a - b) ** 2 / (a + b) ** 2
    c = math.pi * (a + b)
    x = 0
    tot = 1
    while x < 10:
        x = x + 1
        tot = tot + (1 / 4 ** x) * h ** x
    return tot * c

def plot():
    x = 100
    mine = []
    his = []
    real  = []
    while x < 1000:
        b = 100
        x = x + 30
        a = x

        # This is a formula for the perimiter of an elipse from history
        his.append((2 * math.pi * math.sqrt((a **2 + b ** 2)/2)))
        #his.append(((a-b)**2) / ((a+b) ** 2))
        peristrings = peristring(a, b)
        dog = peri(peristrings, a, b)
        print(dog)

        #This is my estimation
        mine.append(dog)
        
        real.append(elipper(a,b))

        plt.plot(real)
        plt.plot(his)
        plt.plot(mine)

        plt.draw()
        plt.pause(0.00001)
        plt.clf()

    plt.plot(real)
    plt.plot(his)
    plt.plot(mine)
    plt.draw()
    plt.pause(1000000000000)

plot()
print(peristring(10,100))
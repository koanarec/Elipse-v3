#import random
import matplotlib.pyplot as plt
import copy
import random
import itertools
import keyboard
import ast
import time
import numpy

def fixlist(a):
    new = ""
    final = ""
    bb = copy.deepcopy(a)
    bb = bb.split()
    for x in bb:
        a_string = str(copy.deepcopy(x))
        if a_string[len(a_string)-2:] == "]]":
            a_string = str(eval(a_string[:len(a_string)-2]))+"]]"
        elif a_string[len(a_string)-2:] == "],":
            a_string = str(eval(a_string[:len(a_string) - 2])) + "],"
        elif a_string[0] == "[" and a_string[1] == "[":
            a_string = "[[" + str(eval(a_string[2:len(a_string) - 1])) + ","
        elif a_string[0] == "[" and a_string[len(a_string)-1] == ",":
            a_string = "[" + str(eval(a_string[1:len(a_string) - 1])) + ","
        else:
            a_string = str(eval(a_string[:len(a_string)-1]))+","
        new = new + a_string

    return(ast.literal_eval(new))

#dfk = fixlist("[[0, 7, 1, -4, -3, -4, -4, 0, -3], [3, 0, 5, 2, 2, -1, -7, -3, -1], [0, 6, -5, -1, -7, 6, 4, 2, 5], \
  #       [0, -1, 3, 7, -3, -1, -1, 0, 699], [-2, 3, 0, -2, 4, 3, -5, 6, 49], [3, 6-1, 5, 0, 6, -1, -89, 31, -1], \
   #      [5, 4, -3, 8, 8, -6, -299, 5, 0], [0, -1, 3, 4, 31, 3, -5, 0, 0], [6, 9, -2, 5, 5392, -44, 0, 0, 0]]")

#print(dfk)
#breakpoint()
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


class Creature:
    def __init__(self, guts=[]):
        self.__guts = guts

    def return_fitness(self):
        tests = 0
        finslist = []
        while tests < 1000:
            tests = tests + 15
            answer = elipper(100, tests)
            guess = 0
            for x, y in itertools.product(range(0, len(self.__guts)), range(0, len(self.__guts))):
                guess = guess + self.__guts[x][y] * 100 ** (x - (len(self.__guts)) // 2) * tests ** (
                            y - (len(self.__guts)) // 2)
            # print(-(abs(answer - guess)))
            # print(answer, guess, ((abs(answer - guess))))
            finslist.append((abs(answer - guess)))
        totals = 0
        for x in finslist:
            totals += x
        #print(-(totals // len(finslist)))
        return -(totals // len(finslist))

    def __lt__(self, other):
        return self.return_fitness() > other.return_fitness()

    # for index, value in numpy.ndenumerate(self.__guts):
    def evolve(self):
        save = open("temp.txt", "w")
        save.write(str(creatures[0].return_guts()))
        save.close()

        a = open('temp.txt', 'r')
        b = a.readline()
        srr = ""
        lcv = 0
        for x in b:
            adds = int(random.randint(-1, 1))
            if x in "0123456789" and random.randint(0,100)>99 and adds != 0:
                origonal = int(b[lcv])
                # print(type(adds),type(origonal))
                news = int(adds + origonal)
                z = str(news)

                srr = srr + z

            else:

                z = str(b[lcv])
                if len(z) > 1:
                    print(z)
                srr = srr + z

            lcv = lcv + 1
        try:
            self.__guts = copy.deepcopy(ast.literal_eval(srr))
        except:
            try:
                self.__guts = copy.deepcopy(fixlist(srr))
            except:
                print("failed to update guts", str(srr))
        a.close()


    def __str__(self):
        return str(self.return_fitness())

    def __int__(self):
        return int(self.return_fitness())

    def return_guts(self):
        return str(self.__guts)


def print_graph(creatures):
    all_stengths = 0
    for x in creatures:
        all_stengths = all_stengths + x.return_fitness()
    all_stengths = all_stengths // len(creatures)

    # print(creatures[0].return_fitness())

    av_vals.append(all_stengths)
    max_vals.append(creatures[0].return_fitness())
    alex = (creatures[0].return_fitness())
    min_vals.append(creatures[len(creatures) - 1].return_fitness())

    plt.plot(max_vals)
    plt.title(str(alex))
    # plt.plot(min_vals)
    # plt.plot(av_vals)

    plt.draw()
    plt.pause(0.00001)
    plt.clf()





number_of_creatures = 16
try:
    a = open('peri.txt', 'r')
    b = a.readline()
    b = ast.literal_eval(b)
    a.close()
except:
    # 8 = 69
    seb = [0, 0, 0, 0, 0,0,0,0,0, 0, 0, 0, 0]
    b = []
    for x in seb:
        b.append(seb)

creatures = []
lcv = 32
while lcv > 0:
    lcv = lcv - 1
    creatures.append(Creature(b))

max_vals = []
min_vals = []
av_vals = []
lcv = 0
while lcv < 10000000000000:
    lcv = lcv + 1
    creatures.sort()

    save = open("peri.txt", "w")
    save.write(str(creatures[0].return_guts()))
    save.close()

    print_graph(creatures)

    best_quater = copy.deepcopy(creatures[:len(creatures) // 4])
    upper_quartile = copy.deepcopy(creatures[len(creatures) // 4:(len(creatures) // 4) * 2])

    creatures.clear()
    del creatures[:]
    creatures = []

    for x in best_quater:
        creatures.append(x)
        temp = copy.deepcopy(x)
        temp.evolve()
        creatures.append(temp)
    for x in upper_quartile:
        creatures.append(x)
        temp = copy.deepcopy(x)
        temp.evolve()
        creatures.append(temp)

    if keyboard.is_pressed('q'):
        max_vals = []
        min_vals = []
        av_vals = []

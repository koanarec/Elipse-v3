import matplotlib.pyplot as plt
import copy
import random
import itertools
import keyboard
import ast


# This function takes a string representation of a list and then finds all of the elements that have not been calculated
# for example; "1+1" will turn into 2. It returns a list
def fix_list(list_to_fix):
    new = ""
    bb = copy.deepcopy(list_to_fix)
    bb = bb.split()
    for part_of_string_of_list in bb:
        a_string = str(copy.deepcopy(part_of_string_of_list))
        if a_string[len(a_string) - 2:] == "]]":
            a_string = str(eval(a_string[:len(a_string) - 2])) + "]]"
        elif a_string[len(a_string) - 2:] == "],":
            a_string = str(eval(a_string[:len(a_string) - 2])) + "],"
        elif a_string[0] == "[" and a_string[1] == "[":
            a_string = "[[" + str(eval(a_string[2:len(a_string) - 1])) + ","
        elif a_string[0] == "[" and a_string[len(a_string) - 1] == ",":
            a_string = "[" + str(eval(a_string[1:len(a_string) - 1])) + ","
        else:
            a_string = str(eval(a_string[:len(a_string) - 1])) + ","
        new = new + a_string
    return ast.literal_eval(new)


# This function will return the real perimiter of an elipse
def elipper(a, b):
    import math
    h = (a - b) ** 2 / (a + b) ** 2
    c = math.pi * (a + b)
    counter_for_infinite_series = 0
    tot = 1
    while counter_for_infinite_series < 10:
        counter_for_infinite_series = counter_for_infinite_series + 1
        tot = tot + (1 / 4 ** counter_for_infinite_series) * h ** counter_for_infinite_series
    return tot * c


# This class holds the each formula to calculate the perimeter and mess about with it
class Creature:
    def __init__(self, guts):
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
            finslist.append((abs(answer - guess)))
        totals = 0
        for x in finslist:
            totals += x
        return -(totals // len(finslist))

    def __lt__(self, other):
        return self.return_fitness() > other.return_fitness()

    def evolve(self):
        saves = open("temp.txt", "w")
        saves.write(str(creatures[0].return_guts()))
        saves.close()

        a = open('temp.txt', 'r')
        b = a.readline()
        srr = ""
        lcv = 0
        for x in b:
            adds = int(random.randint(-1, 1))
            if x in "0123456789" and random.randint(0, 100) > 99 and adds != 0:
                origonal = int(b[lcv])
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
                self.__guts = copy.deepcopy(fix_list(srr))
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


# This initalizes the loop and imports the best creature from before, it will generate new creatures if it cannot
# import the old ones
number_of_creatures = 16
try:
    a = open('peri.txt', 'r')
    b = a.readline()
    b = ast.literal_eval(b)
    a.close()
except:
    # 8 = 69
    seb = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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

    # This saves the best animal in a text file
    save = open("peri.txt", "w")
    save.write(str(creatures[0].return_guts()))
    save.close()

    print_graph(creatures)


    # This isn't very good. It chooses which creatures to kill, evolve and replicate
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

    # This can reset the graph that you look at just to help read changes
    if keyboard.is_pressed('q'):
        max_vals = []
        min_vals = []
        av_vals = []

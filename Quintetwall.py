from random import *
import itertools
import bisect
seed()

#
#
# Type foo() and wait...10 seconds?
#
#

Wzero = 12
Wfive = 21
Wtens = 16

def foo():
    h = [0,0,0,0,0,0,0,0,0,0,0,0]
    step = 0
    for i in range(0,100000):
        step+=1
        shield = 0
        Wz = Wzero
        Wf = Wfive
        Wt = Wtens

        for j in range(0,5):
            t = randomweight(Wz,Wt,Wf)
            if t == "Zero":
                shield+=0
                Wz -= 1
            if t == "Ten":
                shield+=10
                Wt -= 1
            if t == "Five":
                shield+=5
                Wf -= 1

        if   shield == 0:  h[0]+=1
        elif shield == 5:  h[1]+=1
        elif shield == 10: h[2]+=1
        elif shield == 15: h[3]+=1
        elif shield == 20: h[4]+=1
        elif shield == 25: h[5]+=1
        elif shield == 30: h[6]+=1
        elif shield == 35: h[7]+=1
        elif shield == 40: h[8]+=1
        elif shield == 45: h[9]+=1
        elif shield == 50: h[10]+=1

    print("Results after calling {} Quintet Walls\n".format(step))
    for i in range (0,11):
        print("{}000 shield: {}%".format(i*5,h[i]/1000))

def randomweight(wz,wt,wf):
    weighted_choices = [('Zero', wz), ('Ten', wt), ('Five', wf)]
    population = [val for val, cnt in weighted_choices for i in range(cnt)]
    choice(population)
    choices, weights = zip(*weighted_choices)
    cumdist = list(itertools.accumulate(weights))
    x = random() * cumdist[-1]
    return (choices[bisect.bisect(cumdist, x)])

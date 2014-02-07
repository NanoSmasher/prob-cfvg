import math
from fractions import *
from Ride import *

maxi_1 = 0
g1_1 = 0
g2_1 = 0
g3_1 = 0
maxi_2 = 0
g1_2 = 0
g2_2 = 0
g3_2 = 0
maxi_3 = 0
g1_3 = 0
g2_3 = 0
g3_3 = 0
maxi_4 = 0
g1_4 = 0
g2_4 = 0
g3_4 = 0
maxi_5 = 0
g1_5 = 0
g2_5 = 0
g3_5 = 0

def Clean():
    global maxi_1, g1_1, g2_1, g3_1
    global maxi_2, g1_2, g2_2, g3_2
    global maxi_3, g1_3, g2_3, g3_3
    global maxi_4, g1_4, g2_4, g3_4
    global maxi_5, g1_5, g2_5, g3_5
    maxi_1 = 0
    g1_1 = 0
    g2_1 = 0
    g3_1 = 0
    maxi_2 = 0
    g1_2 = 0
    g2_2 = 0
    g3_2 = 0
    maxi_3 = 0
    g1_3 = 0
    g2_3 = 0
    g3_3 = 0
    maxi_4 = 0
    g1_4 = 0
    g2_4 = 0
    g3_4 = 0
    maxi_5 = 0
    g1_5 = 0
    g2_5 = 0
    g3_5 = 0

def Complete (tot,a,b,c):
    global maxi_1, g1_1, g2_1, g3_1
    global maxi_2, g1_2, g2_2, g3_2
    global maxi_3, g1_3, g2_3, g3_3
    global maxi_4, g1_4, g2_4, g3_4
    global maxi_5, g1_5, g2_5, g3_5
    if tot > maxi_1:
        maxi_5 = maxi_4
        g1_5 = g1_4
        g2_5 = g2_4
        g3_5 = g3_4
        maxi_4 = maxi_3
        g1_4 = g1_3
        g2_4 = g2_3
        g3_4 = g3_3
        maxi_3 = maxi_2
        g1_3 = g1_2
        g2_3 = g2_2
        g3_3 = g3_2
        maxi_2 = maxi_1
        g1_2 = g1_1
        g2_2 = g2_1
        g3_2 = g3_1
        maxi_1 = tot
        g1_1 = a
        g2_1 = b
        g3_1 = c
    elif tot > maxi_2:
        maxi_5 = maxi_4
        g1_5 = g1_4
        g2_5 = g2_4
        g3_5 = g3_4
        maxi_4 = maxi_3
        g1_4 = g1_3
        g2_4 = g2_3
        g3_4 = g3_3
        maxi_3 = maxi_2
        g1_3 = g1_2
        g2_3 = g2_2
        g3_3 = g3_2
        maxi_2 = tot
        g1_2 = a
        g2_2 = b
        g3_2 = c
    elif tot > maxi_3:
        maxi_5 = maxi_4
        g1_5 = g1_4
        g2_5 = g2_4
        g3_5 = g3_4
        maxi_4 = maxi_3
        g1_4 = g1_3
        g2_4 = g2_3
        g3_4 = g3_3
        maxi_3 = tot
        g1_3 = a
        g2_3 = b
        g3_3 = c
    elif tot > maxi_4:
        maxi_5 = maxi_4
        g1_5 = g1_4
        g2_5 = g2_4
        g3_5 = g3_4
        maxi_4 = tot
        g1_4 = a
        g2_4 = b
        g3_4 = c
    elif tot > maxi_5:
        maxi_5 = tot
        g1_5 = a
        g2_5 = b
        g3_5 = c

def targetf(a,b,c,text="norm"):
    if text == "gen1":
        tot = Gen1Ride(a,b,c)
    elif text == "gen2":
        tot = Gen2Ride(a,b,c)
    elif text == "gen4":
        tot = Gen4Ride(a,b,c)
    else:
        tot = BasicRide(a,b,c)
    return tot

def CheckAll(text = "norm"):
    '''
    options:
        norm, gen1, gen2
    '''
    combined = 0
    global maxi_1, g1_1, g2_1, g3_1
    global maxi_2, g1_2, g2_2, g3_2
    global maxi_3, g1_3, g2_3, g3_3
    global maxi_4, g1_4, g2_4, g3_4
    global maxi_5, g1_5, g2_5, g3_5
    for a in range(1,32):
        for b in range(1,32):
            for c in range(1,32):
                if (a+b+c == 32) & (a>4) & (b>4):
                    combined+=1
                    tot = targetf(a,b,c,text)
                    Complete(tot,a,b,c)
    print("Based on {} different grade ratios".format(combined))
    print("The top 5 (ordered gr1-gr2-gr3) for highest ride consistency are:")
    print("1st {}-{}-{} at {}%".format(g1_1,g2_1,g3_1,round(float(maxi_1)*100,5)))
    print("2nd {}-{}-{} at {}%".format(g1_2,g2_2,g3_2,round(float(maxi_2)*100,5)))
    print("3rd {}-{}-{} at {}%".format(g1_3,g2_3,g3_3,round(float(maxi_3)*100,5)))
    print("4th {}-{}-{} at {}%".format(g1_4,g2_4,g3_4,round(float(maxi_4)*100,5)))
    print("5th {}-{}-{} at {}%".format(g1_5,g2_5,g3_5,round(float(maxi_5)*100,5)))
    print("\nCreated by the Brampton Booster\n")
    Clean()

def main():
    print("Command: CheckAll()")
    print("-----modifiers-----")
    print("     norm: Regular, non-supported grade ratios")
    print("     gen1: 4 copies of Lox/Ergodiel chain support")
    print("     gen2: 4 copies of Stern/PBD chain support")
    print("     gen4: 4 copies of Artemis chain support")

if __name__ == '__main__':
    main()

import math
from fractions import *

################################################################################
#
#    Start of Calculations.
#
#
#    The methodology of how compareTrig finds thes values is done like this:
#
#        We break it down into individual sets
#    > Two possible attack formations, R>V>R and V>R>R-P*,
#        (since they are clearly better then R>R>V)
#
#    >> Each formation will have two revelant defensive options
#        (the third one is neglegible)
#
#    >>>Each option breaks down the kinds of triggers you check in twin drive
#        (Double Crit, 1 Heal and 1 Draw, etc)
#
#    >>>>It is furthur broken down to individual drive and damage checks
#        (3 heals in a row, one draw)
#
#    >>>>>Odds of each event, and its state is recorded and multiplied out
#
#
#    > Back to here, to print the result
#
#    This function eventually prints out a 5 x 5 table containing eight values,
#    4 alloted for each dealt damage,delta cards and shield for every offensive
#    and defensive plan I covered.
#
################################################################################


def dmg3(ht,ct,dt):
    '''Returns values for the event when 3 damage is taken'''
    dmg = 0     # there isn't a point to initilize it, but...
    sld = []
    hin = 0

    # Here is the peachiest calculation of them all.

    nt=33       # to make things easier to read and more consistent w/format
    hththt = Fraction(ht,49)*Fraction(ht-1,48)*Fraction(ht-2,47)
    hthtct = Fraction(ht,49)*Fraction(ht-1,48)*Fraction(ct,47) + Fraction(ht,49)*Fraction(ct,48)*Fraction(ht-1,47) + Fraction(ct,49)*Fraction(ht,48)*Fraction(ht-1,47)
    hthtdt = Fraction(ht,49)*Fraction(ht-1,48)*Fraction(dt,47) + Fraction(ht,49)*Fraction(dt,48)*Fraction(ht-1,47) + Fraction(dt,49)*Fraction(ht,48)*Fraction(ht-1,47)
    hthtnt = Fraction(ht,49)*Fraction(ht-1,48)*Fraction(nt,47) + Fraction(ht,49)*Fraction(nt,48)*Fraction(ht-1,47) + Fraction(nt,49)*Fraction(ht,48)*Fraction(ht-1,47)
    htctct = Fraction(ct,49)*Fraction(ct-1,48)*Fraction(ht,47) + Fraction(ct,49)*Fraction(ht,48)*Fraction(ct-1,47) + Fraction(ht,49)*Fraction(ct,48)*Fraction(ct-1,47)
    htctdt = Fraction(ht,49)*Fraction(ct,48)*Fraction(dt,47) + Fraction(ht,49)*Fraction(dt,48)*Fraction(ct,47) + Fraction(ct,49)*Fraction(ht,48)*Fraction(dt,47) + Fraction(ct,49)*Fraction(dt,48)*Fraction(ht,47) + Fraction(dt,49)*Fraction(ht,48)*Fraction(ct,47) + Fraction(dt,49)*Fraction(ht,48)*Fraction(ct,47)
    htctnt = Fraction(ht,49)*Fraction(ct,48)*Fraction(nt,47) + Fraction(ht,49)*Fraction(nt,48)*Fraction(ct,47) + Fraction(ct,49)*Fraction(ht,48)*Fraction(nt,47) + Fraction(ct,49)*Fraction(nt,48)*Fraction(ht,47) + Fraction(nt,49)*Fraction(ht,48)*Fraction(ct,47) + Fraction(nt,49)*Fraction(ht,48)*Fraction(ct,47)
    htdtdt = Fraction(dt,49)*Fraction(dt-1,48)*Fraction(ht,47) + Fraction(dt,49)*Fraction(ht,48)*Fraction(dt-1,47) + Fraction(ht,49)*Fraction(dt,48)*Fraction(dt-1,47)
    htdtnt = Fraction(ht,49)*Fraction(dt,48)*Fraction(nt,47) + Fraction(ht,49)*Fraction(nt,48)*Fraction(dt,47) + Fraction(dt,49)*Fraction(ht,48)*Fraction(nt,47) + Fraction(dt,49)*Fraction(nt,48)*Fraction(ht,47) + Fraction(nt,49)*Fraction(ht,48)*Fraction(dt,47) + Fraction(nt,49)*Fraction(ht,48)*Fraction(dt,47)
    htntnt = Fraction(nt,49)*Fraction(nt-1,48)*Fraction(ht,47) + Fraction(nt,49)*Fraction(ht,48)*Fraction(nt-1,47) + Fraction(ht,49)*Fraction(nt,48)*Fraction(nt-1,47)
    ctctct = Fraction(ct,49)*Fraction(ct-1,48)*Fraction(ct-2,47)
    ctctdt = Fraction(ct,49)*Fraction(ct-1,48)*Fraction(dt,47) + Fraction(ct,49)*Fraction(dt,48)*Fraction(ct-1,47) + Fraction(dt,49)*Fraction(ct,48)*Fraction(ct-1,47)
    ctctnt = Fraction(ct,49)*Fraction(ct-1,48)*Fraction(nt,47) + Fraction(ct,49)*Fraction(nt,48)*Fraction(ct-1,47) + Fraction(nt,49)*Fraction(ct,48)*Fraction(ct-1,47)
    ctdtdt = Fraction(dt,49)*Fraction(dt-1,48)*Fraction(ct,47) + Fraction(dt,49)*Fraction(ct,48)*Fraction(dt-1,47) + Fraction(ct,49)*Fraction(dt,48)*Fraction(dt-1,47)
    ctdtnt = Fraction(ct,49)*Fraction(dt,48)*Fraction(nt,47) + Fraction(ct,49)*Fraction(nt,48)*Fraction(dt,47) + Fraction(dt,49)*Fraction(ct,48)*Fraction(nt,47) + Fraction(dt,49)*Fraction(nt,48)*Fraction(ct,47) + Fraction(nt,49)*Fraction(ct,48)*Fraction(dt,47) + Fraction(nt,49)*Fraction(ct,48)*Fraction(dt,47)
    ctntnt = Fraction(nt,49)*Fraction(nt-1,48)*Fraction(ct,47) + Fraction(nt,49)*Fraction(ct,48)*Fraction(nt-1,47) + Fraction(ct,49)*Fraction(nt,48)*Fraction(nt-1,47)
    dtdtdt = Fraction(dt,49)*Fraction(dt-1,48)*Fraction(dt-2,47)
    dtdtnt = Fraction(dt,49)*Fraction(dt-1,48)*Fraction(nt,47) + Fraction(dt,49)*Fraction(nt,48)*Fraction(dt-1,47) + Fraction(nt,49)*Fraction(dt,48)*Fraction(dt-1,47)
    dtntnt = Fraction(nt,49)*Fraction(nt-1,48)*Fraction(dt,47) + Fraction(nt,49)*Fraction(dt,48)*Fraction(nt-1,47) + Fraction(dt,49)*Fraction(nt,48)*Fraction(nt-1,47)
    ntntnt = Fraction(nt,49)*Fraction(nt-1,48)*Fraction(nt-2,47)
    #20 events total
    ##    print(hththt+hthtct+hthtdt+hthtnt+htctct+htctdt+htctnt+htdtdt+htdtnt+\
    ##htntnt+ctctct+ctctdt+ctctnt+ctdtdt+ctdtnt+ctntnt+dtdtdt+dtdtnt+dtntnt+ntntnt)
    #confirm it all adds up to 1

    #check damage given
    dmg += 3*(ctctct+ctctdt+ctctnt+ctdtdt+ctdtnt+ctntnt+dtdtdt+dtdtnt+dtntnt+ntntnt)
    dmg += 2*(htctct+htctdt+htctnt+htdtdt+htdtnt+htntnt)
    dmg += 1*(hthtct+hthtdt+hthtnt)
    dmg += 0*(hththt)                            ##for lulz

    #shield saved
    sld.append(ntntnt)
    sld.append(htntnt+dtntnt+ctntnt)
    sld.append(hthtnt+htctnt+htdtnt+ctctnt+ctdtnt+dtdtnt)
    sld.append(hththt+hthtct+hthtdt+htctct+htctdt+htdtdt+ctctct+ctctdt+ctdtdt+dtdtdt)

    #cards drawn
    hin = 3*(dtdtdt) + 2*(htdtdt+ctdtdt+dtdtnt) + 1*(hthtdt+htctdt+htdtnt+ctctdt+ctdtnt+dtntnt)

    return [dmg, sld, hin]

def dmg2(ht,ct,dt):
    '''Returns values for the event when 2 damage is taken'''
    dmg = 0
    sld = []
    hin = 0

    nt=33
    htht = Fraction(ht,49)*Fraction(ht-1,48)
    htct = Fraction(ht,49)*Fraction(ct,48) + Fraction(ct,49)*Fraction(ht,48)
    htdt = Fraction(ht,49)*Fraction(dt,48) + Fraction(dt,49)*Fraction(ht,48)
    htnt = Fraction(ht,49)*Fraction(nt,48) + Fraction(nt,49)*Fraction(ht,48)
    ctct = Fraction(ct,49)*Fraction(ct-1,48)
    ctdt = Fraction(ct,49)*Fraction(dt,48) + Fraction(dt,49)*Fraction(ct,48)
    ctnt = Fraction(ct,49)*Fraction(nt,48) + Fraction(nt,49)*Fraction(ct,48)
    dtdt = Fraction(dt,49)*Fraction(dt-1,48)
    dtnt = Fraction(dt,49)*Fraction(nt,48) + Fraction(nt,49)*Fraction(dt,48)
    ntnt = Fraction(nt,49)*Fraction(nt-1,48)
    #confirm it all adds up to 1
    ##print(htht+htct+htdt+htnt+ctct+ctdt+ctnt+dtdt+dtnt+ntnt)

    dmg += 2*(ctct+ctdt+ctnt+dtdt+dtnt+ntnt)
    dmg += 1*(htct+htdt+htnt)
    sld.append(ntnt)
    sld.append(htnt+ctnt+dtnt)
    sld.append(htht+htct+htdt+ctct+ctdt+dtdt)

    hin += 2*(dtdt) + 1*(htdt+ctdt+dtnt)

    return [dmg, sld, hin]

def dmg1(ht,ct,dt):
    '''Returns values for the event when 1 damage is taken'''
    # shortened cause I'm too lazy
    return [Fraction(49-ht,49),Fraction(16,49),Fraction(dt,49)]

def drive(hT,cT,dT):
    '''Returns values for the twin drive'''
    # Drive check odds.
    hThT = Fraction(hT,49)*Fraction(hT-1,48)
    hTcT = Fraction(hT,49)*Fraction(cT,48)+Fraction(cT,49)*Fraction(hT,48)
    hTdT = Fraction(hT,49)*Fraction(dT,48)+Fraction(dT,49)*Fraction(hT,48)
    hTnT = Fraction(hT,49)*Fraction(33,48)+Fraction(33,49)*Fraction(hT,48)
    cTcT = Fraction(cT,49)*Fraction(cT-1,48)
    cTdT = Fraction(cT,49)*Fraction(dT,48)+Fraction(dT,49)*Fraction(cT,48)
    cTnT = Fraction(cT,49)*Fraction(33,48)+Fraction(33,49)*Fraction(cT,48)
    dTdT = Fraction(dT,49)*Fraction(dT-1,48)
    dTnT = Fraction(dT,49)*Fraction(33,48)+Fraction(33,49)*Fraction(dT,48)
    nTnT = Fraction(22,49)
    #repackage the odds as a list.
    drive = [hThT,hTcT,hTdT,hTnT,cTcT,cTdT,cTnT,dTdT,dTnT,nTnT]
    # confirm it all adds up to 1
    ##    total = 0
    ##    for i in range(0,10): total += drive[i]
    ##    print(total)

    dmgstg = [] # 4 x 3 matrix with columns of damage dealt and stages gained
    dmgstg.append([nTnT, dTnT+hTnT, dTdT+hTdT+hThT, nTnT+dTnT+hTnT+dTdT+hTdT+hThT])
    dmgstg.append([0, cTnT, hTcT+cTdT, cTnT+hTcT+cTdT])
    dmgstg.append([0,0,cTcT,cTcT])

    dmgh = 2*hThT + hTcT+hTdT+hTnT    #damage healed
    drw = 2*dTdT + hTdT+cTdT+dTnT     #cards drawn

    return [dmgstg,dmgh,drw,drive]

def r_guardRG(hT,cT,dT,ht,ct,dt):
    '''returns expected outcome for RVR and guarding the first rearguard attack'''
    # initialize all the variables
    drivecheck = drive(hT,cT,dT)
    state = [0,0,0,0,0]
    d1 = dmg1(ht,ct,dt)
    d2 = dmg2(ht,ct,dt)
    d3 = dmg3(ht,ct,dt)

    # for all events that dealt x damage, find actual damage
    state[0] += drivecheck[0][0][3]*d1[0] ##drive check no crits
    state[0] += drivecheck[0][1][3]*d2[0]
    state[0] += drivecheck[0][2][3]*d3[0]

    # find out card loss for different events
    state[1] += 1 # for guarding the first rearguard
    state[1] += (drivecheck[0][0][0])*(1)
    state[1] += (drivecheck[0][0][1])*((1-d1[1])*2+d1[1])
    state[1] += (drivecheck[0][0][2])*(2)
    state[1] += (drivecheck[0][1][1])*((d2[1][0])*2+(d2[1][1]+d2[1][2])*1)
    state[1] += (drivecheck[0][1][2])*((d2[1][0]+d2[1][1])*2+(d2[1][2])*1)
    state[1] += (drivecheck[0][2][2])*((d3[1][0]+d3[1][1])*2+(d3[1][2]+d3[1][3])*1)

    # find how many cards are recovered to get the total card loss
    recover = 0
    recover += drivecheck[0][0][3]*d1[2] ##drive check no crits
    recover += drivecheck[0][1][3]*d2[2]
    recover += drivecheck[0][2][3]*d3[2]
    state[1] -= recover

    # find out shield loss for different events
    state[2] += 2
    state[2] += (drivecheck[0][0][0])*((1-d1[1])*2+d1[1]*1)
    state[2] += (drivecheck[0][0][1])*((1-d1[1])*3+d1[1]*2)
    state[2] += (drivecheck[0][0][2])*((1-d1[1])*4+d1[1]*3)
    state[2] += (drivecheck[0][1][1])*(d2[1][0]*3+d2[1][1]*2+d2[1][2]*1)
    state[2] += (drivecheck[0][1][2])*(d2[1][0]*4+d2[1][1]*3+d2[1][2]*2)
    state[2] += (drivecheck[0][2][2])*(d3[1][0]*4+d3[1][1]*3+d3[1][2]*2+d3[1][3]*1)
    state[2] *= 5000

    state[3] = drivecheck[1]    # Calculate damage you recovered
    state[4] = drivecheck[2]    # Calculate extra amount of cards drawn.
    return state

def r_guardVG(hT,cT,dT,ht,ct,dt):
    '''returns expected outcome for RVR and guarding the vanguard attack'''
    # initialize all the variables
    drivecheck = drive(hT,cT,dT)
    state = [0,0,0,0,0]
    d1 = dmg1(ht,ct,dt)
    d2 = dmg2(ht,ct,dt)
    d3 = dmg3(ht,ct,dt)

    # find damage
    state[0] += d1[0]

    # find out card loss for different events
    y = d1[1]             # get damage trigger
    n = 1-d1[1]           # no damage trigger
    state[1] += (drivecheck[0][0][0])*(n*3+y*2)
    state[1] += (drivecheck[0][0][1])*(n*4+y*2)
    state[1] += (drivecheck[0][0][2])*(n*4+y*3)
    state[1] += (drivecheck[0][1][1])*(n*4+y*2)
    state[1] += (drivecheck[0][1][2])*(n*4+y*3)
    state[1] += (drivecheck[0][2][2])*(n*4+y*3)

    # find how many cards are recovered to get the total card loss
    recover = 0
    recover += d1[2]
    state[1] -= recover

    # find out shield loss for different events
    ## Using y and n from before
    state[2] += (drivecheck[0][0][0])*(n*5+y*3)
    state[2] += (drivecheck[0][0][1])*(n*6+y*4)
    state[2] += (drivecheck[0][0][2])*(n*7+y*5)
    state[2] += (drivecheck[0][1][1])*(n*6+y*4)
    state[2] += (drivecheck[0][1][2])*(n*7+y*5)
    state[2] += (drivecheck[0][2][2])*(n*7+y*5)
    state[2] *= 5000

    state[3] = drivecheck[1]    # Calculate damage you recovered
    state[4] = drivecheck[2]    # Calculate extra amount of cards drawn.
    return state

def v_guardRG(hT,cT,dT,ht,ct,dt):
    '''returns expected outcome for VRR and guarding both rearguards'''
    # initialize all the variables
    drivecheck = drive(hT,cT,dT)
    state = [0,0,0,0,0]
    d1 = dmg1(ht,ct,dt)
    d2 = dmg2(ht,ct,dt)
    d3 = dmg3(ht,ct,dt)

    # for all events that dealt x damage, find actual damage
    state[0] += drivecheck[0][0][3]*d1[0]
    state[0] += drivecheck[0][1][3]*d2[0]
    state[0] += drivecheck[0][2][3]*d3[0]

    # find out card loss for different events
    state[1] += (drivecheck[0][0][0])*(2)
    state[1] += (drivecheck[0][0][1])*((1-d1[1])*3+d1[1]*2)
    state[1] += (drivecheck[0][0][2])*(3)
    state[1] += (drivecheck[0][1][1])*((d2[1][0])*3+(d2[1][1]+d2[1][2])*2)
    state[1] += (drivecheck[0][1][2])*((d2[1][0]+d2[1][1])*3+(d2[1][2])*2)
    state[1] += (drivecheck[0][2][2])*((d3[1][0]+d3[1][1])*3+(d3[1][2]+d3[1][3])*2)

    # find how many cards are recovered to get the total card loss
    recover = 0
    recover += drivecheck[0][0][3]*d1[2] ##drive check no crits
    recover += drivecheck[0][1][3]*d2[2]
    recover += drivecheck[0][2][3]*d3[2]
    state[1] -= recover

    # find out shield loss for different events
    state[2] += (drivecheck[0][0][0])*((1-d1[1])*4+d1[1]*2)
    state[2] += (drivecheck[0][0][1])*((1-d1[1])*5+d1[1]*3)
    state[2] += (drivecheck[0][0][2])*((1-d1[1])*6+d1[1]*4)
    state[2] += (drivecheck[0][1][1])*(d2[1][0]*5+d2[1][1]*3+d2[1][2]*1)
    state[2] += (drivecheck[0][1][2])*(d2[1][0]*6+d2[1][1]*4+d2[1][2]*2)
    state[2] += (drivecheck[0][2][2])*(d3[1][0]*6+d3[1][1]*4+d3[1][2]*2+d3[1][3]*1)
    state[2] *= 5000

    state[3] = drivecheck[1]    # Calculate damage you recovered
    state[4] = drivecheck[2]    # Calculate extra amount of cards drawn.
    return state

def v_guardVG(hT,cT,dT,ht,ct,dt):
    '''returns expected outcome for VRR and guarding the vanguard attack'''
    # initialize all the variables
    drivecheck = drive(hT,cT,dT)
    state = [0,0,0,0,0]
    d1 = dmg1(ht,ct,dt)
    d2 = dmg2(ht,ct,dt)
    d3 = dmg3(ht,ct,dt)

    # find damage
    state[0] += d1[0]

    # find out card loss for different events
    state[1] += (drivecheck[0][0][0])*(3)
    state[1] += (drivecheck[0][0][1])*(3)
    state[1] += (drivecheck[0][0][2])*(4)
    state[1] += (drivecheck[0][1][1])*(4)
    state[1] += (drivecheck[0][1][2])*(4)
    state[1] += (drivecheck[0][2][2])*(4)

    # find how many cards are recovered to get the total card loss
    recover = 0
    recover += d1[2]
    state[1] -= recover

    # find out shield loss for different events
    state[2] += 3
    state[2] += (drivecheck[0][0][0])*(2)
    state[2] += (drivecheck[0][0][1])*(2)
    state[2] += (drivecheck[0][0][2])*(2)
    state[2] += (drivecheck[0][1][1])*(3)
    state[2] += (drivecheck[0][1][2])*(4)
    state[2] += (drivecheck[0][2][2])*(4)
    state[2] *= 5000

    state[3] = drivecheck[1]    # Calculate damage you recovered
    state[4] = drivecheck[2]    # Calculate extra amount of cards drawn.
    return state

def rvr(hT,cT,dT,ht,ct,dt):
    # guard first rear
    guardrear = r_guardRG(hT,cT,dT,ht,ct,dt)
    #guard vanguard
    guardvan = r_guardVG(hT,cT,dT,ht,ct,dt)
    return [guardrear,guardvan]

def vrr(hT,cT,dT,ht,ct,dt):
    # guard lower critical rg
    guardrear = v_guardRG(hT,cT,dT,ht,ct,dt)
    #guard vanguard
    guardvan = v_guardVG(hT,cT,dT,ht,ct,dt)
    return [guardrear,guardvan]

def compareTrig(a,b,c,d,e,f):
    '''Prints delta cards/damage of competing trigger lineups

    [a]:               Number of Heal Triggers in your deck
    [b]:           Number of Critical Triggers in your deck
    [c]:               Number of Draw Triggers in your deck
    [d]:     Number of Heal Triggers in your opponents deck
    [e]: Number of Critical Triggers in your opponents deck
    [f]:     Number of Draw Triggers in your opponents deck
    '''

    r = rvr(a,b,c,d,e,f)
    v = vrr(a,b,c,d,e,f)
    print("Attack |Defensive Measure    |DMG done |Card loss |Shield loss |DMG you heal |Cards you gain")
    print("-------|---------------------|---------|----------|------------|-------------|--------------")
    print("R>V>R  |Let Vanguard Through | {:^7.3} | {:^8.4} |   {}    |  {:^8.3}   |{:^11.3}"\
    .format(float(r[0][0]),float(r[0][1]),(int)(r[0][2]),float(r[0][3]),float(r[0][4])))
    print("R>V>R  |Let Rearguard Through| {:^7.3} | {:^8.4} |   {}    |  {:^8.3}   |{:^11.3}"\
    .format(float(r[1][0]),float(r[1][1]),(int)(r[1][2]),float(r[1][3]),float(r[1][4])))
    print("V>R>R  |Let Vanguard Through | {:^7.3} | {:^8.4} |   {}    |  {:^8.3}   |{:^11.3}"\
    .format(float(v[0][0]),float(v[0][1]),(int)(v[0][2]),float(v[0][3]),float(v[0][4])))
    print("V>R>R  |Let Rearguard Through| {:^7.3} | {:^8.4} |   {}    |  {:^8.3}   |{:^11.3}"\
    .format(float(v[1][0]),float(v[1][1]),(int)(v[1][2]),float(v[1][3]),float(v[1][4])))
    return

################################################################################
#
#           End of Calculations. Start of User Interface.
#
################################################################################

from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        b = (int)(ycrit.get())
        a = (int)(yheal.get())
        c = (int)(ydraw.get())
        e = (int)(fcrit.get())
        d = (int)(fheal.get())
        f = (int)(fdraw.get())
        if (a+b+c != 16 | d+e+f != 16): err.set("ERROR: not 16 triggers")
        else:
            r = rvr(a,b,c,d,e,f)
            v = vrr(a,b,c,d,e,f)
            dam1.set(float(r[0][0]))
            car1.set(float(r[0][1]))
            shi1.set(float(r[0][2]))
            dam2.set(float(r[1][0]))
            car2.set(float(r[1][1]))
            shi2.set(float(r[1][2]))
            dam3.set(float(v[0][0]))
            car3.set(float(v[0][1]))
            shi3.set(float(v[0][2]))
            dam4.set(float(v[1][0]))
            car4.set(float(v[1][1]))
            shi4.set(float(v[1][2]))
            hea.set(float(r[0][3]))
            gai.set(float(r[0][4]))
            err.set("")
    except ValueError:
        err.set("ERROR: Non-numerical Input")
        pass

from tkinter import messagebox
def assume(*args):
    try:
        messagebox.showinfo("Assumptions","""
    ASSUMPTIONS MADE
        No stand triggers
        Opponent guards one attack only
        No effects
        2/2/2 field
        Deck is sufficiently randomized
        Opponent guards optimally
        End of assumptions

    MADE BY
        Brampton Booster

        bramptonbooster.wordpress.com
        https://github.com/NanoSmasher/prob-cfvg
        bramptonbooster@hotmail.ca

    THANKS FOR USING MY PROGRAM!
        """)
    except ValueError:
        pass

# Main window
root = Tk()
root.title("Trigger Advantage Comparison - Created by Brampton Booster")
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

# Labels
ttk.Label(mainframe, text="# Crit Triggers").grid(column=2, row=1)
ttk.Label(mainframe, text="# Heal Triggers").grid(column=3, row=1)
ttk.Label(mainframe, text="# Draw Triggers").grid(column=4, row=1)
ttk.Label(mainframe, text="Your trig ratios").grid(column=1, row=2,)
ttk.Label(mainframe, text="Your Opponents'").grid(column=1, row=3)
ttk.Label(mainframe, text="Attack Plan").grid(column=1, row=5)
ttk.Label(mainframe, text="Defensive Measure").grid(column=2, row=5)
ttk.Label(mainframe, text="DMG done").grid(column=3, row=5)
ttk.Label(mainframe, text="Card loss").grid(column=4, row=5)
ttk.Label(mainframe, text="Shield loss").grid(column=5, row=5)
ttk.Label(mainframe, text="R>V>R").grid(column=1, row=6)
ttk.Label(mainframe, text="R>V>R").grid(column=1, row=7)
ttk.Label(mainframe, text="V>R>R").grid(column=1, row=8)
ttk.Label(mainframe, text="V>R>R").grid(column=1, row=9)
ttk.Label(mainframe, text="Let Vanguard Through").grid(column=2, row=6)
ttk.Label(mainframe, text="Let Rearguard Through").grid(column=2, row=7)
ttk.Label(mainframe, text="Let Vanguard Through").grid(column=2, row=8)
ttk.Label(mainframe, text="Let Rearguard Through").grid(column=2, row=9)
ttk.Label(mainframe, text="Damage you heal").grid(column=1, row=11)
ttk.Label(mainframe, text="Cards you draw").grid(column=1, row=12)

# Input
ycrit = StringVar()
yheal = StringVar()
ydraw = StringVar()
fcrit = StringVar()
fheal = StringVar()
fdraw = StringVar()

you_c = ttk.Entry(mainframe, width=8, textvariable=ycrit)
you_c.grid(column=2, row=2)
you_h = ttk.Entry(mainframe, width=8, textvariable=yheal)
you_h.grid(column=3, row=2)
you_d = ttk.Entry(mainframe, width=8, textvariable=ydraw)
you_d.grid(column=4, row=2)
foe_c = ttk.Entry(mainframe, width=8, textvariable=fcrit)
foe_c.grid(column=2, row=3)
foe_h = ttk.Entry(mainframe, width=8, textvariable=fheal)
foe_h.grid(column=3, row=3)
foe_d = ttk.Entry(mainframe, width=8, textvariable=fdraw)
foe_d.grid(column=4, row=3)
##

# Output
dam1 = StringVar()
car1 = StringVar()
shi1 = StringVar()
dam2 = StringVar()
car2 = StringVar()
shi2 = StringVar()
dam3 = StringVar()
car3 = StringVar()
shi3 = StringVar()
dam4 = StringVar()
car4 = StringVar()
shi4 = StringVar()
hea = StringVar()
gai = StringVar()
err = StringVar()

ttk.Label(mainframe, textvariable=dam1).grid(column=3, row=6)
ttk.Label(mainframe, textvariable=car1).grid(column=4, row=6)
ttk.Label(mainframe, textvariable=shi1).grid(column=5, row=6)
ttk.Label(mainframe, textvariable=dam2).grid(column=3, row=7)
ttk.Label(mainframe, textvariable=car2).grid(column=4, row=7)
ttk.Label(mainframe, textvariable=shi2).grid(column=5, row=7)
ttk.Label(mainframe, textvariable=dam3).grid(column=3, row=8)
ttk.Label(mainframe, textvariable=car3).grid(column=4, row=8)
ttk.Label(mainframe, textvariable=shi3).grid(column=5, row=8)
ttk.Label(mainframe, textvariable=dam4).grid(column=3, row=9)
ttk.Label(mainframe, textvariable=car4).grid(column=4, row=9)
ttk.Label(mainframe, textvariable=shi4).grid(column=5, row=9)
ttk.Label(mainframe, textvariable=hea).grid(column=2, row=11)
ttk.Label(mainframe, textvariable=gai).grid(column=2, row=12)
ttk.Label(mainframe, textvariable=err).grid(column=5, row=11)

# Button and Finishing Touches
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=5, row=12, sticky=(E,S))
ttk.Button(mainframe, text="About", command=assume).grid(column=5, row=13, sticky=(E,S))
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)
root.bind('<Return>', calculate)
you_c.focus()
##

root.mainloop()
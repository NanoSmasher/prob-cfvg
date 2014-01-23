import math
from fractions import *

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
    state[2] += 2               # for guarding the first rearguard
    state[2] += (drivecheck[0][0][0])*((1-d1[1])*2+d1[1]*1)
    state[2] += (drivecheck[0][0][1])*((1-d1[1])*3+d1[1]*2)
    state[2] += (drivecheck[0][0][2])*((1-d1[1])*4+d1[1]*3)
    state[2] += (drivecheck[0][1][1])*(d2[1][0]*3+d2[1][1]*2+d2[1][2]*1)
    state[2] += (drivecheck[0][1][2])*(d2[1][0]*4+d2[1][1]*3+d2[1][2]*2)
    state[2] += (drivecheck[0][2][2])*(d3[1][0]*4+d3[1][1]*3+d3[1][2]*2+d3[1][3]*1)
    state[2] *= 5000            # to convert from stage notation to shield value

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
    y = dmg1[1]             # get damage trigger
    n = 1-dmg1[1]           # no damage trigger
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

    state[3] = drivecheck[1]    # Calculate damage you recovered
    state[4] = drivecheck[2]    # Calculate extra amount of cards drawn.
    return state

def v_guardRG(hT,cT,dT,ht,ct,dt):
    '''returns expected outcome for VRR and guarding the first rearguard attack'''
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
    state[2] += 2               # for guarding the first rearguard
    state[2] += (drivecheck[0][0][0])*((1-d1[1])*2+d1[1]*1)
    state[2] += (drivecheck[0][0][1])*((1-d1[1])*3+d1[1]*2)
    state[2] += (drivecheck[0][0][2])*((1-d1[1])*4+d1[1]*3)
    state[2] += (drivecheck[0][1][1])*(d2[1][0]*3+d2[1][1]*2+d2[1][2]*1)
    state[2] += (drivecheck[0][1][2])*(d2[1][0]*4+d2[1][1]*3+d2[1][2]*2)
    state[2] += (drivecheck[0][2][2])*(d3[1][0]*4+d3[1][1]*3+d3[1][2]*2+d3[1][3]*1)
    state[2] *= 5000            # to convert from stage notation to shield value

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
    v_guardRG(hT,cT,dT,ht,ct,dt)
    #guard vanguard
##    v_guardVG(hT,cT,dT,ht,ct,dt)
    return

def compareTrig(a,b,c,d,e,f):
    '''Prints delta cards/damage of competing trigger lineups

    [a]:               Number of Heal Triggers in your deck
    [b]:           Number of Critical Triggers in your deck
    [c]:               Number of Draw Triggers in your deck
    [d]:     Number of Heal Triggers in your opponents deck
    [e]: Number of Critical Triggers in your opponents deck
    [f]:     Number of Draw Triggers in your opponents deck
    '''

    '''
    The methodology of how compareTrig finds thes values is done like this:
        We break it down into individual sets
    > Two possible attack formations, R>V>R and V>R>R-P*,
        (since they are clearly better then R>R>V)
    >> Each formation will have two revelant defensive options
        (the third one is neglegible)
    >>>Each option breaks down the kinds of triggers you check in twin drive
        (Double Crit, 1 Heal and 1 Draw, etc)
    >>>>It is furthur broken down to individual drive and damage checks
        (3 heals in a row, one draw)
    >>>>>Odds of each event, and its state is recorded and multiplied out
    > Back to here, to print the result

    This function eventually prints out a 5 x 5 table containing eight values,
    4 alloted for each âˆ†damage,âˆ†cards and shield for every offensive and
    defensive plan I covered.
    '''
    r = rvr(a,b,c,d,e,f)
    ##    vrr(a,b,c,d,e,f)
    print("Attack |Defensive Measure |DMG done |Cards loss |Shield loss |DMG you heal |Cards you gain")
    print("R>V>R  |Guard Rearguard   |{}       |{}         |{}          |{}           |{}".format(r[0][0],r[0][1],r[0][2],r[0][3],r[0][4]))
    print("R>V>R  |Guard Vanguard    |{}       |{}         |{}          |{}           |{}".format(r[1][0],r[1][1],r[1][2],r[1][3],r[1][4]))
    return

def assume():
    print("> No stand triggers.")
    print("> Opponent guards one attack only")
    print("> No effects")
    print("> 2/2/2 field")
    print("> Deck is sufficiently randomized")
    print("> End of assumptions")
    return

def main():
    print("Type in compareTrig([a],[b],[c],[d],[e],[f])\n")
    print("[a]:               Number of Heal Triggers in your deck")
    print("[b]:           Number of Critical Triggers in your deck")
    print("[c]:               Number of Draw Triggers in your deck")
    print("[d]:     Number of Heal Triggers in your opponents deck")
    print("[e]: Number of Critical Triggers in your opponents deck")
    print("[f]:     Number of Draw Triggers in your opponents deck")
    print("\n Type in assume() for assumptions made in calculation")
    print("\n                                        BramptonBooster")
    pass

if __name__ == '__main__':
    main()

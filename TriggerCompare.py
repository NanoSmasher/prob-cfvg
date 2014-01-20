import math
from fractions import *
from Hyper_Calculator import *

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
    sld.append(3*(hththt+hthtct+hthtdt+htctct+htctdt+htdtdt+ctctct+ctctdt+ctdtdt+dtdtdt))
    sld.append(2*(hthtnt+htctnt+htdtnt+ctctnt+ctdtnt+dtdtnt))
    sld.append(1*(htntnt+dtntnt+ctntnt))
    sld.append(0*(ntntnt))                       ## for lulz again

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
    sld.append(2*(htht+htct+htdt+ctct+ctdt+dtdt))
    sld.append(1*(htnt+ctnt+dtnt))
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

    deal = [] #damage dealt
    deal.append(nTnT+ dTnT + dTdT + hTdT + hTnT + hThT)
    deal.append(hTcT + cTdT + cTnT)
    deal.append(cTcT)

    dmgh = 2*hThT + hTcT + hTdT + hTnT    #damage healed
    drw = 2*dTdT + hTdT + cTdT + dTnT     #cards drawn

    return [deal,dmgh,drw,drive]

def r_guardRG(hT,cT,dT,ht,ct,dt):
    '''returns expected outcome for RVR and guarding the first rearguard attack'''
    # initialize all the variables
    drivecheck = drive(hT,cT,dT)
    state = [0,0,0,0,0]
    d1 = dmg1(ht,ct,dt)
    d2 = dmg2(ht,ct,dt)
    d3 = dmg3(ht,ct,dt)

    # for all events that dealt 3 damage, find actual damage
    state[0] += drivecheck[0][0]*d1[0] ##lol
    state[0] += drivecheck[0][1]*d2[0]
    state[0] += drivecheck[0][2]*d3[0]


    state[3] = drivecheck[1]    # Calculate damage you recovered
    state[4] = drivecheck[2]    # Calculate extra amount of cards drawn.
    return state

def rvr(hT,cT,dT,ht,ct,dt):
    # guard first rear
    guardrear = r_guardRG(hT,cT,dT,ht,ct,dt)
    print("Attack |Defensive Measure |DMG done |Cards loss |Shield loss |DMG you heal |Cards you gain")
    print("R>V>R  |Guard Rearguard   |{}       |           |            |{}           |{}".format(guardrear[0],guardrear[3],guardrear[4]))

##    r_guardVG(hT,cT,dT,ht,ct,dt)
    return

##def vrr(hT,cT,dT,ht,ct,dt):
##    # guard lower critical rg
##    v_guardRG(hT,cT,dT,ht,ct,dt)
##
##    v_guardVG(hT,cT,dT,ht,ct,dt)
##    return

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
    4 alloted for each ∆damage,∆cards and shield for every offensive and
    defensive plan I covered.
    '''
    rvr(a,b,c,d,e,f)
##    vrr(a,b,c,d,e,f)
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

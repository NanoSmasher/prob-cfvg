import math
from fractions import *
from Hyper_Calculator import *

def dmg3(ht,ct,dt):
    dmg = 0     # there isn't a point to initilize it, but...
    sld = 0
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
    dmg += 0*(hththt)                       #for lulz

    #shield saved
    sld += 3*(hththt+hthtct+hthtdt+htctct+htctdt+htdtdt+ctctct+ctctdt+ctdtdt+dtdtdt)
    sld += 2*(hthtnt+htctnt+htdtnt+ctctnt+ctdtnt+dtdtnt)
    sld += 1*(htntnt+dtntnt+ctntnt)
    sld += 0*(ntntnt)                       # for lulz again

    #cards drawn
    hin = 3*(dtdtdt) + 2*(htdtdt+ctdtdt+dtdtnt) + 1*(hthtdt+htctdt+htdtnt+ctctdt+ctdtnt+dtntnt)

    return [dmg, sld, hin]

def dmg2(ht,ct,dt):
    dmg = 0
    sld = 0
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
    ##print(htht+htct+htdt+htnt+ctct+ctdt+ctnt+dtdt+dtnt+ntnt)
    #confirm it all adds up to 1

    dmg += 2*(ctct+ctdt+ctnt+dtdt+dtnt+ntnt)
    dmg += 1*(htct+htdt+htnt)
    sld += 2*(htht+htct+htdt+ctct+ctdt+dtdt)
    sld += 1*(htnt+ctnt+dtnt)
    hin += 2*(dtdt) + 1*(htdt+ctdt+dtnt)

    return [dmg, sld, hin]

def dmg1(ht,ct,dt):
    # shortened cause I'm too lazy
    return [Fraction(49-ht,49),Fraction(16,49),Fraction(dt,49)]

def r_guardRG(hT,cT,dT,ht,ct,dt):
    # option 1

    cid = 0     #Change in damage
    cu = 0      #Cards used

    drive = []
    drive.append(Fraction(hT,49)*Fraction(hT-1,48))
    drive.append(Fraction(hT,49)*Fraction(cT,48)+Fraction(cT,49)*Fraction(hT,48))
    drive.append(Fraction(hT,49)*Fraction(dT,48)+Fraction(dT,49)*Fraction(hT,48))
    drive.append(Fraction(hT,49)*Fraction(33,48)+Fraction(33,49)*Fraction(hT,48))
    drive.append(Fraction(cT,49)*Fraction(cT-1,48))
    drive.append(Fraction(cT,49)*Fraction(dT,48)+Fraction(dT,49)*Fraction(cT,48))
    drive.append(Fraction(cT,49)*Fraction(33,48)+Fraction(33,49)*Fraction(cT,48))
    drive.append(Fraction(dT,49)*Fraction(dT-1,48))
    drive.append(Fraction(dT,49)*Fraction(33,48)+Fraction(33,49)*Fraction(dT,48))
    drive.append(Fraction(22,49))
    # Appended drive checks in order (start at 0!):
    # hThT, hTcT, hTdT, hTnT, cTcT, cTdT, cTnT, dTdT, dTnT, nTnT

##    total = 0
##    for i in range(0,10): total += drive[i]
##    print(total)
# confirm it all adds up to 1

    state = [] # contains 2 varibles, one for dmg and another for cards used
    dmg3(ht,ct,dt)
    dmg2(ht,ct,dt)
    dmg1(ht,ct,dt)

    return

def rvr(hT,cT,dT,ht,ct,dt):
    # guard first rear
    r_guardRG(hT,cT,dT,ht,ct,dt)

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

    this section is broken in the following manner:
    Two possible attack formations, R>V>R and V>R>R-P*,
        (since they are clearly better then R>R>V)
    Each formation will have two revelant defensive options
        (the third one is neglegible)
    Each option breaks down the kinds of triggers you check in twin drive
        (Double Crit, 1 Heal and 1 Draw, etc)
    It is furthur broken down to each individual damage check
        (3 heals in a row, one draw)
    The probabilty of each event, and its state is recorded and multiplied out,
    until the result is reached.

    This function eventually prints out a 5 x 3 table containing eight values,
    4 being the delta damage for each offensive+defense plan,
    while the other 4 is for the delta cards used by the opponent.
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

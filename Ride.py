import math
from fractions import *
from Hyper_Calculator import *

def ChanceToGetMin1(ini=0,end=1,n=0,mull=3,first=True):
    ''' Calculates odds on getting at least 1 of a card

        Variables
        ini: initial state
        end: end state
        n: number of copies
        mull: # of cards to mulligan
        first: True if player took the first turn

        Options for (ini) and (end):
            0 Begining of Fight, no cards drawn
            1 The Starting Hand
            2 The Mulligan And First Draw
            3 The End of Turn 1
            4 The Start of Turn 2
            5 The End of Turn 2
            6 The Start of Turn 3 ... and so on (maximum 13)
    '''
    if n<=0|end==0|end<ini|mull<0|mull>5|ini>13|end>13: return 0
    # kill the calculations if something is strange.
    deckcount = 49
    p1 = HGCC(49,n,5,1,"<")
    # Failure to get card
    p2 = HGCC(44+mull,n,mull+1,1,"<")
    deckcount = 43
    if first:
        p3 = 1
    else:
        p3 = Fraction(deckcount-n,deckcount)
        deckcount -= 1                          #Did not want to call HGCC()
    p4 = Fraction(deckcount-n,deckcount)
    deckcount-=1
    p5 = Fraction(deckcount-n,deckcount)
    deckcount-=1
    p6 = Fraction(deckcount-n,deckcount)
    deckcount-=1
    p7 = HGCC(deckcount,n,2,1,"<")
    deckcount-=2
    p8 = Fraction(deckcount-n,deckcount)
    deckcount-=1
    p9 = HGCC(deckcount,n,2,1,"<")
    deckcount-=2
    p10 = Fraction(deckcount-n,deckcount)
    deckcount-=1
    p11 = HGCC(deckcount,n,2,1,"<")
    deckcount-=2
    p12 = Fraction(deckcount-n,deckcount)
    deckcount-=1
    p13 = HGCC(deckcount,n,2,1,"<")
    p = [1,p1,p2,p3,p4,p5,p6,p7,p8,p9,p10,p11,p12,p13]
    # could have made it one tuple, but I like to use extra variables.
    # Also explains why I haven't shortened this into a loop

    total = 1
    for i in range(0,14):
        if (i >= ini) & (i <= end): total *= p[i]
    return 1-total #to get sucess rate

def RideElements(gr1,gr2,gr3,mull=3,first=True):
    ''''Returns chance to ride each grade as a list'''
    c1 = ChanceToGetMin1(0,2,gr1,mull,first)
    c2 = ChanceToGetMin1(0,4,gr2,mull,first)
    c3 = ChanceToGetMin1(0,6,gr3,mull,first)
    return [c1,c2,c3]

def BasicRide(gr1=12,gr2=11,gr3=10,mull=3,first=True):
    '''Returns chance to ride up to grade 3

    Variables
    g1, g2, g3: number of grade 1's, 2's and 3's respectably
    mull: # of cards to mulligan
    first: True if player took the first turn
    '''
    c = RideElements(gr1,gr2,gr3,mull,first=True)
    total = 1
    for i in c:
        total*=i
    return total

def AdvanceRide(gr1=12,gr2=11,gr3=10,gr4=0,mull=3,first=True):
    '''Returns chance to ride up to grade 4

    Variables
    g1, g2, g3, g4: number of grade 1's, 2's, 3's and 4's respectably
    mull: # of cards to mulligan
    first: True if player took the first turn
    '''
    c = RideElements(gr1,gr2,gr3,mull,first=True)
    c4 = ChanceToGetMin1(0,12,gr4,mull,first)
    c.append(c4)
    total = 1
    for i in c:
        total*=i
    return total

def Gen1Ride(g1,g2,g3,mull=3,first=True):
    '''Returns chance to ride up using a Generation I ride chain

    Examples: Lox, Ergodiel
    Assumes 4 of each piece.
    Variables
    g1, g2, g3: number of grade 1's, 2's and 3's respectably
    mull: # of cards to mulligan
    first: True if player took the first turn

    See file for computations
    '''
    '''
    Calculations
    G1*g2*g3
    nG1*g1*g2*g3
    G1*g2*ng3*tG3
    G1*ng2*tG2*g3
    '''
    r1 = ChanceToGetMin1(0,2,4,mull,first)
    re = RideElements(g1-4,g2,g3,mull,first)
    t7 = HGCC(43,4,7,1,">=")
    total = 0
    total += r1*re[1]*re[2]
    total += (1-r1)*re[0]*re[1]*re[2]
    total += r1*re[1]*(1-re[2])*t7
    total += r1*(1-re[1])*t7*re[2]
    return total

def Gen2Ride(gr1=13,gr2=9,gr3=11,r=4,mull=3,first=True):
    '''Returns chance to ride up using a Generation II ride chain

    Examples: Stern, Giraffa
    Variables
    g1, g2, g3: number of grade 1's, 2's and 3's respectably
    r: number of grade one ride chain pieces
    mull: # of cards to mulligan
    first: True if player took the first turn
    '''
    r1 = ChanceToGetMin1(0,2,r,mull,first)
    re = RideElements(gr1-r,gr2,gr3,mull,first)
    total = 0
    total = r1*re[2]+(1-r1)*re[0]*re[1]*re[2]
    return total

def Gen4Ride(r1,r2,r3,mull=3,first=True):
    '''Returns chance to ride up using a Generation IV ride chain

    Examples: Coral, Artemis
    Assumes 4 of each piece.
    Variables
    r1, r2, r3: number of grade 1's, 2's and 3's respectably
    mull: # of cards to mulligan
    first: True if player took the first turn

    See file for computations
    '''
    '''
    Notation
    SH: starting hand
    M: Mulligan
    captial G: the ride chain element
    lovercase g: the non-ride chain element

    Calculations
    SH and M        Top7    2nd Search  After
  1)G1,G2,G3
  2)nG1                                 G2,G3
  3)G1,G2,nG3       G3
  4)G1,G2,nG3       nG3                 G3
  5)G1,nG2,G3       G2
 6a)G1,nG2,G3       nG2     G2
 6b)G1,nG2,G3       nG2     nG2         G2
  7)G1,nG2,nG3      G2                  G3
 7b)G1,nG2,nG3      nG2     G2          G3
 8a)G1,nG2,nG3      G3      G2          G2
 9a)G1,nG2,nG3      nG2,nG3 G2          G2,G3
 9b)G1,nG2,nG3      nG2,nG3 nG2         G2,G3
    '''
    re = RideElements(r1,r2,r3,mull,first)
    #remember, mg1 = re[0]
    mg2 = ChanceToGetMin1(0,2,r2,mull,first)
    mg3 = ChanceToGetMin1(0,2,r3,mull,first)

    t7g2 = HGCC(43,r2,7,1,">=")
    t7g3 = HGCC(43,r3,7,1,">=")

    afgr2 = ChanceToGetMin1(3,4,r2,mull,first)
    afgr3 = ChanceToGetMin1(3,6,r3,mull,first)

    total = BasicRide(gr1,gr2,gr3,mull,first=True)
    total += (1-re[0])*re[1]*re[2] #Need to add chance to get norm gr1
    total += re[0]*mg2*(1-mg3)     * t7g3
    total += re[0]*mg2*(1-mg3)     * (1-t7g3)          * afgr3
    total += re[0]*(1-mg2)*mg3     * t7g2
    total += re[0]*(1-mg2)*mg3     * (1-t7g2)          * afgr2
    total += re[0]*(1-mg2)*(1-mg3) * t7g2              * afgr3
    total += re[0]*(1-mg2)*(1-mg3) * t7g3              * afgr2
    total += re[0]*(1-mg2)*(1-mg3) * (1-t7g2)*(1-t7g3) * afgr2*afgr3
    return total

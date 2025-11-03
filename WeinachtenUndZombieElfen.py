import random
def updatePosition(n,m,pos,rnd):
    #n: Anzahl der Reihen des Welt-Rechtecks
    #m: Anzahl der Spalten des Welt-Rechtecks
    #pos: Position der Figur als nichtnegative ganze Zahl
    #rnd: zufälliger Float im halboffenen Intervall [0, 1)
    if rnd>=0 and rnd<0.25: #nach rechts
        if (pos+1)%m!=0:
            return pos+1
        else:
            return (pos-m)+1
    if rnd>=0.25 and rnd<0.5: #nach links
        if pos%m!=0:
            return pos-1
        else:
            return (pos+m)-1
    if rnd>=0.5 and rnd<0.75: #nach unten
        if pos+m>=m*n:
            return pos-(m*(n-1))
        else:
            return pos+m
    if rnd>=0.75 and rnd<1: #nach oben
        if pos-m<0:
            return pos+(m*(n-1))
        else:
            return pos-m

def updatePositions(n,m,positions):
    neuPosition=positions
    for i in range(len(positions)):
        rnd=random.random()
        neuPosition[i][1]=updatePosition(n,m,positions[i][1],rnd)
    positions=neuPosition
    return positions

def sortPositions(positions):
    a=[]
    neu=[]
    for i in positions:
       a.append(i[1])
    while len(a)>0:
        indexmin=a.index(min(a))
        a.pop(indexmin)
        neu.append(positions[indexmin])
        positions.pop(indexmin)
    positions=neu
    return positions

def extractSquare(positions):
    square=[]
    positions2=sortPositions(positions)
    maxeintrag=positions2[len(positions2)-1][1]
    for i in range(len(positions2)-1,-1,-1):
        if positions2[i][1]==maxeintrag:
            square.append(positions2.pop())
    positions=positions2
    return positions,square

def giftExchange(square):
    H=0
    HH=0
    Z=0
    ZH=0
    for i in square:
        if i[0]=="H":H+=1
        elif i[0]=="HH":HH+=1
        elif i[0]=="Z":Z+=1
        elif i[0] =="ZH":ZH+=1
    if ZH>=1 and (HH>=1 or H>=1):
        for i in square:
            if i[0]=="H":
                i[0]="HH"
    H=0
    HH=0
    Z=0
    ZH=0
    for i in square:
        if i[0]=="H":H+=1
        elif i[0]=="HH":HH+=1
        elif i[0]=="Z":Z+=1
        elif i[0]=="ZH":ZH+=1
    if (Z>=1 or ZH>=1) and (H>=1 or HH>=1):
        if Z>=(2*HH):
            for i in square:
                if i[0]=="H" or i[0]=="HH":
                    i[0]="Z"
        elif Z<(2*HH):
            for i in square:
                if i[0]=="Z":
                    i[0]="ZH"
    return square

def mergeSquare(square,intermediate):
    intermediate2=[]
    for i in intermediate:
        intermediate2.append(i)
    for i in square:
        intermediate2.append(i)
    intermediate=intermediate2
    return intermediate

def christmasFated(positions):
    H=0
    HH=0
    Z=0
    ZH=0
    for i in positions:
        if i[0]=="H":H+=1
        elif i[0]=="HH":HH+=1
        elif i[0]=="Z":Z+=1
        elif i[0]=="ZH":ZH+=1
    if (H==0 and HH==0)or Z==0: return True
    return False

def christmasFate(positions):
    H=0
    HH=0
    Z=0
    ZH=0
    for i in positions:
        if i[0]=="H":H+=1
        elif i[0]=="HH":HH+=1
        elif i[0]=="Z":Z+=1
        elif i[0]=="ZH":ZH+=1
    if christmasFated(positions)==True:
        if H==0 and HH==0: return "Zombies ate my Christmas!"
        if Z==0 and (H>=1 or HH>=1): return "Ho, ho, ho, and a merry Zombie-Christmas!"

def zombieChristmas(n,m,positions):
    while christmasFated(positions)==False:
        updatePositions(n,m,positions)
        giftExchange(positions)
    return christmasFate(positions)


import math, Pokedex

name = "galvantula"
baseHP = Pokedex.findPokemonHP(name)
baseDef = Pokedex.findPokemonDef(name)
defNature = 1.0
baseSpDef = Pokedex.findPokemonSpD(name)
spDefNature = 1.0
ivs = [31,31,31,31,31,31]
usableEVs = 510-252
level = 100
oppAttack = 100
power = 100
STAB = 1.0
effectiveness = 1.0
criticalHit = 1.0
other = 1.0
modifier = STAB*effectiveness*criticalHit*other

def calcHP(evs):
    return math.floor(((2*baseHP+ivs[0]+math.floor(evs/4))*level)/100)+level+10

def calcDefense(evs):
    return math.floor((math.floor(((2*baseDef+ivs[2]+math.floor(evs/4))*level)/100)+5)*defNature)

def calcSpecialDefense(evs):
    return math.floor((math.floor(((2*baseSpDef+ivs[4]+math.floor(evs/4))*level)/100)+5)*spDefNature)

def calcPhysicalDamage(hp,defense):
    return ((2*level/5+2)*oppAttack/defense*power/50+2)*modifier/hp

def calcSpecialDamage(hp,spDefense):
    return ((2*level/5+2)*oppAttack/spDefense*power/50+2)*modifier/hp

def calcScore(pDamage,spDamage):
    return math.sqrt(0.5*(pDamage**2+spDamage**2))

score = 1000
optHPEV = 0
optDefEV = 0
optSpDefEV = 0
for i in range(0,min(usableEVs,252)+1,8):
    for j in range(0,min(usableEVs-i,252)+1,8):
        for k in range(0,min(usableEVs-i-j,252)+1,8):
            tempPDamage = calcPhysicalDamage(calcHP(k),calcDefense(i))
            tempSDamage = calcSpecialDamage(calcHP(k),calcSpecialDefense(j))
            tempScore = calcScore(tempPDamage,tempSDamage)
            if tempScore<score:
                score = tempScore
                optHPEV = k
                optDefEV = i
                optSpDefEV = j
approxHPEV = optHPEV
approxDefEV = optDefEV
approxSpDefEV = optSpDefEV
for i in range(max(approxDefEV-8,0),min(approxDefEV+8,252)+1):
    for j in range(max(approxSpDefEV-8-i,0),min(approxSpDefEV+8-i,252)+1):
        for k in range(max(approxHPEV-8-i-j,0),min(approxHPEV+8-i-j,252)+1):
            tempPDamage = calcPhysicalDamage(calcHP(k),calcDefense(i))
            tempSDamage = calcSpecialDamage(calcHP(k),calcSpecialDefense(j))
            tempScore = calcScore(tempPDamage,tempSDamage)
            if tempScore<score:
                score = tempScore
                optHPEV = k
                optDefEV = i
                optSpDefEV = j
print("Optimal Defensive EV Spread:")
print("HP: %d, Defense: %d, Special Defense: %d; Average damage taken: [%.2f%%, %.2f%%]" % (optHPEV,optDefEV,optSpDefEV,calcScore(calcPhysicalDamage(calcHP(optHPEV),calcDefense(optDefEV)),calcSpecialDamage(calcHP(optHPEV),calcSpecialDefense(optSpDefEV)))*85,calcScore(calcPhysicalDamage(calcHP(optHPEV),calcDefense(optDefEV)),calcSpecialDamage(calcHP(optHPEV),calcSpecialDefense(optSpDefEV)))*100))

#similarEVSets = []
#for i in range(0,min(usableEVs,252)+1):
#   for j in range(0,min(usableEVs-i,252)+1):
#       for k in range(0,min(usableEVs-i-j,252)+1):
#           tempHP = calcHP(k)
#           tempDef = calcDefense(i)
#           tempSpDef = calcSpecialDefense(j)
#           tempPDamage = calcPhysicalDamage(tempHP,tempDef)
#           tempSDamage = calcSpecialDamage(tempHP,tempSpDef)
#           tempScore = calcScore(tempPDamage,tempSDamage)
#            if tempScore==score:
#              set = [i,j,k]
#              similarEVSets.append(set)
#for i in range(len(similarEVSets),0,-1):
#   for j in range(len(similarEVSets),i,-1):
#       if(calcDefense(similarEVSets[i][0])==calcDefense(similarEVSets[j][0])):
#           if(calcSpecialDefense(similarEVSets[i][1])==calcSpecialDefense(similarEVSets[j][1])):
#               if(calcHP(similarEVSets[i][2])==calcHP(similarEVSets[j][2])):
#                   del similarEVSets[j]
#   if similarEVSets[i][0]==optDefEV:
#       if similarEVSets[i][1]==optSpDefEV:
#           if similarEVSets[i][2]==optHPEV:
#               del similarEVSets[i]
#if len(similarEVSets)!=0:
#   print("Other options include:")
#for set in similarEVSets:
#   print("HP: "+set[2]+", Defense: "+set[0]+", Special Defense: "+set[1]+", Damage taken: ["+calcScore(calcPhysicalDamage(calcHP(set[2]),calcDefense(set[0])),calcSpecialDamage(calcHP(set[2]),calcSpecialDefense(set[1])))*0.85+"%, "+calcScore(calcPhysicalDamage(calcHP(set[2]),calcDefense(set[0])),calcSpecialDamage(calcHP(set[2]),calcSpecialDefense(set[1])))+"%]")
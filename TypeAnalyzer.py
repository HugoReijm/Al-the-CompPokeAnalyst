import Pokedex

def defCombineTypes(types):
    if isinstance(types,list):
        wri = []
        wri.append([])
        wri.append([])
        for type in types:
            data = Pokedex.findTypeData(type)
            for w in data["weaknesses"]:
                wri[0].append(w)
            for r in data["resistances"]:
                if r != "":
                    wri[1].append(r)
            for i in data["immunities"]:
                if i != "":
                    wri[1].append(i)
                    wri[1].append(i)
        done = False
        while not done:
            done = True
            for w in wri[0]:
                for r in wri[1]:
                    if w==r:
                        del wri[0][wri[0].index(w)]
                        del wri[1][wri[1].index(r)]
                        done = False
                        break
        return wri
    else:
        return None

def offCombineTypes(types):
    if isinstance(types,list):
        senvene = []
        senvene.append([])
        senvene.append([])
        for type in types:
            data = Pokedex.findTypeData(type)
            for se in data["superEffective"]:
                if se!="":
                    senvene[0].append(se)
            for nve in data["notVeryEffective"]:
                if nve != "":
                    senvene[1].append(nve)
            for ne in data["notEffective"]:
                if ne != "":
                    senvene[1].append(ne)
                    senvene[1].append(ne)
        done = False
        while not done:
            done = True
            for se in senvene[0]:
                for nve in senvene[1]:
                    if se==nve:
                        del senvene[0][senvene[0].index(se)]
                        del senvene[1][senvene[1].index(nve)]
                        done = False
                        break
        return senvene
    else:
        return None

def defSynergy(types):
    if isinstance(types,list):
        tData = []
        for t in types:
            tData.append(Pokedex.findTypeData(t))
        wri = defCombineTypes(types)
        totalW = []
        #totalR = []
        #totalI = []
        for t in types:
            for w in tData[types.index(t)]["weaknesses"]:
                if w!="":
                    totalW.append(w)
            #for r in tData[types.index(t)]["resistances"]:
            #    if r!="":
            #        totalR.append(r)
            #for i in tData[types.index(t)]["immunities"]:
            #    if i!="":
            #        totalI.append(i)
        #score = len(wri[1])/(len(totalR+totalI))- len(wri[0])/len(totalW)
        #score = len(wri[1])-len(wri[0])
        score = len(wri[0])/len(totalW)
        #score = len(wri[1])/(len(totalR)+2*len(totalI))
        return score
    else:
        return None

def offSynergy(types):
    if isinstance(types,list):
        tData = []
        for t in types:
            tData.append(Pokedex.findTypeData(t))
        senvene = offCombineTypes(types)
        totalSE = []
        totalNVE = []
        totalNE = []
        for t in types:
            for se in tData[types.index(t)]["superEffective"]:
                if se!="":
                    totalSE.append(se)
            for nve in tData[types.index(t)]["notVeryEffective"]:
                if nve!="":
                    totalNVE.append(nve)
            for ne in tData[types.index(t)]["notEffective"]:
                if ne!="":
                    totalNE.append(ne)
        #score = len(senvene[1])/(len(totalNVE+totalNE))- len(senvene[0])/len(totalSE)
        #score = len(senvene[1])-len(senvene[0])
        #score = len(senvene[0])/len(totalSE)
        score = len(senvene[1])/(len(totalNVE)+2*len(totalNE))
        return score
    else:
        return None

def allDefScores():
    scores = []
    types = Pokedex.loadTypes()
    listTypes = list(types.keys())
    for t1 in range(len(listTypes)):
        for t2 in range(t1+1,len(listTypes)):
            #scores.append([listTypes[t1],listTypes[t2],defSynergy([listTypes[t1],listTypes[t2]])])
            for t3 in range(t2+1,len(listTypes)):
                scores.append([listTypes[t1],listTypes[t2],listTypes[t3],defSynergy([listTypes[t1],listTypes[t2],listTypes[t3]])])
                #for t4 in range (t3+1,len(listTypes)):
                #    scores.append([listTypes[t1], listTypes[t2], listTypes[t3], listTypes[t4],defSynergy([listTypes[t1], listTypes[t2], listTypes[t3], listTypes[t4]])])
    #cores = sorted(scores, key=lambda score: score[2], reverse=False)
    cores = sorted(scores,key = lambda score: score[3],reverse=False)
    #cores = sorted(scores, key=lambda score: score[4], reverse=False)
    for core in cores:
        print(core)

def allOffScores():
    scores = []
    types = Pokedex.loadTypes()
    listTypes = list(types.keys())
    for t1 in range(len(listTypes)):
        for t2 in range(t1+1,len(listTypes)):
            #scores.append([listTypes[t1],listTypes[t2],offSynergy([listTypes[t1],listTypes[t2]])])
            for t3 in range(t2+1,len(listTypes)):
                #scores.append([listTypes[t1],listTypes[t2],listTypes[t3],offSynergy([listTypes[t1],listTypes[t2],listTypes[t3]])])
                for t4 in range (t3+1,len(listTypes)):
                    scores.append([listTypes[t1], listTypes[t2], listTypes[t3], listTypes[t4],offSynergy([listTypes[t1], listTypes[t2], listTypes[t3], listTypes[t4]])])
    #cores = sorted(scores, key=lambda score: score[2], reverse=False)
    #cores = sorted(scores,key = lambda score: score[3],reverse=False)
    cores = sorted(scores, key=lambda score: score[4], reverse=False)
    for core in cores:
        print(core)

types = ["Dark","Dragon","Steel","Psychic"]
totalSE = []
totalNVE = []
totalNE = []
for t in types:
    totalSE+=Pokedex.findTypeData(t)["superEffective"]
    totalNVE+=Pokedex.findTypeData(t)["notVeryEffective"]
    totalNE+=Pokedex.findTypeData(t)["notEffective"]
print(totalSE)
print(totalNVE)
print(totalNE)
print()
print(offCombineTypes(types)[0])
print(offCombineTypes(types)[1])
print(offSynergy(types))

#allOffScores()

import Pokedex

def tris(cat):
    if cat!="weaknesses" and cat!="resistances":
        return None
    cores = []
    types = Pokedex.loadTypes()
    listTypes = list(types.keys())
    for t1 in range(len(listTypes)):
        #print("type 1:"+listTypes[t1])
        for t2 in range(t1+1,len(listTypes)):
            #print("type 2:"+listTypes[t2])
            if cat == "resistances":
                if listTypes[t2] in types[listTypes[t1]][cat] or listTypes[t2] in types[listTypes[t1]]["immunities"]:
                    for t3 in range(t1+1, len(listTypes)):
                        if listTypes[t2]!=listTypes[t3]:
                            if listTypes[t3] in types[listTypes[t2]][cat] or listTypes[t3] in types[listTypes[t2]]["immunities"]:
                                if listTypes[t1] in types[listTypes[t3]][cat] or listTypes[t1] in types[listTypes[t3]]["immunities"]:
                                #print("type 3:"+listTypes[t3])
                                    cores.append([listTypes[t1],listTypes[t2],listTypes[t3]])
            else:
                if listTypes[t2] in types[listTypes[t1]][cat]:
                    for t3 in range(t1+1, len(listTypes)):
                        if listTypes[t2]!=listTypes[t3] and listTypes[t3] in types[listTypes[t2]][cat] and listTypes[t1] in types[listTypes[t3]][cat]:
                            #print("type 3:"+listTypes[t3])
                            cores.append([listTypes[t1],listTypes[t2],listTypes[t3]])
    return cores

def combineTypes(types):
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
        #print(wri[0])
        #print(wri[1])
        #print()
        done = False
        while not done:
            done = True
            for w in wri[0]:
                for r in wri[1]:
                    if w==r:
                        del wri[0][wri[0].index(w)]
                        del wri[1][wri[1].index(r)]
                        #print(wri[0])
                        #print(wri[1])
                        #print()
                        done = False
                        break
    return wri

def superTris():
    cores = []
    types = Pokedex.loadTypes()
    listTypes = list(types.keys())
    for t1 in range(len(listTypes)):
        for t2 in range(t1+1,len(listTypes)):
            if listTypes[t2] in types[listTypes[t1]]["resistances"] and listTypes[t1] in types[listTypes[t2]]["weaknesses"]:
                for t3 in range(t1+1, len(listTypes)):
                    if listTypes[t2]!=listTypes[t3]:
                        if (listTypes[t3] in types[listTypes[t2]]["resistances"] or listTypes[t3] in types[listTypes[t2]]["immunities"]) and listTypes[t2] in types[listTypes[t3]]["weaknesses"]:
                            if (listTypes[t1] in types[listTypes[t3]]["resistances"] or listTypes[t1] in types[listTypes[t3]]["immunities"]) and listTypes[t3] in types[listTypes[t1]]["weaknesses"]:
                                cores.append([listTypes[t1],listTypes[t2],listTypes[t3]])
    return cores

import MetaDex,Pokedex,json,urllib.request,os

def findTeamMetaMatches(names,tier,size):
    if isinstance(names,list):
        if isinstance(tier,str):
            if isinstance(size,int) and size>0:
                teamMates = MetaDex.findTeamTierTeamMates(names, tier)
                if(teamMates!=None):
                    scoredMates = []
                    for k in range(0, size):
                        scoredMates.append(["Missingno", -100])
                    for k in range(len(teamMates)):
                        for i in range(len(scoredMates)):
                            if scoredMates[i][1] < teamMates[k][1]:
                                for j in range(len(scoredMates) - 1, i, -1):
                                    scoredMates[j] = scoredMates[j - 1]
                                scoredMates[i] = teamMates[k]
                                break
                    return scoredMates
            elif isinstance(size,int) and size==0:
                return []
    return None

def findPokemonMetaSpreads(name,tier,size):
    if Pokedex.findPokemonData(name)!=None:
        if isinstance(tier,str):
            if isinstance(size,int) and size>0:
                spreadsDict = MetaDex.findPokemonTierSpreads(name,tier)
                spreads = []
                for spread in spreadsDict:
                    spreads.append([spread,spreadsDict[spread]])
                if(spreads!=None):
                    scoredSpreads = []
                    for k in range(0, size):
                        scoredSpreads.append(["Hardy:0/0/0/0/0/0", -100])
                    for k in range(len(spreads)):
                        for i in range(len(scoredSpreads)):
                            if scoredSpreads[i][1] < spreads[k][1]:
                                for j in range(len(scoredSpreads) - 1, i, -1):
                                    scoredSpreads[j] = scoredSpreads[j - 1]
                                scoredSpreads[i] = spreads[k]
                                break
                    return scoredSpreads
            elif isinstance(size,int) and size==0:
                return []
    return None

def findPokemonMetaMoves(name,tier,size):
    if Pokedex.findPokemonData(name)!=None:
        if isinstance(tier,str):
            if isinstance(size,int) and size>0:
                movesDict = MetaDex.findPokemonTierMoves(name,tier)
                moves = []
                for move in movesDict:
                    if move != "":
                        moves.append([move,movesDict[move]])
                if(moves!=None):
                    scoredmoves = []
                    for k in range(0, size):
                        scoredmoves.append(["Nothing", -100])
                    for k in range(len(moves)):
                        for i in range(len(scoredmoves)):
                            if scoredmoves[i][1] < moves[k][1]:
                                for j in range(len(scoredmoves) - 1, i, -1):
                                    scoredmoves[j] = scoredmoves[j - 1]
                                scoredmoves[i] = moves[k]
                                break
                    return scoredmoves
            elif isinstance(size,int) and size==0:
                return []
    return None

def findPokemonMetaMovesExc(name,tier,size,moves):
    for move in moves:
        if move == None:
            del move
    if Pokedex.findPokemonData(name)!=None:
        if isinstance(tier,str):
            if isinstance(size,int) and size>0:
                movesDict = MetaDex.findPokemonTierMoves(name,tier)
                moves = []
                for move in movesDict:
                    if move != "":
                        moves.append([move,movesDict[move]])
                if(moves!=None):
                    scoredmoves = []
                    for k in range(0, size):
                        scoredmoves.append(["Nothing", -100])
                    for k in range(len(moves)):
                        for i in range(len(scoredmoves)):
                            if scoredmoves[i][1] < moves[k][1] and Pokedex.findMoveName(moves[k][0]) not in moves:
                                for j in range(len(scoredmoves) - 1, i, -1):
                                    scoredmoves[j] = scoredmoves[j - 1]
                                scoredmoves[i] = moves[k]
                                break
                    return scoredmoves
            elif isinstance(size,int) and size==0:
                return []
    return None

def findPokemonMetaItems(name,tier,size):
    if Pokedex.findPokemonData(name)!=None:
        if isinstance(tier,str):
            if isinstance(size,int) and size>0:
                itemsDict = MetaDex.findPokemonTierItems(name,tier)
                items = []
                for item in itemsDict:
                    items.append([item,itemsDict[item]])
                if(items!=None):
                    scoredItems = []
                    for k in range(0, size):
                        scoredItems.append(["Tackle", -100])
                    for k in range(len(items)):
                        for i in range(len(scoredItems)):
                            if scoredItems[i][1] < items[k][1]:
                                for j in range(len(scoredItems) - 1, i, -1):
                                    scoredItems[j] = scoredItems[j - 1]
                                scoredItems[i] = items[k]
                                break
                    return scoredItems
            elif isinstance(size,int) and size==0:
                return []
    return None

def rawCountTopFinds(tier,size):
    if isinstance(size,int):
        if size>0:
            data = MetaDex.findTierData(tier)
            ldata = []
            for poke in data:
                ldata.append([poke,data[poke]["Raw count"]])
            sdata = sorted(ldata,key=lambda poke: poke[1],reverse=True)
            res = []
            for i in range(size):
                res.append([sdata[i][0],sdata[i][1]])
            return res
        elif size==0:
            return []
    return None

def compress(name):
    if isinstance(name,str)==True:
        n=name.lower()
        nList = list(n)
        for i in range(len(nList)-1,-1,-1):
            if nList[i]==" " or nList[i]=="-" or nList[i]==":":
                del nList[i]
        return "".join(nList)
    else:
        return None

def downloadTier(url):
    if isinstance(url,str)==True:
        if url[42:][:-5] not in MetaDex.getTiers():
            tier = url[42:]
            try:
                with urllib.request.urlopen(url) as file:
                    python_obj = json.loads(file.read().decode())
                file.close
                with open(os.path.dirname(os.path.realpath(__file__))+"/data/tiers/"+tier,"w") as file:
                    json.dump(python_obj,file)
                file.close
                tier = tier[:-5]
                if tier not in MetaDex.getTiers():
                    MetaDex.setTiers(tier)
            except:
                print("I'm sorry, but I couldn't find that file. Download aborted.")
        else:
            print("That tier has already been dowloaded")
    else:
        print("The given variable %s is not a string!" % url)

def upDateTiers(timestamp):
    #TODO: update all tier files
    print(timestamp)

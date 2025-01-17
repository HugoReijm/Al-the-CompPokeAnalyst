import json,os,threading,Tools

def synchronized(func):
    func.__lock__ = threading.Lock()

    def synced_func(*args, **kws):
        with func.__lock__:
            return func(*args, **kws)

    return synced_func

def getTiers():
    with open(os.path.dirname(os.path.realpath(__file__))+"/data/tiers/tiers.txt","r") as data:
        python_list = data.readlines()
    data.close()
    for i in range(len(python_list)):
        python_list[i] = python_list[i].replace("\n","")
    return python_list

@synchronized
def addTier(tier):
    with open(os.path.dirname(os.path.realpath(__file__))+"/data/tiers/tiers.txt", "a") as file:
        file.write(tier+"\n")

__singletonMetaDexList=[]
for i in range(len(getTiers())):
    __singletonMetaDexList.append(None)

@synchronized
def loadTier(tier):
    tiers = getTiers()
    if tier[:-5] in tiers and tier.endswith(".json"):
        if __singletonMetaDexList[tiers.index(tier[:-5])]==None:
            with open(os.path.dirname(os.path.realpath(__file__))+"/data/tiers/"+tier,"r") as data:
                __singletonMetaDexList[tiers.index(tier[:-5])] = json.load(data)
            data.close()
        return __singletonMetaDexList[tiers.index(tier[:-5])]

def findTierInfo(tier):
    return loadTier(tier)["info"]

def findTierData(tier):
    return loadTier(tier)["data"]

def findPokemonTierData(pokemon,tier):
    pokeList = list(pokemon)
    pokeList[0] = pokeList[0].capitalize()
    for letter in range(len(pokeList)):
        if (pokeList[letter]==" " or pokeList[letter]=="-" or pokeList[letter]==":") and Tools.compress(pokemon) not in ["kommoo","hakamoo","jangmoo"]:
            pokeList[letter+1] = pokeList[letter+1].capitalize()
    pokemon = "".join(pokeList)
    data = findTierData(tier)
    if pokemon in data:
        return data[pokemon]
    else:
        return None

def findPokemonTierAbilities(pokemon, tier):
    data = findPokemonTierData(pokemon,tier)
    if data != None:
        return data["Abilities"]
    else:
        return None

def findPokemonTierItems(pokemon, tier):
    data = findPokemonTierData(pokemon,tier)
    if data != None:
        res = {}
        for item in data["Items"]:
            if item!="":
                res[item] = data["Items"][item]
        return res
    else:
        return None

def findPokemonTierRawCount(pokemon, tier):
    data = findPokemonTierData(pokemon,tier)
    if data != None:
        return data["Raw count"]
    else:
        return None

def findPokemonTierSpreads(pokemon, tier):
    data = findPokemonTierData(pokemon,tier)
    if data != None:
        return data["Spreads"]
    else:
        return None

def findPokemonTierChecks(pokemon, tier):
    data = findPokemonTierData(pokemon, tier)
    if data != None:
        return data["Checks and Counters"]
    else:
        return None

def findPokemonTierTeamMates(pokemon, tier):
    data = findPokemonTierData(pokemon,tier)
    if data != None:
        return data["Teammates"]
    else:
        return None

def findTeamTierTeamMates(team, tier):
    data = []
    res = []
    lst = []
    if isinstance(team,list)==True:
        for poke in team:
            data.append(findPokemonTierTeamMates(poke, tier))
        for poke in data[0]:
            if poke not in team:
                res.append([poke, data[0][poke]])
                lst.append(poke)
        for i in range(1, len(data)):
            for poke in data[i]:
                if poke not in team:
                    if poke not in lst:
                        res.append([poke, data[i][poke]])
                        lst.append(poke)
                    elif poke in lst:
                        res[lst.index(poke)] = [poke, (res[lst.index(poke)][1]+data[i][poke])/len(team)]
        return res
    return None

def findPokemonTierUsage(pokemon, tier):
    data = findPokemonTierData(pokemon,tier)
    if data != None:
        return data["usage"]
    else:
        return None

def findPokemonTierMoves(pokemon, tier):
    data = findPokemonTierData(pokemon,tier)
    if data != None:
        res = {}
        for move in data["Moves"]:
            if move!="":
                res[move] = data["Moves"][move]
        return res
    else:
        return None

def findPokemonTierHappiness(pokemon, tier):
    data = findPokemonTierData(pokemon,tier)
    if data != None:
        return data["Happiness"]
    else:
        return None

def findPokemonTierViabilityCeiling(pokemon, tier):
    data = findPokemonTierData(pokemon,tier)
    if data != None:
        return data["Viability Ceiling"]
    else:
        return None
    
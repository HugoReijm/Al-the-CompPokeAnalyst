import json,os

def loadPokedex():
    with open(os.path.dirname(os.path.realpath(__file__))+"/data/pokedex.json","r") as data:
        python_obj = json.load(data)
    data.close()
    return python_obj

def loadLearnSets():
    with open(os.path.dirname(os.path.realpath(__file__))+"/data/learnsets.json","r") as data:
        python_obj = json.load(data)
    data.close()
    return python_obj

def loadTypes():
    with open(os.path.dirname(os.path.realpath(__file__))+"/data/types.json", "r") as data:
        python_obj = json.load(data)
    data.close()
    return python_obj

def loadMoves():
    with open(os.path.dirname(os.path.realpath(__file__))+"/data/moves.json","r") as data:
        python_obj = json.load(data)
    data.close()
    return python_obj

def loadItems():
    with open(os.path.dirname(os.path.realpath(__file__))+"/data/items.json","r") as data:
        python_obj = json.load(data)
    data.close()
    return python_obj

def loadAbilities():
    os.path.dirname(os.path.realpath(__file__))
    with open(os.path.dirname(os.path.realpath(__file__))+"/data/abilities.json","r") as data:
        python_obj = json.load(data)
    data.close()
    return python_obj

def checkPokedex(name):
    pokedex = loadPokedex()
    if isinstance(pokedex, dict) == True:
        if isinstance(name, str) == True:
            n = name.lower()
            nlist = list(n)
            for i in range(len(nlist)-1,-1,-1):
                if nlist[i]==" " or nlist[i]=="-" or nlist[i]==":":
                    del nlist[i]
            n = "".join(nlist)
            if n in pokedex:
                return pokedex[n]
    return None

def findPokemonData(name):
    return checkPokedex(name)

def findPokemonNum(name):
    pokemon = checkPokedex(name)
    if(pokemon!=None):
        return pokemon["num"]
    else:
        return None

def findPokemonSpecies(name):
    pokemon = checkPokedex(name)
    if (pokemon != None):
        return pokemon["species"]
    else:
        return None

def findPokemonBaseSpecies(name):
    pokemon = checkPokedex(name)
    if (pokemon != None) and ("baseSpecies" in pokemon):
        return pokemon["baseSpecies"]
    else:
        return None

def findPokemonForme(name):
    pokemon = checkPokedex(name)
    if (pokemon != None) and ("forme" in pokemon):
        return pokemon["forme"]
    else:
        return None

def findPokemonBaseForme(name):
    pokemon = checkPokedex(name)
    if (pokemon != None) and ("baseForme" in pokemon):
        return pokemon["baseForme"]
    else:
        return None

def findPokemonFormeLetter(name):
    pokemon = checkPokedex(name)
    if (pokemon != None) and ("formeLetter" in pokemon):
        return pokemon["formeLetter"]
    else:
        return None

def findPokemonTypes(name):
    pokemon = checkPokedex(name)
    if (pokemon != None):
        return pokemon["types"]
    else:
        return None

def findPokemonGenderRatios(name):
    pokemon = checkPokedex(name)
    if (pokemon != None) and ("genderRatio" in pokemon):
        return pokemon["genderRatio"]
    else:
        return None

def findPokemonGender(name):
    pokemon = checkPokedex(name)
    if (pokemon != None) and ("gender" in pokemon):
        return pokemon["gender"]
    else:
        return None

def findPokemonBaseStats(name):
    pokemon = checkPokedex(name)
    if (pokemon != None):
        return pokemon["baseStats"]
    else:
        return None

def findPokemonHP(name):
    baseStats = findPokemonBaseStats(name)
    if (baseStats != None):
        return baseStats["hp"]
    else:
        return None

def findPokemonAtk(name):
    baseStats = findPokemonBaseStats(name)
    if (baseStats != None):
        return baseStats["atk"]
    else:
        return None

def findPokemonDef(name):
    baseStats = findPokemonBaseStats(name)
    if (baseStats != None):
        return baseStats["def"]
    else:
        return None

def findPokemonSpA(name):
    baseStats = findPokemonBaseStats(name)
    if (baseStats != None):
        return baseStats["spa"]
    else:
        return None

def findPokemonSpD(name):
    baseStats = findPokemonBaseStats(name)
    if (baseStats != None):
        return baseStats["spd"]
    else:
        return None

def findPokemonSpe(name):
    baseStats = findPokemonBaseStats(name)
    if (baseStats != None):
        return baseStats["spe"]
    else:
        return None

def findPokemonAbilities(name):
    pokemon = checkPokedex(name)
    if (pokemon != None):
        return pokemon["abilities"]
    else:
        return None

def findPokemonHeight(name):
    pokemon = checkPokedex(name)
    if (pokemon != None):
        return pokemon["heightm"]
    else:
        return None

def findPokemonWeight(name):
    pokemon = checkPokedex(name)
    if (pokemon != None):
        return pokemon["weightkg"]
    else:
        return None

def findPokemonColor(name):
    pokemon = checkPokedex(name)
    if (pokemon != None):
        return pokemon["color"]
    else:
        return None

def findPokemonPrevo(name):
    pokemon = checkPokedex(name)
    if (pokemon != None) and ("prevo" in pokemon):
        return pokemon["prevo"]
    else:
        return None

def findPokemonEvos(name):
    pokemon = checkPokedex(name)
    if (pokemon != None) and ("evos" in pokemon):
        return pokemon["evos"]
    else:
        return None

def findPokemonEvoLevel(name):
    pokemon = checkPokedex(name)
    if (pokemon != None) and ("evoLevel" in pokemon):
        return pokemon["evoLevel"]
    else:
        return None

def findPokemonEggGroups(name):
    pokemon = checkPokedex(name)
    if (pokemon != None):
        return pokemon["eggGroups"]
    else:
        return None

def findPokemonOtherFormes(name):
    pokemon = checkPokedex(name)
    if (pokemon != None) and ("otherFormes" in pokemon):
        return pokemon["otherFormes"]
    else:
        return None

def findPokemonLearnSet(name):
    learnsets = loadLearnSets()
    if isinstance(learnsets, dict) == True:
        if isinstance(name, str) == True:
            n = name.lower()
            if n in learnsets:
                return learnsets[n]["learnset"]
    return None

def findTypeData(name):
    types = loadTypes()
    if isinstance(types, dict) == True:
        if isinstance(name, str) == True:
            nList = list(name)
            nList[0] = nList[0].capitalize()
            capName = "".join(nList)
            if capName in types:
                return types[capName]
    return None

def findTypeHPSpreads(name):
    t = findTypeData(name)
    nList = list(name)
    nList[0] = nList[0].capitalize()
    capName = "".join(nList)
    if (t != None):
        if (capName!="Fairy") and (capName!="Normal"):
            return t["hp Sets"]
    return None

def checkMoveDex(name):
    moveDex = loadMoves()
    if isinstance(moveDex, dict) == True:
        if isinstance(name, str) == True:
            n = name.lower()
            nlist = list(n)
            for i in range(len(nlist) - 1, -1, -1):
                if nlist[i] == " " or nlist[i] == "-" or nlist[i] == "," or nlist[i] == "'":
                    del nlist[i]
            n = "".join(nlist)
            if n in moveDex:
                return moveDex[n]
    return None

def findMoveData(name):
    return checkMoveDex(name)

def findMoveNumber(name):
    move = checkMoveDex(name)
    if (move != None):
        if "num" in move:
            return move["num"]
        else:
            return None
    else:
        return None

def findMoveAccuracy(name):
    move = checkMoveDex(name)
    if (move != None):
        return move["accuracy"]
    else:
        return None

def findMoveBasePower(name):
    move = checkMoveDex(name)
    if (move != None):
        return move["basePower"]
    else:
        return None

def findMoveCategory(name):
    move = checkMoveDex(name)
    if (move != None):
        return move["category"]
    else:
        return None

def findMoveDesc(name):
    move = checkMoveDex(name)
    if "desc" in move:
        return move["desc"]
    else:
        return None

def findMoveShortDesc(name):
    move = checkMoveDex(name)
    if "shortDesc" in move:
        return move["shortDesc"]
    else:
        return None

def findMoveID(name):
    move = checkMoveDex(name)
    if (move != None):
        return move["id"]
    else:
        return None

def findMoveName(name):
    move = checkMoveDex(name)
    if (move != None):
        return move["name"]
    else:
        return None

def findMovePP(name):
    move = checkMoveDex(name)
    if (move != None):
        return move["pp"]
    else:
        return None

def findMovePriority(name):
    move = checkMoveDex(name)
    if (move != None):
        return move["priority"]
    else:
        return None

def findMoveFlags(name):
    move = checkMoveDex(name)
    if (move != None):
        return move["flags"]
    else:
        return None

def findMoveIsZ(name):
    move = checkMoveDex(name)
    if move != None :
        if "isZ" in move:
            return move["isZ"]
        else:
            return None
    else:
        return None

def findMoveZPower(name):
    move = checkMoveDex(name)
    if (move != None):
        if "zMovePower" in move:
            return move["zMovePower"]
        else:
            return None
    else:
        return None

def findMoveCritRatio(name):
    move = checkMoveDex(name)
    if (move != None):
        if "critRatio" in move:
            return move["critRatio"]
        else:
            return None
    else:
        return None

def findMoveSecondary(name):
    move = checkMoveDex(name)
    if (move != None):
        if "secondary" in move:
            return move["secondary"]
        else:
            return None
    else:
        return None

def findMoveTarget(name):
    move = checkMoveDex(name)
    if (move != None):
        return move["target"]
    else:
        return None

def findMoveType(name):
    move = checkMoveDex(name)
    if (move != None):
        return move["type"]
    else:
        return None

def findMoveContestType(name):
    move = checkMoveDex(name)
    if (move != None):
        return move["contestType"]
    else:
        return None

def checkItemDex(name):
    itemDex = loadItems()
    if isinstance(itemDex, dict) == True:
        if isinstance(name, str) == True:
            n = name.lower()
            nlist = list(n)
            for i in range(len(nlist) - 1, -1, -1):
                if nlist[i] == " " or nlist[i] == "-" or nlist[i] == ":" or nlist[i]=="'":
                    del nlist[i]
            n = "".join(nlist)
            if n in itemDex:
                return itemDex[n]
    return None

def findItemData(name):
    return checkItemDex(name)

def findItemID(name):
    item = checkItemDex(name)
    if (item != None):
        return item["id"]
    else:
        return None

def findItemName(name):
    item = checkItemDex(name)
    if (item != None):
        return item["name"]
    else:
        return None

def findItemIsUnreleased(name):
    item = checkItemDex(name)
    if (item != None):
        if "isUnreleased" in item:
            return item["isUnreleased"]
        else:
            return None
    else:
        return None

def findItemSpriteNum(name):
    item = checkItemDex(name)
    if (item != None):
        if "spritenum" in item:
            return item["spritenum"]
        else:
            return None
    else:
        return None

def findItemMegaStone(name):
    item = checkItemDex(name)
    if (item != None):
        if "megaStone" in item:
            return item["megaStone"]
        else:
            return None
    else:
        return None

def findItemMegaEvolves(name):
    item = checkItemDex(name)
    if (item != None):
        if "megaEvolves" in item:
            return item["megaEvolves"]
        else:
            return None
    else:
        return None

def findItemNum(name):
    item = checkItemDex(name)
    if (item != None):
        if "num" in item:
            return item["num"]
        else:
            return None
    else:
        return None

def findItemGen(name):
    item = checkItemDex(name)
    if (item != None):
        return item["gen"]
    else:
        return None

def findItemDesc(name):
    item = checkItemDex(name)
    if (item != None):
        if "desc" in item:
            return item["desc"]
        else:
            return None
    else:
        return None

def findItemFling(name):
    item = checkItemDex(name)
    if (item != None):
        if "fling" in item:
            return item["fling"]
        else:
            return None
    else:
        return None

def findItemFlingBasePower(name):
    flingData = findItemFling(name)
    if flingData != None:
        return flingData["basePower"]
    else:
        return None

def findItemNaturalGift(name):
    item = checkItemDex(name)
    if (item != None):
        if "naturalGift" in item:
            return item["naturalGift"]
        else:
            return None
    else:
        return None

def findItemNaturalGiftBasePower(name):
    naturalGiftData = findItemNaturalGift(name)
    if naturalGiftData != None:
        return naturalGiftData["basePower"]
    else:
        return None

def findItemNaturalGiftType(name):
    naturalGiftData = findItemNaturalGift(name)
    if naturalGiftData != None:
        return naturalGiftData["type"]
    else:
        return None

def findItemIsNonstandard(name):
    item = checkItemDex(name)
    if (item != None):
        if "isNonstandard" in item:
            return item["isNonstandard"]
        else:
            return None
    else:
        return None

def checkAbilityDex(name):
    abilityDex = loadAbilities()
    if isinstance(abilityDex, dict) == True:
        if isinstance(name, str) == True:
            n = name.lower()
            nlist = list(n)
            for i in range(len(nlist) - 1, -1, -1):
                if nlist[i] == " " or nlist[i] == "-" or nlist[i] == ":" or nlist[i] == "'":
                    del nlist[i]
            n = "".join(nlist)
            if n in abilityDex:
                return abilityDex[n]
    return None

def findAbilityData(name):
    return checkAbilityDex(name)

def findAbilityID(name):
    ability = checkAbilityDex(name)
    if (ability != None):
        return ability["id"]
    else:
        return None

def findAbilityName(name):
    ability = checkAbilityDex(name)
    if (ability != None):
        return ability["name"]
    else:
        return None

def findAbilityRating(name):
    ability = checkAbilityDex(name)
    if (ability != None):
        return ability["rating"]
    else:
        return None

def findAbilityNum(name):
    ability = checkAbilityDex(name)
    if (ability != None):
        return ability["num"]
    else:
        return None

def findAbilityDesc(name):
    ability = checkAbilityDex(name)
    if (ability != None):
        if "desc" in ability:
            return ability["desc"]
        else:
            return None
    else:
        return None

def findAbilityShortDesc(name):
    ability = checkAbilityDex(name)
    if (ability != None):
        return ability["shortDesc"]
    else:
        return None

#items = loadItems()
#for str in ["num","fling"]:
#    print("All moves without "+str)
#    for p in items:
#        if str not in items[p]:
#            print(p)
#    print()

#ability = loadAbilities()
#for str in ["desc","shortDesc","id","name","rating","num"]:
#    print("All abilities without "+str)
#    for a in ability:
#        if str not in ability[a]:
#            print(a)
#    print()

#l1 = ["helo", "hello","hi","cheese"]
#l2=[]
#for i in range(len(l1)):
#    l2.append(l1[i])
#del l2[l2.index("cheese")]
#print(l1)

#print(findMoveShortDesc("Transform"))

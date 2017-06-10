import urllib.request, json, random

#Converting JSon File from Project Folder to Python Dictionary
def convertJSONfromFolder(name):
    if isinstance(name,str)==True:
        with open(name,"r") as data:
            python_obj = json.load(data)
            return python_obj
    else:
        print("The given variable %s is not a string!" % name)

#Converting Text File to Python Object
def convertTextfromFolder(name):
    if isinstance(name,str)==True:
        with open(name,"r") as data:
            python_obj = data.read()
            return python_obj
    else:
        print("The given variable %s is not a string!" % name)

#Converting JSon File from URL to Python Dictionary
def convertJSONfromURL(url):
    if isinstance(url,str)==True:
        with urllib.request.urlopen(url) as url:
            python_obj = json.loads(url.read().decode())
            return python_obj
    else:
        print("The given variable %s is not a string!" % url)

def rewritePokedex():
    with open("data/pokedex.txt") as data:
        python_obj = data.readlines()
    data.close()
    k = 0
    seperated = []
    for i in range(len(python_obj)):
        if python_obj[i] == "\t},\n":
            pokemon = []
            for j in range(k,i+1):
                pokemon.append(python_obj[j])
            seperated.append(pokemon)
            k=i+1
    for pokemon in seperated:
        for index in range(len(pokemon)-1):
            valuelist = list(pokemon[index])
            for startindex in range(len(valuelist)):
                if valuelist[startindex]!="\t" and valuelist[startindex]!="\n" and valuelist[startindex]!="{" and valuelist[startindex]!='"':
                    i = startindex
                    break
            j = pokemon[index].index(":")
            valuelist[i]='"'+valuelist[i]
            valuelist[j]='"'+valuelist[j]
            if "genderRatio" in pokemon[index]:
                m = pokemon[index].index("M:")
                f = pokemon[index].index("F:")
                valuelist[m]='"'+valuelist[m]+'"'
                valuelist[f] = '"' + valuelist[f] + '"'
            if "baseStats" in pokemon[index]:
                hp = pokemon[index].index("hp")
                atk = pokemon[index].index("atk")
                defen = pokemon[index].index("def")
                spa = pokemon[index].index("spa")
                spd = pokemon[index].index("spd")
                spe = pokemon[index].index("spe")
                valuelist[hp] = '"'+valuelist[hp]
                valuelist[hp+1] = valuelist[hp+1]+'"'
                valuelist[atk] = '"' + valuelist[atk]
                valuelist[atk+2] = valuelist[atk+2] + '"'
                valuelist[defen] = '"' + valuelist[defen]
                valuelist[defen+2] = valuelist[defen+2] + '"'
                valuelist[spa] = '"' + valuelist[spa]
                valuelist[spa+2] = valuelist[spa+2] + '"'
                valuelist[spd] = '"' + valuelist[spd]
                valuelist[spd+2] = valuelist[spd+2] + '"'
                valuelist[spe] = '"' + valuelist[spe]
                valuelist[spe+2] = valuelist[spe+2] + '"'
            if "abilities" in pokemon[index]:
                zero = pokemon[index].index("0:")
                valuelist[zero] = '"' + valuelist[zero] + '"'
                if pokemon[index].find("1:")!=-1:
                    one = pokemon[index].index("1:")
                    valuelist[one] = '"' + valuelist[one] + '"'
                if pokemon[index].find("H:")!=-1:
                    h = pokemon[index].index("H:")
                    valuelist[h] = '"' + valuelist[h] + '"'
                if pokemon[index].find("S:")!=-1:
                    s = pokemon[index].index("S:")
                    valuelist[s] = '"' + valuelist[s] + '"'
            pokemon[index] = "".join(valuelist)
        if ",\n" in pokemon[len(pokemon)-2]:
            i = pokemon[len(pokemon)-2].index(",\n")
            lastlist = list(pokemon[len(pokemon)-2])
            del lastlist[i]
            pokemon[len(pokemon) - 2] = "".join(lastlist)
    file= open("data/pokedex-test.json","w")
    for pokemon in seperated:
        for line in pokemon:
            file.write(line)
    file.close()

def rewriteLearnSets():
    with open("data/learnsets.txt") as data:
        python_obj = data.readlines()
    data.close()
    k = 0
    seperated = []
    for i in range(len(python_obj)):
        if python_obj[i] == "\t}},\n":
            pokemon = []
            for j in range(k,i+1):
                pokemon.append(python_obj[j])
            seperated.append(pokemon)
            k=i+1
    #print(seperated[2])
    for pokemon in seperated:
        for index in range(len(pokemon)-1):
            valuelist = list(pokemon[index])
            for startindex in range(len(valuelist)):
                if valuelist[startindex]!="\t" and valuelist[startindex]!="\n" and valuelist[startindex]!="{" and valuelist[startindex]!='"':
                    i = startindex
                    break
            j = pokemon[index].index(":")
            valuelist[i]='"'+valuelist[i]
            valuelist[j]='"'+valuelist[j]
            pokemon[index] = "".join(valuelist)
            if ": {learnset: {\n" in pokemon[0]:
                i = pokemon[0].index("learnset: {\n")
                firstlist = list(pokemon[0])
                firstlist[i] = '"'+firstlist[i]
                firstlist[i+8] = '"'+firstlist[i+8]
                pokemon[0] = "".join(firstlist)
            if ",\n" in pokemon[len(pokemon) - 2]:
                i = pokemon[len(pokemon) - 2].index(",\n")
                lastlist = list(pokemon[len(pokemon) - 2])
                del lastlist[i]
                pokemon[len(pokemon) - 2] = "".join(lastlist)
    #print(seperated[2])
    file = open("data/learnsets-test.json", "w")
    for pokemon in seperated:
        for line in pokemon:
            file.write(line)
    file.close()

def rewriteMoves():
    #BIT OF A MESS. DONT REALLY USE
    with open("data/moves.txt") as data:
        python_obj = data.readlines()
    data.close()
    k = 0
    seperated = []
    for i in range(len(python_obj)):
        if python_obj[i] == "\t},\n":
            pokemon = []
            for j in range(k,i+1):
                pokemon.append(python_obj[j])
            seperated.append(pokemon)
            k=i+1
    #print(seperated[3])
    #for line in seperated[len(seperated)-1]:
    #    print(line)
    for data in seperated:
        for index in range(1,len(data)-1):
            valuelist = list(data[index])
            if ":" in data[index]:
                for startindex in range(len(valuelist)):
                    if valuelist[startindex]!="\t" and valuelist[startindex]!="\n" and valuelist[startindex]!="{":
                        i = startindex
                        break
                j = data[index].index(":")
                valuelist[i]='"'+valuelist[i]
                valuelist[j]='"'+valuelist[j]
                data[index] = "".join(valuelist)
            if 'zMoveBoost":' in data[index]:
                stats = ["hp:","atk:","def:","spa:","spd","spe"]
                for s in stats:
                    if s in data[index]:
                        i = data[index].index(s)
                        indexlist = list(data[index])
                        indexlist[i] = '"' + indexlist[i]
                        if s=="hp:":
                            indexlist[i + 2] = '"' + indexlist[i + 2]
                        else:
                            indexlist[i + 3] = '"' + indexlist[i + 3]
                        data[index] = "".join(indexlist)
            for str in ["contact:","recharge:","protect:","mirror:","punch:","defrost:","heal:","snatch:","powder:","pulse:","distance:","bullet:","authentic:","mystery:",'reflectable:','bite:','nonsky:','sound:',"charge:","gravity:"]:
                if str in data[index]:
                    i = data[index].index(str)
                    indexlist = list(data[index])
                    indexlist[i] = '"'+indexlist[i]
                    indexlist[i+len(str)-1] = '"'+indexlist[i+len(str)-1]
                    data[index] = "".join(indexlist)

            if 'boosts":' in data[index]:
                for j in range(index+1,len(data)):
                    if "\t\t},\n" in data[j]:
                        if "," in data[j-1]:
                            indexlist = list(data[j-1])
                            i = indexlist.index(",")
                            del indexlist[i]
                            data[j-1] = "".join(indexlist)
                            break
            indexlist = list(data[index])
            for i in range(len(indexlist)-1,0,-1):
                if "," == indexlist[i]:
                    if "'" == indexlist[i-1]:
                        for j in range(i-2,0,-1):
                            if "'" == indexlist[j]:
                                indexlist[i-1]='"'
                                indexlist[j]='"'
                                break
            data[index]="".join(indexlist)
        for str in ['onTry','onHit','basePowerCallback','effect','beforeTurnCallback','onAfterSubDamage','damageCallback','onPrepareHit','beforeMoveCallback','onMoveAborted',"onEffectiveness",'onAfterMove','onModifyMove','onSourceBasePower','onEnd','onMoveFail','onBasePower']:
            for eIndex in range(len(data)-1,0,-1):
                if str in data[eIndex]:
                    for i in range(eIndex+1,len(data)):
                        if not data[i].startswith("\t\t\t") or "\t\t}," in data[i]:
                            for k in range(i, eIndex - 1, -1):
                                del data[k]
                            break
        if 'flags":' in data[index] and data[index+1].startswith("\t\t\t"):
            for f in range(index + 1, len(data)):
                if not data[f].startswith("\t\t\t") or "\t\t}," in data[f]:
                    for k in range(f, index - 1, -1):
                        del data[k]
                    break
        if ",\n" in data[len(data) - 2]:
            i = data[len(data) - 2].index(",\n")
            lastlist = list(data[len(data) - 2])
            del lastlist[i]
            data[len(data) - 2] = "".join(lastlist)
    file = open("data/moves-test.json", "w")
    for data in seperated:
        for line in data:
            file.write(line)
    file.close()

def rewriteItem():
    with open("data/items.txt") as data:
        python_obj = data.readlines()
    data.close()
    k = 0
    seperated = []
    for i in range(len(python_obj)):
        if python_obj[i] == "\t},\n":
            pokemon = []
            for j in range(k, i + 1):
                pokemon.append(python_obj[j])
            seperated.append(pokemon)
            k = i + 1
    for item in seperated:
        for index in range(1, len(item) - 1):
            valuelist = list(item[index])
            if ":" in item[index]:
                for startindex in range(len(valuelist)):
                    if valuelist[startindex] != "\t" and valuelist[startindex] != "\n" and valuelist[startindex] != "{":
                        i = startindex
                        break
                j = item[index].index(":")
                valuelist[i] = '"' + valuelist[i]
                valuelist[j] = '"' + valuelist[j]
                item[index] = "".join(valuelist)
            indexlist = list(item[index])
            for i in range(len(indexlist) - 1, 0, -1):
                if "," == indexlist[i]:
                    if "'" == indexlist[i - 1]:
                        for j in range(i - 2, 0, -1):
                            if "'" == indexlist[j]:
                                indexlist[i - 1] = '"'
                                indexlist[j] = '"'
                                break
            item[index] = "".join(indexlist)
        for str in ["onTakeItem","onBasePower","onUpdate","onTry","onTrapPokemon","onEat","onStart","onAfter","onHit","onDamage","onEffectiveness","onChargeMove","onImmunity","onDisableMove","onModify","onSource","onResidual","onSwitchIn","onPrimal","onAttract"]:
            for eIndex in range(len(item)-1,0,-1):
                if str in item[eIndex]:
                    for i in range(eIndex+1,len(item)):
                        if not item[i].startswith("\t\t\t") or "\t\t}," in item[i]:
                            for k in range(i, eIndex - 1, -1):
                                del item[k]
                            break
        if ",\n" in item[len(item) - 2]:
            i = item[len(item) - 2].index(",\n")
            lastlist = list(item[len(item) - 2])
            del lastlist[i]
            item[len(item) - 2] = "".join(lastlist)
        file = open("data/items-test.json", "w")
        for item in seperated:
            for line in item:
                file.write(line)
        file.close()

def rewriteAbilities():
    with open("data/abilities.txt") as data:
        python_obj = data.readlines()
    data.close()
    k = 0
    seperated = []
    for i in range(len(python_obj)):
        if python_obj[i] == "\t},\n":
            pokemon = []
            for j in range(k, i + 1):
                pokemon.append(python_obj[j])
            seperated.append(pokemon)
            k = i + 1
    #randint = random.randint(0,len(seperated)-1)
    #for i in range(len(seperated[randint])):
    #    print(seperated[randint][i])
    for ability in seperated:
        for index in range(1, len(ability) - 1):
            valuelist = list(ability[index])
            if ":" in ability[index]:
                for startindex in range(len(valuelist)):
                    if valuelist[startindex] != "\t" and valuelist[startindex] != "\n" and valuelist[startindex] != "{":
                        i = startindex
                        break
                j = ability[index].index(":")
                valuelist[i] = '"' + valuelist[i]
                valuelist[j] = '"' + valuelist[j]
                ability[index] = "".join(valuelist)
        done = False
        while done == False:
            done = True
            for index in range(1,len(ability)):
                if "{" in ability[index]:
                    for k in range(index,len(ability)-1):
                        if ability[k] == "\t\t},\n":
                            endindex = k
                            break
                    for k in range(endindex,index-1,-1):
                        del ability[k]
                    done = False
                    break
                else:
                    continue

        if ",\n" in ability[len(ability) - 2]:
            print(ability[len(ability) - 2])
            i = ability[len(ability) - 2].index(",\n")
            lastlist = list(ability[len(ability) - 2])
            del lastlist[i]
            ability[len(ability) - 2] = "".join(lastlist)
    #for i in range(len(seperated[randint])):
    #    print(seperated[randint][i])

    file = open("data/abilities-test.json", "w")
    for ability in seperated:
        for line in ability:
            file.write(line)
    file.close()
# name = "data/pokedex-test.json"
# python_obj=convertJSONfromFolder(name)
# print(type(python_obj))
# print(python_obj["arceus"]["baseStats"]["hp"])

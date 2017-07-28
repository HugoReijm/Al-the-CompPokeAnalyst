from tkinter import *
from tkinter import ttk
import Pokedex, MetaDex, Tools

class TeamAnalyzer:

    @staticmethod
    def defCombineTypes(types, scrappy):
        if isinstance(types, list):
            wri = []
            wri.append([])
            wri.append([])
            wri.append([])
            # seperating between single and dual type Pokemon
            if len(types) == 2 and types[0] != types[1]:
                wri.append([])
                wri.append([])

                # collecting data on type #1
                data1 = Pokedex.findTypeData(types[0])
                w1 = []
                r1 = []
                i1 = []
                for w in data1["weaknesses"]:
                    if w != "":
                        w1.append(w)
                for r in data1["resistances"]:
                    if r != "":
                        r1.append(r)
                for i in data1["immunities"]:
                    if i != "":
                        i1.append(i)

                # collecting data on type #2
                data2 = Pokedex.findTypeData(types[1])
                w2 = []
                r2 = []
                i2 = []
                for w in data2["weaknesses"]:
                    if w != "":
                        w2.append(w)
                for r in data2["resistances"]:
                    if r != "":
                        r2.append(r)
                for i in data2["immunities"]:
                    if i != "":
                        i2.append(i)

                # combining weaknesses
                done = False
                while not done:
                    done = True
                    for a in w1:
                        for b in w2:
                            if a == b:
                                wri[0].append(a)
                                del w1[w1.index(a)]
                                del w2[w2.index(b)]
                                done = False
                                break
                for a in w1:
                    wri[1].append(a)
                for b in w2:
                    wri[1].append(b)

                # combining resistances
                done = False
                while not done:
                    done = True
                    for a in r1:
                        for b in r2:
                            if a == b:
                                wri[3].append(a)
                                del r1[r1.index(a)]
                                del r2[r2.index(b)]
                                done = False
                                break
                for a in r1:
                    wri[2].append(a)
                for b in r2:
                    wri[2].append(b)

                for a in i1:
                    if a in ["Normal", "Fighting"]:
                        if scrappy == False:
                            wri[4].append(a)
                    else:
                        wri[4].append(a)
                for b in i2:
                    if b in ["Normal", "Fighting"]:
                        if scrappy == False:
                            wri[4].append(b)
                    else:
                        wri[4].append(b)

                done = False
                while not done:
                    done = True
                    for w in wri[1]:
                        for r in wri[2]:
                            if w == r:
                                del wri[1][wri[1].index(w)]
                                del wri[2][wri[2].index(r)]
                                done = False
                                break

                for a in wri[4]:
                    done = False
                    while not done:
                        done = True
                        for b in wri[2]:
                            if a == b:
                                del wri[2][wri[2].index(b)]
                                done = False
                                break
                    done = False
                    while not done:
                        done = True
                        for b in wri[1]:
                            if a == b:
                                del wri[1][wri[1].index(b)]
                                done = False
                                break
                done = False
                while not done:
                    done = True
                    for a in wri[4]:
                        for b in wri[4]:
                            if a == b and a is not b:
                                del wri[4][wri[4].index(a)]
                                done = False
                                break
            else:
                data = Pokedex.findTypeData(types[0])
                for w in data["weaknesses"]:
                    if w != "":
                        wri[0].append(w)
                for r in data["resistances"]:
                    if r != "":
                        wri[1].append(r)
                for i in data["immunities"]:
                    if i != "":
                        if i in ["Normal", "Fighting"]:
                            if scrappy == False:
                                wri[2].append(i)
                        else:
                            wri[2].append(i)
            return wri
        else:
            return None

    @staticmethod
    def calcDamage(level, basePower, atk, defn, modifier):
        return (((2 * level / 5 + 2) * basePower * atk / defn) / 50 + 2) * modifier

    def checkAndCounters(self,shell):
        self.counterMssngr.config(state=NORMAL)
        self.counterMssngr.delete(1.0, END)
        for poke in MetaDex.findTierData(shell.tierfile):
            if MetaDex.findPokemonTierUsage(poke,shell.tierfile)>0.0095:
                #Find necessary pokemon data
                pokeName = Pokedex.findPokemonSpecies(poke)
                pokeAbilities = []
                abilities = Pokedex.findPokemonAbilities(pokeName)
                for index in abilities:
                    pokeAbilities.append(abilities[index])
                pokeTyping=Pokedex.findPokemonTypes(pokeName)
                maxlevel=0
                for member in shell.teamMatesDict:
                    if shell.teamMatesDict[member]["level"]>maxlevel:
                        maxlevel=shell.teamMatesDict[member]["level"]
                pokeBaseStats=[]
                pokeBaseStats.append(Pokedex.findPokemonBaseStats(pokeName)["hp"])
                pokeBaseStats.append(Pokedex.findPokemonBaseStats(pokeName)["atk"])
                pokeBaseStats.append(Pokedex.findPokemonBaseStats(pokeName)["def"])
                pokeBaseStats.append(Pokedex.findPokemonBaseStats(pokeName)["spa"])
                pokeBaseStats.append(Pokedex.findPokemonBaseStats(pokeName)["spd"])
                pokeBaseStats.append(Pokedex.findPokemonBaseStats(pokeName)["spe"])
                pokeHP=shell.hpStatCalc(pokeBaseStats[0], 0, 31, maxlevel)
                maxDamage = 0

                sunnyday = False
                raindance = False
                sandstorm = False
                hail = False
                electricterrain=False
                psychicterrain=False
                grassyterrain=False
                mistyterrain=False
                for member in shell.teamMatesDict:
                    for m in shell.teamMatesDict[member]["moves"]:
                        if shell.teamMatesDict[member]["moves"][m] == "Sunny Day":
                            sunnyday = True
                        elif shell.teamMatesDict[member]["moves"][m] == "Rain Dance":
                            raindance = True
                        elif shell.teamMatesDict[member]["moves"][m] == "Sandstorm":
                            sandstorm = True
                        elif shell.teamMatesDict[member]["moves"][m] == "Hail":
                            hail = True
                        elif shell.teamMatesDict[member]["moves"][m] == "Electric Terrain":
                            electricterrain=True
                        elif shell.teamMatesDict[member]["moves"][m] == "Psychic Terrain":
                            psychicterrain=True
                        elif shell.teamMatesDict[member]["moves"][m] == "Grassy Terrain":
                            grassyterrain=True
                        elif shell.teamMatesDict[member]["moves"][m] == "Misty Terrain":
                            mistyterrain=True

                for member in shell.teamMatesDict:
                    if shell.teamMatesDict[member]["ability"] == "Scrappy":
                        combinedWRI = self.defCombineTypes(pokeTyping, True)
                    else:
                        combinedWRI = self.defCombineTypes(pokeTyping, False)

                    memberTyping = Pokedex.findPokemonTypes(member)
                    for move in shell.teamMatesDict[member]["moves"]:
                        if shell.teamMatesDict[member]["moves"][move]!=None:
                            moveCat = Pokedex.findMoveCategory(shell.teamMatesDict[member]["moves"][move])
                            if moveCat != "Status":
                                modifier = 1
                                powerMod = 1
                                physAtkMod = 1
                                physDefMod = 1
                                specAtkMod = 1
                                specDefMod = 1

                                #Member's Ability
                                if shell.teamMatesDict[member]["ability"] in ["Huge Power", "Pure Power"]:
                                    physAtkMod = physAtkMod * 2

                                #Member's Abilities Modifying Types
                                moveType = Pokedex.findMoveType(shell.teamMatesDict[member]["moves"][move])
                                if moveType == "Normal":
                                    if shell.teamMatesDict[member]["ability"] == "Aerilate":
                                        powerMod = powerMod * 1.2
                                        moveType = "Flying"
                                    elif shell.teamMatesDict[member]["ability"] == "Pixilate":
                                        powerMod = powerMod * 1.2
                                        moveType = "Fairy"
                                    elif shell.teamMatesDict[member]["ability"] == "Galvanize":
                                        powerMod = powerMod * 1.2
                                        moveType = "Electric"
                                    elif shell.teamMatesDict[member]["ability"] == "Refrigerate":
                                        powerMod = powerMod * 1.2
                                        moveType = "Ice"
                                else:
                                    if shell.teamMatesDict[member]["ability"] == "Normalize":
                                        powerMod = powerMod * 1.2
                                        moveType = "Normal"

                                #Member's Items Modifying Types
                                if shell.teamMatesDict[member]["item"] in ["Silk Scarf"]:
                                    if moveType == "Normal":
                                        powerMod = powerMod * 1.2
                                elif shell.teamMatesDict[member]["item"] in ["Flame Plate", "Charcoal"]:
                                    if "Arceus" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Judgement":
                                            if shell.teamMatesDict[member]["item"] == "Flame Plate":
                                                moveType = "Fire"
                                    if moveType == "Fire":
                                        powerMod = powerMod * 1.2
                                elif shell.teamMatesDict[member]["item"] in ["Splash Plate", "Mystic Water","Sea Incense", "Wave Incense"]:
                                    if "Arceus" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Judgement":
                                            if shell.teamMatesDict[member]["item"] == "Splash Plate":
                                                moveType = "Water"
                                    if moveType == "Water":
                                        powerMod = powerMod * 1.2
                                elif shell.teamMatesDict[member]["item"] in ["Zap Plate", "Magnet"]:
                                    if "Arceus" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Judgement":
                                            if shell.teamMatesDict[member]["item"] == "Zap Plate":
                                                moveType = "Electric"
                                    if moveType == "Electric":
                                        powerMod = powerMod * 1.2
                                elif shell.teamMatesDict[member]["item"] in ["Meadow Plate", "Miracle Seed","Rose Incense"]:
                                    if "Arceus" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Judgement":
                                            if shell.teamMatesDict[member]["item"] == "Meadow Plate":
                                                moveType = "Grass"
                                    if moveType == "Grass":
                                        powerMod = powerMod * 1.2
                                elif shell.teamMatesDict[member]["item"] in ["Icicle Plate", "Never-Melt Ice"]:
                                    if "Arceus" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Judgement":
                                            if shell.teamMatesDict[member]["item"] == "Icicle Plate":
                                                moveType = "Ice"
                                    if moveType == "Ice":
                                        powerMod = powerMod * 1.2
                                elif shell.teamMatesDict[member]["item"] in ["Fist Plate", "Black Belt"]:
                                    if "Arceus" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Judgement":
                                            if shell.teamMatesDict[member]["item"] == "Fist Plate":
                                                moveType = "Fighting"
                                    if moveType == "Fighting":
                                        powerMod = powerMod * 1.2
                                elif shell.teamMatesDict[member]["item"] in ["Toxic Plate", "Poison Barb"]:
                                    if "Arceus" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Judgement":
                                            if shell.teamMatesDict[member]["item"] == "Toxic Plate":
                                                moveType = "Poison"
                                    if moveType == "Poison":
                                        powerMod = powerMod * 1.2
                                elif shell.teamMatesDict[member]["item"] in ["Earth Plate", "Soft Sand"]:
                                    if "Arceus" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Judgement":
                                            if shell.teamMatesDict[member]["item"] == "Earth Plate":
                                                moveType = "Ground"
                                    if moveType == "Ground":
                                        powerMod = powerMod * 1.2
                                elif shell.teamMatesDict[member]["item"] in ["Sky Plate", "Sharp Beak"]:
                                    if "Arceus" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Judgement":
                                            if shell.teamMatesDict[member]["item"] == "Sky Plate":
                                                moveType = "Flying"
                                    if moveType == "Flying":
                                        powerMod = powerMod * 1.2
                                elif shell.teamMatesDict[member]["item"] in ["Mind Plate", "Twisted Spoon","Odd Incense"]:
                                    if "Arceus" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Judgement":
                                            if shell.teamMatesDict[member]["item"] == "Mind Plate":
                                                moveType = "Psychic"
                                    if moveType == "Psychic":
                                        powerMod = powerMod * 1.2
                                elif shell.teamMatesDict[member]["item"] in ["Insect Plate", "Silver Powder"]:
                                    if "Arceus" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Judgement":
                                            if shell.teamMatesDict[member]["item"] == "Insect Plate":
                                                moveType = "Bug"
                                    if moveType == "Bug":
                                        powerMod = powerMod * 1.2
                                elif shell.teamMatesDict[member]["item"] in ["Stone Plate", "Hard Stone","Rock Incense"]:
                                    if "Arceus" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Judgement":
                                            if shell.teamMatesDict[member]["item"] == "Stone Plate":
                                                moveType = "Rock"
                                    if moveType == "Rock":
                                        powerMod = powerMod * 1.2
                                elif shell.teamMatesDict[member]["item"] in ["Spooky Plate", "Spell Tag"]:
                                    if "Arceus" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Judgement":
                                            if shell.teamMatesDict[member]["item"] == "Spooky Plate":
                                                moveType = "Ghost"
                                    if moveType == "Ghost":
                                        powerMod = powerMod * 1.2
                                elif shell.teamMatesDict[member]["item"] in ["Draco Plate", "Dragon Fang"]:
                                    if "Arceus" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Judgement":
                                            if shell.teamMatesDict[member]["item"] == "Draco Plate":
                                                moveType = "Dragon"
                                    if moveType == "Dragon":
                                        powerMod = powerMod * 1.2
                                elif shell.teamMatesDict[member]["item"] in ["Dread Plate", "Black Glasses"]:
                                    if "Arceus" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Judgement":
                                            if shell.teamMatesDict[member]["item"] == "Dread Plate":
                                                moveType = "Dark"
                                    if moveType == "Dark":
                                        powerMod = powerMod * 1.2
                                elif shell.teamMatesDict[member]["item"] in ["Iron Plate", "Metal Coat"]:
                                    if "Arceus" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Judgement":
                                            if shell.teamMatesDict[member]["item"] == "Iron Plate":
                                                moveType = "Steel"
                                    if moveType == "Steel":
                                        powerMod = powerMod * 1.2
                                elif shell.teamMatesDict[member]["item"] in ["Pixie Plate"]:
                                    if "Arceus" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Judgement":
                                            if shell.teamMatesDict[member]["item"] == "Pixie Plate":
                                                moveType = "Fairy"
                                    if moveType == "Fairy":
                                        powerMod = powerMod * 1.2

                                if shell.teamMatesDict[member]["item"] == "Fire Memory":
                                    if "Silvally" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move]=="Multi Attack":
                                            moveType="Fire"
                                elif shell.teamMatesDict[member]["item"] == "Water Memory":
                                    if "Silvally" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move]=="Multi Attack":
                                            moveType="Water"
                                elif shell.teamMatesDict[member]["item"] == "Electric Memory":
                                    if "Silvally" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Multi Attack":
                                            moveType="Electric"
                                elif shell.teamMatesDict[member]["item"] == "Grass Memory":
                                    if "Silvally" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Multi Attack":
                                            moveType = "Grass"
                                elif shell.teamMatesDict[member]["item"] == "Ice Memory":
                                    if "Silvally" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Multi Attack":
                                            moveType = "Ice"
                                elif shell.teamMatesDict[member]["item"] == "Fighting Memory":
                                    if "Silvally" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Multi Attack":
                                            moveType = "Fighting"
                                elif shell.teamMatesDict[member]["item"] == "Toxic Memory":
                                    if "Silvally" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Multi Attack":
                                            moveType = "Toxic"
                                elif shell.teamMatesDict[member]["item"] == "Ground Memory":
                                    if "Silvally" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Multi Attack":
                                            moveType = "Ground"
                                elif shell.teamMatesDict[member]["item"] == "Flying Memory":
                                    if "Silvally" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Multi Attack":
                                            moveType = "Flying"
                                elif shell.teamMatesDict[member]["item"] == "Psychic Memory":
                                    if "Silvally" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Multi Attack":
                                            moveType = "Psychic"
                                elif shell.teamMatesDict[member]["item"] == "Bug Memory":
                                    if "Silvally" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Multi Attack":
                                            moveType = "Bug"
                                elif shell.teamMatesDict[member]["item"] == "Rock Memory":
                                    if "Silvally" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Multi Attack":
                                            moveType = "Rock"
                                elif shell.teamMatesDict[member]["item"] == "Ghost Memory":
                                    if "Silvally" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Multi Attack":
                                            moveType = "Ghost"
                                elif shell.teamMatesDict[member]["item"] == "Dragon Memory":
                                    if "Silvally" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Multi Attack":
                                            moveType = "Dragon"
                                elif shell.teamMatesDict[member]["item"] == "Dark Memory":
                                    if "Silvally" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Multi Attack":
                                            moveType = "Dark"
                                elif shell.teamMatesDict[member]["item"] == "Steel Memory":
                                    if "Silvally" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Multi Attack":
                                            moveType = "Steel"
                                elif shell.teamMatesDict[member]["item"] == "Fairy Memory":
                                    if "Silvally" in shell.teamMatesDict[member]["species"]:
                                        if shell.teamMatesDict[member]["moves"][move] == "Multi Attack":
                                            moveType = "Fairy"

                                #Effectiveness
                                if len(combinedWRI) == 3:
                                    if moveType in combinedWRI[0]:
                                        modifier = modifier * 2
                                        if ("Solid Rock" in pokeAbilities or "Filter" in pokeAbilities) and shell.teamMatesDict[member]["ability"] not in ["Mold Breaker","Teravolt","Turboblaze"]:
                                            modifier=modifier*0.75
                                    elif moveType in combinedWRI[1]:
                                        modifier = modifier * 0.5
                                    elif moveType in combinedWRI[2]:
                                        modifier = 0
                                    if "Wonder Guard" in pokeAbilities and shell.teamMatesDict[member]["ability"] not in ["Mold Breaker","Teravolt","Turboblaze"] and moveType not in combinedWRI[0]:
                                        modifier = 0
                                elif len(combinedWRI) == 5:
                                    if moveType in combinedWRI[0]:
                                        modifier = modifier * 4
                                        if ("Solid Rock" in pokeAbilities or "Filter" in pokeAbilities) and shell.teamMatesDict[member]["ability"] not in ["Mold Breaker","Teravolt","Turboblaze"]:
                                            modifier=modifier*0.75
                                    elif moveType in combinedWRI[1]:
                                        modifier = modifier * 2
                                        if ("Solid Rock" in pokeAbilities or "Filter" in pokeAbilities) and shell.teamMatesDict[member]["ability"] not in ["Mold Breaker","Teravolt","Turboblaze"]:
                                            modifier=modifier*0.75
                                    elif moveType in combinedWRI[2]:
                                        modifier = modifier * 0.5
                                    elif moveType in combinedWRI[3]:
                                        modifier = modifier * 0.25
                                    elif moveType in combinedWRI[4]:
                                        modifier = 0
                                    if "Wonder Guard" in pokeAbilities and moveType not in combinedWRI[0] and moveType not in combinedWRI[1]:
                                        modifier = 0
                                else:
                                    print("Oops, something went wrong here.")

                                #Weather
                                if shell.teamMatesDict[member]["ability"]=="Drought" or sunnyday:
                                    if moveType=="Fire":
                                        modifier=modifier*1.5
                                    elif moveType=="Water":
                                        modifier=modifier*0.5
                                elif shell.teamMatesDict[member]["ability"]=="Desolate Land":
                                    if moveType == "Fire":
                                        modifier = modifier * 1.5
                                    elif moveType == "Water":
                                        modifier = 0
                                elif shell.teamMatesDict[member]["ability"]=="Drizzle" or raindance:
                                    if moveType == "Water":
                                        modifier=modifier*1.5
                                    elif moveType == "Fire":
                                        modifier=modifier*0.5
                                elif shell.teamMatesDict[member]["ability"]=="Primordial Sea":
                                    if moveType == "Water":
                                        modifier=modifier*1.5
                                    elif moveType == "Fire":
                                        modifier=0
                                elif shell.teamMatesDict[member]["ability"]=="Sand Stream" or sandstorm:
                                    if "Rock" in pokeTyping:
                                        if moveCat=="Special":
                                            specDefMod=specDefMod*1.5
                                    if shell.teamMatesDict["ability"] == "sandforce":
                                        if moveType in ["Steel","Ground","Rock"]:
                                            powerMod=powerMod*1.33
                                elif shell.teamMatesDict[member]["ability"]=="Snow Warning" or hail:
                                    pass
                                if "Delta Stream" in pokeAbilities:
                                    if "Flying" in pokeTyping:
                                        if moveType in ["Electric","Rock","Ice"]:
                                            modifier=powerMod*0.5

                                #Terrains
                                if shell.teamMatesDict[member]["ability"]=="Electric Surge" or electricterrain:
                                    if moveType=="Electric":
                                        if "Flying" not in memberTyping and shell.teamMatesDict[member]["ability"]!="Levitate":
                                            powerMod=powerMod*1.5
                                elif shell.teamMatesDict[member]["ability"]=="Psychic Surge" or psychicterrain:
                                    if moveType=="Psychic":
                                        if "Flying" not in memberTyping and shell.teamMatesDict[member]["ability"] != "Levitate":
                                            powerMod=powerMod*1.5
                                elif shell.teamMatesDict[member]["ability"]=="Grassy Surge" or grassyterrain:
                                    if moveType=="Grass":
                                        if "Flying" not in memberTyping and shell.teamMatesDict[member]["ability"] != "Levitate":
                                            powerMod=powerMod*1.50
                                    elif shell.teamMatesDict[member]["moves"][move] in ["Earthquake","Bulldoze","Magnitude"]:
                                        powerMod=powerMod*0.5
                                elif shell.teamMatesDict[member]["ability"]=="Misty Surge" or mistyterrain:
                                    if moveType=="Dragon":
                                        if "Flying" not in memberTyping and shell.teamMatesDict[member]["ability"] != "Levitate":
                                            if "Flying" not in pokeTyping and "Levitate" not in pokeAbilities:
                                                powerMod=powerMod*0.5

                                #Typings and Abilities
                                if moveType == "Fire":
                                    if "Flash Fire" in pokeAbilities and shell.teamMatesDict[member]["ability"] not in ["Mold Breaker","Teravolt","Turboblaze"]:
                                        modifier = 0
                                    elif "Primordial Sea" in pokeAbilities:
                                        modifier=0
                                    elif "Drizzle" in pokeAbilities and shell.teamMatesDict[member]["ability"]!="Drizzle" and not raindance:
                                        modifier=modifier*0.5
                                    elif "Dry Skin" in pokeAbilities:
                                        modifier = modifier * 1.25
                                    elif ("Drought" in pokeAbilities or "Desolate Land" in pokeAbilities) and shell.teamMatesDict[member]["ability"] not in ["Drought","Desolate Land"] and not sunnyday:
                                        modifier=modifier*1.5
                                    elif "Fluffy" in pokeAbilities:
                                        modifier = modifier * 2
                                    elif ("Thick Fat" in pokeAbilities or "Water Bubble" in pokeAbilities) and shell.teamMatesDict[member]["ability"] not in ["Mold Breaker","Teravolt","Turboblaze"]:
                                        modifier = modifier * 0.5
                                elif moveType == "Water":
                                    if ("Storm Drain" in pokeAbilities or "Water Absorb" in pokeAbilities) and shell.teamMatesDict[member]["ability"] not in ["Mold Breaker","Teravolt","Turboblaze"]:
                                        modifier = 0
                                    elif "Desolate Land" in pokeAbilities:
                                        modifier=0
                                    elif "Drought" in pokeAbilities and shell.teamMatesDict[member]["ability"]!="Drought" and not sunnyday:
                                        modifier=modifier*0.5
                                    elif ("Drizzle" in pokeAbilities or "Primordial Sea" in pokeAbilities) and shell.teamMatesDict[member]["ability"] not in ["Drizzle","Primordial Sea"] and not raindance:
                                        modifier=modifier*1.5
                                    if shell.teamMatesDict[member]["ability"] == "Water Bubble":
                                        powerMod = powerMod * 2
                                elif moveType == "Electric" and ("Lightning Rod" in pokeAbilities or "Volt Absorb" in pokeAbilities or "Motor Drive" in pokeAbilities) and shell.teamMatesDict[member]["ability"] not in ["Mold Breaker","Teravolt","Turboblaze"]:
                                        modifier = 0
                                elif moveType == "Grass" and "Sap Sipper" in pokeAbilities and shell.teamMatesDict[member]["ability"] not in ["Mold Breaker","Teravolt","Turboblaze"]:
                                    modifier = 0
                                elif moveType == "Ice" and "Thick Fat" in pokeAbilities and shell.teamMatesDict[member]["ability"] not in ["Mold Breaker","Teravolt","Turboblaze"]:
                                    modifier = modifier * 0.5
                                elif moveType == "Ground" and "Levitate" in pokeAbilities and shell.teamMatesDict[member]["ability"] not in ["Mold Breaker","Teravolt","Turboblaze"]:
                                    modifier = 0
                                elif moveType == "Dark" and shell.teamMatesDict[member]["ability"] == "Dark Aura":
                                    if "Aura Break" in pokeAbilities:
                                        powerMod = powerMod * 0.75
                                    else:
                                        powerMod = powerMod * 1.33
                                elif moveType == "Fairy" and shell.teamMatesDict[member]["ability"] == "Fairy Aura":
                                    if "Aura Break" in pokeAbilities:
                                        powerMod = powerMod * 0.75
                                    else:
                                        powerMod = powerMod * 1.33

                                #Member's Moves
                                for m in shell.teamMatesDict[member]["moves"]:
                                    if shell.teamMatesDict[member]["moves"][m] in ["Bulk Up","Coil","Curse","Dragon Dance","Gear Up","Growth","Hone Claws","Howl","Meditate","Power-Up Punch","Sharpen","Shift Gear","Work Up"] and "unaware" not in pokeAbilities:
                                        physAtkMod = physAtkMod * 1.5
                                    elif shell.teamMatesDict[member]["moves"][m] in ["Leer", "Tail Whip", "Tickle"]:
                                        if "Big Pecks" not in pokeAbilities and "Clear Body" not in pokeAbilities and "Full Metal Body" not in pokeAbilities and "White Smoke" not in pokeAbilities:
                                            if "Flower Veil" not in pokeAbilities:
                                                physDefMod = physDefMod * 0.66
                                            else:
                                                if "Grass" not in pokeTyping:
                                                    physDefMod = physDefMod * 0.66
                                    elif shell.teamMatesDict[member]["moves"][m] in ["Shell Smash","Swords Dance"] and "unaware" not in pokeAbilities:
                                        physAtkMod = physAtkMod * 2
                                    elif shell.teamMatesDict[member]["moves"][m] in ["Screech"]:
                                        if "Big Pecks" not in pokeAbilities and "Clear Body" not in pokeAbilities and "Full Metal Body" not in pokeAbilities and "White Smoke" not in pokeAbilities:
                                            if "Flower Veil" not in pokeAbilities:
                                                physDefMod = physDefMod * 0.5
                                            else:
                                                if "Grass" not in pokeTyping:
                                                    physDefMod = physDefMod * 0.5
                                    elif shell.teamMatesDict[member]["moves"][m] in ["Belly Drum"] and "unaware" not in pokeAbilities:
                                        physAtkMod = physAtkMod * 4
                                    elif shell.teamMatesDict[member]["moves"][m] in ["Calm Mind","Gear Up","Growth","Quiver Dance","Work Up"] and "unaware" not in pokeAbilities:
                                        specAtkMod = specAtkMod * 1.5
                                    elif shell.teamMatesDict[member]["moves"][m] in ["Geomancy","Nasty Plot","Shell Smash"] and "unaware" not in pokeAbilities:
                                        specAtkMod = specAtkMod * 2
                                    elif shell.teamMatesDict[member]["moves"][m] in ["Acid Spray","Fake Tears","Metal Sound"]:
                                        if "Clear Body" not in pokeAbilities and "Full Metal Body" not in pokeAbilities and "White Smoke" not in pokeAbilities:
                                            if "Flower Veil" not in pokeAbilities:
                                                specDefMod = specDefMod * 0.66
                                            else:
                                                if "Grass" not in pokeTyping:
                                                    specDefMod = specDefMod * 0.66
                                    elif shell.teamMatesDict[member]["moves"][m] in ["Tail Glow"] and "unaware" not in pokeAbilities:
                                        specAtkMod = specAtkMod * 2.5
                                if shell.teamMatesDict[member]["moves"][move] == "Knock Off":
                                    powerMod = powerMod * 1.5
                                elif shell.teamMatesDict[member]["moves"][move] in ["Self-Destruct","Explosion"]:
                                    if shell.teamMatesDict[member]["ability"] not in ["Mold Breaker","Teravolt","Turboblaze"] and "Damp" in pokeAbilities:
                                        modifier = 0
                                elif shell.teamMatesDict[member]["moves"][move] in ["Hyper Voice", "Perish Song", "Snore","Uproar"]:
                                    if shell.teamMatesDict[member]["ability"] not in ["Mold Breaker","Teravolt","Turboblaze"] and "Soundproof" in pokeAbilities:
                                        modifier = 0
                                elif shell.teamMatesDict[member]["moves"][move] in ["Fissure", "Guillotine", "Horn Drill","Sheer Cold"]:
                                    if shell.teamMatesDict[member]["ability"] not in ["Mold Breaker","Teravolt","Turboblaze"] and "Sturdy" in pokeAbilities:
                                        modifier = 0
                                    else:
                                        modifier = 1000000

                                #Member's Items
                                if shell.teamMatesDict[member]["item"] == "Life Orb":
                                    modifier = modifier * 1.3
                                if shell.teamMatesDict[member]["item"] == "Choice Band":
                                    physAtkMod = physAtkMod * 1.5
                                elif shell.teamMatesDict[member]["item"] == "Muscle Band":
                                    physAtkMod = physAtkMod * 1.1
                                if shell.teamMatesDict[member]["item"] == "Choice Specs":
                                    specAtkMod = specAtkMod * 1.5
                                elif shell.teamMatesDict[member]["item"] == "Wise Glasses":
                                    specAtkMod = specAtkMod * 1.1

                                if shell.teamMatesDict[member]["species"] == "Dialga" and \
                                                shell.teamMatesDict[member]["item"] == "Adamant Orb":
                                    if moveType in ["Steel", "Dragon"]:
                                        powerMod = powerMod * 1.2
                                elif shell.teamMatesDict[member]["species"] == "Palkia" and \
                                                shell.teamMatesDict[member]["item"] == "Lustrous Orb":
                                    if moveType in ["Water", "Dragon"]:
                                        powerMod = powerMod * 1.2
                                elif "Giratina" in shell.teamMatesDict[member]["species"] and \
                                                shell.teamMatesDict[member]["item"] == "Griseous Orb":
                                    if moveType in ["Ghost", "Dragon"]:
                                        powerMod = powerMod * 1.2
                                elif shell.teamMatesDict[member]["species"] in ["Latios", "Latias"] and \
                                                shell.teamMatesDict[member]["item"] == "Soul Dew":
                                    if moveType in ["Psychic", "Dragon"]:
                                        powerMod = powerMod * 1.2
                                    specAtkMod = specAtkMod * 1.5
                                elif ("Marowak" in shell.teamMatesDict[member]["species"] or "Cubone" in shell.teamMatesDict[member]["species"]) and shell.teamMatesDict[member]["item"] == "Thick Club":
                                    physAtkMod = physAtkMod * 2

                                # TODO: contact? make sure u check out protective pads

                                #Poke's Ability

                                #Poke's Moves

                                #Poke's Items
                                if "eviolite" in MetaDex.findPokemonTierItems(pokeName,shell.tierfile):
                                    physDefMod = physDefMod*1.5
                                    specDefMod = specDefMod*1.5
                                elif pokeName in ["Latios", "Latias"] and "Soul Dew" in MetaDex.findPokemonTierItems(pokeName,shell.tierfile):
                                    specDefMod = specDefMod*1.5

                                #STAB
                                if (moveType in memberTyping and shell.teamMatesDict[member]["ability"]!="Adaptability") or shell.teamMatesDict[member]["ability"]=="Protean":
                                    modifier = modifier * 1.5
                                elif moveType in memberTyping and shell.teamMatesDict[member]["ability"]=="Adaptability":
                                    modifier=modifier*2

                                # Expected value of a uniform stochast on [0.85,1]
                                modifier = modifier * 0.925

                                #Physical/Special Split and the necessary abilities/moves/items ect.
                                if moveCat == "Physical":
                                    physDamage = self.calcDamage(shell.teamMatesDict[member]["level"],
                                        Pokedex.findMoveBasePower(shell.teamMatesDict[member]["moves"][move])*powerMod,
                                        shell.atkStatCalc(shell.teamMatesDict[member]["baseStats"]["atk"],
                                            shell.teamMatesDict[member]["evs"]["atk"],
                                            shell.teamMatesDict[member]["ivs"]["atk"],
                                            shell.teamMatesDict[member]["level"],
                                            shell.teamMatesDict[member]["nature"])*physAtkMod,
                                        shell.defStatCalc(pokeBaseStats[2], 0, 31,maxlevel, "Serious")*physDefMod,
                                        modifier)/pokeHP
                                    if physDamage > maxDamage:
                                        maxDamage = physDamage
                                elif moveCat == "Special":
                                    specDamage = self.calcDamage(shell.teamMatesDict[member]["level"],
                                        Pokedex.findMoveBasePower(shell.teamMatesDict[member]["moves"][move])*powerMod,
                                        shell.spaStatCalc(shell.teamMatesDict[member]["baseStats"]["spa"],
                                            shell.teamMatesDict[member]["evs"]["spa"],
                                            shell.teamMatesDict[member]["ivs"]["spa"],
                                            shell.teamMatesDict[member]["level"],
                                            shell.teamMatesDict[member]["nature"])*specAtkMod,
                                        shell.spdStatCalc(pokeBaseStats[4], 0, 31, maxlevel, "Serious")*specDefMod,
                                        modifier)/pokeHP
                                    if specDamage > maxDamage:
                                        maxDamage = specDamage

                if maxDamage < 0.5:
                    self.counterMssngr.config(state=NORMAL)
                    if len(pokeTyping)==1:
                        self.counterMssngr.insert(END, "%s:\n  %s/%s/%s/%s/%s/%s\n  %s\n  Damage: %.2f%%\n\n" % (pokeName,pokeBaseStats[0],pokeBaseStats[1],pokeBaseStats[2],pokeBaseStats[3],pokeBaseStats[4],pokeBaseStats[5],pokeTyping[0],maxDamage * 100))
                    elif len(pokeTyping)==2:
                        self.counterMssngr.insert(END, "%s:\n  %s/%s/%s/%s/%s/%s\n  %s, %s\n  Damage: %.2f%%\n\n" % (pokeName,pokeBaseStats[0],pokeBaseStats[1],pokeBaseStats[2],pokeBaseStats[3],pokeBaseStats[4],pokeBaseStats[5],pokeTyping[0],pokeTyping[1],maxDamage * 100))
                    self.counterMssngr.config(state=DISABLED)

    def threats(self,shell):
        self.threatMssngr.config(state=NORMAL)
        self.threatMssngr.delete(1.0, END)
        for poke in MetaDex.findTierData(shell.tierfile):
            if MetaDex.findPokemonTierUsage(poke,shell.tierfile)>0.0095:
                pokeDict = Tools.buildPokemon(poke, shell.tierfile)
                pokeTyping = Pokedex.findPokemonTypes(pokeDict["species"])
                minDamage = 1000000

                psunnyday = False
                praindance = False
                psandstorm = False
                phail = False
                pelectricterrain=False
                ppsychicterrain=False
                pgrassyterrain=False
                pmistyterrain=False
                for m in pokeDict["moves"]:
                    if pokeDict["moves"][m] == "sunnyday":
                        psunnyday = True
                    elif pokeDict["moves"][m] == "raindance":
                        praindance = True
                    elif pokeDict["moves"][m] == "sandstorm":
                        psandstorm = True
                    elif pokeDict["moves"][m] == "hail":
                        phail = True
                    elif pokeDict["moves"][m] == "electricterrain":
                        pelectricterrain=True
                    elif pokeDict["moves"][m] == "psychicterrain":
                        ppsychicterrain=True
                    elif pokeDict["moves"][m] == "grassyterrain":
                        pgrassyterrain=True
                    elif pokeDict["moves"][m] == "mistyterrain":
                        pmistyterrain=True

                msunnyday = False
                mraindance = False
                msandstorm = False
                mhail = False
                melectricterrain = False
                mpsychicterrain = False
                mgrassyterrain = False
                mmistyterrain = False
                for member in shell.teamMatesDict:
                    for m in shell.teamMatesDict[member]["moves"]:
                        if shell.teamMatesDict[member]["moves"][m] == "Sunny Day":
                            msunnyday = True
                        elif shell.teamMatesDict[member]["moves"][m] == "Rain Dance":
                            mraindance = True
                        elif shell.teamMatesDict[member]["moves"][m] == "Sandstorm":
                            msandstorm = True
                        elif shell.teamMatesDict[member]["moves"][m] == "Hail":
                            mhail = True
                        elif shell.teamMatesDict[member]["moves"][m] == "electricterrain":
                            melectricterrain = True
                        elif shell.teamMatesDict[member]["moves"][m] == "psychicterrain":
                            mpsychicterrain = True
                        elif shell.teamMatesDict[member]["moves"][m] == "grassyterrain":
                            mgrassyterrain = True
                        elif shell.teamMatesDict[member]["moves"][m] == "mistyterrain":
                            mmistyterrain = True

                for member in shell.teamMatesDict:
                    maxDamage = 0
                    memberHP = shell.hpStatCalc(shell.teamMatesDict[member]["baseStats"]["hp"], shell.teamMatesDict[member]["evs"]["hp"],
                                          shell.teamMatesDict[member]["ivs"]["hp"], shell.teamMatesDict[member]["level"])
                    memberTyping = Pokedex.findPokemonTypes(shell.teamMatesDict[member]["species"])
                    if pokeDict["ability"] == "scrappy":
                        combinedWRI = self.defCombineTypes(memberTyping, True)
                    else:
                        combinedWRI = self.defCombineTypes(memberTyping, False)

                    for move in pokeDict["moves"]:
                        if pokeDict["moves"][move] != None:
                            moveData = Pokedex.findMoveData(pokeDict["moves"][move])

                            if moveData["category"] != "Status":
                                moveType = moveData["type"]
                                modifier = 1
                                powerMod = 1
                                physAtkMod = 1
                                physDefMod = 1
                                specAtkMod = 1
                                specDefMod = 1

                                #Poke's Ability
                                if pokeDict["ability"] in ["hugepower", "purepower"]:
                                    physAtkMod = physAtkMod * 2

                                #Poke's Abilities Affecting Move Typing
                                if moveType == "Normal":
                                    if pokeDict["ability"] == "aerilate":
                                        powerMod = powerMod * 1.2
                                        moveType = "Flying"
                                    elif pokeDict["ability"] == "pixilate":
                                        powerMod = powerMod * 1.2
                                        moveType = "Fairy"
                                    elif pokeDict["ability"] == "galvanize":
                                        powerMod = powerMod * 1.2
                                        moveType = "Electric"
                                    elif pokeDict["ability"] == "refrigerate":
                                        powerMod = powerMod * 1.2
                                        moveType = "Ice"
                                else:
                                    if pokeDict["ability"] == "normalize":
                                        powerMod = powerMod * 1.2
                                        moveType = "Normal"

                                #Poke's Items Modifying Types
                                if pokeDict["item"] in ["silkscarf"]:
                                    if moveType == "Normal":
                                        powerMod = powerMod * 1.2
                                elif pokeDict["item"] in ["flameplate", "charcoal"]:
                                    if "Arceus" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "judgement":
                                            if pokeDict["item"] == "flameplate":
                                                moveType = "Fire"
                                    if moveType == "Fire":
                                        powerMod = powerMod * 1.2
                                elif pokeDict["item"] in ["splashplate", "mysticwater", "seaincense", "waveincense"]:
                                    if "Arceus" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "judgement":
                                            if pokeDict["item"] == "splashplate":
                                                moveType = "Water"
                                    if moveType == "Water":
                                        powerMod = powerMod * 1.2
                                elif pokeDict["item"] in ["zapplate", "magnet"]:
                                    if "Arceus" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "judgement":
                                            if pokeDict["item"] == "zapplate":
                                                moveType = "Electric"
                                    if moveType == "Electric":
                                        powerMod = powerMod * 1.2
                                elif pokeDict["item"] in ["meadowplate", "miracleseed", "roseincense"]:
                                    if "Arceus" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "judgement":
                                            if pokeDict["item"] == "meadowplate":
                                                moveType = "Grass"
                                    if moveType == "Graass":
                                        powerMod = powerMod * 1.2
                                elif pokeDict["item"] in ["icicleplate", "nevermeltice"]:
                                    if "Arceus" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "judgement":
                                            if pokeDict["item"] == "icicleplate":
                                                moveType = "Ice"
                                    if moveType == "Ice":
                                        powerMod = powerMod * 1.2
                                elif pokeDict["item"] in ["fistplate", "blackbelt"]:
                                    if "Arceus" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "judgement":
                                            if pokeDict["item"] == "fistplate":
                                                moveType = "Fighting"
                                    if moveType == "Fighting":
                                        powerMod = powerMod * 1.2
                                elif pokeDict["item"] in ["toxicplate", "poisonbarb"]:
                                    if "Arceus" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "judgement":
                                            if pokeDict["item"] == "toxicplate":
                                                moveType = "Poison"
                                    if moveType == "Poison":
                                        powerMod = powerMod * 1.2
                                elif pokeDict["item"] in ["earthplate", "softsand"]:
                                    if "Arceus" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "judgement":
                                            if pokeDict["item"] == "earthplate":
                                                moveType = "Ground"
                                    if moveType == "Ground":
                                        powerMod = powerMod * 1.2
                                elif pokeDict["item"] in ["skyplate", "sharpbeak"]:
                                    if "Arceus" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "judgement":
                                            if pokeDict["item"] == "splashplate":
                                                moveType = "Water"
                                    if moveType == "Flying":
                                        powerMod = powerMod * 1.2
                                elif pokeDict["item"] in ["mindplate", "twistedspoon", "oddincense"]:
                                    if "Arceus" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "judgement":
                                            if pokeDict["item"] == "mindplate":
                                                moveType = "Psychic"
                                    if moveType == "Psychic":
                                        powerMod = powerMod * 1.2
                                elif pokeDict["item"] in ["insectplate", "silverpowder"]:
                                    if "Arceus" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "judgement":
                                            if pokeDict["item"] == "insectplate":
                                                moveType = "Bug"
                                    if moveType == "Bug":
                                        powerMod = powerMod * 1.2
                                elif pokeDict["item"] in ["stoneplate", "hardstone", "rockincense"]:
                                    if "Arceus" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "judgement":
                                            if pokeDict["item"] == "stoneplate":
                                                moveType = "Rock"
                                    if moveType == "Rock":
                                        powerMod = powerMod * 1.2
                                elif pokeDict["item"] in ["spookyplate", "spelltag"]:
                                    if "Arceus" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "judgement":
                                            if pokeDict["item"] == "spookyplate":
                                                moveType = "Ghost"
                                    if moveType == "Ghost":
                                        powerMod = powerMod * 1.2
                                elif pokeDict["item"] in ["dracoplate", "dragonfang"]:
                                    if "Arceus" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "judgement":
                                            if pokeDict["item"] == "dracoplate":
                                                moveType = "Dragon"
                                    if moveType == "Dragon":
                                        powerMod = powerMod * 1.2
                                elif pokeDict["item"] in ["dreadplate", "blackglasses"]:
                                    if "Arceus" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "judgement":
                                            if pokeDict["item"] == "dreadplate":
                                                moveType = "Dark"
                                    if moveType == "Dark":
                                        powerMod = powerMod * 1.2
                                elif pokeDict["item"] in ["ironplate", "metalcoat"]:
                                    if "Arceus" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "judgement":
                                            if pokeDict["item"] == "ironplate":
                                                moveType = "Steel"
                                    if moveType == "Steel":
                                        powerMod = powerMod * 1.2
                                elif pokeDict["item"] in ["pixieplate"]:
                                    if "Arceus" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "judgement":
                                            if pokeDict["item"] == "pixieplate":
                                                moveType = "Fairy"
                                    if moveType == "Fairy":
                                        powerMod = powerMod * 1.2

                                if pokeDict["item"] == "firememory":
                                    if "Silvally" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "multiattack":
                                            moveType = "Fire"
                                elif pokeDict["item"] == "watermemory":
                                    if "Silvally" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "multiattack":
                                            moveType = "Water"
                                elif pokeDict["item"] == "electricmemory":
                                    if "Silvally" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "multiattack":
                                            moveType = "Electric"
                                elif pokeDict["item"] == "grassmemory":
                                    if "Silvally" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "multiattack":
                                            moveType = "Grass"
                                elif pokeDict["item"] == "icememory":
                                    if "Silvally" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "multiattack":
                                            moveType = "Ice"
                                elif pokeDict["item"] == "fightingmemory":
                                    if "Silvally" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "multiattack":
                                            moveType = "Fighting"
                                elif pokeDict["item"] == "toxicmemory":
                                    if "Silvally" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "multiattack":
                                            moveType = "Toxic"
                                elif pokeDict["item"] == "groundmemory":
                                    if "Silvally" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "multiattack":
                                            moveType = "Ground"
                                elif pokeDict["item"] == "flyingmemory":
                                    if "Silvally" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "multiattack":
                                            moveType = "Flying"
                                elif pokeDict["item"] == "psychicmemory":
                                    if "Silvally" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "multiattack":
                                            moveType = "Psychic"
                                elif pokeDict["item"] == "bugmemory":
                                    if "Silvally" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "multiattack":
                                            moveType = "Bug"
                                elif pokeDict["item"] == "rockmemory":
                                    if "Silvally" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "multiattack":
                                            moveType = "Rock"
                                elif pokeDict["item"] == "ghostmemory":
                                    if "Silvally" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "multiattack":
                                            moveType = "Ghost"
                                elif pokeDict["item"] == "dragonmemory":
                                    if "Silvally" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "multiattack":
                                            moveType = "Dragon"
                                elif pokeDict["item"] == "darkmemory":
                                    if "Silvally" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "multiattack":
                                            moveType = "Dark"
                                elif pokeDict["item"] == "steelmemory":
                                    if "Silvally" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "multiattack":
                                            moveType = "Steel"
                                elif pokeDict["item"] == "fairymemory":
                                    if "Silvally" in pokeDict["species"]:
                                        if pokeDict["moves"][move] == "multiattack":
                                            moveType = "Fairy"

                                #Effectiveness
                                if len(combinedWRI) == 3:
                                    if moveType in combinedWRI[0]:
                                        modifier = modifier * 2
                                        if shell.teamMatesDict[member]["ability"] in ["Solid Rock", "Filter"] and pokeDict["ability"] not in ["moldbreaker","teravolt","turboblaze"]:
                                            modifier=modifier*0.75
                                    elif moveType in combinedWRI[1]:
                                        modifier = modifier * 0.5
                                    elif moveType in combinedWRI[2]:
                                        modifier = 0
                                    if pokeDict["ability"] not in ["moldbreaker","teravolt","turboblaze"] and shell.teamMatesDict[member][
                                        "ability"] == "Wonder Guard" and moveType not in combinedWRI[0]:
                                        modifier = 0
                                elif len(combinedWRI) == 5:
                                    if moveType in combinedWRI[0]:
                                        modifier = modifier * 4
                                        if shell.teamMatesDict[member]["ability"] in ["Solid Rock", "Filter"] and pokeDict["ability"] not in ["moldbreaker","teravolt","turboblaze"]:
                                            modifier = modifier * 0.75
                                    elif moveType in combinedWRI[1]:
                                        modifier = modifier * 2
                                        if shell.teamMatesDict[member]["ability"] in ["Solid Rock", "Filter"] and pokeDict["ability"] not in ["moldbreaker","teravolt","turboblaze"]:
                                            modifier = modifier * 0.75
                                    elif moveType in combinedWRI[2]:
                                        modifier = modifier * 0.5
                                    elif moveType in combinedWRI[3]:
                                        modifier = modifier * 0.25
                                    elif moveType in combinedWRI[4]:
                                        modifier = 0
                                    if shell.teamMatesDict[member]["ability"] == "Wonder Guard" and moveType not in combinedWRI[0] and moveType not in combinedWRI[1]:
                                        modifier = 0
                                else:
                                    print("Oops, something went wrong here.")

                                #Poke's Weather
                                if pokeDict["ability"]=="drought" or psunnyday:
                                    if moveType == "Fire":
                                        modifier = modifier * 1.5
                                    elif moveType == "Water":
                                        modifier = modifier * 0.5
                                elif pokeDict["ability"]=="desolateland":
                                    if moveType == "Fire":
                                        modifier = modifier * 1.5
                                    elif moveType == "Water":
                                        modifier = 0
                                elif pokeDict["ability"] =="drizzle" or praindance:
                                    if moveType == "Water":
                                        modifier = modifier * 1.5
                                    elif moveType == "Fire":
                                        modifier = modifier * 0.5
                                elif pokeDict["ability"]=="primordialsea":
                                    if moveType == "Water":
                                        modifier = modifier * 1.5
                                    elif moveType == "Fire":
                                        modifier = 0
                                elif pokeDict["ability"]=="sandstream" or psandstorm:
                                    if pokeDict["ability"] == "sandforce":
                                        if moveType in ["Steel","Ground","Rock"]:
                                            powerMod=powerMod*1.33
                                elif pokeDict["ability"]=="snowwarning" or phail:
                                    pass

                                #Poke's Terrains
                                if pokeDict["ability"] == "electricsurge" or pelectricterrain:
                                    if moveType == "Electric":
                                        if "Flying" not in pokeTyping and pokeDict["ability"] != "levitate":
                                            powerMod = powerMod * 1.5
                                elif pokeDict["ability"] == "psychicsurge" or ppsychicterrain:
                                    if moveType == "Psychic":
                                        if "Flying" not in pokeTyping and pokeDict["ability"] != "levitate":
                                            powerMod = powerMod * 1.5
                                elif pokeDict["ability"] == "grassysurge" or pgrassyterrain:
                                    if moveType == "Grass":
                                        if "Flying" not in pokeTyping and pokeDict["ability"] != "levitate":
                                            powerMod = powerMod * 1.5
                                    elif pokeDict["moves"][move] in ["earthquake","bulldoze","magnitude"]:
                                        powerMod = powerMod * 0.5
                                elif pokeDict["ability"] == "mistysurge" or pmistyterrain:
                                    if moveType == "Dragon":
                                        if "Flying" not in pokeTyping and shell.pokeDict["ability"] != "levitate":
                                            if "Flying" not in memberTyping and shell.teamMatesDict[member]["ability"]!="Levitate":
                                                powerMod = powerMod * 0.5

                                #Member's Weather
                                if (shell.teamMatesDict[member]["ability"] in ["Drought"] or msunnyday) and pokeDict["ability"] not in ["drought","desolateland"] and not psunnyday:
                                    if moveType == "Fire":
                                        modifier = modifier * 1.5
                                    elif moveType == "Water":
                                        modifier = modifier * 0.5
                                elif shell.teamMatesDict[member]["ability"] in ["Desolate Land"] and pokeDict["ability"] not in ["drought","desolateland"] and not psunnyday:
                                    if moveType == "Fire":
                                        modifier = modifier * 1.5
                                    elif moveType == "Water":
                                        modifier = 0
                                elif (shell.teamMatesDict[member]["ability"] in ["Drizzle"] or mraindance) and pokeDict["ability"] not in ["drizzle","primordialsea"] and not praindance:
                                    if moveType == "Water":
                                        modifier = modifier * 1.5
                                    elif moveType == "Fire":
                                        modifier = modifier * 0.5
                                elif shell.teamMatesDict[member]["ability"] in ["Primordial Sea"] and pokeDict["ability"] not in ["drizzle","primordialsea"] and not praindance:
                                    if moveType == "Water":
                                        modifier = modifier * 1.5
                                    elif moveType == "Fire":
                                        modifier = 0
                                elif shell.teamMatesDict[member]["ability"] in ["Sand Stream"] or msandstorm:
                                    if "Rock" in memberTyping:
                                        if moveData["category"] == "Special":
                                            specDefMod = specDefMod*1.5
                                elif shell.teamMatesDict[member]["ability"] in ["Snow Warning"] or mhail:
                                    pass
                                elif shell.teamMatesDict[member]["ability"]=="Delta Stream":
                                    if "Flying" in memberTyping:
                                        if moveType in ["Electric", "Rock", "Ice"]:
                                            modifier = modifier * 0.5

                                #Member's Terrain
                                if (shell.teamMatesDict[member]["ability"] == "Electric Surge" or melectricterrain) and not (pokeDict["ability"] == "electricsurge" or pelectricterrain):
                                    if moveType == "Electric":
                                        if "Flying" not in pokeTyping and pokeDict["ability"] != "Levitate":
                                            powerMod = powerMod * 1.5
                                elif (shell.teamMatesDict[member]["ability"] == "Psychic Surge" or mpsychicterrain) and not (pokeDict["ability"] == "psychicsurge" or ppsychicterrain):
                                    if moveType == "Psychic":
                                        if "Flying" not in pokeTyping and pokeDict["ability"] != "Levitate":
                                            powerMod = powerMod * 1.5
                                elif (shell.teamMatesDict[member]["ability"] == "Grassy Surge" or mgrassyterrain) and not (pokeDict["ability"] == "grassysurge" or pgrassyterrain):
                                    if moveType == "Grass":
                                        if "Flying" not in pokeTyping and pokeDict["ability"] != "Levitate":
                                            powerMod = powerMod * 1.5
                                    elif pokeDict["moves"][move] in ["Earthquake", "Bulldoze","Magnitude"]:
                                        powerMod = powerMod * 0.5
                                elif (shell.teamMatesDict[member]["ability"] == "Misty Surge" or mmistyterrain) and not (pokeDict["ability"] == "mistysurge" or pmistyterrain):
                                    if moveType == "Dragon":
                                        if "Flying" not in pokeTyping and pokeDict["ability"] != "levitate":
                                            if "Flying" not in memberTyping and shell.teamMatesDict[member]["ability"]!="Levitate":
                                                powerMod = powerMod * 0.5

                                if moveType == "Fire":
                                    if shell.teamMatesDict[member]["ability"] == "Flash Fire" and pokeDict["ability"] not in ["Mold Breaker","Teravolt","Turboblaze"]:
                                        modifier = 0
                                    elif shell.teamMatesDict[member]["ability"] in ["Thick Fat","Water Bubble"] and pokeDict["ability"] not in ["Mold Breaker","Teravolt","Turboblaze"]:
                                        modifier = modifier * 0.5
                                    elif shell.teamMatesDict[member]["ability"] == "Dry Skin":
                                        modifier = modifier * 1.25
                                    elif shell.teamMatesDict[member]["ability"] == "Fluffy":
                                        modifier = modifier * 2
                                elif moveType == "Water":
                                    if shell.teamMatesDict[member]["ability"] in ["Storm Drain","Water Absorb","Dry Skin"] and pokeDict["ability"] not in ["moldbreaker","teravolt","turboblaze"]:
                                        modifier = 0
                                    if pokeDict["ability"] == "waterbubble":
                                        powerMod = powerMod * 2
                                elif moveType == "Electric" and shell.teamMatesDict[member]["ability"] in ["Lightning Rod","Volt Absorb","Motor Drive"] and pokeDict["ability"] not in ["moldbreaker","teravolt","turboblaze"]:
                                    modifier = 0
                                elif moveType == "Grass" and shell.teamMatesDict[member]["ability"] == "Sap Sipper" and pokeDict["ability"] not in ["moldbreaker","teravolt","turboblaze"]:
                                    modifier = 0
                                elif moveType == "Ice" and shell.teamMatesDict[member]["ability"] == "Thick Fat" and pokeDict["ability"] not in ["moldbreaker","teravolt","turboblaze"]:
                                    modifier = modifier * 0.5
                                elif moveType == "Ground" and shell.teamMatesDict[member]["ability"] == "Levitate" and pokeDict["ability"] not in ["moldbreaker","teravolt","turboblaze"]:
                                    modifier = 0
                                elif moveType == "Dark" and pokeDict["ability"] == "darkaura":
                                    if shell.teamMatesDict[member]["ability"] == "Aura Break":
                                        powerMod = 0.75 * powerMod
                                    else:
                                        powerMod = 1.33 * powerMod
                                elif moveType == "Fairy" and pokeDict["ability"] == "fairyaura":
                                    if shell.teamMatesDict[member]["ability"] == "Aura Break":
                                        powerMod = 0.75 * powerMod
                                    else:
                                        powerMod = 1.33 * powerMod

                                #Poke's Moves
                                for m in pokeDict["moves"]:
                                    if pokeDict["moves"][m] in ["bulkup", "coil", "curse", "dragondance","gearup", "growth", "honeclaws", "howl","meditate", "poweruppunch", "sharpen","shiftgear", "workup"] and shell.teamMatesDict[member]["ability"] != "Unaware":
                                        physAtkMod = physAtkMod * 1.5
                                    elif pokeDict["moves"][m] in ["leer", "tailwhip", "tickle"]:
                                        if shell.teamMatesDict[member]["ability"] not in ["Big Pecks","Clear Body","Full Metal Body","White Smoke"]:
                                            if shell.teamMatesDict[member]["ability"] != "Flower Veil":
                                                physDefMod = physDefMod * 0.66
                                            else:
                                                if "Grass" not in pokeTyping:
                                                    physDefMod = physDefMod * 0.66
                                    elif pokeDict["moves"][m] in ["shellsmash", "swordsdance"] and shell.teamMatesDict[member]["ability"] != "Unaware":
                                        physAtkMod = physAtkMod * 2
                                    elif pokeDict["moves"][m] in ["screech"] and shell.teamMatesDict[member]["ability"] != "Unaware":
                                        if shell.teamMatesDict[member]["ability"] not in ["Big Pecks","Clear Body","Full Metal Body","White Smoke"]:
                                            if shell.teamMatesDict[member]["ability"] != "Flower Veil":
                                                physDefMod = physDefMod * 0.5
                                            else:
                                                if "Grass" not in pokeTyping:
                                                    physDefMod = physDefMod * 0.5
                                    elif pokeDict["moves"][m] in ["bellydrum"] and shell.teamMatesDict[member]["ability"] != "Unaware":
                                        physAtkMod = physAtkMod * 4
                                    elif pokeDict["moves"][m] in ["calmmind","gearup","growth","quiverdance","workup"] and shell.teamMatesDict[member]["ability"]!="Unaware":
                                        specAtkMod = specAtkMod * 1.5
                                    elif pokeDict["moves"][m] in ["geomancy", "nastyplot","shellsmash"] and shell.teamMatesDict[member]["ability"]!="Unaware":
                                        specAtkMod = specAtkMod * 2
                                    elif pokeDict["moves"][m] in ["acidspray","faketears","metalsound"]:
                                        if shell.teamMatesDict[member]["ability"] not in ["Clear Body","Full Metal Body","White Smoke"]:
                                            if shell.teamMatesDict[member]["ability"]!="Flower Veil":
                                                specDefMod=specDefMod*0.5
                                            else:
                                                if "Grass" not in memberTyping:
                                                    specDefMod=specDefMod*0.5
                                    elif pokeDict["moves"][m] in ["tailglow"] and shell.teamMatesDict[member]["ability"]!="Unaware":
                                        specAtkMod = specAtkMod * 2.5
                                if pokeDict["moves"][move] == "knockoff":
                                    if shell.teamMatesDict[member]["item"] != None:
                                        powerMod = powerMod * 1.5
                                elif pokeDict["moves"][move] in ["selfdestruct", "explosion"]:
                                    if pokeDict["ability"] not in ["moldbreaker","teravolt","turboblaze"] and shell.teamMatesDict[member]["ability"] == "Damp":
                                        modifier = 0
                                elif pokeDict["moves"][move] in ["hypervoice", "perishsong", "snore", "uproar"]:
                                    if pokeDict["ability"] not in ["moldbreaker","teravolt","turboblaze"] and shell.teamMatesDict[member]["ability"] == "Soundproof":
                                        modifier = 0
                                elif pokeDict["moves"][move] in ["fissure", "guillotine", "horndrill", "sheercold"]:
                                    if shell.teamMatesDict[member]["ability"] == "Sturdy" and pokeDict["ability"] not in ["moldbreaker","teravolt","turboblaze"]:
                                        modifier = 0
                                    else:
                                        modifier = 1000000

                                #Poke's Items
                                if pokeDict["item"] == "choiceband":
                                    physAtkMod = physAtkMod * 1.5
                                elif pokeDict["item"] == "muscleband":
                                    physAtkMod = physAtkMod * 1.1
                                elif pokeDict["item"] == "choicespecs":
                                    specAtkMod=specAtkMod*1.5
                                elif pokeDict["item"] == "wiseglasses":
                                    specAtkMod = specAtkMod * 1.1

                                if pokeDict["item"] == "lifeorb":
                                    modifier=modifier*1.3
                                if pokeDict["species"] == "Dialga" and pokeDict["item"] == "adamantorb":
                                    if moveType in ["Steel", "Dragon"]:
                                        powerMod = powerMod * 1.2
                                elif pokeDict["species"] == "Palkia" and pokeDict["item"] == "lustrousorb":
                                    if moveType in ["Water", "Dragon"]:
                                        powerMod = powerMod * 1.2
                                elif "Giratina" in pokeDict["species"] and pokeDict["item"] == "griseousorb":
                                    if moveType in ["Ghost", "Dragon"]:
                                        powerMod = powerMod * 1.2
                                elif pokeDict["species"] in ["Latios", "Latias"] and pokeDict["item"] == "souldew":
                                    if moveType in ["Psychic", "Dragon"]:
                                        powerMod = powerMod * 1.2
                                    specAtkMod=specAtkMod*1.5
                                elif ("Marowak" in pokeDict["species"] or "Cubone" in pokeDict["species"]) and pokeDict["item"] == "thickclub":
                                    physAtkMod=physAtkMod*2

                                # TODO: contact? make sure u check out protective pads

                                #Member's Abilities
                                if shell.teamMatesDict[member]["ability"] in ["Stamina", "Intimidate"]:
                                    physDefMod = physDefMod*1.5

                                #Member's Moves
                                for m in shell.teamMatesDict[member]["moves"]:
                                    if shell.teamMatesDict[member]["moves"][m] in ["Bulk Up", "Coil",
                                                                                   "Cosmic Power", "Curse",
                                                                                   "Defend Order",
                                                                                   "Defense Curl", "Harden",
                                                                                   "Skull Bash", "Withdraw",
                                                                                   "Stockpile"] and pokeDict["ability"] != "unaware":
                                        physDefMod = physDefMod*1.5
                                    elif shell.teamMatesDict[member]["moves"][m] in ["Baby-Doll Eyes", "Growl",
                                                                                     "Lunge", "Noble Roar",
                                                                                     "Parting Shot",
                                                                                     "Play Nice",
                                                                                     "Strength Sap",
                                                                                     "Tearful Look", "Tickle",
                                                                                     "Trop Kick"]:
                                        if pokeDict["ability"] not in ["hypercutter","clearbody","fullmetalbody","whitesmoke"]:
                                            if pokeDict["ability"] != "flowerveil":
                                                physAtkMod = physAtkMod*0.66
                                            else:
                                                if "Grass" not in pokeTyping:
                                                    physAtkMod = physAtkMod * 0.66
                                    elif shell.teamMatesDict[member]["moves"][m] in ["Acid Armor",
                                                                                     "Aurora Veil", "Barrier",
                                                                                     "Iron Defense",
                                                                                     "Reflect"] and pokeDict["ability"] != "unaware":
                                        physDefMod = physDefMod * 2
                                    elif shell.teamMatesDict[member]["moves"][m] in ["Charm", "Feather Dance"]:
                                        if pokeDict["ability"] not in ["hypercutter","clearbody","fullmetalbody","whitesmoke"]:
                                            if pokeDict["ability"] != "flowerveil":
                                                physAtkMod = physAtkMod*0.5
                                            else:
                                                if "Grass" not in pokeTyping:
                                                    physAtkMod = physAtkMod * 0.5
                                    elif shell.teamMatesDict[member]["moves"][m] in ["Cotton Guard"] and pokeDict["ability"] != "unaware":
                                        physDefMod = physDefMod * 2.5
                                    elif shell.teamMatesDict[member]["moves"][m] in ["Aromatic Mist","Calm Mind","Cosmic Power","Defend Order","Quiver Dance","Stockpile"] and pokeDict["ability"]!="unaware":
                                        specDefMod=specDefMod*1.5
                                    elif shell.teamMatesDict[member]["moves"][m] in ["Confide","Noble Roar","Parting Shot","Snarl","Struggle Bug","Tearful Look"]:
                                        if pokeDict["ability"] not in ["clearbody","fullmetalbody","whitesmoke"]:
                                            if pokeDict["ability"] != "flowerveil":
                                                specAtkMod = specAtkMod*0.66
                                            else:
                                                if "Grass" not in pokeTyping:
                                                    specAtkMod = specAtkMod * 0.66
                                    elif shell.teamMatesDict[member]["moves"][m] in ["Amnesia","Geomancy","Light Screen","Aurora Veil"] and pokeDict["ability"]!="unaware":
                                        specDefMod=specDefMod*2
                                    elif shell.teamMatesDict[member]["moves"][m] in ["Eerie Impulse"]:
                                        if pokeDict["ability"] not in ["clearbody","fullmetalbody","whitesmoke"]:
                                            if pokeDict["ability"] != "flowerveil":
                                                specAtkMod = specAtkMod*0.5
                                            else:
                                                if "Grass" not in pokeTyping:
                                                    specAtkMod = specAtkMod * 0.5

                                #Member's Items
                                if shell.teamMatesDict[member]["item"] == "Eviolite":
                                    if Pokedex.findPokemonEvos(shell.teamMatesDict[member]["species"]) != None:
                                        physDefMod = physDefMod*1.5
                                        specDefMod = specDefMod * 1.5
                                elif shell.teamMatesDict[member]["item"] == "Assault Vest":
                                    specDefMod = specDefMod * 1.5
                                elif shell.teamMatesDict[member]["item"] == "Soul Dew":
                                    if shell.teamMatesDict[member]["species"] in ["Latios", "Latias"]:
                                            specDefMod = specDefMod*1.5

                                # STAB
                                if (moveType in pokeTyping and pokeDict["ability"] != "adaptability") or pokeDict["ability"] == "protean":
                                    modifier = modifier * 1.5
                                elif moveType in pokeTyping or pokeDict["ability"] == "adaptability":
                                    modifier = modifier * 2

                                # Expected value of a uniform stochast on [0.85,1]
                                modifier = modifier * 0.925

                                #Physical/Special Split with needed abilities/items/moves ect.
                                if moveData["category"] == "Physical":
                                    physDamage = self.calcDamage(pokeDict["level"], moveData["basePower"]*powerMod,
                                        shell.atkStatCalc(pokeDict["baseStats"]["atk"], pokeDict["evs"]["atk"],
                                                    pokeDict["ivs"]["atk"], pokeDict["level"],
                                                    pokeDict["nature"])*physAtkMod,
                                        shell.defStatCalc(shell.teamMatesDict[member]["baseStats"]["def"],
                                                    shell.teamMatesDict[member]["evs"]["def"],
                                                    shell.teamMatesDict[member]["ivs"]["def"],
                                                    shell.teamMatesDict[member]["level"],
                                                    shell.teamMatesDict[member]["nature"])*physDefMod,
                                        modifier) / memberHP
                                    if maxDamage < physDamage:
                                        maxDamage = physDamage
                                elif moveData["category"] == "Special":
                                    specDamage = self.calcDamage(pokeDict["level"], moveData["basePower"]*powerMod,
                                        shell.spaStatCalc(pokeDict["baseStats"]["spa"], pokeDict["evs"]["spa"],
                                                    pokeDict["ivs"]["spa"], pokeDict["level"],
                                                    pokeDict["nature"])*specAtkMod,
                                        shell.spdStatCalc(shell.teamMatesDict[member]["baseStats"]["spd"],
                                                    shell.teamMatesDict[member]["evs"]["spd"],
                                                    shell.teamMatesDict[member]["ivs"]["spd"],
                                                    shell.teamMatesDict[member]["level"],
                                                    shell.teamMatesDict[member]["nature"])*specDefMod,
                                        modifier) / memberHP
                                    if maxDamage < specDamage:
                                        maxDamage = specDamage

                    if maxDamage < minDamage:
                        minDamage = maxDamage
                if minDamage != 1000000 and minDamage > 0.5:
                    self.threatMssngr.config(state=NORMAL)
                    if len(pokeTyping) == 1:
                        self.threatMssngr.insert(END,"%s:\n  %s/%s/%s/%s/%s/%s\n  %s\n  Ability: %s\n  Item: %s\n  Nature: %s\n  Spread: %s/%s/%s/%s/%s/%s\n  Moveset:\n    %s\n    %s\n    %s\n    %s\n  Min Damage: %.2f%%\n\n" % (
                             pokeDict["species"], pokeDict["baseStats"]["hp"],
                             pokeDict["baseStats"]["atk"], pokeDict["baseStats"]["def"],
                             pokeDict["baseStats"]["spa"], pokeDict["baseStats"]["spd"],
                             pokeDict["baseStats"]["spe"], pokeTyping[0], pokeDict["ability"],
                             pokeDict["item"], pokeDict["nature"], pokeDict["evs"]["hp"],
                             pokeDict["evs"]["atk"], pokeDict["evs"]["def"], pokeDict["evs"]["spa"],
                             pokeDict["evs"]["spd"], pokeDict["evs"]["spe"],
                             pokeDict["moves"]["move1"], pokeDict["moves"]["move2"],
                             pokeDict["moves"]["move3"], pokeDict["moves"]["move4"],
                             minDamage * 100))
                    elif len(pokeTyping) == 2:
                        self.threatMssngr.insert(END,"%s:\n  %s/%s/%s/%s/%s/%s\n  %s, %s\n  Ability: %s\n  Item: %s\n  Nature: %s\n  Spread: %s/%s/%s/%s/%s/%s\n  Moveset:\n    %s\n    %s\n    %s\n    %s\n  Min Damage: %.2f%%\n\n" % (
                             pokeDict["species"], pokeDict["baseStats"]["hp"],
                             pokeDict["baseStats"]["atk"], pokeDict["baseStats"]["def"],
                             pokeDict["baseStats"]["spa"], pokeDict["baseStats"]["spd"],
                             pokeDict["baseStats"]["spe"], pokeTyping[0], pokeTyping[1], pokeDict["ability"],
                             pokeDict["item"], pokeDict["nature"], pokeDict["evs"]["hp"],
                             pokeDict["evs"]["atk"], pokeDict["evs"]["def"], pokeDict["evs"]["spa"],
                             pokeDict["evs"]["spd"], pokeDict["evs"]["spe"],
                             pokeDict["moves"]["move1"], pokeDict["moves"]["move2"],
                             pokeDict["moves"]["move3"], pokeDict["moves"]["move4"],
                             minDamage * 100))
                    self.threatMssngr.config(state=DISABLED)

    def offTypeColor(self,typeArray,total,zeroDef,halfDef,twoDef):
        score = typeArray[0]+(total-typeArray[0]-typeArray[1]-typeArray[2])/2-typeArray[1]-2*typeArray[2]
        if score<=-2.0:
            if typeArray[2] != 0:
                zeroDef.config(bg="orange red")
            if typeArray[1] != 0:
                halfDef.config(bg="orange red")
            if typeArray[0] != 0:
                twoDef.config(bg="green yellow")
        elif -1.0<=score<=1.0:
            if typeArray[2] != 0:
                zeroDef.config(bg="sienna1")
            if typeArray[1] != 0:
                halfDef.config(bg="sienna1")
            if typeArray[0] != 0:
                twoDef.config(bg="green yellow")
        else:
            if typeArray[2] != 0:
                zeroDef.config(bg="sienna1")
            if typeArray[1] != 0:
                halfDef.config(bg="sienna1")
            if typeArray[0] != 0:
                twoDef.config(bg="green2")

        if typeArray[2]==0:
            zeroDef.config(bg="gray95")
        if typeArray[1]==0:
            halfDef.config(bg="gray95")
        if typeArray[0]==0:
            twoDef.config(bg="gray95")

    def defTypeColor(self,typeArray,zeroDef,quarterDef,halfDef,twoDef,fourDef):
        score = 2*typeArray[4]+2*typeArray[3]+typeArray[2]-typeArray[1]-2*typeArray[0]
        if score>=2:
            if typeArray[4] != 0:
                zeroDef.config(bg="green2")
            if typeArray[3] != 0:
                quarterDef.config(bg="green2")
            if typeArray[2] != 0:
                halfDef.config(bg="green2")
            if typeArray[1] != 0:
                twoDef.config(bg="sienna1")
            if typeArray[0] != 0:
                fourDef.config(bg="sienna1")
        elif 0<=score<=1:
            if typeArray[4] != 0:
                zeroDef.config(bg="green yellow")
            if typeArray[3] != 0:
                quarterDef.config(bg="green yellow")
            if typeArray[2] != 0:
                halfDef.config(bg="green yellow")
            if typeArray[1] != 0:
                twoDef.config(bg="sienna1")
            if typeArray[0] != 0:
                fourDef.config(bg="sienna1")
        else:
            if typeArray[4] != 0:
                zeroDef.config(bg="green yellow")
            if typeArray[3] != 0:
                quarterDef.config(bg="green yellow")
            if typeArray[2] != 0:
                halfDef.config(bg="green yellow")
            if typeArray[1] != 0:
                twoDef.config(bg="orange red")
            if typeArray[0] != 0:
                fourDef.config(bg="orange red")

        if typeArray[4]==0:
            zeroDef.config(bg="gray95")
        if typeArray[3]==0:
            quarterDef.config(bg="gray95")
        if typeArray[2]==0:
            halfDef.config(bg="gray95")
        if typeArray[1]==0:
            twoDef.config(bg="gray95")
        if typeArray[0]==0:
            fourDef.config(bg="gray95")

    def statColor(self,stat,hpStat):
        if hpStat:
            if 0<stat<=19:
                return "orange red"
            elif stat<=38:
                return "orange"
            elif stat<=56:
                return "yellow"
            elif stat<=75:
                return "lawn green"
            elif stat<=150:
                return "cornflower blue"
        else:
            if 0<stat<=15:
                return "orange red"
            elif stat<=30:
                return "orange"
            elif stat<=45:
                return "yellow"
            elif stat<=60:
                return "lawn green"
            elif stat<=150:
                return "cornflower blue"

    def respond(self,text):
        self.adviceMssngr.config(state=NORMAL)
        self.adviceMssngr.insert(END,"%s\n\n" % text)
        self.adviceMssngr.see(END)
        self.adviceMssngr.config(state=DISABLED)

    def resistancesText(self,type,teamTwoWeaknessesArray,teamWeaknessesArray):
        text=""
        res = Pokedex.findTypeData(type)["resistances"]
        im = Pokedex.findTypeData(type)["immunities"]
        for i in teamTwoWeaknessesArray:
            if i in res or i in im:
                if text=="":
                    text+=i
                else:
                    text+=", "+i
        for i in teamWeaknessesArray:
            if i in res or i in im:
                if text=="":
                    text+=i
                else:
                    text+=", "+i
        return "(Covers "+text+")"

    def superEffectiveText(self,type,teamTwoNVEArray,teamNVEArray):
        text = ""
        se = Pokedex.findTypeData(type)["superEffective"]
        for i in teamTwoNVEArray:
            if i in se:
                if text == "":
                    text += i
                else:
                    text += ", " + i
        for i in teamNVEArray:
            if i in se:
                if text == "":
                    text += i
                else:
                    text += ", " + i
        return "(Covers " + text + ")"

    def defTypeCoverage(self,shell):
        defTypeArrays = [self.normalDefArray, self.fireDefArray, self.waterDefArray, self.electricDefArray,
                         self.grassDefArray, self.iceDefArray, self.fightingDefArray, self.poisonDefArray,
                         self.groundDefArray, self.flyingDefArray, self.psychicDefArray, self.bugDefArray,
                         self.rockDefArray, self.ghostDefArray, self.dragonDefArray, self.darkDefArray,
                         self.steelDefArray, self.fairyDefArray]
        typeStrings = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground", "Flying",
                       "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
        teamWeaknessesArray = []
        teamTwoWeaknessesArray = []
        for i in range(len(defTypeArrays)):
            score = 2 * defTypeArrays[i][4] + 2 * defTypeArrays[i][3] + defTypeArrays[i][2] - defTypeArrays[i][1] - 2 * \
                                                                                                                    defTypeArrays[
                                                                                                                        i][
                                                                                                                        0]
            if score <= -2:
                teamTwoWeaknessesArray.append(typeStrings[i])
            elif score == -1:
                teamWeaknessesArray.append(typeStrings[i])

        bestTypes = []
        for type in typeStrings:
            weak=Pokedex.findTypeData(type)["weaknesses"]
            res = Pokedex.findTypeData(type)["resistances"]
            im = Pokedex.findTypeData(type)["immunities"]
            score = 0
            for string in teamTwoWeaknessesArray:
                if string in res or string in im:
                    score += 2
                if string in weak:
                    score += -2
            for string in teamWeaknessesArray:
                if string in res or string in im:
                    score += 1
                if string in weak:
                    score += -1
            if score > 0:
                bestTypes.append([type, score])
        for i in range(len(bestTypes)):
            for j in range(i, len(bestTypes)):
                if bestTypes[i][1] < bestTypes[j][1]:
                    temp = bestTypes[i]
                    bestTypes[i] = bestTypes[j]
                    bestTypes[j] = temp
        firstChoice = []
        for i in range(len(bestTypes)):
            if bestTypes[i][1] != bestTypes[0][1]:
                break
            else:
                firstChoice.append(bestTypes[i])
        for i in firstChoice:
            del bestTypes[bestTypes.index(i)]
        secondChoice = []
        for i in range(len(bestTypes)):
            if bestTypes[i][1] != bestTypes[0][1]:
                break
            else:
                secondChoice.append(bestTypes[i])
        for i in secondChoice:
            del bestTypes[bestTypes.index(i)]

        # text = "Considering that you are still weak to the following move types:"
        # for string in teamTwoWeaknessesArray:
        #    text+="\n    "+string
        # if len(teamTwoWeaknessesArray)!=0:
        #    text+="\nAnd that you may experience annoyance with the following move types:"
        # for string in teamWeaknessesArray:
        #    text+="\n    "+string
        if len(firstChoice) > 0:
            text = "I suggest to add a Pokemon with one of the following types:"
            for type in firstChoice:
                text += "\n    " + type[0] + " " + self.resistancesText(type[0], teamTwoWeaknessesArray,
                                                                        teamWeaknessesArray)
            if len(secondChoice) > 0:
                text += "\n\nHowever, if you need some more ideas, you could also choose a Pokemon with one of the following types"
                for type in secondChoice:
                    text += "\n    " + type[0] + " " + self.resistancesText(type[0], teamTwoWeaknessesArray,
                                                                            teamWeaknessesArray)
        elif len(secondChoice) > 0:
            text = "I suggest to maybe add a Pokemon with one of the following types:"
            for type in secondChoice:
                text += "\n    " + type[0] + " " + self.resistancesText(type[0], teamTwoWeaknessesArray,
                                                                        teamWeaknessesArray)
        else:
            text = "Everything is looking good!"
        # if len(teamTwoWeaknessesArray)<=1 and len(teamWeaknessesArray)<=2 and len(teamTwoWeaknessesArray)+len(teamTwoWeaknessesArray)<=2:
        #    text+="\n\nHowever, this isn't a huge problem. Your team will probably be fine if you don't"
        self.respond(text)
        self.respond("")

    def offTypeCoverage(self,shell):
        offTypeArrays = [self.normalOffArray, self.fireOffArray, self.waterOffArray, self.electricOffArray,
                         self.grassOffArray, self.iceOffArray, self.fightingOffArray, self.poisonOffArray,
                         self.groundOffArray, self.flyingOffArray, self.psychicOffArray, self.bugOffArray,
                         self.rockOffArray, self.ghostOffArray, self.dragonOffArray, self.darkOffArray,
                         self.steelOffArray, self.fairyOffArray]
        typeStrings = ["Normal", "Fire", "Water", "Electric", "Grass", "Ice", "Fighting", "Poison", "Ground",
                       "Flying", "Psychic", "Bug", "Rock", "Ghost", "Dragon", "Dark", "Steel", "Fairy"]
        k = 0
        for member in shell.teamMatesDict:
            for move in shell.teamMatesDict[member]["moves"]:
                if shell.teamMatesDict[member]["moves"][move] != None and Pokedex.findMoveCategory(
                        shell.teamMatesDict[member]["moves"][move]) != "Status":
                    k += 1
        teamNVEArray = []
        teamTwoNVEArray = []
        for i in range(len(offTypeArrays)):
            score = offTypeArrays[i][0] + (k - offTypeArrays[i][0] - offTypeArrays[i][1] - offTypeArrays[i][2]) / 2 - \
                    offTypeArrays[i][1] - 2 * offTypeArrays[i][2]
            if score <= -2:
                teamTwoNVEArray.append(typeStrings[i])
            elif score == -1:
                teamNVEArray.append(typeStrings[i])

        bestTypes = []
        for type in typeStrings:
            se = Pokedex.findTypeData(type)["superEffective"]
            score = 0
            for string in teamTwoNVEArray:
                if string in se:
                    score += 2
            for string in teamNVEArray:
                if string in se:
                    score += 1
            if score > 0:
                bestTypes.append([type, score])
        for i in range(len(bestTypes)):
            for j in range(i, len(bestTypes)):
                if bestTypes[i][1] < bestTypes[j][1]:
                    temp = bestTypes[i]
                    bestTypes[i] = bestTypes[j]
                    bestTypes[j] = temp

        firstChoice = []
        for i in range(len(bestTypes)):
            if bestTypes[i][1] != bestTypes[0][1]:
                break
            else:
                firstChoice.append(bestTypes[i])
        for i in firstChoice:
            del bestTypes[bestTypes.index(i)]
        secondChoice = []
        for i in range(len(bestTypes)):
            if bestTypes[i][1] != bestTypes[0][1]:
                break
            else:
                secondChoice.append(bestTypes[i])
        for i in secondChoice:
            del bestTypes[bestTypes.index(i)]

        # text = "Considering that you can't hit the following types Super Effectively:"
        # for string in teamTwoNVEArray:
        #    text += "\n    " + string
        # if len(teamTwoNVEArray) != 0:
        #    text += "\nAnd that you may experience annoyance with the following types:"
        # for string in teamNVEArray:
        #    text += "\n    " + string
        if len(firstChoice) > 0:
            text = "I suggest to add a move of the following types:"
            for type in firstChoice:
                text += "\n    " + type[0] + " " + self.superEffectiveText(type[0], teamTwoNVEArray,
                                                                           teamNVEArray)
            if len(secondChoice) > 0:
                text += "\n\nHowever, if you need some more ideas, you could also choose a move of the following types"
                for type in secondChoice:
                    text += "\n    " + type[0] + " " + self.superEffectiveText(type[0], teamTwoNVEArray,
                                                                               teamNVEArray)
        elif len(secondChoice) > 0:
            text = "I suggest to maybe add a move of the following types:"
            for type in secondChoice:
                text += "\n    " + type[0] + " " + self.superEffectiveText(type[0], teamTwoNVEArray,
                                                                           teamNVEArray)
        else:
            text = "Everything is looking good!"

        # if len(teamTwoNVEArray) <= 1 and len(teamNVEArray) <= 2 and len(teamTwoNVEArray) + len(
        #        teamTwoNVEArray) <= 2:
        #    text += "\n\nHowever, this isn't a huge problem. Your team will probably be fine if you don't"
        self.respond(text)
        self.respond("")

    def weatherTeamsText(self,shell,isSunTeam,isHarshSunTeam,isRainTeam,isHarshRainTeam,isHailTeam,isSandTeam,isHarshWindTeam):
        if isSunTeam:
            text=""
            text+="There is potential for making a Sun team here. Sun teams specialize in using Fire and Grass-type Pokemon to strike hard and fast. The sun also offers protection to Pokemon who are afraid of Water-type moves, such as Fire, Rock, and Ground-types."
            text+="\n\nHere's a complete list of the affects that the Sun can have:"
            text+="\n*    Sunlight stays on the field for 5 turns, unless overridden by other weather conditions"
            text+="\n\n*    Pokemon holding a Heat Rock can summon the Sun for 8 turns"
            text+="\n\n*    Fire-type move's base power is increased by 50%"
            text+="\n\n*    Water-type move's base power is decreased by 50%"
            text+="\n\n*    The moves Solar Beam and Solar Blade do not require charging"
            text+="\n\n*    The move Thunder's accuracy is reduced by 50%"
            text+="\n\n*    The move Hurricane's accuracy is reduced by 50%"
            text+="\n\n*    The moves Synthesis, Morning Sun, and Moonlight recover 66% of the user's maximum HP"
            text+="\n\n*    The move Growth raises the Atk stat of the user by 1 extra stage"
            text+="\n\n*    Pokemon with the ability Chlorophyll have their Spe raised by 100%"
            text+="\n\n*    Pokemon with the ability Dry Skin recieve twice the damage from Fire attacks and also lose 1/8 of their maximum HP every turn"
            text+="\n\n*    Cherrim changes into it's Sunshine Form."
            text+="\n\n*    Cherrim's Flower Gift ability raises its ally's Atk and SpD by 1 stage"
            text+="\n\n*    Pokemon with the ability Leaf Guard are protected from status conditions"
            text+="\n\n*    Pokemon with the ability Solar Power have their SpA increased by 1 stage and also lose 1/8 of their maximum HP every turn."
            text+="\n\n*    Castform changes into it's Sunny Form."
            text+="\n\n*    The move Weather Ball doubles in power and becomes a Fire move"
            text+="\n\nNotable Sun setters are:"
            text+="\n    Charizard-Mega-X"
            text+="\n    Torkoal"
            text+="\n    Groudon"
            text+="\n    Ninetales"
            self.respond(text)
            self.respond("")
        elif isHarshSunTeam:
            text = ""
            text += "There is potential for making a Harsh Sun team here. Harsh Sun teams specialize in using Fire and Grass-type Pokemon to strike hard and fast. The Harsh Sun also offers immunity to Pokemon who are afraid of Water-type moves, such as Fire, Rock, and Ground-types."
            text += "\n\nHere's a complete list of the affects that the Sun can have:"
            text += "\n*    Fire-type move's base power is increased by 50%"
            text += "\n\n*    Water-type moves do not work at all"
            text += "\n\n*    The moves Sunny Day, Rain Dance, Hail, and Sandstorm will not work"
            text += "\n\n*    The abilities Drought, Drizzle, Snow Warning, and Sand Stream will not activate"
            text += "\n\n*    The moves Solar Beam and Solar Blade do not require charging"
            text += "\n\n*    The move Thunder's accuracy is reduced by 50%"
            text += "\n\n*    The move Hurricane's accuracy is reduced by 50%"
            text += "\n\n*    The moves Synthesis, Morning Sun, and Moonlight recover 66% of the user's maximum HP"
            text += "\n\n*    The move Growth raises the Atk stat of the user by 1 extra stage"
            text += "\n\n*    Pokemon with the ability Chlorophyll have their Spe raised by 100%"
            text += "\n\n*    Pokemon with the ability Dry Skin recieve twice the damage from Fire attacks and also lose 1/8 of their maximum HP every turn"
            text += "\n\n*    Cherrim changes into it's Sunshine Form."
            text += "\n\n*    Cherrim's Flower Gift ability raises its ally's Atk and SpD by 1 stage"
            text += "\n\n*    Pokemon with the ability Leaf Guard are protected from status conditions"
            text += "\n\n*    Pokemon with the ability Solar Power have their SpA increased by 1 stage and also lose 1/8 of their maximum HP every turn."
            text += "\n\n*    Castform changes into it's Sunny Form."
            text += "\n\n*    The move Weather Ball doubles in power and becomes a Fire move"
            text += "\n\nHarsh Sunlight can only be summoned by Groudon-Primal, using its ability Desolate Land"
            self.respond(text)
            self.respond("")
        elif isRainTeam:
            text=""
            text+="There is potential for making a Rain team here. Rain teams are centered around Water and Electric-type Pokemon, either by making them more sustainable or increasing their overal power. Steel and Grass types also appreciate the Rain, considering that they are then more protected from Fire-type moves."
            text+="\n\nHere's a complete list of the affects that the Rain can have:"
            text+="\n*    Rain stays on the field for 5 turns, unless overridden by other weather conditions"
            text+="\n\n*    Pokemon holding a Damp Rock can summon the Rain for 8 turns"
            text+="\n\n*    Water-type move's base power is increased by 50%"
            text+="\n\n*    Fire-type move's base power is decreased by 50%"
            text+="\n\n*    The moves Solar Beam requires two turns to charge"
            text+="\n\n*    The move Thunder's accuracy is increased to 100%"
            text+="\n\n*    The move Hurricane's accuracy is increased to 100%"
            text+="\n\n*    The moves Synthesis, Morning Sun, and Moonlight recover 25% of the user's maximum HP"
            text+="\n\n*    Pokemon with the ability Dry Skin recover 1/4 of their maximum HP from Water moves instead of taking damage. They also regain 1/8 of their maximum HP every turn"
            text+="\n\n*    Pokemon with the ability Hydration are cured from status conditions every turn"
            text+="\n\n*    Pokemon with the ability Rain Dish regain 1/16th of their maximum HP every turn"
            text+="\n\n*    Pokemon with the ability Swift Swim have their Spe raised by 100%"
            text+="\n\n*    Castform changes into it's Rain Form."
            text+="\n\n*    The move Weather Ball doubles in power and becomes a Water move"
            text += "\n\nNotable Rain setters are:"
            text += "\n    Politoed"
            text += "\n    Pelipper"
            text += "\n    Kyogre"
            self.respond(text)
            self.respond("")
        elif isHarshRainTeam:
            text = ""
            text += "There is potential for making a Heavy Rain team here. Heavy Rain teams are centered around Water and Electric-type Pokemon, either by making them more sustainable or increasing their overal power. Steel and Grass types also appreciate the Rain, considering that they are then immune to Fire-type moves."
            text += "\n\nHere's a complete list of the affects that the Rain can have:"
            text += "\n*    Water-type move's base power is increased by 50%"
            text += "\n\n*    Fire-type moves do not work at all"
            text += "\n\n*    The moves Sunny Day, Rain Dance, Hail, and Sandstorm will not work"
            text += "\n\n*    The abilities Drought, Drizzle, Snow Warning, and Sand Stream will not activate"
            text += "\n\n*    The moves Solar Beam requires two turns to charge"
            text += "\n\n*    The move Thunder's accuracy is increased to 100%"
            text += "\n\n*    The move Hurricane's accuracy is increased to 100%"
            text += "\n\n*    The moves Synthesis, Morning Sun, and Moonlight recover 25% of the user's maximum HP"
            text += "\n\n*    Pokemon with the ability Dry Skin recover 1/4 of their maximum HP from Water moves instead of taking damage. They also regain 1/8 of their maximum HP every turn"
            text += "\n\n*    Pokemon with the ability Hydration are cured from status conditions every turn"
            text += "\n\n*    Pokemon with the ability Rain Dish regain 1/16th of their maximum HP every turn"
            text += "\n\n*    Pokemon with the ability Swift Swim have their Spe raised by 100%"
            text += "\n\n*    Castform changes into it's Rain Form."
            text += "\n\n*    The move Weather Ball doubles in power and becomes a Water move"
            text += "\n\nHeavy Rain can only be summoned by Kyogre-Primal, using its ability Primordial Sea"
            self.respond(text)
            self.respond("")
        elif isHailTeam:
            text=""
            text+="I see you are using Hail in your team. Hail is difficult to make an entire team around, but it does offer some interesting buffs for Ice types."
            text += "\n\nHere's a complete list of the affects that Hail can have:"
            text += "\n*    Hail stays on the field for 5 turns, unless overridden by other weather conditions"
            text += "\n\n*    Pokemon holding an Icy Rock can summon Hail for 8 turns"
            text += "\n\n*    All non-Ice-type Pokemon lose 1/16th of their maximum HP every turn"
            text += "\n\n*    The move Blizzard's accuracy is increased to 100%"
            text += "\n\n*    The moves Synthesis, Morning Sun, and Moonlight recover 25% of the user's maximum HP"
            text += "\n\n*    Pokemon with the ability Ice Body recover 1/16th of their maximum HP every turn"
            text += "\n\n*    Pokemon with the ability Snow Cloak have their evasion raised by 20%"
            text += "\n\n*    Pokemon with the ability Slush Rush have their Spe raised by 100%"
            text += "\n\n*    Castform changes into it's Snowy Form."
            text += "\n\n*    The move Weather Ball doubles in power and becomes an Ice move"
            text += "\n\n*    The move Aurora Veil will reduce direct damage taken by the user by 50%, for 5 turns. Is affected by Light Clay"
            text += "\n\nNotable Hail setters are:"
            text += "\n    Abomasnow"
            text += "\n    Abomasnow-Mega"
            text += "\n    Vanilluxe"
            text += "\n    Ninetales-Alolan"
            text += "\n    Aurorus"
            self.respond(text)
            self.respond("")
        elif isSandTeam:
            text=""
            text+="There is potential for making a Sand team here. Sand teams focus on helping Rock, Steel, and Ground-type Pokemon by buffing them and their moves."
            text += "\n\nHere's a complete list of the affects that Hail can have:"
            text += "\n*A Sandstorm stays on the field for 5 turns, unless overridden by other weather conditions"
            text += "\n*Pokemon holding a Smooth Rock can summon a Sandstorm for 8 turns"
            text += "\n*All non-Rock, Steel, and Ground-type Pokemon lose 1/16th of their maximum HP every turn"
            text += "\n*Rock-type Pokemon have their SpD raised by 1 stage"
            text += "\n*The move Solar Beam's power is reduced by 50%"
            text += "\n*The move Shore Up recovers 100% of the user's maximum HP"
            text += "\n*The moves Synthesis, Morning Sun, and Moonlight recover 25% of the user's maximum HP"
            text += "\n*Pokemon with the ability Sand Veil have their evasion raised by 20%"
            text += "\n*Pokemon with the ability Sand Rush have their Spe raised by 100%"
            text += "\n*Pokemon with the ability Sand Force have their Rock, Steel, and Ground-type moves' power increased by 33%"
            text += "\n*The move Weather Ball doubles in power and becomes a Rock move"
            text += "\n\nNotable Hail setters are:"
            text += "\n    Tyranitar"
            text += "\n    Tyranitar-Mega"
            text += "\n    Hippowdon"
            text += "\n    Gigalith"
            self.respond(text)
            self.respond("")
        elif isHarshWindTeam:
            text = ""
            text += "I see you are using Delta Stream in your team. Strong Wind is difficult to make an entire team around, but it does offer some interesting affects."
            text += "\n\nHere's a complete list of the affects that Strong Winds can have:"
            text += "\n*    The moves Sunny Day, Rain Dance, Hail, and Sandstorm will not work"
            text += "\n\n*    The abilities Drought, Drizzle, Snow Warning, and Sand Stream will not activate"
            text += "\n\n*    Overrides the affects of Heavy Rain and Harsh Sun"
            text += "\n\n*    Moves used against Flying-type Pokemon that are Super-Effective instead deal neutral damage"
            text += "\n\nHarsh Sunlight can only be summoned by Rayquaza-Mega, using its ability Delta Stream"
            self.respond(text)
            self.respond("")

    def trickRoomTeamText(self,shell,isTrickRoomTeam):
        if isTrickRoomTeam:
            text = ""
            text += "There is potential for making a Trick Room team here. Trick Room teams specialize in turning slow but powerful Pokemon into lightning fast sweepers."
            self.respond(text)

    def update(self,shell,option):
        if self.toplevel.state() in ["iconic","icon","withdrawn"]:
            self.toplevel.deiconify()

        if option=="species":
            self.normalDefArray = [0, 0, 0, 0, 0]
            self.fireDefArray = [0, 0, 0, 0, 0]
            self.waterDefArray = [0, 0, 0, 0, 0]
            self.electricDefArray = [0, 0, 0, 0, 0]
            self.grassDefArray = [0, 0, 0, 0, 0]
            self.iceDefArray = [0, 0, 0, 0, 0]
            self.fightingDefArray = [0, 0, 0, 0, 0]
            self.poisonDefArray = [0, 0, 0, 0, 0]
            self.groundDefArray = [0, 0, 0, 0, 0]
            self.flyingDefArray = [0, 0, 0, 0, 0]
            self.psychicDefArray = [0, 0, 0, 0, 0]
            self.bugDefArray = [0, 0, 0, 0, 0]
            self.rockDefArray = [0, 0, 0, 0, 0]
            self.ghostDefArray = [0, 0, 0, 0, 0]
            self.dragonDefArray = [0, 0, 0, 0, 0]
            self.darkDefArray = [0, 0, 0, 0, 0]
            self.steelDefArray = [0, 0, 0, 0, 0]
            self.fairyDefArray = [0, 0, 0, 0, 0]

            typesDict = Pokedex.loadTypes()

            #for member in shell.teamMatesDict:

            for member in shell.teamMateNames:
                typesList = Pokedex.findPokemonTypes(member)
                if len(typesList)==2:
                    wriplus = self.defCombineTypes(typesList,False)
                    for wType in wriplus[0]:
                        if wType == "Normal":
                            self.normalDefArray[0]+=1
                        elif wType == "Fire":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Flash Fire", "Primordial Sea"]:
                                    self.fireDefArray[4]+=1
                                elif shell.teamMatesDict[member]["ability"] in ["Thick Fat", "Water Bubble", "Drizzle"]:
                                    self.fireDefArray[1]+=1
                                else:
                                    self.fireDefArray[0] += 1
                            else:
                                self.fireDefArray[0]+=1
                        elif wType == "Water":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Storm Drain", "Water Absorb", "Desolate Land","Dry Skin"]:
                                    self.waterDefArray[4]+=1
                                elif shell.teamMatesDict[member]["ability"] in ["Drought"]:
                                    self.waterDefArray[1]+=1
                                else:
                                    self.waterDefArray[0] += 1
                            else:
                                self.waterDefArray[0]+=1
                        elif wType == "Electric":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Lightning Rod", "Volt Absorb","Motor Drive"]:
                                    self.electricDefArray[4]+=1
                                else:
                                    self.electricDefArray[0] += 1
                            else:
                                self.electricDefArray[0]+=1
                        elif wType == "Grass":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Sap Sipper"]:
                                    self.grassDefArray[4]+=1
                                else:
                                    self.grassDefArray[0] += 1
                            else:
                                self.grassDefArray[0]+=1
                        elif wType == "Ice":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Thick Fat"]:
                                    self.iceDefArray[1]+=1
                                else:
                                    self.iceDefArray[0] += 1
                            else:
                                self.iceDefArray[0]+=1
                        elif wType == "Fighting":
                            self.fightingDefArray[0]+=1
                        elif wType == "Poison":
                            self.poisonDefArray[0]+=1
                        elif wType == "Ground":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Levitate"]:
                                    self.groundDefArray[4]+=1
                                else:
                                    self.groundDefArray[0]+=1
                            else:
                                self.groundDefArray[0]+=1
                        elif wType == "Flying":
                            self.flyingDefArray[0]+=1
                        elif wType == "Psychic":
                            self.psychicDefArray[0]+=1
                        elif wType == "Bug":
                            self.bugDefArray[0]+=1
                        elif wType == "Rock":
                            self.rockDefArray[0]+=1
                        elif wType == "Ghost":
                            self.ghostDefArray[0]+=1
                        elif wType == "Dragon":
                            self.dragonDefArray[0]+=1
                        elif wType == "Dark":
                            self.darkDefArray[0]+=1
                        elif wType == "Steel":
                            self.steelDefArray[0]+=1
                        elif wType == "Fairy":
                            self.fairyDefArray[0]+=1
                        elif wType == "":
                            pass
                        else:
                            print("An error occurred when registering Double Weaknesses")
                    for wType in wriplus[1]:
                        if wType == "Normal":
                            self.normalDefArray[1]+=1
                        elif wType == "Fire":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Flash Fire", "Primordial Sea"]:
                                    self.fireDefArray[4]+=1
                                elif shell.teamMatesDict[member]["ability"] in ["Thick Fat", "Water Bubble", "Drizzle"]:
                                    pass
                                elif shell.teamMatesDict[member]["ability"] in ["Fluffy"]:
                                    self.fireDefArray[0]+=1
                                else:
                                    self.fireDefArray[1]+=1
                            else:
                                self.fireDefArray[1]+=1
                        elif wType == "Water":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Storm Drain", "Water Absorb", "Desolate Land","Dry Skin"]:
                                    self.waterDefArray[4]+=1
                                elif shell.teamMatesDict[member]["ability"] in ["Drought"]:
                                    pass
                                else:
                                    self.waterDefArray[1]+=1
                            else:
                                self.waterDefArray[1]+=1
                        elif wType == "Electric":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Lightning Rod", "Volt Absorb", "Motor Drive"]:
                                    self.electricDefArray[4]+=1
                                else:
                                    self.electricDefArray[1]+=1
                            else:
                                self.electricDefArray[1]+=1
                        elif wType == "Grass":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Sap Sipper"]:
                                    self.grassDefArray[4]+=1
                                else:
                                    self.grassDefArray[1]+=1
                            else:
                                self.grassDefArray[1]+=1
                        elif wType == "Ice":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Thick Fat"]:
                                    pass
                                else:
                                    self.iceDefArray[1]+=1
                            else:
                                self.iceDefArray[1]+=1
                        elif wType == "Fighting":
                            self.fightingDefArray[1]+=1
                        elif wType == "Poison":
                            self.poisonDefArray[1]+=1
                        elif wType == "Ground":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Levitate"]:
                                    self.groundDefArray[4]+=1
                                else:
                                    self.groundDefArray[1]+=1
                            else:
                                self.groundDefArray[1]+=1
                        elif wType == "Flying":
                            self.flyingDefArray[1]+=1
                        elif wType == "Psychic":
                            self.psychicDefArray[1]+=1
                        elif wType == "Bug":
                            self.bugDefArray[1]+=1
                        elif wType == "Rock":
                            self.rockDefArray[1]+=1
                        elif wType == "Ghost":
                            self.ghostDefArray[1]+=1
                        elif wType == "Dragon":
                            self.dragonDefArray[1]+=1
                        elif wType == "Dark":
                            self.darkDefArray[1]+=1
                        elif wType == "Steel":
                            self.steelDefArray[1]+=1
                        elif wType == "Fairy":
                            self.fairyDefArray[1]+=1
                        elif wType == "":
                            pass
                        else:
                            print("An error occurred when registering Weaknesses")
                    for rType in wriplus[2]:
                        if rType == "Normal":
                            self.normalDefArray[2]+=1
                        elif rType == "Fire":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Flash Fire", "Primordial Sea"]:
                                    self.fireDefArray[4]+=1
                                elif shell.teamMatesDict[member]["ability"] in ["Thick Fat", "Water Bubble", "Drizzle"]:
                                    self.fireDefArray[3]+=1
                                elif shell.teamMatesDict[member]["ability"] in ["Fluffy"]:
                                    pass
                                else:
                                    self.fireDefArray[2]+=1
                            else:
                                self.fireDefArray[2]+=1
                        elif rType == "Water":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Storm Drain", "Water Absorb", "Desolate Land","Dry Skin"]:
                                    self.waterDefArray[4]+=1
                                elif shell.teamMatesDict[member]["ability"] in ["Drought"]:
                                    self.waterDefArray[3]+=1
                                else:
                                    self.waterDefArray[2]+=1
                            else:
                                self.waterDefArray[2]+=1
                        elif rType == "Electric":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Lightning Rod", "Volt Absorb", "Motor Drive"]:
                                    self.electricDefArray[4]+=1
                                else:
                                    self.electricDefArray[2]+=1
                            else:
                                self.electricDefArray[2]+=1
                        elif rType == "Grass":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Sap Sipper"]:
                                    self.grassDefArray[4]+=1
                                else:
                                    self.grassDefArray[2]+=1
                            else:
                                self.grassDefArray[2]+=1
                        elif rType == "Ice":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Thick Fat"]:
                                    self.iceDefArray[3]+=1
                                else:
                                    self.iceDefArray[2]+=1
                            else:
                                self.iceDefArray[2]+=1
                        elif rType == "Fighting":
                            self.fightingDefArray[2]+=1
                        elif rType == "Poison":
                            self.poisonDefArray[2]+=1
                        elif rType == "Ground":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Levitate"]:
                                    self.groundDefArray[4]+=1
                                else:
                                    self.groundDefArray[2]+=1
                            else:
                                self.groundDefArray[2]+=1
                        elif rType == "Flying":
                            self.flyingDefArray[2]+=1
                        elif rType == "Psychic":
                            self.psychicDefArray[2]+=1
                        elif rType == "Bug":
                            self.bugDefArray[2]+=1
                        elif rType == "Rock":
                            self.rockDefArray[2]+=1
                        elif rType == "Ghost":
                            self.ghostDefArray[2]+=1
                        elif rType == "Dragon":
                            self.dragonDefArray[2]+=1
                        elif rType == "Dark":
                            self.darkDefArray[2]+=1
                        elif rType == "Steel":
                            self.steelDefArray[2]+=1
                        elif rType == "Fairy":
                            self.fairyDefArray[2]+=1
                        elif rType == "":
                            pass
                        else:
                            print("An error occurred when registering Resistances")
                    for rType in wriplus[3]:
                        if rType == "Normal":
                            self.normalDefArray[3]+=1
                        elif rType == "Fire":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Flash Fire", "Primordial Sea"]:
                                    self.fireDefArray[4]+=1
                                elif shell.teamMatesDict[member]["ability"] in ["Fluffy"]:
                                    self.fireDefArray[2]+=1
                                else:
                                    self.fireDefArray[3]+=1
                            else:
                                self.fireDefArray[3]+=1
                        elif rType == "Water":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Storm Drain", "Water Absorb", "Desolate Land","Dry Skin"]:
                                    self.waterDefArray[4]+=1
                                else:
                                    self.waterDefArray[3]+=1
                            else:
                                self.waterDefArray[3]+=1
                        elif rType == "Electric":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Lightning Rod", "Volt Absorb", "Motor Drive"]:
                                    self.electricDefArray[4]+=1
                                else:
                                    self.electricDefArray[3]+=1
                            else:
                                self.electricDefArray[3]+=1
                        elif rType == "Grass":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Sap Sipper"]:
                                    self.grassDefArray[4]+=1
                                else:
                                    self.grassDefArray[3]+=1
                            else:
                                self.grassDefArray[3]+=1
                        elif rType == "Ice":
                            self.iceDefArray[3]+=1
                        elif rType == "Fighting":
                            self.fightingDefArray[3]+=1
                        elif rType == "Poison":
                            self.poisonDefArray[3]+=1
                        elif rType == "Ground":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Levitate"]:
                                    self.groundDefArray[4]+=1
                                else:
                                    self.groundDefArray[3]+=1
                            else:
                                self.groundDefArray[3]+=1
                        elif rType == "Flying":
                            self.flyingDefArray[3]+=1
                        elif rType == "Psychic":
                            self.psychicDefArray[3]+=1
                        elif rType == "Bug":
                            self.bugDefArray[3]+=1
                        elif rType == "Rock":
                            self.rockDefArray[3]+=1
                        elif rType == "Ghost":
                            self.ghostDefArray[3]+=1
                        elif rType == "Dragon":
                            self.dragonDefArray[3]+=1
                        elif rType == "Dark":
                            self.darkDefArray[3]+=1
                        elif rType == "Steel":
                            self.steelDefArray[3]+=1
                        elif rType == "Fairy":
                            self.fairyDefArray[3]+=1
                        elif rType == "":
                            pass
                        else:
                            print("An error occurred when registering Double Resistances")
                    for iType in wriplus[4]:
                        if iType == "Normal":
                            self.normalDefArray[4]+=1
                        elif iType == "Fire":
                            self.fireDefArray[4]+=1
                        elif iType == "Water":
                            self.waterDefArray[4]+=1
                        elif iType == "Electric":
                            self.electricDefArray[4]+=1
                        elif iType == "Grass":
                            self.grassDefArray[4]+=1
                        elif iType == "Ice":
                            self.iceDefArray[4]+=1
                        elif iType == "Fighting":
                            self.fightingDefArray[4]+=1
                        elif iType == "Poison":
                            self.poisonDefArray[4]+=1
                        elif iType == "Ground":
                            self.groundDefArray[4]+=1
                        elif iType == "Flying":
                            self.flyingDefArray[4]+=1
                        elif iType == "Psychic":
                            self.psychicDefArray[4]+=1
                        elif iType == "Bug":
                            self.bugDefArray[4]+=1
                        elif iType == "Rock":
                            self.rockDefArray[4]+=1
                        elif iType == "Ghost":
                            self.ghostDefArray[4]+=1
                        elif iType == "Dragon":
                            self.dragonDefArray[4]+=1
                        elif iType == "Dark":
                            self.darkDefArray[4]+=1
                        elif iType == "Steel":
                            self.steelDefArray[4]+=1
                        elif iType == "Fairy":
                            self.fairyDefArray[4]+=1
                        elif iType == "":
                            pass
                        else:
                            print("An error occurred when registering Immunities")
                else:
                    w = typesDict[typesList[0]]["weaknesses"]
                    for wType in w:
                        if wType == "Normal":
                            self.normalDefArray[1]+=1
                        elif wType == "Fire":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Flash Fire", "Primordial Sea"]:
                                    self.fireDefArray[4]+=1
                                elif shell.teamMatesDict[member]["ability"] in ["Thick Fat", "Water Bubble", "Drizzle"]:
                                    pass
                                elif shell.teamMatesDict[member]["ability"] in ["Fluffy"]:
                                    self.fireDefArray[0]+=1
                                else:
                                    self.fireDefArray[1]+=1
                            else:
                                self.fireDefArray[1]+=1
                        elif wType == "Water":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Storm Drain", "Water Absorb", "Desolate Land", "Dry Skin"]:
                                    self.waterDefArray[4]+=1
                                elif shell.teamMatesDict[member]["ability"] in ["Drought"]:
                                    pass
                                else:
                                    self.waterDefArray[1]+=1
                            else:
                                self.waterDefArray[1]+=1
                        elif wType == "Electric":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Lightning Rod", "Volt Absorb", "Motor Drive"]:
                                    self.electricDefArray[4]+=1
                                else:
                                    self.electricDefArray[1]+=1
                            else:
                                self.electricDefArray[1]+=1
                        elif wType == "Grass":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Sap Sipper"]:
                                    self.grassDefArray[4]+=1
                                else:
                                    self.grassDefArray[1]+=1
                            else:
                                self.grassDefArray[1]+=1
                        elif wType == "Ice":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Thick Fat"]:
                                    pass
                                else:
                                    self.iceDefArray[1]+=1
                            else:
                                self.iceDefArray[1]+=1
                        elif wType == "Fighting":
                            self.fightingDefArray[1]+=1
                        elif wType == "Poison":
                            self.poisonDefArray[1]+=1
                        elif wType == "Ground":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Levitate"]:
                                    self.groundDefArray[4]+=1
                                else:
                                    self.groundDefArray[1]+=1
                            else:
                                self.groundDefArray[1]+=1
                        elif wType == "Flying":
                            self.flyingDefArray[1]+=1
                        elif wType == "Psychic":
                            self.psychicDefArray[1]+=1
                        elif wType == "Bug":
                            self.bugDefArray[1]+=1
                        elif wType == "Rock":
                            self.rockDefArray[1]+=1
                        elif wType == "Ghost":
                            self.ghostDefArray[1]+=1
                        elif wType == "Dragon":
                            self.dragonDefArray[1]+=1
                        elif wType == "Dark":
                            self.darkDefArray[1]+=1
                        elif wType == "Steel":
                            self.steelDefArray[1]+=1
                        elif wType == "Fairy":
                            self.fairyDefArray[1]+=1
                        elif wType == "":
                            pass
                        else:
                            print("An error occurred when registering Weaknesses")
                    r = typesDict[typesList[0]]["resistances"]
                    for rType in r:
                        if rType == "Normal":
                            self.normalDefArray[2]+=1
                        elif rType == "Fire":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Flash Fire", "Primordial Sea"]:
                                    self.fireDefArray[4]+=1
                                elif shell.teamMatesDict[member]["ability"] in ["Thick Fat", "Water Bubble", "Drizzle"]:
                                    self.fireDefArray[3]+=1
                                elif shell.teamMatesDict[member]["ability"] in ["Fluffy"]:
                                    pass
                                else:
                                    self.fireDefArray[2]+=1
                            else:
                                self.fireDefArray[2]+=1
                        elif rType == "Water":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Storm Drain", "Water Absorb", "Desolate Land","Dry Skin"]:
                                    self.waterDefArray[4]+=1
                                elif shell.teamMatesDict[member]["ability"] in ["Drought"]:
                                    self.waterDefArray[3]+=1
                                else:
                                    self.waterDefArray[2]+=1
                            else:
                                self.waterDefArray[2]+=1
                        elif rType == "Electric":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Lightning Rod", "Volt Absorb", "Motor Drive"]:
                                    self.electricDefArray[4]+=1
                                else:
                                    self.electricDefArray[2]+=1
                            else:
                                self.electricDefArray[2]+=1
                        elif rType == "Grass":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Sap Sipper"]:
                                    self.grassDefArray[4]+=1
                                else:
                                    self.grassDefArray[2]+=1
                            else:
                                self.grassDefArray[2]+=1
                        elif rType == "Ice":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Thick Fat"]:
                                    self.iceDefArray[3]+=1
                                else:
                                    self.iceDefArray[2]+=1
                            else:
                                self.iceDefArray[2]+=1
                        elif rType == "Fighting":
                            self.fightingDefArray[2]+=1
                        elif rType == "Poison":
                            self.poisonDefArray[2]+=1
                        elif rType == "Ground":
                            if member in shell.teamMatesDict:
                                if shell.teamMatesDict[member]["ability"] in ["Levitate"]:
                                    self.groundDefArray[4]+=1
                                else:
                                    self.groundDefArray[2]+=1
                            else:
                                self.groundDefArray[2]+=1
                        elif rType == "Flying":
                            self.flyingDefArray[2]+=1
                        elif rType == "Psychic":
                            self.psychicDefArray[2]+=1
                        elif rType == "Bug":
                            self.bugDefArray[2]+=1
                        elif rType == "Rock":
                            self.rockDefArray[2]+=1
                        elif rType == "Ghost":
                            self.ghostDefArray[2]+=1
                        elif rType == "Dragon":
                            self.dragonDefArray[2]+=1
                        elif rType == "Dark":
                            self.darkDefArray[2]+=1
                        elif rType == "Steel":
                            self.steelDefArray[2]+=1
                        elif rType == "Fairy":
                            self.fairyDefArray[2]+=1
                        elif rType == "":
                            pass
                        else:
                            print("An error occurred when registering Resistances")
                    i = typesDict[typesList[0]]["immunities"]
                    for iType in i:
                        if iType == "Normal":
                            self.normalDefArray[4]+=1
                        elif iType == "Fire":
                            self.fireDefArray[4]+=1
                        elif iType == "Water":
                            self.waterDefArray[4]+=1
                        elif iType == "Electric":
                            self.electricDefArray[4]+=1
                        elif iType == "Grass":
                            self.grassDefArray[4]+=1
                        elif iType == "Ice":
                            self.iceDefArray[4]+=1
                        elif iType == "Fighting":
                            self.fightingDefArray[4]+=1
                        elif iType == "Poison":
                            self.poisonDefArray[4]+=1
                        elif iType == "Ground":
                            self.groundDefArray[4]+=1
                        elif iType == "Flying":
                            self.flyingDefArray[4]+=1
                        elif iType == "Psychic":
                            self.psychicDefArray[4]+=1
                        elif iType == "Bug":
                            self.bugDefArray[4]+=1
                        elif iType == "Rock":
                            self.rockDefArray[4]+=1
                        elif iType == "Ghost":
                            self.ghostDefArray[4]+=1
                        elif iType == "Dragon":
                            self.dragonDefArray[4]+=1
                        elif iType == "Dark":
                            self.darkDefArray[4]+=1
                        elif iType == "Steel":
                            self.steelDefArray[4]+=1
                        elif iType == "Fairy":
                            self.fairyDefArray[4]+=1
                        elif iType == "":
                            pass
                        else:
                            print("An error occurred when registering Immunities")

            self.normalzeroDefText.set(self.normalDefArray[4])
            self.normalquarterDefText.set(self.normalDefArray[3])
            self.normalhalfDefText.set(self.normalDefArray[2])
            self.normaloneDefText.set(len(shell.teamMateNames)-self.normalDefArray[4]-self.normalDefArray[3]-self.normalDefArray[2]-self.normalDefArray[1]-self.normalDefArray[0])
            self.normaltwoDefText.set(self.normalDefArray[1])
            self.normalfourDefText.set(self.normalDefArray[0])
            self.defTypeColor(self.normalDefArray,self.normalzeroDefLabel,self.normalquarterDefLabel,self.normalhalfDefLabel,self.normaltwoDefLabel,self.normalfourDefLabel)

            self.firezeroDefText.set(self.fireDefArray[4])
            self.firequarterDefText.set(self.fireDefArray[3])
            self.firehalfDefText.set(self.fireDefArray[2])
            self.fireoneDefText.set(len(shell.teamMateNames)-self.fireDefArray[4]-self.fireDefArray[3]-self.fireDefArray[2]-self.fireDefArray[1]-self.fireDefArray[0])
            self.firetwoDefText.set(self.fireDefArray[1])
            self.firefourDefText.set(self.fireDefArray[0])
            self.defTypeColor(self.fireDefArray, self.firezeroDefLabel, self.firequarterDefLabel, self.firehalfDefLabel,self.firetwoDefLabel, self.firefourDefLabel)

            self.waterzeroDefText.set(self.waterDefArray[4])
            self.waterquarterDefText.set(self.waterDefArray[3])
            self.waterhalfDefText.set(self.waterDefArray[2])
            self.wateroneDefText.set(len(shell.teamMateNames)-self.waterDefArray[4]-self.waterDefArray[3]-self.waterDefArray[2]-self.waterDefArray[1]-self.waterDefArray[0])
            self.watertwoDefText.set(self.waterDefArray[1])
            self.waterfourDefText.set(self.waterDefArray[0])
            self.defTypeColor(self.waterDefArray, self.waterzeroDefLabel, self.waterquarterDefLabel, self.waterhalfDefLabel,self.watertwoDefLabel, self.waterfourDefLabel)

            self.electriczeroDefText.set(self.electricDefArray[4])
            self.electricquarterDefText.set(self.electricDefArray[3])
            self.electrichalfDefText.set(self.electricDefArray[2])
            self.electriconeDefText.set(len(shell.teamMateNames)-self.electricDefArray[4]-self.electricDefArray[3]-self.electricDefArray[2]-self.electricDefArray[1]-self.electricDefArray[0])
            self.electrictwoDefText.set(self.electricDefArray[1])
            self.electricfourDefText.set(self.electricDefArray[0])
            self.defTypeColor(self.electricDefArray, self.electriczeroDefLabel, self.electricquarterDefLabel, self.electrichalfDefLabel,self.electrictwoDefLabel, self.electricfourDefLabel)

            self.grasszeroDefText.set(self.grassDefArray[4])
            self.grassquarterDefText.set(self.grassDefArray[3])
            self.grasshalfDefText.set(self.grassDefArray[2])
            self.grassoneDefText.set(len(shell.teamMateNames)-self.grassDefArray[4]-self.grassDefArray[3]-self.grassDefArray[2]-self.grassDefArray[1]-self.grassDefArray[0])
            self.grasstwoDefText.set(self.grassDefArray[1])
            self.electricfourDefText.set(self.grassDefArray[0])
            self.defTypeColor(self.grassDefArray, self.grasszeroDefLabel, self.grassquarterDefLabel, self.grasshalfDefLabel,self.grasstwoDefLabel, self.grassfourDefLabel)

            self.icezeroDefText.set(self.iceDefArray[4])
            self.icequarterDefText.set(self.iceDefArray[3])
            self.icehalfDefText.set(self.iceDefArray[2])
            self.iceoneDefText.set(len(shell.teamMateNames)-self.iceDefArray[4]-self.iceDefArray[3]-self.iceDefArray[2]-self.iceDefArray[1]-self.iceDefArray[0])
            self.icetwoDefText.set(self.iceDefArray[1])
            self.icefourDefText.set(self.iceDefArray[0])
            self.defTypeColor(self.iceDefArray, self.icezeroDefLabel, self.icequarterDefLabel, self.icehalfDefLabel,self.icetwoDefLabel, self.icefourDefLabel)

            self.fightingzeroDefText.set(self.fightingDefArray[4])
            self.fightingquarterDefText.set(self.fightingDefArray[3])
            self.fightinghalfDefText.set(self.fightingDefArray[2])
            self.fightingoneDefText.set(len(shell.teamMateNames)-self.fightingDefArray[4]-self.fightingDefArray[3]-self.fightingDefArray[2]-self.fightingDefArray[1]-self.fightingDefArray[0])
            self.fightingtwoDefText.set(self.fightingDefArray[1])
            self.fightingfourDefText.set(self.fightingDefArray[0])
            self.defTypeColor(self.fightingDefArray, self.fightingzeroDefLabel, self.fightingquarterDefLabel, self.fightinghalfDefLabel,self.fightingtwoDefLabel, self.fightingfourDefLabel)

            self.poisonzeroDefText.set(self.poisonDefArray[4])
            self.poisonquarterDefText.set(self.poisonDefArray[3])
            self.poisonhalfDefText.set(self.poisonDefArray[2])
            self.poisononeDefText.set(len(shell.teamMateNames)-self.poisonDefArray[4]-self.poisonDefArray[3]-self.poisonDefArray[2]-self.poisonDefArray[1]-self.poisonDefArray[0])
            self.poisontwoDefText.set(self.poisonDefArray[1])
            self.poisonfourDefText.set(self.poisonDefArray[0])
            self.defTypeColor(self.poisonDefArray, self.poisonzeroDefLabel, self.poisonquarterDefLabel, self.poisonhalfDefLabel,self.poisontwoDefLabel, self.poisonfourDefLabel)

            self.groundzeroDefText.set(self.groundDefArray[4])
            self.groundquarterDefText.set(self.groundDefArray[3])
            self.groundhalfDefText.set(self.groundDefArray[2])
            self.groundoneDefText.set(len(shell.teamMateNames)-self.groundDefArray[4]-self.groundDefArray[3]-self.groundDefArray[2]-self.groundDefArray[1]-self.groundDefArray[0])
            self.groundtwoDefText.set(self.groundDefArray[1])
            self.groundfourDefText.set(self.groundDefArray[0])
            self.defTypeColor(self.groundDefArray, self.groundzeroDefLabel, self.groundquarterDefLabel, self.groundhalfDefLabel,self.groundtwoDefLabel, self.groundfourDefLabel)

            self.flyingzeroDefText.set(self.flyingDefArray[4])
            self.flyingquarterDefText.set(self.flyingDefArray[3])
            self.flyinghalfDefText.set(self.flyingDefArray[2])
            self.flyingoneDefText.set(len(shell.teamMateNames)-self.flyingDefArray[4]-self.flyingDefArray[3]-self.flyingDefArray[2]-self.flyingDefArray[1]-self.flyingDefArray[0])
            self.flyingtwoDefText.set(self.flyingDefArray[1])
            self.flyingfourDefText.set(self.flyingDefArray[0])
            self.defTypeColor(self.flyingDefArray, self.flyingzeroDefLabel, self.flyingquarterDefLabel, self.flyinghalfDefLabel,self.flyingtwoDefLabel, self.flyingfourDefLabel)

            self.psychiczeroDefText.set(self.psychicDefArray[4])
            self.psychicquarterDefText.set(self.psychicDefArray[3])
            self.psychichalfDefText.set(self.psychicDefArray[2])
            self.psychiconeDefText.set(len(shell.teamMateNames)-self.psychicDefArray[4]-self.psychicDefArray[3]-self.psychicDefArray[2]-self.psychicDefArray[1]-self.psychicDefArray[0])
            self.psychictwoDefText.set(self.psychicDefArray[1])
            self.psychicfourDefText.set(self.psychicDefArray[0])
            self.defTypeColor(self.psychicDefArray, self.psychiczeroDefLabel, self.psychicquarterDefLabel, self.psychichalfDefLabel,self.psychictwoDefLabel, self.psychicfourDefLabel)

            self.bugzeroDefText.set(self.bugDefArray[4])
            self.bugquarterDefText.set(self.bugDefArray[3])
            self.bughalfDefText.set(self.bugDefArray[2])
            self.bugoneDefText.set(len(shell.teamMateNames)-self.bugDefArray[4]-self.bugDefArray[3]-self.bugDefArray[2]-self.bugDefArray[1]-self.bugDefArray[0])
            self.bugtwoDefText.set(self.bugDefArray[1])
            self.bugfourDefText.set(self.bugDefArray[0])
            self.defTypeColor(self.bugDefArray, self.bugzeroDefLabel, self.bugquarterDefLabel, self.bughalfDefLabel,self.bugtwoDefLabel, self.bugfourDefLabel)

            self.rockzeroDefText.set(self.rockDefArray[4])
            self.rockquarterDefText.set(self.rockDefArray[3])
            self.rockhalfDefText.set(self.rockDefArray[2])
            self.rockoneDefText.set(len(shell.teamMateNames)-self.rockDefArray[4]-self.rockDefArray[3]-self.rockDefArray[2]-self.rockDefArray[1]-self.rockDefArray[0])
            self.rocktwoDefText.set(self.rockDefArray[1])
            self.rockfourDefText.set(self.rockDefArray[0])
            self.defTypeColor(self.rockDefArray, self.rockzeroDefLabel, self.rockquarterDefLabel, self.rockhalfDefLabel,self.rocktwoDefLabel, self.rockfourDefLabel)

            self.ghostzeroDefText.set(self.ghostDefArray[4])
            self.ghostquarterDefText.set(self.ghostDefArray[3])
            self.ghosthalfDefText.set(self.ghostDefArray[2])
            self.ghostoneDefText.set(len(shell.teamMateNames)-self.ghostDefArray[4]-self.ghostDefArray[3]-self.ghostDefArray[2]-self.ghostDefArray[1]-self.ghostDefArray[0])
            self.ghosttwoDefText.set(self.ghostDefArray[1])
            self.ghostfourDefText.set(self.ghostDefArray[0])
            self.defTypeColor(self.ghostDefArray, self.ghostzeroDefLabel, self.ghostquarterDefLabel, self.ghosthalfDefLabel,self.ghosttwoDefLabel, self.ghostfourDefLabel)

            self.dragonzeroDefText.set(self.dragonDefArray[4])
            self.dragonquarterDefText.set(self.dragonDefArray[3])
            self.dragonhalfDefText.set(self.dragonDefArray[2])
            self.dragononeDefText.set(len(shell.teamMateNames)-self.dragonDefArray[4]-self.dragonDefArray[3]-self.dragonDefArray[2]-self.dragonDefArray[1]-self.dragonDefArray[0])
            self.dragontwoDefText.set(self.dragonDefArray[1])
            self.dragonfourDefText.set(self.dragonDefArray[0])
            self.defTypeColor(self.dragonDefArray, self.dragonzeroDefLabel, self.dragonquarterDefLabel, self.dragonhalfDefLabel,self.dragontwoDefLabel, self.dragonfourDefLabel)

            self.darkzeroDefText.set(self.darkDefArray[4])
            self.darkquarterDefText.set(self.darkDefArray[3])
            self.darkhalfDefText.set(self.darkDefArray[2])
            self.darkoneDefText.set(len(shell.teamMateNames)-self.darkDefArray[4]-self.darkDefArray[3]-self.darkDefArray[2]-self.darkDefArray[1]-self.darkDefArray[0])
            self.darktwoDefText.set(self.darkDefArray[1])
            self.darkfourDefText.set(self.darkDefArray[0])
            self.defTypeColor(self.darkDefArray, self.darkzeroDefLabel, self.darkquarterDefLabel, self.darkhalfDefLabel,self.darktwoDefLabel, self.darkfourDefLabel)

            self.steelzeroDefText.set(self.steelDefArray[4])
            self.steelquarterDefText.set(self.steelDefArray[3])
            self.steelhalfDefText.set(self.steelDefArray[2])
            self.steeloneDefText.set(len(shell.teamMateNames)-self.steelDefArray[4]-self.steelDefArray[3]-self.steelDefArray[2]-self.steelDefArray[1]-self.steelDefArray[0])
            self.steeltwoDefText.set(self.steelDefArray[1])
            self.steelfourDefText.set(self.steelDefArray[0])
            self.defTypeColor(self.steelDefArray, self.steelzeroDefLabel, self.steelquarterDefLabel, self.steelhalfDefLabel,self.steeltwoDefLabel, self.steelfourDefLabel)

            self.fairyzeroDefText.set(self.fairyDefArray[4])
            self.fairyquarterDefText.set(self.fairyDefArray[3])
            self.fairyhalfDefText.set(self.fairyDefArray[2])
            self.fairyoneDefText.set(len(shell.teamMateNames)-self.fairyDefArray[4]-self.fairyDefArray[3]-self.fairyDefArray[2]-self.fairyDefArray[1]-self.fairyDefArray[0])
            self.fairytwoDefText.set(self.fairyDefArray[1])
            self.fairyfourDefText.set(self.fairyDefArray[0])
            self.defTypeColor(self.fairyDefArray, self.fairyzeroDefLabel, self.fairyquarterDefLabel, self.fairyhalfDefLabel,self.fairytwoDefLabel, self.fairyfourDefLabel)

        elif option=="moves":
            self.normalOffArray = [0,0,0]
            self.fireOffArray = [0,0,0]
            self.waterOffArray = [0,0,0]
            self.electricOffArray = [0,0,0]
            self.grassOffArray = [0,0,0]
            self.iceOffArray = [0,0,0]
            self.fightingOffArray = [0,0,0]
            self.poisonOffArray = [0,0,0]
            self.groundOffArray = [0,0,0]
            self.flyingOffArray = [0,0,0]
            self.psychicOffArray = [0,0,0]
            self.bugOffArray = [0,0,0]
            self.rockOffArray = [0,0,0]
            self.ghostOffArray = [0,0,0]
            self.dragonOffArray = [0,0,0]
            self.darkOffArray = [0,0,0]
            self.steelOffArray = [0,0,0]
            self.fairyOffArray = [0,0,0]

            typesDict = Pokedex.loadTypes()

            k=0
            for member in shell.teamMatesDict:
                for move in shell.teamMatesDict[member]["moves"]:
                    if shell.teamMatesDict[member]["moves"][move] != None and Pokedex.findMoveCategory(shell.teamMatesDict[member]["moves"][move])!="Status":
                        k+=1
                        type = Pokedex.findMoveType(shell.teamMatesDict[member]["moves"][move])
                        se = typesDict[type]["superEffective"]
                        for seType in se:
                            if seType == "Normal":
                                self.normalOffArray[0]+=1
                            elif seType == "Fire":
                                self.fireOffArray[0]+=1
                            elif seType == "Water":
                                self.waterOffArray[0]+=1
                            elif seType == "Electric":
                                self.electricOffArray[0]+=1
                            elif seType == "Grass":
                                self.grassOffArray[0]+=1
                            elif seType == "Ice":
                                self.iceOffArray[0]+=1
                            elif seType == "Fighting":
                                self.fightingOffArray[0]+=1
                            elif seType == "Poison":
                                self.poisonOffArray[0]+=1
                            elif seType == "Ground":
                                self.groundOffArray[0]+=1
                            elif seType == "Flying":
                                self.flyingOffArray[0]+=1
                            elif seType == "Psychic":
                                self.psychicOffArray[0]+=1
                            elif seType == "Bug":
                                self.bugOffArray[0]+=1
                            elif seType == "Rock":
                                self.rockOffArray[0]+=1
                            elif seType == "Ghost":
                                self.ghostOffArray[0]+=1
                            elif seType == "Dragon":
                                self.dragonOffArray[0]+=1
                            elif seType == "Dark":
                                self.darkOffArray[0]+=1
                            elif seType == "Steel":
                                self.steelOffArray[0]+=1
                            elif seType == "Fairy":
                                self.fairyOffArray[0]+=1
                            elif seType == "":
                                pass
                            else:
                                print("An error occurred when registering Super Effectivenesses")
                        nve = typesDict[type]["notVeryEffective"]
                        for nveType in nve:
                            if nveType == "Normal":
                                self.normalOffArray[1]+=1
                            elif nveType == "Fire":
                                self.fireOffArray[1]+=1
                            elif nveType == "Water":
                                self.waterOffArray[1]+=1
                            elif nveType == "Electric":
                                self.electricOffArray[1]+=1
                            elif nveType == "Grass":
                                self.grassOffArray[1]+=1
                            elif nveType == "Ice":
                                self.iceOffArray[1]+=1
                            elif nveType == "Fighting":
                                self.fightingOffArray[1]+=1
                            elif nveType == "Poison":
                                self.poisonOffArray[1]+=1
                            elif nveType == "Ground":
                                self.groundOffArray[1]+=1
                            elif nveType == "Flying":
                                self.flyingOffArray[1]+=1
                            elif nveType == "Psychic":
                                self.psychicOffArray[1]+=1
                            elif nveType == "Bug":
                                self.bugOffArray[1]+=1
                            elif nveType == "Rock":
                                self.rockOffArray[1]+=1
                            elif nveType == "Ghost":
                                self.ghostOffArray[1]+=1
                            elif nveType == "Dragon":
                                self.dragonOffArray[1]+=1
                            elif nveType == "Dark":
                                self.darkOffArray[1]+=1
                            elif nveType == "Steel":
                                self.steelOffArray[1]+=1
                            elif nveType == "Fairy":
                                self.fairyOffArray[1]+=1
                            elif nveType == "":
                                pass
                            else:
                                print("An error occurred when registering Not-Very-Effectivenesses")
                        ne = typesDict[type]["notEffective"]
                        for neType in ne:
                            if neType == "Normal":
                                self.normalOffArray[2]+=1
                            elif neType == "Fire":
                                self.fireOffArray[2]+=1
                            elif neType == "Water":
                                self.waterOffArray[2]+=1
                            elif neType == "Electric":
                                self.electricOffArray[2]+=1
                            elif neType == "Grass":
                                self.grassOffArray[2]+=1
                            elif neType == "Ice":
                                self.iceOffArray[2]+=1
                            elif neType == "Fighting":
                                self.fightingOffArray[2]+=1
                            elif neType == "Poison":
                                self.poisonOffArray[2]+=1
                            elif neType == "Ground":
                                self.groundOffArray[2]+=1
                            elif neType == "Flying":
                                self.flyingOffArray[2]+=1
                            elif neType == "Psychic":
                                self.psychicOffArray[2]+=1
                            elif neType == "Bug":
                                self.bugOffArray[2]+=1
                            elif neType == "Rock":
                                self.rockOffArray[2]+=1
                            elif neType == "Ghost":
                                self.ghostOffArray[2]+=1
                            elif neType == "Dragon":
                                self.dragonOffArray[2]+=1
                            elif neType == "Dark":
                                self.darkOffArray[2]+=1
                            elif neType == "Steel":
                                self.steelOffArray[2]+=1
                            elif neType == "Fairy":
                                self.fairyOffArray[2]+=1
                            elif neType == "":
                                pass
                            else:
                                print("An error occurred when registering No-Effectivenesses")

            self.normalzeroOffText.set(self.normalOffArray[2])
            self.normalhalfOffText.set(self.normalOffArray[1])
            self.normaloneOffText.set(k-self.normalOffArray[2]-self.normalOffArray[1]-self.normalOffArray[0])
            self.normaltwoOffText.set(self.normalOffArray[0])
            self.offTypeColor(self.normalOffArray,k,self.normalzeroOffLabel,self.normalhalfOffLabel,self.normaltwoOffLabel)

            self.firezeroOffText.set(self.fireOffArray[2])
            self.firehalfOffText.set(self.fireOffArray[1])
            self.fireoneOffText.set(k-self.fireOffArray[2]-self.fireOffArray[1]-self.fireOffArray[0])
            self.firetwoOffText.set(self.fireOffArray[0])
            self.offTypeColor(self.fireOffArray, k, self.firezeroOffLabel, self.firehalfOffLabel, self.firetwoOffLabel)

            self.waterzeroOffText.set(self.waterOffArray[2])
            self.waterhalfOffText.set(self.waterOffArray[1])
            self.wateroneOffText.set(k-self.waterOffArray[2]-self.waterOffArray[1]-self.waterOffArray[0])
            self.watertwoOffText.set(self.waterOffArray[0])
            self.offTypeColor(self.waterOffArray, k, self.waterzeroOffLabel, self.waterhalfOffLabel, self.watertwoOffLabel)

            self.electriczeroOffText.set(self.electricOffArray[2])
            self.electrichalfOffText.set(self.electricOffArray[1])
            self.electriconeOffText.set(k-self.electricOffArray[2]-self.electricOffArray[1]-self.electricOffArray[0])
            self.electrictwoOffText.set(self.electricOffArray[0])
            self.offTypeColor(self.electricOffArray, k, self.electriczeroOffLabel, self.electrichalfOffLabel, self.electrictwoOffLabel)

            self.grasszeroOffText.set(self.grassOffArray[2])
            self.grasshalfOffText.set(self.grassOffArray[1])
            self.grassoneOffText.set(k-self.grassOffArray[2]-self.grassOffArray[1]-self.grassOffArray[0])
            self.grasstwoOffText.set(self.grassOffArray[0])
            self.offTypeColor(self.grassOffArray, k, self.grasszeroOffLabel, self.grasshalfOffLabel, self.grasstwoOffLabel)

            self.icezeroOffText.set(self.iceOffArray[2])
            self.icehalfOffText.set(self.iceOffArray[1])
            self.iceoneOffText.set(k-self.iceOffArray[2]-self.iceOffArray[1]-self.iceOffArray[0])
            self.icetwoOffText.set(self.iceOffArray[0])
            self.offTypeColor(self.iceOffArray, k, self.icezeroOffLabel, self.icehalfOffLabel, self.icetwoOffLabel)

            self.fightingzeroOffText.set(self.fightingOffArray[2])
            self.fightinghalfOffText.set(self.fightingOffArray[1])
            self.fightingoneOffText.set(k-self.fightingOffArray[2]-self.fightingOffArray[1]-self.fightingOffArray[0])
            self.fightingtwoOffText.set(self.fightingOffArray[0])
            self.offTypeColor(self.fightingOffArray, k, self.fightingzeroOffLabel, self.fightinghalfOffLabel, self.fightingtwoOffLabel)

            self.poisonzeroOffText.set(self.poisonOffArray[2])
            self.poisonhalfOffText.set(self.poisonOffArray[1])
            self.poisononeOffText.set(k-self.poisonOffArray[2]-self.poisonOffArray[1]-self.poisonOffArray[0])
            self.poisontwoOffText.set(self.poisonOffArray[0])
            self.offTypeColor(self.poisonOffArray, k, self.poisonzeroOffLabel, self.poisonhalfOffLabel, self.poisontwoOffLabel)

            self.groundzeroOffText.set(self.groundOffArray[2])
            self.groundhalfOffText.set(self.groundOffArray[1])
            self.groundoneOffText.set(k-self.groundOffArray[2]-self.groundOffArray[1]-self.groundOffArray[0])
            self.groundtwoOffText.set(self.groundOffArray[0])
            self.offTypeColor(self.groundOffArray, k, self.groundzeroOffLabel, self.groundhalfOffLabel, self.groundtwoOffLabel)

            self.flyingzeroOffText.set(self.flyingOffArray[2])
            self.flyinghalfOffText.set(self.flyingOffArray[1])
            self.flyingoneOffText.set(k-self.flyingOffArray[2]-self.flyingOffArray[1]-self.flyingOffArray[0])
            self.flyingtwoOffText.set(self.flyingOffArray[0])
            self.offTypeColor(self.flyingOffArray, k, self.flyingzeroOffLabel, self.flyinghalfOffLabel, self.flyingtwoOffLabel)

            self.psychiczeroOffText.set(self.psychicOffArray[2])
            self.psychichalfOffText.set(self.psychicOffArray[1])
            self.psychiconeOffText.set(k-self.psychicOffArray[2]-self.psychicOffArray[1]-self.psychicOffArray[0])
            self.psychictwoOffText.set(self.psychicOffArray[0])
            self.offTypeColor(self.psychicOffArray, k, self.psychiczeroOffLabel, self.psychichalfOffLabel, self.psychictwoOffLabel)

            self.bugzeroOffText.set(self.bugOffArray[2])
            self.bughalfOffText.set(self.bugOffArray[1])
            self.bugoneOffText.set(k-self.bugOffArray[2]-self.bugOffArray[1]-self.bugOffArray[0])
            self.bugtwoOffText.set(self.bugOffArray[0])
            self.offTypeColor(self.bugOffArray, k, self.bugzeroOffLabel, self.bughalfOffLabel, self.bugtwoOffLabel)

            self.rockzeroOffText.set(self.rockOffArray[2])
            self.rockhalfOffText.set(self.rockOffArray[1])
            self.rockoneOffText.set(k-self.rockOffArray[2]-self.rockOffArray[1]-self.rockOffArray[0])
            self.rocktwoOffText.set(self.rockOffArray[0])
            self.offTypeColor(self.rockOffArray, k, self.rockzeroOffLabel, self.rockhalfOffLabel, self.rocktwoOffLabel)

            self.ghostzeroOffText.set(self.ghostOffArray[2])
            self.ghosthalfOffText.set(self.ghostOffArray[1])
            self.ghostoneOffText.set(k-self.ghostOffArray[2]-self.ghostOffArray[1]-self.ghostOffArray[0])
            self.ghosttwoOffText.set(self.ghostOffArray[0])
            self.offTypeColor(self.ghostOffArray, k, self.ghostzeroOffLabel, self.ghosthalfOffLabel, self.ghosttwoOffLabel)

            self.dragonzeroOffText.set(self.dragonOffArray[2])
            self.dragonhalfOffText.set(self.dragonOffArray[1])
            self.dragononeOffText.set(k-self.dragonOffArray[2]-self.dragonOffArray[1]-self.dragonOffArray[0])
            self.dragontwoOffText.set(self.dragonOffArray[0])
            self.offTypeColor(self.dragonOffArray, k, self.dragonzeroOffLabel, self.dragonhalfOffLabel, self.dragontwoOffLabel)

            self.darkzeroOffText.set(self.darkOffArray[2])
            self.darkhalfOffText.set(self.darkOffArray[1])
            self.darkoneOffText.set(k-self.darkOffArray[2]-self.darkOffArray[1]-self.darkOffArray[0])
            self.darktwoOffText.set(self.darkOffArray[0])
            self.offTypeColor(self.darkOffArray, k, self.darkzeroOffLabel, self.darkhalfOffLabel, self.darktwoOffLabel)

            self.steelzeroOffText.set(self.steelOffArray[2])
            self.steelhalfOffText.set(self.steelOffArray[1])
            self.steeloneOffText.set(k-self.steelOffArray[2]-self.steelOffArray[1]-self.steelOffArray[0])
            self.steeltwoOffText.set(self.steelOffArray[0])
            self.offTypeColor(self.steelOffArray, k, self.steelzeroOffLabel, self.steelhalfOffLabel, self.steeltwoOffLabel)

            self.fairyzeroOffText.set(self.fairyOffArray[2])
            self.fairyhalfOffText.set(self.fairyOffArray[1])
            self.fairyoneOffText.set(k-self.fairyOffArray[2]-self.fairyOffArray[1]-self.fairyOffArray[0])
            self.fairytwoOffText.set(self.fairyOffArray[0])
            self.offTypeColor(self.fairyOffArray, k, self.fairyzeroOffLabel, self.fairyhalfOffLabel, self.fairytwoOffLabel)

        elif option=="stats":
            scale=150/714
            self.sumStats = [0,0,0,0,0,0]
            if any(shell.teamMatesDict):
                for member in shell.teamMatesDict:
                    self.sumStats[0] += shell.hpStatCalc(shell.teamMatesDict[member]["baseStats"]["hp"],shell.teamMatesDict[member]["evs"]["hp"],shell.teamMatesDict[member]["ivs"]["hp"],shell.teamMatesDict[member]["level"])
                    self.sumStats[1] += shell.atkStatCalc(shell.teamMatesDict[member]["baseStats"]["atk"],shell.teamMatesDict[member]["evs"]["atk"],shell.teamMatesDict[member]["ivs"]["atk"],shell.teamMatesDict[member]["level"],shell.teamMatesDict[member]["nature"])
                    self.sumStats[2] += shell.defStatCalc(shell.teamMatesDict[member]["baseStats"]["def"],shell.teamMatesDict[member]["evs"]["def"],shell.teamMatesDict[member]["ivs"]["def"],shell.teamMatesDict[member]["level"],shell.teamMatesDict[member]["nature"])
                    self.sumStats[3] += shell.spaStatCalc(shell.teamMatesDict[member]["baseStats"]["spa"],shell.teamMatesDict[member]["evs"]["spa"],shell.teamMatesDict[member]["ivs"]["spa"],shell.teamMatesDict[member]["level"],shell.teamMatesDict[member]["nature"])
                    self.sumStats[4] += shell.spdStatCalc(shell.teamMatesDict[member]["baseStats"]["spd"],shell.teamMatesDict[member]["evs"]["spd"],shell.teamMatesDict[member]["ivs"]["spd"],shell.teamMatesDict[member]["level"],shell.teamMatesDict[member]["nature"])
                    self.sumStats[5] += shell.speStatCalc(shell.teamMatesDict[member]["baseStats"]["spe"],shell.teamMatesDict[member]["evs"]["spe"],shell.teamMatesDict[member]["ivs"]["spe"],shell.teamMatesDict[member]["level"],shell.teamMatesDict[member]["nature"])

                self.averageHPCanvas.coords(self.avHPBar, 0, 0, int(self.sumStats[0] / len(shell.teamMatesDict) * scale), 20)
                self.avHP.set(int(self.sumStats[0] / len(shell.teamMatesDict)))
                self.averageHPCanvas.itemconfig(self.avHPBar, fill=self.statColor(
                    int(self.sumStats[0] / len(shell.teamMatesDict) * scale), True))

                self.averageAtkCanvas.coords(self.avAtkBar, 0, 0, int(self.sumStats[1] / len(shell.teamMatesDict) * scale),20)
                self.avAtk.set(int(self.sumStats[1] / len(shell.teamMatesDict)))
                self.averageAtkCanvas.itemconfig(self.avAtkBar, fill=self.statColor(
                    int(self.sumStats[1] / len(shell.teamMatesDict) * scale), False))

                self.averageDefCanvas.coords(self.avDefBar, 0, 0, int(self.sumStats[2] / len(shell.teamMatesDict) * scale),20)
                self.avDef.set(int(self.sumStats[2] / len(shell.teamMatesDict)))
                self.averageDefCanvas.itemconfig(self.avDefBar, fill=self.statColor(
                    int(self.sumStats[2] / len(shell.teamMatesDict) * scale), False))

                self.averageSpACanvas.coords(self.avSpABar, 0, 0, int(self.sumStats[3] / len(shell.teamMatesDict) * scale),20)
                self.avSpA.set(int(self.sumStats[3] / len(shell.teamMatesDict)))
                self.averageSpACanvas.itemconfig(self.avSpABar, fill=self.statColor(
                    int(self.sumStats[3] / len(shell.teamMatesDict) * scale), False))

                self.averageSpDCanvas.coords(self.avSpDBar, 0, 0, int(self.sumStats[4] / len(shell.teamMatesDict) * scale),20)
                self.avSpD.set(int(self.sumStats[4] / len(shell.teamMatesDict)))
                self.averageSpDCanvas.itemconfig(self.avSpDBar, fill=self.statColor(
                    int(self.sumStats[4] / len(shell.teamMatesDict) * scale), False))

                self.averageSpeCanvas.coords(self.avSpeBar, 0, 0, int(self.sumStats[5] / len(shell.teamMatesDict) * scale),20)
                self.avSpe.set(int(self.sumStats[5] / len(shell.teamMatesDict)))
                self.averageSpeCanvas.itemconfig(self.avSpeBar, fill=self.statColor(
                    int(self.sumStats[5] / len(shell.teamMatesDict) * scale), False))
            else:
                for member in shell.teamMateNames:
                    memberBaseStats = Pokedex.findPokemonBaseStats(member)
                    level=100
                    if "vgc" in shell.tier or "battlespot" in shell.tier:
                        level=50
                    self.sumStats[0] += shell.hpStatCalc(memberBaseStats["hp"],0,31,level)
                    self.sumStats[1] += shell.atkStatCalc(memberBaseStats["atk"],0,31,level,"Serious")
                    self.sumStats[2] += shell.defStatCalc(memberBaseStats["def"],0,31,level,"Serious")
                    self.sumStats[3] += shell.spaStatCalc(memberBaseStats["spa"],0,31,level,"Serious")
                    self.sumStats[4] += shell.spdStatCalc(memberBaseStats["spd"],0,31,level,"Serious")
                    self.sumStats[5] += shell.speStatCalc(memberBaseStats["spe"],0,31,level,"Serious")

                self.averageHPCanvas.coords(self.avHPBar, 0, 0, int(self.sumStats[0] / len(shell.teamMateNames) * scale),20)
                self.avHP.set(int(self.sumStats[0] / len(shell.teamMateNames)))
                self.averageHPCanvas.itemconfig(self.avHPBar, fill=self.statColor(
                    int(self.sumStats[0] / len(shell.teamMateNames) * scale), True))

                self.averageAtkCanvas.coords(self.avAtkBar, 0, 0,int(self.sumStats[1] / len(shell.teamMateNames) * scale), 20)
                self.avAtk.set(int(self.sumStats[1] / len(shell.teamMateNames)))
                self.averageAtkCanvas.itemconfig(self.avAtkBar, fill=self.statColor(
                    int(self.sumStats[1] / len(shell.teamMateNames) * scale), False))

                self.averageDefCanvas.coords(self.avDefBar, 0, 0,int(self.sumStats[2] / len(shell.teamMateNames) * scale), 20)
                self.avDef.set(int(self.sumStats[2] / len(shell.teamMateNames)))
                self.averageDefCanvas.itemconfig(self.avDefBar, fill=self.statColor(
                    int(self.sumStats[2] / len(shell.teamMateNames) * scale), False))

                self.averageSpACanvas.coords(self.avSpABar, 0, 0,int(self.sumStats[3] / len(shell.teamMateNames) * scale), 20)
                self.avSpA.set(int(self.sumStats[3] / len(shell.teamMateNames)))
                self.averageSpACanvas.itemconfig(self.avSpABar, fill=self.statColor(
                    int(self.sumStats[3] / len(shell.teamMateNames) * scale), False))

                self.averageSpDCanvas.coords(self.avSpDBar, 0, 0,int(self.sumStats[4] / len(shell.teamMateNames) * scale), 20)
                self.avSpD.set(int(self.sumStats[4] / len(shell.teamMateNames)))
                self.averageSpDCanvas.itemconfig(self.avSpDBar, fill=self.statColor(
                    int(self.sumStats[4] / len(shell.teamMateNames) * scale), False))

                self.averageSpeCanvas.coords(self.avSpeBar, 0, 0,int(self.sumStats[5] / len(shell.teamMateNames) * scale), 20)
                self.avSpe.set(int(self.sumStats[5] / len(shell.teamMateNames)))
                self.averageSpeCanvas.itemconfig(self.avSpeBar, fill=self.statColor(
                    int(self.sumStats[5] / len(shell.teamMateNames) * scale), False))

        elif option=="physpec Offense":
            physSum=0
            specSum=0
            if any(shell.teamMatesDict):
                for member in shell.teamMatesDict:
                    physMoveSum=0
                    specMoveSum=0
                    for move in shell.teamMatesDict[member]["moves"]:
                        if shell.teamMatesDict[member]["moves"][move] != None:
                            cat = Pokedex.findMoveCategory(shell.teamMatesDict[member]["moves"][move])
                            if cat == "Physical":
                                physMoveSum+=Pokedex.findMoveBasePower(shell.teamMatesDict[member]["moves"][move])
                            elif cat == "Special":
                                specMoveSum+=Pokedex.findMoveBasePower(shell.teamMatesDict[member]["moves"][move])
                    if (physMoveSum+specMoveSum)!=0:
                        physSum+=shell.atkStatCalc(shell.teamMatesDict[member]["baseStats"]["atk"],shell.teamMatesDict[member]["evs"]["atk"],shell.teamMatesDict[member]["ivs"]["atk"],shell.teamMatesDict[member]["level"],shell.teamMatesDict[member]["nature"])*physMoveSum/(physMoveSum+specMoveSum)
                        specSum+=shell.spaStatCalc(shell.teamMatesDict[member]["baseStats"]["spa"],shell.teamMatesDict[member]["evs"]["spa"],shell.teamMatesDict[member]["ivs"]["spa"],shell.teamMatesDict[member]["level"],shell.teamMatesDict[member]["nature"])*specMoveSum/(physMoveSum+specMoveSum)
                    else:
                        physSum += shell.atkStatCalc(shell.teamMatesDict[member]["baseStats"]["atk"],shell.teamMatesDict[member]["evs"]["atk"],shell.teamMatesDict[member]["ivs"]["atk"],shell.teamMatesDict[member]["level"],shell.teamMatesDict[member]["nature"])
                        specSum += shell.spaStatCalc(shell.teamMatesDict[member]["baseStats"]["spa"],shell.teamMatesDict[member]["evs"]["spa"],shell.teamMatesDict[member]["ivs"]["spa"],shell.teamMatesDict[member]["level"],shell.teamMatesDict[member]["nature"])

            else:
                for member in shell.teamMateNames:
                    physMoveSum=0
                    specMoveSum=0
                    level=100
                    if "vgc" in shell.tier or "battlespot" in shell.tier:
                        level=50
                    physSum += shell.atkStatCalc(Pokedex.findPokemonBaseStats(member)["atk"],0,31,50,"Serious")
                    specSum += shell.spaStatCalc(Pokedex.findPokemonBaseStats(member)["spa"],0,31,50,"Serious")

            self.offBalance=physSum/(physSum+specSum)*self.physpecOffCanvas.winfo_reqwidth()
            self.physpecOffCanvas.coords(self.physOffBar,0,0,int(self.offBalance),20)
            self.physpecOffCanvas.coords(self.specOffBar,int(self.offBalance),0,self.physpecOffCanvas.winfo_reqwidth(), 20)

        elif option=="physpec Defense":
            physSum = 0
            specSum = 0
            if any(shell.teamMatesDict):
                for member in shell.teamMatesDict:
                    physSum += shell.defStatCalc(shell.teamMatesDict[member]["baseStats"]["def"],shell.teamMatesDict[member]["evs"]["def"],shell.teamMatesDict[member]["ivs"]["def"],shell.teamMatesDict[member]["level"],shell.teamMatesDict[member]["nature"])
                    specSum += shell.spdStatCalc(shell.teamMatesDict[member]["baseStats"]["spd"],shell.teamMatesDict[member]["evs"]["spd"],shell.teamMatesDict[member]["ivs"]["spd"],shell.teamMatesDict[member]["level"],shell.teamMatesDict[member]["nature"])
            else:
                for member in shell.teamMateNames:
                    level = 100
                    if "vgc" in shell.tier or "battlespot" in shell.tier:
                        level=50
                    physSum += shell.defStatCalc(Pokedex.findPokemonBaseStats(member)["def"],0,31,level,"Serious")
                    specSum += shell.spdStatCalc(Pokedex.findPokemonBaseStats(member)["spd"],0,31,level,"Serious")

            self.defBalance = physSum / (physSum + specSum) * self.physpecDefCanvas.winfo_reqwidth()
            self.physpecDefCanvas.coords(self.physOffBar, 0, 0, int(self.defBalance), 20)
            self.physpecDefCanvas.coords(self.specOffBar, int(self.defBalance), 0, self.physpecDefCanvas.winfo_reqwidth(), 20)
            
        elif option=="advice":
            self.adviceMssngr.config(state=NORMAL)
            self.adviceMssngr.delete(1.0, END)
            if len(shell.teamMateNames)>1:
                self.respond("Let's take a look at your team...")

            #Defensive Type Coverage
            if len(shell.teamMateNames)>1:
                self.respond("First, Defensive Type Coverage")
                self.defTypeCoverage(shell)

            if len(shell.teamMatesDict)>0:
                isSunTeam=False
                isHarshSunTeam=False
                isRainTeam=False
                isHarshRainTeam=False
                isHailTeam=False
                isSandTeam=False
                isHarshWindTeam=False

                isTrickRoomTeam=False

                movesTotal=0
                for member in shell.teamMatesDict:
                    if shell.teamMatesDict[member]["ability"] == "Drought":
                        isSunTeam=True
                    elif shell.teamMatesDict[member]["ability"] == "Desolate Land":
                        isHarshSunTeam=True
                    elif shell.teamMatesDict[member]["ability"] == "Drizzle":
                        isRainTeam=True
                    elif shell.teamMatesDict[member]["ability"] == "Primordial Sea":
                        isHarshRainTrue=True
                    elif shell.teamMatesDict[member]["ability"] == "Snow Warning":
                        isHailTeam=True
                    elif shell.teamMatesDict[member]["ability"] == "Sand Stream":
                        isSandTeam=True
                    elif shell.teamMatesDict[member]["ability"] == "Delta Stream":
                        isHarshWindTeam = True
                    for move in shell.teamMatesDict[member]["moves"]:
                        if shell.teamMatesDict[member]["moves"][move]!=None:
                            movesTotal+=1
                            if shell.teamMatesDict[member]["moves"][move]=="Sunny Day":
                                isSunTeam=True
                            elif shell.teamMatesDict[member]["moves"][move]=="Rain Dance":
                                isRainTeam=True
                            elif shell.teamMatesDict[member]["moves"][move]=="Hail":
                                isHailTeam=True
                            elif shell.teamMatesDict[member]["moves"][move]=="Sand Storm":
                                isSandTeam=True
                            elif shell.teamMatesDict[member]["moves"][move]=="Trick Room":
                                isTrickRoomTeam=True
                if movesTotal>=8:
                    #Offensive Type Coverage
                    self.respond("Next, Offensive Type Coverage")
                    self.offTypeCoverage(shell)

                    self.weatherTeamsText(shell,isSunTeam,isHarshSunTeam,isRainTeam,isHarshRainTeam,isHailTeam,isSandTeam,isHarshWindTeam)

                    self.trickRoomTeamText(shell,isTrickRoomTeam)
                if movesTotal>=12:
                    #Entry Hazard Setters and Removers
                    if "doubles" not in shell.tier and "vgc" not in shell.tier:
                        removal = False
                        setter = False
                        for member in shell.teamMatesDict:
                            for m in shell.teamMatesDict[member]["moves"]:
                                if shell.teamMatesDict[member]["moves"][m] in ["Defog", "Rapid Spin"]:
                                    removal = True
                                elif shell.teamMatesDict[member]["moves"][m] in ["Spikes", "Toxic Spikes",
                                                                                 "Stealth Rock", "Sticky Web"]:
                                    setter = True
                        if not removal:
                            self.respond(
                                "Oh, you don't have a Pokemon to remove entry hazards. Entry hazards can hurt your Pokemon everytime they switch in and give your opponent the winning advantage. Consider giving one of your Pokemon the move Defog or Rapid Spin")
                        if not setter:
                            self.respond(
                                "Oh, you don't have a Pokemon to set entry hazards. Entry hazards can damage your opponent's Pokemon everytime they switch in and can give you the winning advatage. Consider giving one of your Pokemon the move Stealth Rock, Spikes, Toxic Spikes, or Sticky Web")

            #Offensive and Defensive Balance
            if len(shell.teamMateNames)>1:
                self.respond("Next, Offensive Balance")
                if self.offBalance<=self.physpecOffCanvas.winfo_reqwidth()*0.2:
                    self.respond("Whoa, your offensive balance is WAY off. Add some physical attackers to your team so that you don't get countered by a specially defensive wall!")
                elif self.offBalance<=self.physpecOffCanvas.winfo_reqwidth()*0.4:
                    self.respond("Mmmmm you seem to be leaning towards the specially offensive side of the spectrum. Depending on your team, this can be fine, but I would still suggest to add a physical attacker.")
                elif self.offBalance<=self.physpecOffCanvas.winfo_reqwidth()*0.6:
                    self.respond("You have some nice offensive balance in this team!")
                elif self.offBalance<=self.physpecOffCanvas.winfo_reqwidth()*0.8:
                    self.respond("Mmmmm you seem to be leaning towards the physically offensive side of the spectrum. Depending on your team, this can be fine, but I would still suggest to add a special attacker.")
                elif self.offBalance<=self.physpecOffCanvas.winfo_reqwidth():
                    self.respond("Whoa, your offensive balance is WAY off. Add some special attackers to your team so that you don't get countered by a physically defensive wall!")

                self.respond("Next, Defensive Balance")
                if self.defBalance<=self.physpecDefCanvas.winfo_reqwidth()*0.2:
                    self.respond("Whoa, your defensive balance is WAY off. Add some physical defenders to your team so that you don't get swept by a specially offensive sweeper!")
                elif self.defBalance<=self.physpecDefCanvas.winfo_reqwidth()*0.4:
                    self.respond("Mmmmm you seem to be leaning towards the specially defensive side of the spectrum. Depending on your team, this can be fine, but I would still suggest to add a physical defender.")
                elif self.defBalance<=self.physpecDefCanvas.winfo_reqwidth()*0.6:
                    self.respond("You have some nice defensive balance in this team!")
                elif self.defBalance<=self.physpecDefCanvas.winfo_reqwidth()*0.8:
                    self.respond("Mmmmm you seem to be leaning towards the physically defensive side of the spectrum. Depending on your team, this can be fine, but I would still suggest to add a special defender.")
                elif self.defBalance<=self.physpecDefCanvas.winfo_reqwidth():
                    self.respond("Whoa, your defensive balance is WAY off. Add some special defender to your team so that you don't get swept by a physically offensive sweeper!")
                self.respond("")

            # Average Team Stats
            #if len(shell.teamMatesDict)>1:
            #    self.respond(
            #        "Now for the team's average stats\nPlease note that I am excluding boosts from items, abilities, and/or moves.")
            #    sumTotal = sum(self.sumStats)
            #    if (self.sumStats[1]+self.sumStats[3]+self.sumStats[5])/sumTotal>=0.66:
            #        self.respond("It seems that you're going for a Hyper Offensive team. In other words, you are currently focussing on hitting hard and fast.")
            #    elif 0.152<=self.sumStats[1]/sumTotal<=0.184 and 0.152<=self.sumStats[2]/sumTotal<=0.184 and 0.152<=self.sumStats[3]/sumTotal<=0.184 and 0.152<=self.sumStats[4]/sumTotal<=0.184 and 0.152<=self.sumStats[5]/sumTotal<=0.184:
            #        self.respond("It seems that you're going for a Balanced Team. In other words, you are currently focussing on finding a balance between offense and defense.")
            #    elif (self.sumStats[0]+self.sumStats[2]+self.sumStats[4])/sumTotal>=0.75:
            #        self.respond("It seems that you're going for a stall team. In other words, you are currently focussing on outlasting the opponent through high defenses and status conditions.")
            #    self.respond("")

    def __init__(self,toplevel):
        self.toplevel=toplevel
        self.toplevel.geometry("872x700")
        self.toplevel.title("Team Analyzer")
        offCovFrame = Frame(self.toplevel)
        offCovFrame.pack(side=LEFT,fill=Y)
        Label(offCovFrame, text="Offensive Coverage").grid(row=0, column=0, columnspan=11,sticky=EW)
        ttk.Separator(offCovFrame, orient=HORIZONTAL).grid(row=1, column=3, columnspan=7, sticky=EW)
        ttk.Separator(offCovFrame, orient=HORIZONTAL).grid(row=3, column=1, columnspan=10, sticky=EW)
        ttk.Separator(offCovFrame, orient=HORIZONTAL).grid(row=22, column=1, columnspan=10, sticky=EW)
        ttk.Separator(offCovFrame, orient=VERTICAL).grid(row=4, column=0, rowspan=18, sticky=NS, padx=(10,0))
        ttk.Separator(offCovFrame, orient=VERTICAL).grid(row=2, column=2, rowspan=20, sticky=NS)
        ttk.Separator(offCovFrame, orient=VERTICAL).grid(row=2, column=4, rowspan=20, sticky=NS)
        ttk.Separator(offCovFrame, orient=VERTICAL).grid(row=2, column=6, rowspan=20, sticky=NS)
        ttk.Separator(offCovFrame, orient=VERTICAL).grid(row=2, column=8, rowspan=20, sticky=NS)
        ttk.Separator(offCovFrame, orient=VERTICAL).grid(row=2, column=10, rowspan=20, sticky=NS)

        Label(offCovFrame, text="0").grid(row=2, column=3, padx=10)
        Label(offCovFrame, text="1/2").grid(row=2, column=5, padx=5)
        Label(offCovFrame, text="1").grid(row=2, column=7, padx=10)
        Label(offCovFrame, text="2").grid(row=2, column=9, padx=10)

        Label(offCovFrame, text="Normal", anchor=W).grid(row=4, column=1, pady=1)
        self.normalzeroOffText = StringVar()
        self.normalzeroOffText.set("0")
        self.normalzeroOffLabel=Label(offCovFrame, textvariable=self.normalzeroOffText, anchor=W)
        self.normalzeroOffLabel.grid(row=4, column=3)
        self.normalhalfOffText = StringVar()
        self.normalhalfOffText.set("0")
        self.normalhalfOffLabel=Label(offCovFrame, textvariable=self.normalhalfOffText, anchor=W)
        self.normalhalfOffLabel.grid(row=4, column=5)
        self.normaloneOffText = StringVar()
        self.normaloneOffText.set("0")
        Label(offCovFrame, textvariable=self.normaloneOffText, anchor=W).grid(row=4, column=7)
        self.normaltwoOffText = StringVar()
        self.normaltwoOffText.set("0")
        self.normaltwoOffLabel=Label(offCovFrame, textvariable=self.normaltwoOffText, anchor=W)
        self.normaltwoOffLabel.grid(row=4, column=9)

        Label(offCovFrame, text="Fire", anchor=W).grid(row=5, column=1, pady=1)
        self.firezeroOffText = StringVar()
        self.firezeroOffText.set("0")
        self.firezeroOffLabel=Label(offCovFrame, textvariable=self.firezeroOffText, anchor=W)
        self.firezeroOffLabel.grid(row=5, column=3)
        self.firehalfOffText = StringVar()
        self.firehalfOffText.set("0")
        self.firehalfOffLabel=Label(offCovFrame, textvariable=self.firehalfOffText, anchor=W)
        self.firehalfOffLabel.grid(row=5, column=5)
        self.fireoneOffText = StringVar()
        self.fireoneOffText.set("0")
        Label(offCovFrame, textvariable=self.fireoneOffText, anchor=W).grid(row=5, column=7)
        self.firetwoOffText = StringVar()
        self.firetwoOffText.set("0")
        self.firetwoOffLabel=Label(offCovFrame, textvariable=self.firetwoOffText, anchor=W)
        self.firetwoOffLabel.grid(row=5, column=9)

        Label(offCovFrame, text="Water", anchor=W).grid(row=6, column=1, pady=1)
        self.waterzeroOffText = StringVar()
        self.waterzeroOffText.set("0")
        self.waterzeroOffLabel=Label(offCovFrame, textvariable=self.waterzeroOffText, anchor=W)
        self.waterzeroOffLabel.grid(row=6, column=3)
        self.waterhalfOffText = StringVar()
        self.waterhalfOffText.set("0")
        self.waterhalfOffLabel=Label(offCovFrame, textvariable=self.waterhalfOffText, anchor=W)
        self.waterhalfOffLabel.grid(row=6, column=5)
        self.wateroneOffText = StringVar()
        self.wateroneOffText.set("0")
        Label(offCovFrame, textvariable=self.wateroneOffText, anchor=W).grid(row=6, column=7)
        self.watertwoOffText = StringVar()
        self.watertwoOffText.set("0")
        self.watertwoOffLabel=Label(offCovFrame, textvariable=self.watertwoOffText, anchor=W)
        self.watertwoOffLabel.grid(row=6, column=9)

        Label(offCovFrame, text="Electric", anchor=W).grid(row=7, column=1, pady=1)
        self.electriczeroOffText = StringVar()
        self.electriczeroOffText.set("0")
        self.electriczeroOffLabel=Label(offCovFrame, textvariable=self.electriczeroOffText, anchor=W)
        self.electriczeroOffLabel.grid(row=7, column=3)
        self.electrichalfOffText = StringVar()
        self.electrichalfOffText.set("0")
        self.electrichalfOffLabel=Label(offCovFrame, textvariable=self.electrichalfOffText, anchor=W)
        self.electrichalfOffLabel.grid(row=7, column=5)
        self.electriconeOffText = StringVar()
        self.electriconeOffText.set("0")
        Label(offCovFrame, textvariable=self.electriconeOffText, anchor=W).grid(row=7, column=7)
        self.electrictwoOffText = StringVar()
        self.electrictwoOffText.set("0")
        self.electrictwoOffLabel=Label(offCovFrame, textvariable=self.electrictwoOffText, anchor=W)
        self.electrictwoOffLabel.grid(row=7, column=9)

        Label(offCovFrame, text="Grass", anchor=W).grid(row=8, column=1, pady=1)
        self.grasszeroOffText = StringVar()
        self.grasszeroOffText.set("0")
        self.grasszeroOffLabel=Label(offCovFrame, textvariable=self.grasszeroOffText, anchor=W)
        self.grasszeroOffLabel.grid(row=8, column=3)
        self.grasshalfOffText = StringVar()
        self.grasshalfOffText.set("0")
        self.grasshalfOffLabel=Label(offCovFrame, textvariable=self.grasshalfOffText, anchor=W)
        self.grasshalfOffLabel.grid(row=8, column=5)
        self.grassoneOffText = StringVar()
        self.grassoneOffText.set("0")
        Label(offCovFrame, textvariable=self.grassoneOffText, anchor=W).grid(row=8, column=7)
        self.grasstwoOffText = StringVar()
        self.grasstwoOffText.set("0")
        self.grasstwoOffLabel=Label(offCovFrame, textvariable=self.grasstwoOffText, anchor=W)
        self.grasstwoOffLabel.grid(row=8, column=9)

        Label(offCovFrame, text="Ice", anchor=W).grid(row=9, column=1, pady=1)
        self.icezeroOffText = StringVar()
        self.icezeroOffText.set("0")
        self.icezeroOffLabel=Label(offCovFrame, textvariable=self.icezeroOffText, anchor=W)
        self.icezeroOffLabel.grid(row=9, column=3)
        self.icehalfOffText = StringVar()
        self.icehalfOffText.set("0")
        self.icehalfOffLabel=Label(offCovFrame, textvariable=self.icehalfOffText, anchor=W)
        self.icehalfOffLabel.grid(row=9, column=5)
        self.iceoneOffText = StringVar()
        self.iceoneOffText.set("0")
        Label(offCovFrame, textvariable=self.iceoneOffText, anchor=W).grid(row=9, column=7)
        self.icetwoOffText = StringVar()
        self.icetwoOffText.set("0")
        self.icetwoOffLabel=Label(offCovFrame, textvariable=self.icetwoOffText, anchor=W)
        self.icetwoOffLabel.grid(row=9, column=9)

        Label(offCovFrame, text="Fighting", anchor=W).grid(row=10, column=1, pady=1)
        self.fightingzeroOffText = StringVar()
        self.fightingzeroOffText.set("0")
        self.fightingzeroOffLabel=Label(offCovFrame, textvariable=self.fightingzeroOffText, anchor=W)
        self.fightingzeroOffLabel.grid(row=10, column=3)
        self.fightinghalfOffText = StringVar()
        self.fightinghalfOffText.set("0")
        self.fightinghalfOffLabel=Label(offCovFrame, textvariable=self.fightinghalfOffText, anchor=W)
        self.fightinghalfOffLabel.grid(row=10, column=5)
        self.fightingoneOffText = StringVar()
        self.fightingoneOffText.set("0")
        Label(offCovFrame, textvariable=self.fightingoneOffText, anchor=W).grid(row=10, column=7)
        self.fightingtwoOffText = StringVar()
        self.fightingtwoOffText.set("0")
        self.fightingtwoOffLabel=Label(offCovFrame, textvariable=self.fightingtwoOffText, anchor=W)
        self.fightingtwoOffLabel.grid(row=10, column=9)

        Label(offCovFrame, text="Poison", anchor=W).grid(row=11, column=1, pady=1)
        self.poisonzeroOffText = StringVar()
        self.poisonzeroOffText.set("0")
        self.poisonzeroOffLabel=Label(offCovFrame, textvariable=self.poisonzeroOffText, anchor=W)
        self.poisonzeroOffLabel.grid(row=11, column=3)
        self.poisonhalfOffText = StringVar()
        self.poisonhalfOffText.set("0")
        self.poisonhalfOffLabel=Label(offCovFrame, textvariable=self.poisonhalfOffText, anchor=W)
        self.poisonhalfOffLabel.grid(row=11, column=5)
        self.poisononeOffText = StringVar()
        self.poisononeOffText.set("0")
        Label(offCovFrame, textvariable=self.poisononeOffText, anchor=W).grid(row=11, column=7)
        self.poisontwoOffText = StringVar()
        self.poisontwoOffText.set("0")
        self.poisontwoOffLabel=Label(offCovFrame, textvariable=self.poisontwoOffText, anchor=W)
        self.poisontwoOffLabel.grid(row=11, column=9)

        Label(offCovFrame, text="Ground", anchor=W).grid(row=12, column=1, pady=1)
        self.groundzeroOffText = StringVar()
        self.groundzeroOffText.set("0")
        self.groundzeroOffLabel=Label(offCovFrame, textvariable=self.groundzeroOffText, anchor=W)
        self.groundzeroOffLabel.grid(row=12, column=3)
        self.groundhalfOffText = StringVar()
        self.groundhalfOffText.set("0")
        self.groundhalfOffLabel=Label(offCovFrame, textvariable=self.groundhalfOffText, anchor=W)
        self.groundhalfOffLabel.grid(row=12, column=5)
        self.groundoneOffText = StringVar()
        self.groundoneOffText.set("0")
        Label(offCovFrame, textvariable=self.groundoneOffText, anchor=W).grid(row=12, column=7)
        self.groundtwoOffText = StringVar()
        self.groundtwoOffText.set("0")
        self.groundtwoOffLabel=Label(offCovFrame, textvariable=self.groundtwoOffText, anchor=W)
        self.groundtwoOffLabel.grid(row=12, column=9)

        Label(offCovFrame, text="Flying", anchor=W).grid(row=13, column=1, pady=1)
        self.flyingzeroOffText = StringVar()
        self.flyingzeroOffText.set("0")
        self.flyingzeroOffLabel=Label(offCovFrame, textvariable=self.flyingzeroOffText, anchor=W)
        self.flyingzeroOffLabel.grid(row=13, column=3)
        self.flyinghalfOffText = StringVar()
        self.flyinghalfOffText.set("0")
        self.flyinghalfOffLabel=Label(offCovFrame, textvariable=self.flyinghalfOffText, anchor=W)
        self.flyinghalfOffLabel.grid(row=13, column=5)
        self.flyingoneOffText = StringVar()
        self.flyingoneOffText.set("0")
        Label(offCovFrame, textvariable=self.flyingoneOffText, anchor=W).grid(row=13, column=7)
        self.flyingtwoOffText = StringVar()
        self.flyingtwoOffText.set("0")
        self.flyingtwoOffLabel=Label(offCovFrame, textvariable=self.flyingtwoOffText, anchor=W)
        self.flyingtwoOffLabel.grid(row=13, column=9)

        Label(offCovFrame, text="Psychic", anchor=W).grid(row=14, column=1, pady=1)
        self.psychiczeroOffText = StringVar()
        self.psychiczeroOffText.set("0")
        self.psychiczeroOffLabel=Label(offCovFrame, textvariable=self.psychiczeroOffText, anchor=W)
        self.psychiczeroOffLabel.grid(row=14, column=3)
        self.psychichalfOffText = StringVar()
        self.psychichalfOffText.set("0")
        self.psychichalfOffLabel=Label(offCovFrame, textvariable=self.psychichalfOffText, anchor=W)
        self.psychichalfOffLabel.grid(row=14, column=5)
        self.psychiconeOffText = StringVar()
        self.psychiconeOffText.set("0")
        Label(offCovFrame, textvariable=self.psychiconeOffText, anchor=W).grid(row=14, column=7)
        self.psychictwoOffText = StringVar()
        self.psychictwoOffText.set("0")
        self.psychictwoOffLabel=Label(offCovFrame, textvariable=self.psychictwoOffText, anchor=W)
        self.psychictwoOffLabel.grid(row=14, column=9)

        Label(offCovFrame, text="Bug", anchor=W).grid(row=15, column=1, pady=1)
        self.bugzeroOffText = StringVar()
        self.bugzeroOffText.set("0")
        self.bugzeroOffLabel=Label(offCovFrame, textvariable=self.bugzeroOffText, anchor=W)
        self.bugzeroOffLabel.grid(row=15, column=3)
        self.bughalfOffText = StringVar()
        self.bughalfOffText.set("0")
        self.bughalfOffLabel=Label(offCovFrame, textvariable=self.bughalfOffText, anchor=W)
        self.bughalfOffLabel.grid(row=15, column=5)
        self.bugoneOffText = StringVar()
        self.bugoneOffText.set("0")
        Label(offCovFrame, textvariable=self.bugoneOffText, anchor=W).grid(row=15, column=7)
        self.bugtwoOffText = StringVar()
        self.bugtwoOffText.set("0")
        self.bugtwoOffLabel=Label(offCovFrame, textvariable=self.bugtwoOffText, anchor=W)
        self.bugtwoOffLabel.grid(row=15, column=9)

        Label(offCovFrame, text="Rock", anchor=W).grid(row=16, column=1, pady=1)
        self.rockzeroOffText = StringVar()
        self.rockzeroOffText.set("0")
        self.rockzeroOffLabel=Label(offCovFrame, textvariable=self.rockzeroOffText, anchor=W)
        self.rockzeroOffLabel.grid(row=16, column=3)
        self.rockhalfOffText = StringVar()
        self.rockhalfOffText.set("0")
        self.rockhalfOffLabel=Label(offCovFrame, textvariable=self.rockhalfOffText, anchor=W)
        self.rockhalfOffLabel.grid(row=16, column=5)
        self.rockoneOffText = StringVar()
        self.rockoneOffText.set("0")
        Label(offCovFrame, textvariable=self.rockoneOffText, anchor=W).grid(row=16, column=7)
        self.rocktwoOffText = StringVar()
        self.rocktwoOffText.set("0")
        self.rocktwoOffLabel=Label(offCovFrame, textvariable=self.rocktwoOffText, anchor=W)
        self.rocktwoOffLabel.grid(row=16, column=9)

        Label(offCovFrame, text="Ghost", anchor=W).grid(row=17, column=1, pady=1)
        self.ghostzeroOffText = StringVar()
        self.ghostzeroOffText.set("0")
        self.ghostzeroOffLabel=Label(offCovFrame, textvariable=self.ghostzeroOffText, anchor=W)
        self.ghostzeroOffLabel.grid(row=17, column=3)
        self.ghosthalfOffText = StringVar()
        self.ghosthalfOffText.set("0")
        self.ghosthalfOffLabel=Label(offCovFrame, textvariable=self.ghosthalfOffText, anchor=W)
        self.ghosthalfOffLabel.grid(row=17, column=5)
        self.ghostoneOffText = StringVar()
        self.ghostoneOffText.set("0")
        Label(offCovFrame, textvariable=self.ghostoneOffText, anchor=W).grid(row=17, column=7)
        self.ghosttwoOffText = StringVar()
        self.ghosttwoOffText.set("0")
        self.ghosttwoOffLabel=Label(offCovFrame, textvariable=self.ghosttwoOffText, anchor=W)
        self.ghosttwoOffLabel.grid(row=17, column=9)

        Label(offCovFrame, text="Dragon", anchor=W).grid(row=18, column=1, pady=1)
        self.dragonzeroOffText = StringVar()
        self.dragonzeroOffText.set("0")
        self.dragonzeroOffLabel=Label(offCovFrame, textvariable=self.dragonzeroOffText, anchor=W)
        self.dragonzeroOffLabel.grid(row=18, column=3)
        self.dragonhalfOffText = StringVar()
        self.dragonhalfOffText.set("0")
        self.dragonhalfOffLabel=Label(offCovFrame, textvariable=self.dragonhalfOffText, anchor=W)
        self.dragonhalfOffLabel.grid(row=18, column=5)
        self.dragononeOffText = StringVar()
        self.dragononeOffText.set("0")
        Label(offCovFrame, textvariable=self.dragononeOffText, anchor=W).grid(row=18, column=7)
        self.dragontwoOffText = StringVar()
        self.dragontwoOffText.set("0")
        self.dragontwoOffLabel=Label(offCovFrame, textvariable=self.dragontwoOffText, anchor=W)
        self.dragontwoOffLabel.grid(row=18, column=9)

        Label(offCovFrame, text="Dark", anchor=W).grid(row=19, column=1, pady=1)
        self.darkzeroOffText = StringVar()
        self.darkzeroOffText.set("0")
        self.darkzeroOffLabel=Label(offCovFrame, textvariable=self.darkzeroOffText, anchor=W)
        self.darkzeroOffLabel.grid(row=19, column=3)
        self.darkhalfOffText = StringVar()
        self.darkhalfOffText.set("0")
        self.darkhalfOffLabel=Label(offCovFrame, textvariable=self.darkhalfOffText, anchor=W)
        self.darkhalfOffLabel.grid(row=19, column=5)
        self.darkoneOffText = StringVar()
        self.darkoneOffText.set("0")
        Label(offCovFrame, textvariable=self.darkoneOffText, anchor=W).grid(row=19, column=7)
        self.darktwoOffText = StringVar()
        self.darktwoOffText.set("0")
        self.darktwoOffLabel=Label(offCovFrame, textvariable=self.darktwoOffText, anchor=W)
        self.darktwoOffLabel.grid(row=19, column=9)

        Label(offCovFrame, text="Steel", anchor=W).grid(row=20, column=1, pady=1)
        self.steelzeroOffText = StringVar()
        self.steelzeroOffText.set("0")
        self.steelzeroOffLabel=Label(offCovFrame, textvariable=self.steelzeroOffText, anchor=W)
        self.steelzeroOffLabel.grid(row=20, column=3)
        self.steelhalfOffText = StringVar()
        self.steelhalfOffText.set("0")
        self.steelhalfOffLabel=Label(offCovFrame, textvariable=self.steelhalfOffText, anchor=W)
        self.steelhalfOffLabel.grid(row=20, column=5)
        self.steeloneOffText = StringVar()
        self.steeloneOffText.set("0")
        Label(offCovFrame, textvariable=self.steeloneOffText, anchor=W).grid(row=20, column=7)
        self.steeltwoOffText = StringVar()
        self.steeltwoOffText.set("0")
        self.steeltwoOffLabel=Label(offCovFrame, textvariable=self.steeltwoOffText, anchor=W)
        self.steeltwoOffLabel.grid(row=20, column=9)

        Label(offCovFrame, text="Fairy", anchor=W).grid(row=21, column=1, pady=1)
        self.fairyzeroOffText = StringVar()
        self.fairyzeroOffText.set("0")
        self.fairyzeroOffLabel=Label(offCovFrame, textvariable=self.fairyzeroOffText, anchor=W)
        self.fairyzeroOffLabel.grid(row=21, column=3)
        self.fairyhalfOffText = StringVar()
        self.fairyhalfOffText.set("0")
        self.fairyhalfOffLabel=Label(offCovFrame, textvariable=self.fairyhalfOffText, anchor=W)
        self.fairyhalfOffLabel.grid(row=21, column=5)
        self.fairyoneOffText = StringVar()
        self.fairyoneOffText.set("0")
        Label(offCovFrame, textvariable=self.fairyoneOffText, anchor=W).grid(row=21, column=7)
        self.fairytwoOffText = StringVar()
        self.fairytwoOffText.set("0")
        self.fairytwoOffLabel=Label(offCovFrame, textvariable=self.fairytwoOffText, anchor=W)
        self.fairytwoOffLabel.grid(row=21, column=9)

        middleFrame = Frame(self.toplevel)
        middleFrame.pack(side=LEFT, fill=Y)
        Label(middleFrame,text="Physical/Special Balances").grid(row=0,column=0,columnspan=2,sticky=EW)
        Label(middleFrame,text="Offenive Balance").grid(row=1,column=0,columnspan=2,sticky=EW)
        #Label(middleFrame,text="Physical").place(x=100,y=50)
        #Label(middleFrame,text="Special").place(x=150,y=50)
        self.physpecOffCanvas = Canvas(middleFrame, height=20)
        self.physpecOffCanvas.grid(row=2,column=0,columnspan=2,padx=10,sticky=EW)
        size=self.physpecOffCanvas.winfo_reqwidth()
        self.offBalance = int(size/2)
        self.physOffBar=self.physpecOffCanvas.create_rectangle(0,0,self.offBalance,20,fill="orange red")
        self.specOffBar=self.physpecOffCanvas.create_rectangle(self.offBalance,0,size,20,fill="cornflower blue")
        self.physpecOffCanvas.create_line(size/2,0,size/2,20,fill="green2")

        Label(middleFrame, text="Defensive Balance").grid(row=3,column=0,columnspan=2,sticky=EW)
        self.physpecDefCanvas = Canvas(middleFrame, height=20)
        self.physpecDefCanvas.grid(row=4,column=0,columnspan=2,padx=10,sticky=EW)
        self.defBalance = int(size/2)
        self.physDefBar=self.physpecDefCanvas.create_rectangle(0, 0, self.defBalance, 20, fill="orange red")
        self.specDefBar=self.physpecDefCanvas.create_rectangle(self.defBalance, 0, size, 20, fill="cornflower blue")
        self.physpecDefCanvas.create_line(size/2,0,size/2,20,fill="green2")

        self.adviceMssngr = Text(middleFrame, wrap=WORD,width=45,height=21)
        self.adviceMssngr.grid(row=5,column=0,pady=10,padx=(10,0),sticky=EW)
        self.adviceMssngr.config(state=DISABLED)
        advicescrollbar = Scrollbar(middleFrame, command=self.adviceMssngr.yview)
        advicescrollbar.grid(row=5,column=1,padx=(0,10),pady=10,sticky=NS)
        self.adviceMssngr["yscrollcommand"] = advicescrollbar.set

        defCovFrame = Frame(self.toplevel)
        defCovFrame.pack(side=LEFT,fill=Y)
        Label(defCovFrame, text="Defensive Coverage").grid(row=0, column=0, columnspan=15, sticky=EW)
        ttk.Separator(defCovFrame, orient=HORIZONTAL).grid(row=1, column=2, columnspan=12, sticky=EW)
        ttk.Separator(defCovFrame, orient=HORIZONTAL).grid(row=3, column=1, columnspan=13, sticky=EW)
        ttk.Separator(defCovFrame, orient=HORIZONTAL).grid(row=22, column=1, columnspan=13, sticky=EW)
        ttk.Separator(defCovFrame, orient=VERTICAL).grid(row=4, column=0, rowspan=18, sticky=NS)
        ttk.Separator(defCovFrame, orient=VERTICAL).grid(row=2, column=2, rowspan=20, sticky=NS)
        ttk.Separator(defCovFrame, orient=VERTICAL).grid(row=2, column=4, rowspan=20, sticky=NS)
        ttk.Separator(defCovFrame, orient=VERTICAL).grid(row=2, column=6, rowspan=20, sticky=NS)
        ttk.Separator(defCovFrame, orient=VERTICAL).grid(row=2, column=8, rowspan=20, sticky=NS)
        ttk.Separator(defCovFrame, orient=VERTICAL).grid(row=2, column=10, rowspan=20, sticky=NS)
        ttk.Separator(defCovFrame, orient=VERTICAL).grid(row=2, column=12, rowspan=20, sticky=NS)
        ttk.Separator(defCovFrame, orient=VERTICAL).grid(row=2, column=14, rowspan=20, sticky=NS,padx=(0,10))

        Label(defCovFrame, text="0").grid(row=2, column=3, padx=10)
        Label(defCovFrame, text="1/4").grid(row=2, column=5, padx=5)
        Label(defCovFrame, text="1/2").grid(row=2, column=7, padx=5)
        Label(defCovFrame, text="1").grid(row=2, column=9, padx=10)
        Label(defCovFrame, text="2").grid(row=2, column=11, padx=10)
        Label(defCovFrame, text="4").grid(row=2, column=13, padx=10)

        Label(defCovFrame, text="Normal", anchor=W).grid(row=4, column=1, pady=1)
        self.normalzeroDefText = StringVar()
        self.normalzeroDefText.set("0")
        self.normalzeroDefLabel=Label(defCovFrame, textvariable=self.normalzeroDefText, anchor=W)
        self.normalzeroDefLabel.grid(row=4, column=3)
        self.normalquarterDefText = StringVar()
        self.normalquarterDefText.set("0")
        self.normalquarterDefLabel =Label(defCovFrame, textvariable=self.normalquarterDefText, anchor=W)
        self.normalquarterDefLabel.grid(row=4,column=5)
        self.normalhalfDefText = StringVar()
        self.normalhalfDefText.set("0")
        self.normalhalfDefLabel =Label(defCovFrame, textvariable=self.normalhalfDefText, anchor=W)
        self.normalhalfDefLabel.grid(row=4, column=7)
        self.normaloneDefText = StringVar()
        self.normaloneDefText.set("0")
        Label(defCovFrame, textvariable=self.normaloneDefText, anchor=W).grid(row=4, column=9)
        self.normaltwoDefText = StringVar()
        self.normaltwoDefText.set("0")
        self.normaltwoDefLabel =Label(defCovFrame, textvariable=self.normaltwoDefText, anchor=W)
        self.normaltwoDefLabel.grid(row=4, column=11)
        self.normalfourDefText = StringVar()
        self.normalfourDefText.set("0")
        self.normalfourDefLabel =Label(defCovFrame, textvariable=self.normalfourDefText, anchor=W)
        self.normalfourDefLabel.grid(row=4, column=13)

        Label(defCovFrame, text="Fire", anchor=W).grid(row=5, column=1, pady=1)
        self.firezeroDefText = StringVar()
        self.firezeroDefText.set("0")
        self.firezeroDefLabel=Label(defCovFrame, textvariable=self.firezeroDefText, anchor=W)
        self.firezeroDefLabel.grid(row=5, column=3)
        self.firequarterDefText = StringVar()
        self.firequarterDefText.set("0")
        self.firequarterDefLabel=Label(defCovFrame, textvariable=self.firequarterDefText, anchor=W)
        self.firequarterDefLabel.grid(row=5,column=5)
        self.firehalfDefText = StringVar()
        self.firehalfDefText.set("0")
        self.firehalfDefLabel=Label(defCovFrame, textvariable=self.firehalfDefText, anchor=W)
        self.firehalfDefLabel.grid(row=5, column=7)
        self.fireoneDefText = StringVar()
        self.fireoneDefText.set("0")
        Label(defCovFrame, textvariable=self.fireoneDefText, anchor=W).grid(row=5, column=9)
        self.firetwoDefText = StringVar()
        self.firetwoDefText.set("0")
        self.firetwoDefLabel=Label(defCovFrame, textvariable=self.firetwoDefText, anchor=W)
        self.firetwoDefLabel.grid(row=5, column=11)
        self.firefourDefText = StringVar()
        self.firefourDefText.set("0")
        self.firefourDefLabel=Label(defCovFrame, textvariable=self.firefourDefText, anchor=W)
        self.firefourDefLabel.grid(row=5, column=13)

        Label(defCovFrame, text="Water", anchor=W).grid(row=6, column=1, pady=1)
        self.waterzeroDefText = StringVar()
        self.waterzeroDefText.set("0")
        self.waterzeroDefLabel=Label(defCovFrame, textvariable=self.waterzeroDefText, anchor=W)
        self.waterzeroDefLabel.grid(row=6, column=3)
        self.waterquarterDefText = StringVar()
        self.waterquarterDefText.set("0")
        self.waterquarterDefLabel=Label(defCovFrame, textvariable=self.waterquarterDefText, anchor=W)
        self.waterquarterDefLabel.grid(row=6,column=5)
        self.waterhalfDefText = StringVar()
        self.waterhalfDefText.set("0")
        self.waterhalfDefLabel=Label(defCovFrame, textvariable=self.waterhalfDefText, anchor=W)
        self.waterhalfDefLabel.grid(row=6, column=7)
        self.wateroneDefText = StringVar()
        self.wateroneDefText.set("0")
        Label(defCovFrame, textvariable=self.wateroneDefText, anchor=W).grid(row=6, column=9)
        self.watertwoDefText = StringVar()
        self.watertwoDefText.set("0")
        self.watertwoDefLabel=Label(defCovFrame, textvariable=self.watertwoDefText, anchor=W)
        self.watertwoDefLabel.grid(row=6, column=11)
        self.waterfourDefText = StringVar()
        self.waterfourDefText.set("0")
        self.waterfourDefLabel=Label(defCovFrame, textvariable=self.waterfourDefText, anchor=W)
        self.waterfourDefLabel.grid(row=6, column=13)

        Label(defCovFrame, text="Electric", anchor=W).grid(row=7, column=1, pady=1)
        self.electriczeroDefText = StringVar()
        self.electriczeroDefText.set("0")
        self.electriczeroDefLabel=Label(defCovFrame, textvariable=self.electriczeroDefText, anchor=W)
        self.electriczeroDefLabel.grid(row=7, column=3)
        self.electricquarterDefText = StringVar()
        self.electricquarterDefText.set("0")
        self.electricquarterDefLabel=Label(defCovFrame, textvariable=self.electricquarterDefText, anchor=W)
        self.electricquarterDefLabel.grid(row=7,column=5)
        self.electrichalfDefText = StringVar()
        self.electrichalfDefText.set("0")
        self.electrichalfDefLabel=Label(defCovFrame, textvariable=self.electrichalfDefText, anchor=W)
        self.electrichalfDefLabel.grid(row=7, column=7)
        self.electriconeDefText = StringVar()
        self.electriconeDefText.set("0")
        Label(defCovFrame, textvariable=self.electriconeDefText, anchor=W).grid(row=7, column=9)
        self.electrictwoDefText = StringVar()
        self.electrictwoDefText.set("0")
        self.electrictwoDefLabel=Label(defCovFrame, textvariable=self.electrictwoDefText, anchor=W)
        self.electrictwoDefLabel.grid(row=7, column=11)
        self.electricfourDefText = StringVar()
        self.electricfourDefText.set("0")
        self.electricfourDefLabel=Label(defCovFrame, textvariable=self.electricfourDefText, anchor=W)
        self.electricfourDefLabel.grid(row=7, column=13)

        Label(defCovFrame, text="Grass", anchor=W).grid(row=8, column=1, pady=1)
        self.grasszeroDefText = StringVar()
        self.grasszeroDefText.set("0")
        self.grasszeroDefLabel=Label(defCovFrame, textvariable=self.grasszeroDefText, anchor=W)
        self.grasszeroDefLabel.grid(row=8, column=3)
        self.grassquarterDefText = StringVar()
        self.grassquarterDefText.set("0")
        self.grassquarterDefLabel=Label(defCovFrame, textvariable=self.grassquarterDefText, anchor=W)
        self.grassquarterDefLabel.grid(row=8,column=5)
        self.grasshalfDefText = StringVar()
        self.grasshalfDefText.set("0")
        self.grasshalfDefLabel=Label(defCovFrame, textvariable=self.grasshalfDefText, anchor=W)
        self.grasshalfDefLabel.grid(row=8, column=7)
        self.grassoneDefText = StringVar()
        self.grassoneDefText.set("0")
        Label(defCovFrame, textvariable=self.grassoneDefText, anchor=W).grid(row=8, column=9)
        self.grasstwoDefText = StringVar()
        self.grasstwoDefText.set("0")
        self.grasstwoDefLabel=Label(defCovFrame, textvariable=self.grasstwoDefText, anchor=W)
        self.grasstwoDefLabel.grid(row=8, column=11)
        self.grassfourDefText = StringVar()
        self.grassfourDefText.set("0")
        self.grassfourDefLabel=Label(defCovFrame, textvariable=self.grassfourDefText, anchor=W)
        self.grassfourDefLabel.grid(row=8, column=13)

        Label(defCovFrame, text="Ice", anchor=W).grid(row=9, column=1, pady=1)
        self.icezeroDefText = StringVar()
        self.icezeroDefText.set("0")
        self.icezeroDefLabel=Label(defCovFrame, textvariable=self.icezeroDefText, anchor=W)
        self.icezeroDefLabel.grid(row=9, column=3)
        self.icequarterDefText = StringVar()
        self.icequarterDefText.set("0")
        self.icequarterDefLabel=Label(defCovFrame, textvariable=self.icequarterDefText, anchor=W)
        self.icequarterDefLabel.grid(row=9,column=5)
        self.icehalfDefText = StringVar()
        self.icehalfDefText.set("0")
        self.icehalfDefLabel=Label(defCovFrame, textvariable=self.icehalfDefText, anchor=W)
        self.icehalfDefLabel.grid(row=9, column=7)
        self.iceoneDefText = StringVar()
        self.iceoneDefText.set("0")
        Label(defCovFrame, textvariable=self.iceoneDefText, anchor=W).grid(row=9, column=9)
        self.icetwoDefText = StringVar()
        self.icetwoDefText.set("0")
        self.icetwoDefLabel=Label(defCovFrame, textvariable=self.icetwoDefText, anchor=W)
        self.icetwoDefLabel.grid(row=9, column=11)
        self.icefourDefText = StringVar()
        self.icefourDefText.set("0")
        self.icefourDefLabel=Label(defCovFrame, textvariable=self.icefourDefText, anchor=W)
        self.icefourDefLabel.grid(row=9, column=13)

        Label(defCovFrame, text="Fighting", anchor=W).grid(row=10, column=1, pady=1)
        self.fightingzeroDefText = StringVar()
        self.fightingzeroDefText.set("0")
        self.fightingzeroDefLabel=Label(defCovFrame, textvariable=self.fightingzeroDefText, anchor=W)
        self.fightingzeroDefLabel.grid(row=10, column=3)
        self.fightingquarterDefText = StringVar()
        self.fightingquarterDefText.set("0")
        self.fightingquarterDefLabel=Label(defCovFrame, textvariable=self.fightingquarterDefText, anchor=W)
        self.fightingquarterDefLabel.grid(row=10,column=5)
        self.fightinghalfDefText = StringVar()
        self.fightinghalfDefText.set("0")
        self.fightinghalfDefLabel=Label(defCovFrame, textvariable=self.fightinghalfDefText, anchor=W)
        self.fightinghalfDefLabel.grid(row=10, column=7)
        self.fightingoneDefText = StringVar()
        self.fightingoneDefText.set("0")
        Label(defCovFrame, textvariable=self.fightingoneDefText, anchor=W).grid(row=10, column=9)
        self.fightingtwoDefText = StringVar()
        self.fightingtwoDefText.set("0")
        self.fightingtwoDefLabel=Label(defCovFrame, textvariable=self.fightingtwoDefText, anchor=W)
        self.fightingtwoDefLabel.grid(row=10, column=11)
        self.fightingfourDefText = StringVar()
        self.fightingfourDefText.set("0")
        self.fightingfourDefLabel=Label(defCovFrame, textvariable=self.fightingfourDefText, anchor=W)
        self.fightingfourDefLabel.grid(row=10, column=13)

        Label(defCovFrame, text="Poison", anchor=W).grid(row=11, column=1, pady=1)
        self.poisonzeroDefText = StringVar()
        self.poisonzeroDefText.set("0")
        self.poisonzeroDefLabel=Label(defCovFrame, textvariable=self.poisonzeroDefText, anchor=W)
        self.poisonzeroDefLabel.grid(row=11, column=3)
        self.poisonquarterDefText = StringVar()
        self.poisonquarterDefText.set("0")
        self.poisonquarterDefLabel=Label(defCovFrame, textvariable=self.poisonquarterDefText, anchor=W)
        self.poisonquarterDefLabel.grid(row=11,column=5)
        self.poisonhalfDefText = StringVar()
        self.poisonhalfDefText.set("0")
        self.poisonhalfDefLabel=Label(defCovFrame, textvariable=self.poisonhalfDefText, anchor=W)
        self.poisonhalfDefLabel.grid(row=11, column=7)
        self.poisononeDefText = StringVar()
        self.poisononeDefText.set("0")
        Label(defCovFrame, textvariable=self.poisononeDefText, anchor=W).grid(row=11, column=9)
        self.poisontwoDefText = StringVar()
        self.poisontwoDefText.set("0")
        self.poisontwoDefLabel=Label(defCovFrame, textvariable=self.poisontwoDefText, anchor=W)
        self.poisontwoDefLabel.grid(row=11, column=11)
        self.poisonfourDefText = StringVar()
        self.poisonfourDefText.set("0")
        self.poisonfourDefLabel=Label(defCovFrame, textvariable=self.poisonfourDefText, anchor=W)
        self.poisonfourDefLabel.grid(row=11, column=13)

        Label(defCovFrame, text="Ground", anchor=W).grid(row=12, column=1, pady=1)
        self.groundzeroDefText = StringVar()
        self.groundzeroDefText.set("0")
        self.groundzeroDefLabel=Label(defCovFrame, textvariable=self.groundzeroDefText, anchor=W)
        self.groundzeroDefLabel.grid(row=12, column=3)
        self.groundquarterDefText = StringVar()
        self.groundquarterDefText.set("0")
        self.groundquarterDefLabel=Label(defCovFrame, textvariable=self.groundquarterDefText, anchor=W)
        self.groundquarterDefLabel.grid(row=12,column=5)
        self.groundhalfDefText = StringVar()
        self.groundhalfDefText.set("0")
        self.groundhalfDefLabel=Label(defCovFrame, textvariable=self.groundhalfDefText, anchor=W)
        self.groundhalfDefLabel.grid(row=12, column=7)
        self.groundoneDefText = StringVar()
        self.groundoneDefText.set("0")
        Label(defCovFrame, textvariable=self.groundoneDefText, anchor=W).grid(row=12, column=9)
        self.groundtwoDefText = StringVar()
        self.groundtwoDefText.set("0")
        self.groundtwoDefLabel=Label(defCovFrame, textvariable=self.groundtwoDefText, anchor=W)
        self.groundtwoDefLabel.grid(row=12, column=11)
        self.groundfourDefText = StringVar()
        self.groundfourDefText.set("0")
        self.groundfourDefLabel=Label(defCovFrame, textvariable=self.groundfourDefText, anchor=W)
        self.groundfourDefLabel.grid(row=12, column=13)

        Label(defCovFrame, text="Flying", anchor=W).grid(row=13, column=1, pady=1)
        self.flyingzeroDefText = StringVar()
        self.flyingzeroDefText.set("0")
        self.flyingzeroDefLabel=Label(defCovFrame, textvariable=self.flyingzeroDefText, anchor=W)
        self.flyingzeroDefLabel.grid(row=13, column=3)
        self.flyingquarterDefText = StringVar()
        self.flyingquarterDefText.set("0")
        self.flyingquarterDefLabel=Label(defCovFrame, textvariable=self.flyingquarterDefText, anchor=W)
        self.flyingquarterDefLabel.grid(row=13,column=5)
        self.flyinghalfDefText = StringVar()
        self.flyinghalfDefText.set("0")
        self.flyinghalfDefLabel=Label(defCovFrame, textvariable=self.flyinghalfDefText, anchor=W)
        self.flyinghalfDefLabel.grid(row=13, column=7)
        self.flyingoneDefText = StringVar()
        self.flyingoneDefText.set("0")
        Label(defCovFrame, textvariable=self.flyingoneDefText, anchor=W).grid(row=13, column=9)
        self.flyingtwoDefText = StringVar()
        self.flyingtwoDefText.set("0")
        self.flyingtwoDefLabel=Label(defCovFrame, textvariable=self.flyingtwoDefText, anchor=W)
        self.flyingtwoDefLabel.grid(row=13, column=11)
        self.flyingfourDefText = StringVar()
        self.flyingfourDefText.set("0")
        self.flyingfourDefLabel=Label(defCovFrame, textvariable=self.flyingfourDefText, anchor=W)
        self.flyingfourDefLabel.grid(row=13, column=13)

        Label(defCovFrame, text="Psychic", anchor=W).grid(row=14, column=1, pady=1)
        self.psychiczeroDefText = StringVar()
        self.psychiczeroDefText.set("0")
        self.psychiczeroDefLabel=Label(defCovFrame, textvariable=self.psychiczeroDefText, anchor=W)
        self.psychiczeroDefLabel.grid(row=14, column=3)
        self.psychicquarterDefText = StringVar()
        self.psychicquarterDefText.set("0")
        self.psychicquarterDefLabel=Label(defCovFrame, textvariable=self.psychicquarterDefText, anchor=W)
        self.psychicquarterDefLabel.grid(row=14,column=5)
        self.psychichalfDefText = StringVar()
        self.psychichalfDefText.set("0")
        self.psychichalfDefLabel=Label(defCovFrame, textvariable=self.psychichalfDefText, anchor=W)
        self.psychichalfDefLabel.grid(row=14, column=7)
        self.psychiconeDefText = StringVar()
        self.psychiconeDefText.set("0")
        Label(defCovFrame, textvariable=self.psychiconeDefText, anchor=W).grid(row=14, column=9)
        self.psychictwoDefText = StringVar()
        self.psychictwoDefText.set("0")
        self.psychictwoDefLabel=Label(defCovFrame, textvariable=self.psychictwoDefText, anchor=W)
        self.psychictwoDefLabel.grid(row=14, column=11)
        self.psychicfourDefText = StringVar()
        self.psychicfourDefText.set("0")
        self.psychicfourDefLabel=Label(defCovFrame, textvariable=self.psychicfourDefText, anchor=W)
        self.psychicfourDefLabel.grid(row=14, column=13)

        Label(defCovFrame, text="Bug", anchor=W).grid(row=15, column=1, pady=1)
        self.bugzeroDefText = StringVar()
        self.bugzeroDefText.set("0")
        self.bugzeroDefLabel=Label(defCovFrame, textvariable=self.bugzeroDefText, anchor=W)
        self.bugzeroDefLabel.grid(row=15, column=3)
        self.bugquarterDefText = StringVar()
        self.bugquarterDefText.set("0")
        self.bugquarterDefLabel=Label(defCovFrame, textvariable=self.bugquarterDefText, anchor=W)
        self.bugquarterDefLabel.grid(row=15,column=5)
        self.bughalfDefText = StringVar()
        self.bughalfDefText.set("0")
        self.bughalfDefLabel=Label(defCovFrame, textvariable=self.bughalfDefText, anchor=W)
        self.bughalfDefLabel.grid(row=15, column=7)
        self.bugoneDefText = StringVar()
        self.bugoneDefText.set("0")
        Label(defCovFrame, textvariable=self.bugoneDefText, anchor=W).grid(row=15, column=9)
        self.bugtwoDefText = StringVar()
        self.bugtwoDefText.set("0")
        self.bugtwoDefLabel=Label(defCovFrame, textvariable=self.bugtwoDefText, anchor=W)
        self.bugtwoDefLabel.grid(row=15, column=11)
        self.bugfourDefText = StringVar()
        self.bugfourDefText.set("0")
        self.bugfourDefLabel=Label(defCovFrame, textvariable=self.bugfourDefText, anchor=W)
        self.bugfourDefLabel.grid(row=15, column=13)

        Label(defCovFrame, text="Rock", anchor=W).grid(row=16, column=1, pady=1)
        self.rockzeroDefText = StringVar()
        self.rockzeroDefText.set("0")
        self.rockzeroDefLabel=Label(defCovFrame, textvariable=self.rockzeroDefText, anchor=W)
        self.rockzeroDefLabel.grid(row=16, column=3)
        self.rockquarterDefText = StringVar()
        self.rockquarterDefText.set("0")
        self.rockquarterDefLabel=Label(defCovFrame, textvariable=self.rockquarterDefText, anchor=W)
        self.rockquarterDefLabel.grid(row=16,column=5)
        self.rockhalfDefText = StringVar()
        self.rockhalfDefText.set("0")
        self.rockhalfDefLabel=Label(defCovFrame, textvariable=self.rockhalfDefText, anchor=W)
        self.rockhalfDefLabel.grid(row=16, column=7)
        self.rockoneDefText = StringVar()
        self.rockoneDefText.set("0")
        Label(defCovFrame, textvariable=self.rockoneDefText, anchor=W).grid(row=16, column=9)
        self.rocktwoDefText = StringVar()
        self.rocktwoDefText.set("0")
        self.rocktwoDefLabel=Label(defCovFrame, textvariable=self.rocktwoDefText, anchor=W)
        self.rocktwoDefLabel.grid(row=16, column=11)
        self.rockfourDefText = StringVar()
        self.rockfourDefText.set("0")
        self.rockfourDefLabel=Label(defCovFrame, textvariable=self.rockfourDefText, anchor=W)
        self.rockfourDefLabel.grid(row=16, column=13)

        Label(defCovFrame, text="Ghost", anchor=W).grid(row=17, column=1, pady=1)
        self.ghostzeroDefText = StringVar()
        self.ghostzeroDefText.set("0")
        self.ghostzeroDefLabel=Label(defCovFrame, textvariable=self.ghostzeroDefText, anchor=W)
        self.ghostzeroDefLabel.grid(row=17, column=3)
        self.ghostquarterDefText = StringVar()
        self.ghostquarterDefText.set("0")
        self.ghostquarterDefLabel=Label(defCovFrame, textvariable=self.ghostquarterDefText, anchor=W)
        self.ghostquarterDefLabel.grid(row=17,column=5)
        self.ghosthalfDefText = StringVar()
        self.ghosthalfDefText.set("0")
        self.ghosthalfDefLabel=Label(defCovFrame, textvariable=self.ghosthalfDefText, anchor=W)
        self.ghosthalfDefLabel.grid(row=17, column=7)
        self.ghostoneDefText = StringVar()
        self.ghostoneDefText.set("0")
        Label(defCovFrame, textvariable=self.ghostoneDefText, anchor=W).grid(row=17, column=9)
        self.ghosttwoDefText = StringVar()
        self.ghosttwoDefText.set("0")
        self.ghosttwoDefLabel=Label(defCovFrame, textvariable=self.ghosttwoDefText, anchor=W)
        self.ghosttwoDefLabel.grid(row=17, column=11)
        self.ghostfourDefText = StringVar()
        self.ghostfourDefText.set("0")
        self.ghostfourDefLabel=Label(defCovFrame, textvariable=self.ghostfourDefText, anchor=W)
        self.ghostfourDefLabel.grid(row=17, column=13)

        Label(defCovFrame, text="Dragon", anchor=W).grid(row=18, column=1, pady=1)
        self.dragonzeroDefText = StringVar()
        self.dragonzeroDefText.set("0")
        self.dragonzeroDefLabel=Label(defCovFrame, textvariable=self.dragonzeroDefText, anchor=W)
        self.dragonzeroDefLabel.grid(row=18, column=3)
        self.dragonquarterDefText = StringVar()
        self.dragonquarterDefText.set("0")
        self.dragonquarterDefLabel=Label(defCovFrame, textvariable=self.dragonquarterDefText, anchor=W)
        self.dragonquarterDefLabel.grid(row=18,column=5)
        self.dragonhalfDefText = StringVar()
        self.dragonhalfDefText.set("0")
        self.dragonhalfDefLabel=Label(defCovFrame, textvariable=self.dragonhalfDefText, anchor=W)
        self.dragonhalfDefLabel.grid(row=18, column=7)
        self.dragononeDefText = StringVar()
        self.dragononeDefText.set("0")
        Label(defCovFrame, textvariable=self.dragononeDefText, anchor=W).grid(row=18, column=9)
        self.dragontwoDefText = StringVar()
        self.dragontwoDefText.set("0")
        self.dragontwoDefLabel=Label(defCovFrame, textvariable=self.dragontwoDefText, anchor=W)
        self.dragontwoDefLabel.grid(row=18, column=11)
        self.dragonfourDefText = StringVar()
        self.dragonfourDefText.set("0")
        self.dragonfourDefLabel=Label(defCovFrame, textvariable=self.dragonfourDefText, anchor=W)
        self.dragonfourDefLabel.grid(row=18, column=13)

        Label(defCovFrame, text="Dark", anchor=W).grid(row=19, column=1, pady=1)
        self.darkzeroDefText = StringVar()
        self.darkzeroDefText.set("0")
        self.darkzeroDefLabel=Label(defCovFrame, textvariable=self.darkzeroDefText, anchor=W)
        self.darkzeroDefLabel.grid(row=19, column=3)
        self.darkquarterDefText = StringVar()
        self.darkquarterDefText.set("0")
        self.darkquarterDefLabel=Label(defCovFrame, textvariable=self.darkquarterDefText, anchor=W)
        self.darkquarterDefLabel.grid(row=19,column=5)
        self.darkhalfDefText = StringVar()
        self.darkhalfDefText.set("0")
        self.darkhalfDefLabel=Label(defCovFrame, textvariable=self.darkhalfDefText, anchor=W)
        self.darkhalfDefLabel.grid(row=19, column=7)
        self.darkoneDefText = StringVar()
        self.darkoneDefText.set("0")
        Label(defCovFrame, textvariable=self.darkoneDefText, anchor=W).grid(row=19, column=9)
        self.darktwoDefText = StringVar()
        self.darktwoDefText.set("0")
        self.darktwoDefLabel=Label(defCovFrame, textvariable=self.darktwoDefText, anchor=W)
        self.darktwoDefLabel.grid(row=19, column=11)
        self.darkfourDefText = StringVar()
        self.darkfourDefText.set("0")
        self.darkfourDefLabel=Label(defCovFrame, textvariable=self.darkfourDefText, anchor=W)
        self.darkfourDefLabel.grid(row=19, column=13)

        Label(defCovFrame, text="Steel", anchor=W).grid(row=20, column=1, pady=1)
        self.steelzeroDefText = StringVar()
        self.steelzeroDefText.set("0")
        self.steelzeroDefLabel=Label(defCovFrame, textvariable=self.steelzeroDefText, anchor=W)
        self.steelzeroDefLabel.grid(row=20, column=3)
        self.steelquarterDefText = StringVar()
        self.steelquarterDefText.set("0")
        self.steelquarterDefLabel=Label(defCovFrame, textvariable=self.steelquarterDefText, anchor=W)
        self.steelquarterDefLabel.grid(row=20,column=5)
        self.steelhalfDefText = StringVar()
        self.steelhalfDefText.set("0")
        self.steelhalfDefLabel=Label(defCovFrame, textvariable=self.steelhalfDefText, anchor=W)
        self.steelhalfDefLabel.grid(row=20, column=7)
        self.steeloneDefText = StringVar()
        self.steeloneDefText.set("0")
        Label(defCovFrame, textvariable=self.steeloneDefText, anchor=W).grid(row=20, column=9)
        self.steeltwoDefText = StringVar()
        self.steeltwoDefText.set("0")
        self.steeltwoDefLabel=Label(defCovFrame, textvariable=self.steeltwoDefText, anchor=W)
        self.steeltwoDefLabel.grid(row=20, column=11)
        self.steelfourDefText = StringVar()
        self.steelfourDefText.set("0")
        self.steelfourDefLabel=Label(defCovFrame, textvariable=self.steelfourDefText, anchor=W)
        self.steelfourDefLabel.grid(row=20, column=13)

        Label(defCovFrame, text="Fairy", anchor=W).grid(row=21, column=1, pady=1)
        self.fairyzeroDefText = StringVar()
        self.fairyzeroDefText.set("0")
        self.fairyzeroDefLabel=Label(defCovFrame, textvariable=self.fairyzeroDefText, anchor=W)
        self.fairyzeroDefLabel.grid(row=21, column=3)
        self.fairyquarterDefText = StringVar()
        self.fairyquarterDefText.set("0")
        self.fairyquarterDefLabel=Label(defCovFrame, textvariable=self.fairyquarterDefText, anchor=W)
        self.fairyquarterDefLabel.grid(row=21,column=5)
        self.fairyhalfDefText = StringVar()
        self.fairyhalfDefText.set("0")
        self.fairyhalfDefLabel=Label(defCovFrame, textvariable=self.fairyhalfDefText, anchor=W)
        self.fairyhalfDefLabel.grid(row=21, column=7)
        self.fairyoneDefText = StringVar()
        self.fairyoneDefText.set("0")
        Label(defCovFrame, textvariable=self.fairyoneDefText, anchor=W).grid(row=21, column=9)
        self.fairytwoDefText = StringVar()
        self.fairytwoDefText.set("0")
        self.fairytwoDefLabel=Label(defCovFrame, textvariable=self.fairytwoDefText, anchor=W)
        self.fairytwoDefLabel.grid(row=21, column=11)
        self.fairyfourDefText = StringVar()
        self.fairyfourDefText.set("0")
        self.fairyfourDefLabel=Label(defCovFrame, textvariable=self.fairyfourDefText, anchor=W)
        self.fairyfourDefLabel.grid(row=21, column=13)

        Label(self.toplevel,text="Checks and Counters").place(x=10, y=470)
        self.counterMssngr = Text(self.toplevel,wrap=WORD)
        self.counterMssngr.place(x=10, y=490, width=250, height=190)
        self.counterMssngr.config(state=DISABLED)
        counterscrollbar = Scrollbar(self.toplevel,command=self.counterMssngr.yview)
        counterscrollbar.place(x=260, y=490, height=190)
        self.counterMssngr["yscrollcommand"] = counterscrollbar.set

        Label(self.toplevel,text="Average Team Stats").place(x=350,y=470)
        Label(self.toplevel,text="HP").place(x=305,y=495)
        Label(self.toplevel,text="Atk").place(x=305,y=528)
        Label(self.toplevel,text="Def").place(x=305,y=561)
        Label(self.toplevel,text="SpA").place(x=305,y=594)
        Label(self.toplevel,text="SpD").place(x=305,y=626)
        Label(self.toplevel,text="Spe").place(x=305,y=660)

        self.averageHPCanvas = Canvas(self.toplevel,width=150, height=20)
        self.averageHPCanvas.place(x=340,y=495)
        self.avHPBar=self.averageHPCanvas.create_rectangle(0, 0, 0, 20, fill="lawn green")
        self.avHP=StringVar()
        self.avHP.set(0)
        Label(self.toplevel,textvariable=self.avHP).place(x=500,y=495)

        self.averageAtkCanvas = Canvas(self.toplevel,width=150, height=20)
        self.averageAtkCanvas.place(x=340,y=528)
        self.avAtkBar =self.averageAtkCanvas.create_rectangle(0, 0, 0, 20, fill="lawn green")
        self.avAtk = StringVar()
        self.avAtk.set(0)
        Label(self.toplevel, textvariable=self.avAtk).place(x=500, y=528)

        self.averageDefCanvas = Canvas(self.toplevel,width=150, height=20)
        self.averageDefCanvas.place(x=340,y=561)
        self.avDefBar =self.averageDefCanvas.create_rectangle(0, 0, 0, 20, fill="lawn green")
        self.avDef = StringVar()
        self.avDef.set(0)
        Label(self.toplevel, textvariable=self.avDef).place(x=500, y=561)

        self.averageSpACanvas = Canvas(self.toplevel,width=150, height=20)
        self.averageSpACanvas.place(x=340,y=594)
        self.avSpABar =self.averageSpACanvas.create_rectangle(0, 0, 0, 20, fill="lawn green")
        self.avSpA = StringVar()
        self.avSpA.set(0)
        Label(self.toplevel, textvariable=self.avSpA).place(x=500, y=594)

        self.averageSpDCanvas = Canvas(self.toplevel,width=150, height=20)
        self.averageSpDCanvas.place(x=340,y=626)
        self.avSpDBar =self.averageSpDCanvas.create_rectangle(0, 0, 0, 20, fill="lawn green")
        self.avSpD = StringVar()
        self.avSpD.set(0)
        Label(self.toplevel, textvariable=self.avSpD).place(x=500, y=626)

        self.averageSpeCanvas = Canvas(self.toplevel,width=150, height=20)
        self.averageSpeCanvas.place(x=340,y=660)
        self.avSpeBar =self.averageSpeCanvas.create_rectangle(0, 0, 0, 20, fill="lawn green")
        self.avSpe = StringVar()
        self.avSpe.set(0)
        Label(self.toplevel, textvariable=self.avSpe).place(x=500, y=660)

        ttk.Separator(self.toplevel,orient=VERTICAL).place(x=340, y=495, height=188)

        Label(self.toplevel,text="Threats").place(x=805,y=470)
        self.threatMssngr = Text(self.toplevel,wrap=WORD)
        self.threatMssngr.place(x=600,y=490,width=250,height=190)
        self.threatMssngr.config(state=DISABLED)
        threatscrollbar = Scrollbar(self.toplevel,command=self.threatMssngr.yview)
        threatscrollbar.place(x=850, y=490,height=190)
        self.threatMssngr["yscrollcommand"] = threatscrollbar.set

        self.sumStats=[]

        self.normalOffArray = []
        self.fireOffArray = []
        self.waterOffArray = []
        self.electricOffArray = []
        self.grassOffArray = []
        self.iceOffArray = []
        self.fightingOffArray = []
        self.poisonOffArray = []
        self.groundOffArray = []
        self.flyingOffArray = []
        self.psychicOffArray = []
        self.bugOffArray = []
        self.rockOffArray = []
        self.ghostOffArray = []
        self.dragonOffArray = []
        self.darkOffArray = []
        self.steelOffArray = []
        self.fairyOffArray = []
        
        self.normalDefArray = []
        self.fireDeffArray = []
        self.waterDefArray = []
        self.electricDefArray = []
        self.grassDefArray = []
        self.iceDefArray = []
        self.fightingDefArray = []
        self.poisonDefArray = []
        self.groundDefArray = []
        self.flyingDefArray = []
        self.psychicDefArray = []
        self.bugDefArray = []
        self.rockDefArray = []
        self.ghostDefArray = []
        self.dragonDefArray = []
        self.darkDefArray = []
        self.steelDefArray = []
        self.fairyDefArray = []
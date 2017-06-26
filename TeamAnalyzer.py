from tkinter import *
from tkinter import ttk
import math, Pokedex, MetaDex, Tools, threading, random, datetime, os, glob

class TeamAnalyzer:

    @staticmethod
    def defCombineTypes(types):
        if isinstance(types,list):
            wri = []
            wri.append([])
            wri.append([])
            wri.append([])
            if len(types)==2 and types[0]!=types[1]:
                wri.append([])
                wri.append([])

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

                done = False
                while not done:
                    done = True
                    for a in w1:
                        for b in w2:
                            if a==b:
                                wri[0].append(a)
                                del w1[w1.index(a)]
                                del w2[w2.index(b)]
                                done = False
                                break
                for a in w1:
                    wri[1].append(a)
                for b in w2:
                    wri[1].append(b)

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
                    wri[4].append(a)
                for b in i2:
                    wri[4].append(b)

                done = False
                while not done:
                    done=True
                    for w in wri[1]:
                        for r in wri[2]:
                            if w==r:
                                del wri[1][wri[1].index(w)]
                                del wri[2][wri[2].index(r)]
                                done=False
                                break

                for a in wri[4]:
                    done = False
                    while not done:
                        done = True
                        for b in wri[2]:
                            if a==b:
                                del wri[2][wri[2].index(b)]
                                done = False
                                break
                    done = False
                    while not done:
                        done = True
                        for b in wri[1]:
                            if a==b:
                                del wri[1][wri[1].index(b)]
                                done = False
                                break
                done = False
                while not done:
                    done = True
                    for a in wri[4]:
                        for b in wri[4]:
                            if a==b and a is not b:
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
                        wri[2].append(i)
            return wri
        else:
            return None

    def offTypeColor(self,typeArray,zeroDef,halfDef,twoDef):
        score = 2*typeArray[2]+typeArray[1]-typeArray[0]
        if score>=2:
            if typeArray[2] != 0:
                zeroDef.config(bg="green2")
            if typeArray[1] != 0:
                halfDef.config(bg="green2")
            if typeArray[0] != 0:
                twoDef.config(bg="sienna1")
        elif -1<=score<=1:
            if typeArray[2] != 0:
                zeroDef.config(bg="green yellow")
            if typeArray[1] != 0:
                halfDef.config(bg="green yellow")
            if typeArray[0] != 0:
                twoDef.config(bg="sienna1")
        else:
            if typeArray[2] != 0:
                zeroDef.config(bg="green yellow")
            if typeArray[1] != 0:
                halfDef.config(bg="green yellow")
            if typeArray[0] != 0:
                twoDef.config(bg="orange red")

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
        elif -1<=score<=1:
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

    def update(self,shell,option):
        if option=="species":
            normalArray = [0, 0, 0, 0, 0]
            fireArray = [0, 0, 0, 0, 0]
            waterArray = [0, 0, 0, 0, 0]
            electricArray = [0, 0, 0, 0, 0]
            grassArray = [0, 0, 0, 0, 0]
            iceArray = [0, 0, 0, 0, 0]
            fightingArray = [0, 0, 0, 0, 0]
            poisonArray = [0, 0, 0, 0, 0]
            groundArray = [0, 0, 0, 0, 0]
            flyingArray = [0, 0, 0, 0, 0]
            psychicArray = [0, 0, 0, 0, 0]
            bugArray = [0, 0, 0, 0, 0]
            rockArray = [0, 0, 0, 0, 0]
            ghostArray = [0, 0, 0, 0, 0]
            dragonArray = [0, 0, 0, 0, 0]
            darkArray = [0, 0, 0, 0, 0]
            steelArray = [0, 0, 0, 0, 0]
            fairyArray = [0, 0, 0, 0, 0]

            typesDict = Pokedex.loadTypes()

            for member in shell.teamMatesDict:
                typesList = Pokedex.findPokemonTypes(member)
                if len(typesList)==2:
                    wriplus = self.defCombineTypes(typesList)
                    for wType in wriplus[0]:
                        if wType == "Normal":
                            normalArray[0]+=1
                        elif wType == "Fire":
                            fireArray[0]+=1
                        elif wType == "Water":
                            waterArray[0]+=1
                        elif wType == "Electric":
                            electricArray[0]+=1
                        elif wType == "Grass":
                            grassArray[0]+=1
                        elif wType == "Ice":
                            iceArray[0]+=1
                        elif wType == "Fighting":
                            fightingArray[0]+=1
                        elif wType == "Poison":
                            poisonArray[0]+=1
                        elif wType == "Ground":
                            groundArray[0]+=1
                        elif wType == "Flying":
                            flyingArray[0]+=1
                        elif wType == "Psychic":
                            psychicArray[0]+=1
                        elif wType == "Bug":
                            bugArray[0]+=1
                        elif wType == "Rock":
                            rockArray[0]+=1
                        elif wType == "Ghost":
                            ghostArray[0]+=1
                        elif wType == "Dragon":
                            dragonArray[0]+=1
                        elif wType == "Dark":
                            darkArray[0]+=1
                        elif wType == "Steel":
                            steelArray[0]+=1
                        elif wType == "Fairy":
                            fairyArray[0]+=1
                        elif wType == "":
                            pass
                        else:
                            print("An error occurred when registering Double Weaknesses")
                    for wType in wriplus[1]:
                        if wType == "Normal":
                            normalArray[1]+=1
                        elif wType == "Fire":
                            fireArray[1]+=1
                        elif wType == "Water":
                            waterArray[1]+=1
                        elif wType == "Electric":
                            electricArray[1]+=1
                        elif wType == "Grass":
                            grassArray[1]+=1
                        elif wType == "Ice":
                            iceArray[1]+=1
                        elif wType == "Fighting":
                            fightingArray[1]+=1
                        elif wType == "Poison":
                            poisonArray[1]+=1
                        elif wType == "Ground":
                            groundArray[1]+=1
                        elif wType == "Flying":
                            flyingArray[1]+=1
                        elif wType == "Psychic":
                            psychicArray[1]+=1
                        elif wType == "Bug":
                            bugArray[1]+=1
                        elif wType == "Rock":
                            rockArray[1]+=1
                        elif wType == "Ghost":
                            ghostArray[1]+=1
                        elif wType == "Dragon":
                            dragonArray[1]+=1
                        elif wType == "Dark":
                            darkArray[1]+=1
                        elif wType == "Steel":
                            steelArray[1]+=1
                        elif wType == "Fairy":
                            fairyArray[1]+=1
                        elif wType == "":
                            pass
                        else:
                            print("An error occurred when registering Weaknesses")
                    for rType in wriplus[2]:
                        if rType == "Normal":
                            normalArray[2]+=1
                        elif rType == "Fire":
                            fireArray[2]+=1
                        elif rType == "Water":
                            waterArray[2]+=1
                        elif rType == "Electric":
                            electricArray[2]+=1
                        elif rType == "Grass":
                            grassArray[2]+=1
                        elif rType == "Ice":
                            iceArray[2]+=1
                        elif rType == "Fighting":
                            fightingArray[2]+=1
                        elif rType == "Poison":
                            poisonArray[2]+=1
                        elif rType == "Ground":
                            groundArray[2]+=1
                        elif rType == "Flying":
                            flyingArray[2]+=1
                        elif rType == "Psychic":
                            psychicArray[2]+=1
                        elif rType == "Bug":
                            bugArray[2]+=1
                        elif rType == "Rock":
                            rockArray[2]+=1
                        elif rType == "Ghost":
                            ghostArray[2]+=1
                        elif rType == "Dragon":
                            dragonArray[2]+=1
                        elif rType == "Dark":
                            darkArray[2]+=1
                        elif rType == "Steel":
                            steelArray[2]+=1
                        elif rType == "Fairy":
                            fairyArray[2]+=1
                        elif rType == "":
                            pass
                        else:
                            print("An error occurred when registering Resistances")
                    for rType in wriplus[3]:
                        if rType == "Normal":
                            normalArray[3]+=1
                        elif rType == "Fire":
                            fireArray[3]+=1
                        elif rType == "Water":
                            waterArray[3]+=1
                        elif rType == "Electric":
                            electricArray[3]+=1
                        elif rType == "Grass":
                            grassArray[3]+=1
                        elif rType == "Ice":
                            iceArray[3]+=1
                        elif rType == "Fighting":
                            fightingArray[3]+=1
                        elif rType == "Poison":
                            poisonArray[3]+=1
                        elif rType == "Ground":
                            groundArray[3]+=1
                        elif rType == "Flying":
                            flyingArray[3]+=1
                        elif rType == "Psychic":
                            psychicArray[3]+=1
                        elif rType == "Bug":
                            bugArray[3]+=1
                        elif rType == "Rock":
                            rockArray[3]+=1
                        elif rType == "Ghost":
                            ghostArray[3]+=1
                        elif rType == "Dragon":
                            dragonArray[3]+=1
                        elif rType == "Dark":
                            darkArray[3]+=1
                        elif rType == "Steel":
                            steelArray[3]+=1
                        elif rType == "Fairy":
                            fairyArray[3]+=1
                        elif rType == "":
                            pass
                        else:
                            print("An error occurred when registering Double Resistances")
                    for iType in wriplus[4]:
                        if iType == "Normal":
                            normalArray[4]+=1
                        elif iType == "Fire":
                            fireArray[4]+=1
                        elif iType == "Water":
                            waterArray[4]+=1
                        elif iType == "Electric":
                            electricArray[4]+=1
                        elif iType == "Grass":
                            grassArray[4]+=1
                        elif iType == "Ice":
                            iceArray[4]+=1
                        elif iType == "Fighting":
                            fightingArray[4]+=1
                        elif iType == "Poison":
                            poisonArray[4]+=1
                        elif iType == "Ground":
                            groundArray[4]+=1
                        elif iType == "Flying":
                            flyingArray[4]+=1
                        elif iType == "Psychic":
                            psychicArray[4]+=1
                        elif iType == "Bug":
                            bugArray[4]+=1
                        elif iType == "Rock":
                            rockArray[4]+=1
                        elif iType == "Ghost":
                            ghostArray[4]+=1
                        elif iType == "Dragon":
                            dragonArray[4]+=1
                        elif iType == "Dark":
                            darkArray[4]+=1
                        elif iType == "Steel":
                            steelArray[4]+=1
                        elif iType == "Fairy":
                            fairyArray[4]+=1
                        elif iType == "":
                            pass
                        else:
                            print("An error occurred when registering Immunities")
                else:
                    w = typesDict[typesList[0]]["weaknesses"]
                    for wType in w:
                        if wType == "Normal":
                            normalArray[1]+=1
                        elif wType == "Fire":
                            fireArray[1]+=1
                        elif wType == "Water":
                            waterArray[1]+=1
                        elif wType == "Electric":
                            electricArray[1]+=1
                        elif wType == "Grass":
                            grassArray[1]+=1
                        elif wType == "Ice":
                            iceArray[1]+=1
                        elif wType == "Fighting":
                            fightingArray[1]+=1
                        elif wType == "Poison":
                            poisonArray[1]+=1
                        elif wType == "Ground":
                            groundArray[1]+=1
                        elif wType == "Flying":
                            flyingArray[1]+=1
                        elif wType == "Psychic":
                            psychicArray[1]+=1
                        elif wType == "Bug":
                            bugArray[1]+=1
                        elif wType == "Rock":
                            rockArray[1]+=1
                        elif wType == "Ghost":
                            ghostArray[1]+=1
                        elif wType == "Dragon":
                            dragonArray[1]+=1
                        elif wType == "Dark":
                            darkArray[1]+=1
                        elif wType == "Steel":
                            steelArray[1]+=1
                        elif wType == "Fairy":
                            fairyArray[1]+=1
                        elif wType == "":
                            pass
                        else:
                            print("An error occurred when registering Weaknesses")
                    r = typesDict[typesList[0]]["resistances"]
                    for rType in r:
                        if rType == "Normal":
                            normalArray[2]+=1
                        elif rType == "Fire":
                            fireArray[2]+=1
                        elif rType == "Water":
                            waterArray[2]+=1
                        elif rType == "Electric":
                            electricArray[2]+=1
                        elif rType == "Grass":
                            grassArray[2]+=1
                        elif rType == "Ice":
                            iceArray[2]+=1
                        elif rType == "Fighting":
                            fightingArray[2]+=1
                        elif rType == "Poison":
                            poisonArray[2]+=1
                        elif rType == "Ground":
                            groundArray[2]+=1
                        elif rType == "Flying":
                            flyingArray[2]+=1
                        elif rType == "Psychic":
                            psychicArray[2]+=1
                        elif rType == "Bug":
                            bugArray[2]+=1
                        elif rType == "Rock":
                            rockArray[2]+=1
                        elif rType == "Ghost":
                            ghostArray[2]+=1
                        elif rType == "Dragon":
                            dragonArray[2]+=1
                        elif rType == "Dark":
                            darkArray[2]+=1
                        elif rType == "Steel":
                            steelArray[2]+=1
                        elif rType == "Fairy":
                            fairyArray[2]+=1
                        elif rType == "":
                            pass
                        else:
                            print("An error occurred when registering Resistances")
                    i = typesDict[typesList[0]]["immunities"]
                    for iType in i:
                        if iType == "Normal":
                            normalArray[4]+=1
                        elif iType == "Fire":
                            fireArray[4]+=1
                        elif iType == "Water":
                            waterArray[4]+=1
                        elif iType == "Electric":
                            electricArray[4]+=1
                        elif iType == "Grass":
                            grassArray[4]+=1
                        elif iType == "Ice":
                            iceArray[4]+=1
                        elif iType == "Fighting":
                            fightingArray[4]+=1
                        elif iType == "Poison":
                            poisonArray[4]+=1
                        elif iType == "Ground":
                            groundArray[4]+=1
                        elif iType == "Flying":
                            flyingArray[4]+=1
                        elif iType == "Psychic":
                            psychicArray[4]+=1
                        elif iType == "Bug":
                            bugArray[4]+=1
                        elif iType == "Rock":
                            rockArray[4]+=1
                        elif iType == "Ghost":
                            ghostArray[4]+=1
                        elif iType == "Dragon":
                            dragonArray[4]+=1
                        elif iType == "Dark":
                            darkArray[4]+=1
                        elif iType == "Steel":
                            steelArray[4]+=1
                        elif iType == "Fairy":
                            fairyArray[4]+=1
                        elif iType == "":
                            pass
                        else:
                            print("An error occurred when registering Immunities")

            self.normalzeroDefText.set(normalArray[4])
            self.normalquarterDefText.set(normalArray[3])
            self.normalhalfDefText.set(normalArray[2])
            self.normaloneDefText.set(len(shell.teamMatesDict)-normalArray[4]-normalArray[3]-normalArray[2]-normalArray[1]-normalArray[0])
            self.normaltwoDefText.set(normalArray[1])
            self.normalfourDefText.set(normalArray[0])
            self.defTypeColor(normalArray,self.normalzeroDefLabel,self.normalquarterDefLabel,self.normalhalfDefLabel,self.normaltwoDefLabel,self.normalfourDefLabel)

            self.firezeroDefText.set(fireArray[4])
            self.firequarterDefText.set(fireArray[3])
            self.firehalfDefText.set(fireArray[2])
            self.fireoneDefText.set(len(shell.teamMatesDict)-fireArray[4]-fireArray[3]-fireArray[2]-fireArray[1]-fireArray[0])
            self.firetwoDefText.set(fireArray[1])
            self.firefourDefText.set(fireArray[0])
            self.defTypeColor(fireArray, self.firezeroDefLabel, self.firequarterDefLabel, self.firehalfDefLabel,self.firetwoDefLabel, self.firefourDefLabel)

            self.waterzeroDefText.set(waterArray[4])
            self.waterquarterDefText.set(waterArray[3])
            self.waterhalfDefText.set(waterArray[2])
            self.wateroneDefText.set(len(shell.teamMatesDict)-waterArray[4]-waterArray[3]-waterArray[2]-waterArray[1]-waterArray[0])
            self.watertwoDefText.set(waterArray[1])
            self.waterfourDefText.set(waterArray[0])
            self.defTypeColor(waterArray, self.waterzeroDefLabel, self.waterquarterDefLabel, self.waterhalfDefLabel,self.watertwoDefLabel, self.waterfourDefLabel)

            self.electriczeroDefText.set(electricArray[4])
            self.electricquarterDefText.set(electricArray[3])
            self.electrichalfDefText.set(electricArray[2])
            self.electriconeDefText.set(len(shell.teamMatesDict)-electricArray[4]-electricArray[3]-electricArray[2]-electricArray[1]-electricArray[0])
            self.electrictwoDefText.set(electricArray[1])
            self.electricfourDefText.set(electricArray[0])
            self.defTypeColor(electricArray, self.electriczeroDefLabel, self.electricquarterDefLabel, self.electrichalfDefLabel,self.electrictwoDefLabel, self.electricfourDefLabel)

            self.grasszeroDefText.set(grassArray[4])
            self.grassquarterDefText.set(grassArray[3])
            self.grasshalfDefText.set(grassArray[2])
            self.grassoneDefText.set(len(shell.teamMatesDict)-grassArray[4]-grassArray[3]-grassArray[2]-grassArray[1]-grassArray[0])
            self.grasstwoDefText.set(grassArray[1])
            self.electricfourDefText.set(grassArray[0])
            self.defTypeColor(grassArray, self.grasszeroDefLabel, self.grassquarterDefLabel, self.grasshalfDefLabel,self.grasstwoDefLabel, self.grassfourDefLabel)

            self.icezeroDefText.set(iceArray[4])
            self.icequarterDefText.set(iceArray[3])
            self.icehalfDefText.set(iceArray[2])
            self.iceoneDefText.set(len(shell.teamMatesDict)-iceArray[4]-iceArray[3]-iceArray[2]-iceArray[1]-iceArray[0])
            self.icetwoDefText.set(iceArray[1])
            self.icefourDefText.set(iceArray[0])
            self.defTypeColor(iceArray, self.icezeroDefLabel, self.icequarterDefLabel, self.icehalfDefLabel,self.icetwoDefLabel, self.icefourDefLabel)

            self.fightingzeroDefText.set(fightingArray[4])
            self.fightingquarterDefText.set(fightingArray[3])
            self.fightinghalfDefText.set(fightingArray[2])
            self.fightingoneDefText.set(len(shell.teamMatesDict)-fightingArray[4]-fightingArray[3]-fightingArray[2]-fightingArray[1]-fightingArray[0])
            self.fightingtwoDefText.set(fightingArray[1])
            self.fightingfourDefText.set(fightingArray[0])
            self.defTypeColor(fightingArray, self.fightingzeroDefLabel, self.fightingquarterDefLabel, self.fightinghalfDefLabel,self.fightingtwoDefLabel, self.fightingfourDefLabel)

            self.poisonzeroDefText.set(poisonArray[4])
            self.poisonquarterDefText.set(poisonArray[3])
            self.poisonhalfDefText.set(poisonArray[2])
            self.poisononeDefText.set(len(shell.teamMatesDict)-poisonArray[4]-poisonArray[3]-poisonArray[2]-poisonArray[1]-poisonArray[0])
            self.poisontwoDefText.set(poisonArray[1])
            self.poisonfourDefText.set(poisonArray[0])
            self.defTypeColor(poisonArray, self.poisonzeroDefLabel, self.poisonquarterDefLabel, self.poisonhalfDefLabel,self.poisontwoDefLabel, self.poisonfourDefLabel)

            self.groundzeroDefText.set(groundArray[4])
            self.groundquarterDefText.set(groundArray[3])
            self.groundhalfDefText.set(groundArray[2])
            self.groundoneDefText.set(len(shell.teamMatesDict)-groundArray[4]-groundArray[3]-groundArray[2]-groundArray[1]-groundArray[0])
            self.groundtwoDefText.set(groundArray[1])
            self.groundfourDefText.set(groundArray[0])
            self.defTypeColor(groundArray, self.groundzeroDefLabel, self.groundquarterDefLabel, self.groundhalfDefLabel,self.groundtwoDefLabel, self.groundfourDefLabel)

            self.flyingzeroDefText.set(flyingArray[4])
            self.flyingquarterDefText.set(flyingArray[3])
            self.flyinghalfDefText.set(flyingArray[2])
            self.flyingoneDefText.set(len(shell.teamMatesDict)-flyingArray[4]-flyingArray[3]-flyingArray[2]-flyingArray[1]-flyingArray[0])
            self.flyingtwoDefText.set(flyingArray[1])
            self.flyingfourDefText.set(flyingArray[0])
            self.defTypeColor(flyingArray, self.flyingzeroDefLabel, self.flyingquarterDefLabel, self.flyinghalfDefLabel,self.flyingtwoDefLabel, self.flyingfourDefLabel)

            self.psychiczeroDefText.set(psychicArray[4])
            self.psychicquarterDefText.set(psychicArray[3])
            self.psychichalfDefText.set(psychicArray[2])
            self.psychiconeDefText.set(len(shell.teamMatesDict)-psychicArray[4]-psychicArray[3]-psychicArray[2]-psychicArray[1]-psychicArray[0])
            self.psychictwoDefText.set(psychicArray[1])
            self.psychicfourDefText.set(psychicArray[0])
            self.defTypeColor(psychicArray, self.psychiczeroDefLabel, self.psychicquarterDefLabel, self.psychichalfDefLabel,self.psychictwoDefLabel, self.psychicfourDefLabel)

            self.bugzeroDefText.set(bugArray[4])
            self.bugquarterDefText.set(bugArray[3])
            self.bughalfDefText.set(bugArray[2])
            self.bugoneDefText.set(len(shell.teamMatesDict)-bugArray[4]-bugArray[3]-bugArray[2]-bugArray[1]-bugArray[0])
            self.bugtwoDefText.set(bugArray[1])
            self.bugfourDefText.set(bugArray[0])
            self.defTypeColor(bugArray, self.bugzeroDefLabel, self.bugquarterDefLabel, self.bughalfDefLabel,self.bugtwoDefLabel, self.bugfourDefLabel)

            self.rockzeroDefText.set(rockArray[4])
            self.rockquarterDefText.set(rockArray[3])
            self.rockhalfDefText.set(rockArray[2])
            self.rockoneDefText.set(len(shell.teamMatesDict)-rockArray[4]-rockArray[3]-rockArray[2]-rockArray[1]-rockArray[0])
            self.rocktwoDefText.set(rockArray[1])
            self.rockfourDefText.set(rockArray[0])
            self.defTypeColor(rockArray, self.rockzeroDefLabel, self.rockquarterDefLabel, self.rockhalfDefLabel,self.rocktwoDefLabel, self.rockfourDefLabel)

            self.ghostzeroDefText.set(ghostArray[4])
            self.ghostquarterDefText.set(ghostArray[3])
            self.ghosthalfDefText.set(ghostArray[2])
            self.ghostoneDefText.set(len(shell.teamMatesDict)-ghostArray[4]-ghostArray[3]-ghostArray[2]-ghostArray[1]-ghostArray[0])
            self.ghosttwoDefText.set(ghostArray[1])
            self.ghostfourDefText.set(ghostArray[0])
            self.defTypeColor(ghostArray, self.ghostzeroDefLabel, self.ghostquarterDefLabel, self.ghosthalfDefLabel,self.ghosttwoDefLabel, self.ghostfourDefLabel)

            self.dragonzeroDefText.set(dragonArray[4])
            self.dragonquarterDefText.set(dragonArray[3])
            self.dragonhalfDefText.set(dragonArray[2])
            self.dragononeDefText.set(len(shell.teamMatesDict)-dragonArray[4]-dragonArray[3]-dragonArray[2]-dragonArray[1]-dragonArray[0])
            self.dragontwoDefText.set(dragonArray[1])
            self.dragonfourDefText.set(dragonArray[0])
            self.defTypeColor(dragonArray, self.dragonzeroDefLabel, self.dragonquarterDefLabel, self.dragonhalfDefLabel,self.dragontwoDefLabel, self.dragonfourDefLabel)

            self.darkzeroDefText.set(darkArray[4])
            self.darkquarterDefText.set(darkArray[3])
            self.darkhalfDefText.set(darkArray[2])
            self.darkoneDefText.set(len(shell.teamMatesDict)-darkArray[4]-darkArray[3]-darkArray[2]-darkArray[1]-darkArray[0])
            self.darktwoDefText.set(darkArray[1])
            self.darkfourDefText.set(darkArray[0])
            self.defTypeColor(darkArray, self.darkzeroDefLabel, self.darkquarterDefLabel, self.darkhalfDefLabel,self.darktwoDefLabel, self.darkfourDefLabel)

            self.steelzeroDefText.set(steelArray[4])
            self.steelquarterDefText.set(steelArray[3])
            self.steelhalfDefText.set(steelArray[2])
            self.steeloneDefText.set(len(shell.teamMatesDict)-steelArray[4]-steelArray[3]-steelArray[2]-steelArray[1]-steelArray[0])
            self.steeltwoDefText.set(steelArray[1])
            self.steelfourDefText.set(steelArray[0])
            self.defTypeColor(steelArray, self.steelzeroDefLabel, self.steelquarterDefLabel, self.steelhalfDefLabel,self.steeltwoDefLabel, self.steelfourDefLabel)

            self.fairyzeroDefText.set(fairyArray[4])
            self.fairyquarterDefText.set(fairyArray[3])
            self.fairyhalfDefText.set(fairyArray[2])
            self.fairyoneDefText.set(len(shell.teamMatesDict)-fairyArray[4]-fairyArray[3]-fairyArray[2]-fairyArray[1]-fairyArray[0])
            self.fairytwoDefText.set(fairyArray[1])
            self.fairyfourDefText.set(fairyArray[0])
            self.defTypeColor(fairyArray, self.fairyzeroDefLabel, self.fairyquarterDefLabel, self.fairyhalfDefLabel,self.fairytwoDefLabel, self.fairyfourDefLabel)

        elif option=="moves":
            normalArray = [0,0,0]
            fireArray = [0,0,0]
            waterArray = [0,0,0]
            electricArray = [0,0,0]
            grassArray = [0,0,0]
            iceArray = [0,0,0]
            fightingArray = [0,0,0]
            poisonArray = [0,0,0]
            groundArray = [0,0,0]
            flyingArray = [0,0,0]
            psychicArray = [0,0,0]
            bugArray = [0,0,0]
            rockArray = [0,0,0]
            ghostArray = [0,0,0]
            dragonArray = [0,0,0]
            darkArray = [0,0,0]
            steelArray = [0,0,0]
            fairyArray = [0,0,0]

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
                                normalArray[0]+=1
                            elif seType == "Fire":
                                fireArray[0]+=1
                            elif seType == "Water":
                                waterArray[0]+=1
                            elif seType == "Electric":
                                electricArray[0]+=1
                            elif seType == "Grass":
                                grassArray[0]+=1
                            elif seType == "Ice":
                                iceArray[0]+=1
                            elif seType == "Fighting":
                                fightingArray[0]+=1
                            elif seType == "Poison":
                                poisonArray[0]+=1
                            elif seType == "Ground":
                                groundArray[0]+=1
                            elif seType == "Flying":
                                flyingArray[0]+=1
                            elif seType == "Psychic":
                                psychicArray[0]+=1
                            elif seType == "Bug":
                                bugArray[0]+=1
                            elif seType == "Rock":
                                rockArray[0]+=1
                            elif seType == "Ghost":
                                ghostArray[0]+=1
                            elif seType == "Dragon":
                                dragonArray[0]+=1
                            elif seType == "Dark":
                                darkArray[0]+=1
                            elif seType == "Steel":
                                steelArray[0]+=1
                            elif seType == "Fairy":
                                fairyArray[0]+=1
                            elif seType == "":
                                pass
                            else:
                                print("An error occurred when registering Super Effectivenesses")
                        nve = typesDict[type]["notVeryEffective"]
                        for nveType in nve:
                            if nveType == "Normal":
                                normalArray[1]+=1
                            elif nveType == "Fire":
                                fireArray[1]+=1
                            elif nveType == "Water":
                                waterArray[1]+=1
                            elif nveType == "Electric":
                                electricArray[1]+=1
                            elif nveType == "Grass":
                                grassArray[1]+=1
                            elif nveType == "Ice":
                                iceArray[1]+=1
                            elif nveType == "Fighting":
                                fightingArray[1]+=1
                            elif nveType == "Poison":
                                poisonArray[1]+=1
                            elif nveType == "Ground":
                                groundArray[1]+=1
                            elif nveType == "Flying":
                                flyingArray[1]+=1
                            elif nveType == "Psychic":
                                psychicArray[1]+=1
                            elif nveType == "Bug":
                                bugArray[1]+=1
                            elif nveType == "Rock":
                                rockArray[1]+=1
                            elif nveType == "Ghost":
                                ghostArray[1]+=1
                            elif nveType == "Dragon":
                                dragonArray[1]+=1
                            elif nveType == "Dark":
                                darkArray[1]+=1
                            elif nveType == "Steel":
                                steelArray[1]+=1
                            elif nveType == "Fairy":
                                fairyArray[1]+=1
                            elif nveType == "":
                                pass
                            else:
                                print("An error occurred when registering Not-Very-Effectivenesses")
                        ne = typesDict[type]["notEffective"]
                        for neType in ne:
                            if neType == "Normal":
                                normalArray[2]+=1
                            elif neType == "Fire":
                                fireArray[2]+=1
                            elif neType == "Water":
                                waterArray[2]+=1
                            elif neType == "Electric":
                                electricArray[2]+=1
                            elif neType == "Grass":
                                grassArray[2]+=1
                            elif neType == "Ice":
                                iceArray[2]+=1
                            elif neType == "Fighting":
                                fightingArray[2]+=1
                            elif neType == "Poison":
                                poisonArray[2]+=1
                            elif neType == "Ground":
                                groundArray[2]+=1
                            elif neType == "Flying":
                                flyingArray[2]+=1
                            elif neType == "Psychic":
                                psychicArray[2]+=1
                            elif neType == "Bug":
                                bugArray[2]+=1
                            elif neType == "Rock":
                                rockArray[2]+=1
                            elif neType == "Ghost":
                                ghostArray[2]+=1
                            elif neType == "Dragon":
                                dragonArray[2]+=1
                            elif neType == "Dark":
                                darkArray[2]+=1
                            elif neType == "Steel":
                                steelArray[2]+=1
                            elif neType == "Fairy":
                                fairyArray[2]+=1
                            elif neType == "":
                                pass
                            else:
                                print("An error occurred when registering No-Effectivenesses")

            self.normalzeroOffText.set(normalArray[2])
            self.normalhalfOffText.set(normalArray[1])
            self.normaloneOffText.set(k-normalArray[2]-normalArray[1]-normalArray[0])
            self.normaltwoOffText.set(normalArray[0])
            #self.offTypeColor(normalArray,self.normalzeroOffLabel,self.normalhalfOffLabel,self.normaltwoOffLabel)

            self.firezeroOffText.set(fireArray[2])
            self.firehalfOffText.set(fireArray[1])
            self.fireoneOffText.set(k-fireArray[2]-fireArray[1]-fireArray[0])
            self.firetwoOffText.set(fireArray[0])
            #self.offTypeColor(fireArray, self.firezeroOffLabel, self.firehalfOffLabel, self.firetwoOffLabel)

            self.waterzeroOffText.set(waterArray[2])
            self.waterhalfOffText.set(waterArray[1])
            self.wateroneOffText.set(k-waterArray[2]-waterArray[1]-waterArray[0])
            self.watertwoOffText.set(waterArray[0])
            #self.offTypeColor(waterArray, self.waterzeroOffLabel, self.waterhalfOffLabel, self.watertwoOffLabel)

            self.electriczeroOffText.set(electricArray[2])
            self.electrichalfOffText.set(electricArray[1])
            self.electriconeOffText.set(k-electricArray[2]-electricArray[1]-electricArray[0])
            self.electrictwoOffText.set(electricArray[0])
            #self.offTypeColor(electricArray, self.electriczeroOffLabel, self.electrichalfOffLabel, self.electrictwoOffLabel)

            self.grasszeroOffText.set(grassArray[2])
            self.grasshalfOffText.set(grassArray[1])
            self.grassoneOffText.set(k-grassArray[2]-grassArray[1]-grassArray[0])
            self.grasstwoOffText.set(grassArray[0])
            #self.offTypeColor(grassArray, self.grasszeroOffLabel, self.grasshalfOffLabel, self.grasstwoOffLabel)

            self.icezeroOffText.set(iceArray[2])
            self.icehalfOffText.set(iceArray[1])
            self.iceoneOffText.set(k-iceArray[2]-iceArray[1]-iceArray[0])
            self.icetwoOffText.set(iceArray[0])
            #self.offTypeColor(iceArray, self.icezeroOffLabel, self.icehalfOffLabel, self.icetwoOffLabel)

            self.fightingzeroOffText.set(fightingArray[2])
            self.fightinghalfOffText.set(fightingArray[1])
            self.fightingoneOffText.set(k-fightingArray[2]-fightingArray[1]-fightingArray[0])
            self.fightingtwoOffText.set(fightingArray[0])
            #self.offTypeColor(fightingArray, self.fightingzeroOffLabel, self.fightinghalfOffLabel, self.fightingtwoOffLabel)

            self.poisonzeroOffText.set(poisonArray[2])
            self.poisonhalfOffText.set(poisonArray[1])
            self.poisononeOffText.set(k-poisonArray[2]-poisonArray[1]-poisonArray[0])
            self.poisontwoOffText.set(poisonArray[0])
            #self.offTypeColor(poisonArray, self.poisonzeroOffLabel, self.poisonhalfOffLabel, self.poisontwoOffLabel)

            self.groundzeroOffText.set(groundArray[2])
            self.groundhalfOffText.set(groundArray[1])
            self.groundoneOffText.set(k-groundArray[2]-groundArray[1]-groundArray[0])
            self.groundtwoOffText.set(groundArray[0])
            #self.offTypeColor(groundArray, self.groundzeroOffLabel, self.groundhalfOffLabel, self.groundtwoOffLabel)

            self.flyingzeroOffText.set(flyingArray[2])
            self.flyinghalfOffText.set(flyingArray[1])
            self.flyingoneOffText.set(k-flyingArray[2]-flyingArray[1]-flyingArray[0])
            self.flyingtwoOffText.set(flyingArray[0])
            #self.offTypeColor(flyingArray, self.flyingzeroOffLabel, self.flyinghalfOffLabel, self.flyingtwoOffLabel)

            self.psychiczeroOffText.set(psychicArray[2])
            self.psychichalfOffText.set(psychicArray[1])
            self.psychiconeOffText.set(k-psychicArray[2]-psychicArray[1]-psychicArray[0])
            self.psychictwoOffText.set(psychicArray[0])
            #self.offTypeColor(psychicArray, self.psychiczeroOffLabel, self.psychichalfOffLabel, self.psychictwoOffLabel)

            self.bugzeroOffText.set(bugArray[2])
            self.bughalfOffText.set(bugArray[1])
            self.bugoneOffText.set(k-bugArray[2]-bugArray[1]-bugArray[0])
            self.bugtwoOffText.set(bugArray[0])
            #self.offTypeColor(bugArray, self.bugzeroOffLabel, self.bughalfOffLabel, self.bugtwoOffLabel)

            self.rockzeroOffText.set(rockArray[2])
            self.rockhalfOffText.set(rockArray[1])
            self.rockoneOffText.set(k-rockArray[2]-rockArray[1]-rockArray[0])
            self.rocktwoOffText.set(rockArray[0])
            #self.offTypeColor(rockArray, self.rockzeroOffLabel, self.rockhalfOffLabel, self.rocktwoOffLabel)

            self.ghostzeroOffText.set(ghostArray[2])
            self.ghosthalfOffText.set(ghostArray[1])
            self.ghostoneOffText.set(k-ghostArray[2]-ghostArray[1]-ghostArray[0])
            self.ghosttwoOffText.set(ghostArray[0])
            #self.offTypeColor(ghostArray, self.ghostzeroOffLabel, self.ghosthalfOffLabel, self.ghosttwoOffLabel)

            self.dragonzeroOffText.set(dragonArray[2])
            self.dragonhalfOffText.set(dragonArray[1])
            self.dragononeOffText.set(k-dragonArray[2]-dragonArray[1]-dragonArray[0])
            self.dragontwoOffText.set(dragonArray[0])
            #self.offTypeColor(dragonArray, self.dragonzeroOffLabel, self.dragonhalfOffLabel, self.dragontwoOffLabel)

            self.darkzeroOffText.set(darkArray[2])
            self.darkhalfOffText.set(darkArray[1])
            self.darkoneOffText.set(k-darkArray[2]-darkArray[1]-darkArray[0])
            self.darktwoOffText.set(darkArray[0])
            #self.offTypeColor(darkArray, self.darkzeroOffLabel, self.darkhalfOffLabel, self.darktwoOffLabel)

            self.steelzeroOffText.set(steelArray[2])
            self.steelhalfOffText.set(steelArray[1])
            self.steeloneOffText.set(k-steelArray[2]-steelArray[1]-steelArray[0])
            self.steeltwoOffText.set(steelArray[0])
            #self.offTypeColor(steelArray, self.steelzeroOffLabel, self.steelhalfOffLabel, self.steeltwoOffLabel)

            self.fairyzeroOffText.set(fairyArray[2])
            self.fairyhalfOffText.set(fairyArray[1])
            self.fairyoneOffText.set(k-fairyArray[2]-fairyArray[1]-fairyArray[0])
            self.fairytwoOffText.set(fairyArray[0])
            #self.offTypeColor(fairyArray, self.fairyzeroOffLabel, self.fairyhalfOffLabel, self.fairytwoOffLabel)

        else:
            print("Whoops, something went wrong with the options for the team analyzer")

    def __init__(self,shell,toplevel):
        toplevel.geometry("872x700")
        toplevel.title("Team Analyzer")
        offCovFrame = Frame(toplevel)
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
        Label(offCovFrame, textvariable=self.normalzeroOffText, anchor=W).grid(row=4, column=3)
        self.normalhalfOffText = StringVar()
        self.normalhalfOffText.set("0")
        Label(offCovFrame, textvariable=self.normalhalfOffText, anchor=W).grid(row=4, column=5)
        self.normaloneOffText = StringVar()
        self.normaloneOffText.set("0")
        Label(offCovFrame, textvariable=self.normaloneOffText, anchor=W).grid(row=4, column=7)
        self.normaltwoOffText = StringVar()
        self.normaltwoOffText.set("0")
        Label(offCovFrame, textvariable=self.normaltwoOffText, anchor=W).grid(row=4, column=9)

        Label(offCovFrame, text="Fire", anchor=W).grid(row=5, column=1, pady=1)
        self.firezeroOffText = StringVar()
        self.firezeroOffText.set("0")
        Label(offCovFrame, textvariable=self.firezeroOffText, anchor=W).grid(row=5, column=3)
        self.firehalfOffText = StringVar()
        self.firehalfOffText.set("0")
        Label(offCovFrame, textvariable=self.firehalfOffText, anchor=W).grid(row=5, column=5)
        self.fireoneOffText = StringVar()
        self.fireoneOffText.set("0")
        Label(offCovFrame, textvariable=self.fireoneOffText, anchor=W).grid(row=5, column=7)
        self.firetwoOffText = StringVar()
        self.firetwoOffText.set("0")
        Label(offCovFrame, textvariable=self.firetwoOffText, anchor=W).grid(row=5, column=9)

        Label(offCovFrame, text="Water", anchor=W).grid(row=6, column=1, pady=1)
        self.waterzeroOffText = StringVar()
        self.waterzeroOffText.set("0")
        Label(offCovFrame, textvariable=self.waterzeroOffText, anchor=W).grid(row=6, column=3)
        self.waterhalfOffText = StringVar()
        self.waterhalfOffText.set("0")
        Label(offCovFrame, textvariable=self.waterhalfOffText, anchor=W).grid(row=6, column=5)
        self.wateroneOffText = StringVar()
        self.wateroneOffText.set("0")
        Label(offCovFrame, textvariable=self.wateroneOffText, anchor=W).grid(row=6, column=7)
        self.watertwoOffText = StringVar()
        self.watertwoOffText.set("0")
        Label(offCovFrame, textvariable=self.watertwoOffText, anchor=W).grid(row=6, column=9)

        Label(offCovFrame, text="Electric", anchor=W).grid(row=7, column=1, pady=1)
        self.electriczeroOffText = StringVar()
        self.electriczeroOffText.set("0")
        Label(offCovFrame, textvariable=self.electriczeroOffText, anchor=W).grid(row=7, column=3)
        self.electrichalfOffText = StringVar()
        self.electrichalfOffText.set("0")
        Label(offCovFrame, textvariable=self.electrichalfOffText, anchor=W).grid(row=7, column=5)
        self.electriconeOffText = StringVar()
        self.electriconeOffText.set("0")
        Label(offCovFrame, textvariable=self.electriconeOffText, anchor=W).grid(row=7, column=7)
        self.electrictwoOffText = StringVar()
        self.electrictwoOffText.set("0")
        Label(offCovFrame, textvariable=self.electrictwoOffText, anchor=W).grid(row=7, column=9)

        Label(offCovFrame, text="Grass", anchor=W).grid(row=8, column=1, pady=1)
        self.grasszeroOffText = StringVar()
        self.grasszeroOffText.set("0")
        Label(offCovFrame, textvariable=self.grasszeroOffText, anchor=W).grid(row=8, column=3)
        self.grasshalfOffText = StringVar()
        self.grasshalfOffText.set("0")
        Label(offCovFrame, textvariable=self.grasshalfOffText, anchor=W).grid(row=8, column=5)
        self.grassoneOffText = StringVar()
        self.grassoneOffText.set("0")
        Label(offCovFrame, textvariable=self.grassoneOffText, anchor=W).grid(row=8, column=7)
        self.grasstwoOffText = StringVar()
        self.grasstwoOffText.set("0")
        Label(offCovFrame, textvariable=self.grasstwoOffText, anchor=W).grid(row=8, column=9)

        Label(offCovFrame, text="Ice", anchor=W).grid(row=9, column=1, pady=1)
        self.icezeroOffText = StringVar()
        self.icezeroOffText.set("0")
        Label(offCovFrame, textvariable=self.icezeroOffText, anchor=W).grid(row=9, column=3)
        self.icehalfOffText = StringVar()
        self.icehalfOffText.set("0")
        Label(offCovFrame, textvariable=self.icehalfOffText, anchor=W).grid(row=9, column=5)
        self.iceoneOffText = StringVar()
        self.iceoneOffText.set("0")
        Label(offCovFrame, textvariable=self.iceoneOffText, anchor=W).grid(row=9, column=7)
        self.icetwoOffText = StringVar()
        self.icetwoOffText.set("0")
        Label(offCovFrame, textvariable=self.icetwoOffText, anchor=W).grid(row=9, column=9)

        Label(offCovFrame, text="Fighting", anchor=W).grid(row=10, column=1, pady=1)
        self.fightingzeroOffText = StringVar()
        self.fightingzeroOffText.set("0")
        Label(offCovFrame, textvariable=self.fightingzeroOffText, anchor=W).grid(row=10, column=3)
        self.fightinghalfOffText = StringVar()
        self.fightinghalfOffText.set("0")
        Label(offCovFrame, textvariable=self.fightinghalfOffText, anchor=W).grid(row=10, column=5)
        self.fightingoneOffText = StringVar()
        self.fightingoneOffText.set("0")
        Label(offCovFrame, textvariable=self.fightingoneOffText, anchor=W).grid(row=10, column=7)
        self.fightingtwoOffText = StringVar()
        self.fightingtwoOffText.set("0")
        Label(offCovFrame, textvariable=self.fightingtwoOffText, anchor=W).grid(row=10, column=9)

        Label(offCovFrame, text="Poison", anchor=W).grid(row=11, column=1, pady=1)
        self.poisonzeroOffText = StringVar()
        self.poisonzeroOffText.set("0")
        Label(offCovFrame, textvariable=self.poisonzeroOffText, anchor=W).grid(row=11, column=3)
        self.poisonhalfOffText = StringVar()
        self.poisonhalfOffText.set("0")
        Label(offCovFrame, textvariable=self.poisonhalfOffText, anchor=W).grid(row=11, column=5)
        self.poisononeOffText = StringVar()
        self.poisononeOffText.set("0")
        Label(offCovFrame, textvariable=self.poisononeOffText, anchor=W).grid(row=11, column=7)
        self.poisontwoOffText = StringVar()
        self.poisontwoOffText.set("0")
        Label(offCovFrame, textvariable=self.poisontwoOffText, anchor=W).grid(row=11, column=9)

        Label(offCovFrame, text="Ground", anchor=W).grid(row=12, column=1, pady=1)
        self.groundzeroOffText = StringVar()
        self.groundzeroOffText.set("0")
        Label(offCovFrame, textvariable=self.groundzeroOffText, anchor=W).grid(row=12, column=3)
        self.groundhalfOffText = StringVar()
        self.groundhalfOffText.set("0")
        Label(offCovFrame, textvariable=self.groundhalfOffText, anchor=W).grid(row=12, column=5)
        self.groundoneOffText = StringVar()
        self.groundoneOffText.set("0")
        Label(offCovFrame, textvariable=self.groundoneOffText, anchor=W).grid(row=12, column=7)
        self.groundtwoOffText = StringVar()
        self.groundtwoOffText.set("0")
        Label(offCovFrame, textvariable=self.groundtwoOffText, anchor=W).grid(row=12, column=9)

        Label(offCovFrame, text="Flying", anchor=W).grid(row=13, column=1, pady=1)
        self.flyingzeroOffText = StringVar()
        self.flyingzeroOffText.set("0")
        Label(offCovFrame, textvariable=self.flyingzeroOffText, anchor=W).grid(row=13, column=3)
        self.flyinghalfOffText = StringVar()
        self.flyinghalfOffText.set("0")
        Label(offCovFrame, textvariable=self.flyinghalfOffText, anchor=W).grid(row=13, column=5)
        self.flyingoneOffText = StringVar()
        self.flyingoneOffText.set("0")
        Label(offCovFrame, textvariable=self.flyingoneOffText, anchor=W).grid(row=13, column=7)
        self.flyingtwoOffText = StringVar()
        self.flyingtwoOffText.set("0")
        Label(offCovFrame, textvariable=self.flyingtwoOffText, anchor=W).grid(row=13, column=9)

        Label(offCovFrame, text="Psychic", anchor=W).grid(row=14, column=1, pady=1)
        self.psychiczeroOffText = StringVar()
        self.psychiczeroOffText.set("0")
        Label(offCovFrame, textvariable=self.psychiczeroOffText, anchor=W).grid(row=14, column=3)
        self.psychichalfOffText = StringVar()
        self.psychichalfOffText.set("0")
        Label(offCovFrame, textvariable=self.psychichalfOffText, anchor=W).grid(row=14, column=5)
        self.psychiconeOffText = StringVar()
        self.psychiconeOffText.set("0")
        Label(offCovFrame, textvariable=self.psychiconeOffText, anchor=W).grid(row=14, column=7)
        self.psychictwoOffText = StringVar()
        self.psychictwoOffText.set("0")
        Label(offCovFrame, textvariable=self.psychictwoOffText, anchor=W).grid(row=14, column=9)

        Label(offCovFrame, text="Bug", anchor=W).grid(row=15, column=1, pady=1)
        self.bugzeroOffText = StringVar()
        self.bugzeroOffText.set("0")
        Label(offCovFrame, textvariable=self.bugzeroOffText, anchor=W).grid(row=15, column=3)
        self.bughalfOffText = StringVar()
        self.bughalfOffText.set("0")
        Label(offCovFrame, textvariable=self.bughalfOffText, anchor=W).grid(row=15, column=5)
        self.bugoneOffText = StringVar()
        self.bugoneOffText.set("0")
        Label(offCovFrame, textvariable=self.bugoneOffText, anchor=W).grid(row=15, column=7)
        self.bugtwoOffText = StringVar()
        self.bugtwoOffText.set("0")
        Label(offCovFrame, textvariable=self.bugtwoOffText, anchor=W).grid(row=15, column=9)

        Label(offCovFrame, text="Rock", anchor=W).grid(row=16, column=1, pady=1)
        self.rockzeroOffText = StringVar()
        self.rockzeroOffText.set("0")
        Label(offCovFrame, textvariable=self.rockzeroOffText, anchor=W).grid(row=16, column=3)
        self.rockhalfOffText = StringVar()
        self.rockhalfOffText.set("0")
        Label(offCovFrame, textvariable=self.rockhalfOffText, anchor=W).grid(row=16, column=5)
        self.rockoneOffText = StringVar()
        self.rockoneOffText.set("0")
        Label(offCovFrame, textvariable=self.rockoneOffText, anchor=W).grid(row=16, column=7)
        self.rocktwoOffText = StringVar()
        self.rocktwoOffText.set("0")
        Label(offCovFrame, textvariable=self.rocktwoOffText, anchor=W).grid(row=16, column=9)

        Label(offCovFrame, text="Ghost", anchor=W).grid(row=17, column=1, pady=1)
        self.ghostzeroOffText = StringVar()
        self.ghostzeroOffText.set("0")
        Label(offCovFrame, textvariable=self.ghostzeroOffText, anchor=W).grid(row=17, column=3)
        self.ghosthalfOffText = StringVar()
        self.ghosthalfOffText.set("0")
        Label(offCovFrame, textvariable=self.ghosthalfOffText, anchor=W).grid(row=17, column=5)
        self.ghostoneOffText = StringVar()
        self.ghostoneOffText.set("0")
        Label(offCovFrame, textvariable=self.ghostoneOffText, anchor=W).grid(row=17, column=7)
        self.ghosttwoOffText = StringVar()
        self.ghosttwoOffText.set("0")
        Label(offCovFrame, textvariable=self.ghosttwoOffText, anchor=W).grid(row=17, column=9)

        Label(offCovFrame, text="Dragon", anchor=W).grid(row=18, column=1, pady=1)
        self.dragonzeroOffText = StringVar()
        self.dragonzeroOffText.set("0")
        Label(offCovFrame, textvariable=self.dragonzeroOffText, anchor=W).grid(row=18, column=3)
        self.dragonhalfOffText = StringVar()
        self.dragonhalfOffText.set("0")
        Label(offCovFrame, textvariable=self.dragonhalfOffText, anchor=W).grid(row=18, column=5)
        self.dragononeOffText = StringVar()
        self.dragononeOffText.set("0")
        Label(offCovFrame, textvariable=self.dragononeOffText, anchor=W).grid(row=18, column=7)
        self.dragontwoOffText = StringVar()
        self.dragontwoOffText.set("0")
        Label(offCovFrame, textvariable=self.dragontwoOffText, anchor=W).grid(row=18, column=9)

        Label(offCovFrame, text="Dark", anchor=W).grid(row=19, column=1, pady=1)
        self.darkzeroOffText = StringVar()
        self.darkzeroOffText.set("0")
        Label(offCovFrame, textvariable=self.darkzeroOffText, anchor=W).grid(row=19, column=3)
        self.darkhalfOffText = StringVar()
        self.darkhalfOffText.set("0")
        Label(offCovFrame, textvariable=self.darkhalfOffText, anchor=W).grid(row=19, column=5)
        self.darkoneOffText = StringVar()
        self.darkoneOffText.set("0")
        Label(offCovFrame, textvariable=self.darkoneOffText, anchor=W).grid(row=19, column=7)
        self.darktwoOffText = StringVar()
        self.darktwoOffText.set("0")
        Label(offCovFrame, textvariable=self.darktwoOffText, anchor=W).grid(row=19, column=9)

        Label(offCovFrame, text="Steel", anchor=W).grid(row=20, column=1, pady=1)
        self.steelzeroOffText = StringVar()
        self.steelzeroOffText.set("0")
        Label(offCovFrame, textvariable=self.steelzeroOffText, anchor=W).grid(row=20, column=3)
        self.steelhalfOffText = StringVar()
        self.steelhalfOffText.set("0")
        Label(offCovFrame, textvariable=self.steelhalfOffText, anchor=W).grid(row=20, column=5)
        self.steeloneOffText = StringVar()
        self.steeloneOffText.set("0")
        Label(offCovFrame, textvariable=self.steeloneOffText, anchor=W).grid(row=20, column=7)
        self.steeltwoOffText = StringVar()
        self.steeltwoOffText.set("0")
        Label(offCovFrame, textvariable=self.steeltwoOffText, anchor=W).grid(row=20, column=9)

        Label(offCovFrame, text="Fairy", anchor=W).grid(row=21, column=1, pady=1)
        self.fairyzeroOffText = StringVar()
        self.fairyzeroOffText.set("0")
        Label(offCovFrame, textvariable=self.fairyzeroOffText, anchor=W).grid(row=21, column=3)
        self.fairyhalfOffText = StringVar()
        self.fairyhalfOffText.set("0")
        Label(offCovFrame, textvariable=self.fairyhalfOffText, anchor=W).grid(row=21, column=5)
        self.fairyoneOffText = StringVar()
        self.fairyoneOffText.set("0")
        Label(offCovFrame, textvariable=self.fairyoneOffText, anchor=W).grid(row=21, column=7)
        self.fairytwoOffText = StringVar()
        self.fairytwoOffText.set("0")
        Label(offCovFrame, textvariable=self.fairytwoOffText, anchor=W).grid(row=21, column=9)

        middleFrame = Frame(toplevel)
        middleFrame.pack(side=LEFT, fill=Y)
        Label(middleFrame,text="Physical/Special Balances").grid(row=0,column=0,columnspan=2,sticky=EW)
        Label(middleFrame,text="Offenive Balance").grid(row=1,column=0,columnspan=2,sticky=EW)
        physpecOffCanvas = Canvas(middleFrame, height=20)
        physpecOffCanvas.grid(row=2,column=0,columnspan=2,padx=10,sticky=EW)
        self.offBalance=50
        size=physpecOffCanvas.winfo_reqwidth()
        physpecOffCanvas.create_rectangle(0,0,self.offBalance,20,fill="orange red")
        physpecOffCanvas.create_rectangle(self.offBalance,0,size,20,fill="cornflower blue")

        Label(middleFrame, text="Defensive Balance").grid(row=3,column=0,columnspan=2,sticky=EW)
        self.physpecDefCanvas = Canvas(middleFrame, height=20)
        self.physpecDefCanvas.grid(row=4,column=0,columnspan=2,padx=10,sticky=EW)
        self.defBalance = 50
        self.physpecDefCanvas.create_rectangle(0, 0, self.defBalance, 20, fill="orange red")
        self.physpecDefCanvas.create_rectangle(self.defBalance, 0, size, 20, fill="cornflower blue")

        self.adviceMssngr = Text(middleFrame, wrap=WORD,width=45,height=21)
        self.adviceMssngr.grid(row=5,column=0,pady=10,padx=(10,0),sticky=EW)
        self.adviceMssngr.config(state=DISABLED)
        advicescrollbar = Scrollbar(middleFrame, command=self.adviceMssngr.yview)
        advicescrollbar.grid(row=5,column=1,padx=(0,10),pady=10,sticky=NS)
        self.adviceMssngr["yscrollcommand"] = advicescrollbar.set

        defCovFrame = Frame(toplevel)
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

        Label(toplevel,text="Counters").place(x=10, y=470)
        self.counterMssngr = Text(toplevel,wrap=WORD)
        self.counterMssngr.place(x=10, y=490, width=250, height=190)
        #self.counterMssngr.config(state=DISABLED)
        counterscrollbar = Scrollbar(toplevel,command=self.counterMssngr.yview)
        counterscrollbar.place(x=260, y=490, height=190)
        self.counterMssngr["yscrollcommand"] = counterscrollbar.set

        Label(toplevel,text="Average Team Stats").place(x=350,y=470)
        Label(toplevel,text="HP").place(x=305,y=495)
        Label(toplevel,text="Atk").place(x=305,y=528)
        Label(toplevel,text="Def").place(x=305,y=561)
        Label(toplevel,text="SpA").place(x=305,y=594)
        Label(toplevel,text="SpD").place(x=305,y=626)
        Label(toplevel,text="Spe").place(x=305,y=660)
        self.averageHPCanvas = Canvas(toplevel,width=150, height=20)
        self.averageHPCanvas.place(x=340,y=495)
        self.averageHPCanvas.create_rectangle(0, 0, 150, 20, fill="lawn green")
        self.averageAtkCanvas = Canvas(toplevel,width=150, height=20)
        self.averageAtkCanvas.place(x=340,y=528)
        self.averageAtkCanvas.create_rectangle(0, 0, 150, 20, fill="lawn green")
        self.averageDefCanvas = Canvas(toplevel,width=150, height=20)
        self.averageDefCanvas.place(x=340,y=561)
        self.averageDefCanvas.create_rectangle(0, 0, 150, 20, fill="lawn green")
        self.averageSpACanvas = Canvas(toplevel,width=150, height=20)
        self.averageSpACanvas.place(x=340,y=594)
        self.averageSpACanvas.create_rectangle(0, 0, 150, 20, fill="lawn green")
        self.averageSpDCanvas = Canvas(toplevel,width=150, height=20)
        self.averageSpDCanvas.place(x=340,y=626)
        self.averageSpDCanvas.create_rectangle(0, 0, 150, 20, fill="lawn green")
        self.averageSpeCanvas = Canvas(toplevel,width=150, height=20)
        self.averageSpeCanvas.place(x=340,y=660)
        self.averageSpeCanvas.create_rectangle(0, 0, 150, 20, fill="lawn green")
        ttk.Separator(toplevel,orient=VERTICAL).place(x=340, y=495, height=188)

        Label(toplevel,text="Threats").place(x=805,y=470)
        self.threatMssngr = Text(toplevel,wrap=WORD)
        self.threatMssngr.place(x=600,y=490,width=250,height=190)
        self.threatMssngr.config(state=DISABLED)
        threatscrollbar = Scrollbar(toplevel,command=self.threatMssngr.yview)
        threatscrollbar.place(x=850, y=490,height=190)
        self.threatMssngr["yscrollcommand"] = threatscrollbar.set

#root = Tk()
#root.resizable(width=False, height=False)
#tl = Toplevel(root)
#TeamAnalyzer(1,tl)
#root.mainloop()

#TeamAnalyzer.defCombineTypes(["Steel","Steel"])
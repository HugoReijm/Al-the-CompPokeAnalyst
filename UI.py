import TeamBuilder,MetaDex,Pokedex,datetime,random,sys

#Function to Add Another TeamMember
def teamAdder():
    teamAdderGate = False
    while not teamAdderGate:
        if len(teamMateNames)==0 :
            print("Which Pokemon would you like to start your team with?")
            res = input("Input: (String) ")
        else:
            if "anythinggoes" not in tier:
                print("Which Pokemon would you like to add to your team? Note that your team can not have two or more Pokemon with the same National Pokedex number!")
                res = input("Input: (String) ")
            else:
                print("Which Pokemon would you like to add to your team?")
                res = input("Input: (String) ")
        species = Pokedex.findPokemonSpecies(res)
        if species != None:
            if MetaDex.findPokemonTierData(species, tierfile) != None:
                if "anythinggoes" not in tier:
                    numList = []
                    for str in teamMateNames:
                        numList.append(Pokedex.findPokemonNum(str))
                    if Pokedex.findPokemonNum(species) in numList:
                        print("Oh, you can not have two or more Pokemon with the same National Pokedex number! You must select another Pokemon.")
                    else:
                        forme = Pokedex.findPokemonForme(species)
                        if forme == "Mega":
                            megaChecks = []
                            for teamMate in teamMateNames:
                                if Pokedex.findPokemonForme(teamMate) == "Mega":
                                    megaChecks.append(False)
                                else:
                                    megaChecks.append(True)
                            if all(megaChecks):
                                teamMateNames.append(species)
                                teamAdderGate = True
                            else:
                                print(
                                    "Oh, I see that you're trying to add another mega to your team. I mean, this is technically allowed, but I wouldn't suggest it. You can only use one mega per battle.")
                                multiMegaGate = False
                                while not multiMegaGate:
                                    print("Are you sure you want multiple megas in your team?")
                                    res = input("Input: (Y/N) ")
                                    if res == "Y":
                                        print("Alright, I'll add another mega then!")
                                        teamMateNames.append(species)
                                        multiMegaGate = True
                                        teamAdderGate = True
                                    elif res == "N":
                                        multiMegaGate = True
                                    else:
                                        print("Um...I don't understand your response...")
                        else:
                            teamMateNames.append(species)
                            teamAdderGate = True
                else:
                    forme = Pokedex.findPokemonForme(species)
                    if forme=="Mega":
                        megaChecks = []
                        for teamMate in teamMateNames:
                            if Pokedex.findPokemonForme(teamMate)=="Mega":
                                megaChecks.append(False)
                            else:
                                megaChecks.append(True)
                        if all(megaChecks):
                            teamMateNames.append(species)
                            teamAdderGate = True
                        else:
                            print("Oh, I see that you're trying to add another mega to your team. I mean, this is technically allowed, but I wouldn't suggest it. You can only use one mega per battle.")
                            multiMegaGate=False
                            while not multiMegaGate:
                                print("Are you sure you want multiple megas in your team?")
                                res = input("Input: (Y/N) ")
                                if res=="Y":
                                    print("Alright, I'll add another mega then!")
                                    teamMateNames.append(species)
                                    multiMegaGate = True
                                    teamAdderGate = True
                                elif res=="N":
                                    multiMegaGate = True
                                else:
                                    print("Um...I don't understand your response...")
                    else:
                        teamMateNames.append(species)
                        teamAdderGate = True
            else:
                print("Oh, I'm sorry. There seems to be a problem.")
                print("Either Pokemon %s is not allowed in tier %s." % (res, tier))
                print("Or it might be that Pokemon %s is SO rare in tier %s that there isn't enough data on it" % (res, tier))
                print("Either way, I suggest chosing another Pokemon. That way I have the data necessary to help you")

print("Hello! I'm Al, here to help build your personal competitive Pokemon team!\nThe great thing is, after we have built your team, I'll automatically export your team so you can easily import it into Pokemon Showdown,\na Competitive Pokemon Battle Simulator used by hundreds of people every day!\n\nLet's get started!")

#Display All Tiers Downloaded Tiers
print("First, we need to decide which tier this team will be used in.")
tiers = MetaDex.getTiers()
for t in range(len(tiers)):
    tList = list(tiers[t])
    cut = tList.index("-")
    tiers[t] = "".join(tList)[:cut]
isDone = False
while not isDone:
    isDone = True
    for t in range(len(tiers)):
        for s in range(len(tiers)-1,t,-1):
            if tiers[s] == tiers[t]:
                del tiers[s]
                isDone = False

#Chosing a Tier
print("Please input one of the following:")
for t in tiers:
    print(t)
chooseTierGate = False
while not chooseTierGate:
    print("Which tier would you like to work in?")
    tier = input("Input: (String) ")
    if tier in tiers:
        confirmTierGate = False
        while not confirmTierGate:
            print("You would like to build a team for %s?" % tier)
            res = input("Input: (Y/N) ")
            if res == "Y":
                chooseTierGate = True
                confirmTierGate = True
            elif res =="N":
                confirmTierGate = True
            else:
                print("Um...I don't understand your response...")
    else:
        print("Um...I don't understand your response...")

#Select Level of Competitiveness
print("Ok, now how hard core do you want to make this team? You have 4 options.")
print("\tFun")
print("\tSerious")
print("\tHard Core")
print("\tChampion")
tierSeverityGate = False
while not tierSeverityGate:
    print("So, what will it be?")
    res= input("Input: (String) ")
    if res in ["fun","Fun"]:
        tier = tier+"-0"
        tierSeverityGate = True
    elif res in ["serious","Serious"]:
        tier = tier+"-1500"
        tierSeverityGate = True
    elif res in ["hard core","hard Core","Hard Core","Hard Core","hardcore","hardCore","Hardcore","HardCore"]:
        if "ou" in tier:
            tier = tier+"-1695"
        else:
            tier = tier+"-1630"
        tierSeverityGate = True
    elif res in ["champion","Champion"]:
        if "ou" in tier:
            tier = tier+"-1825"
        else:
            tier = tier+"-1760"
        tierSeverityGate = True
    else:
        print("Um, I don't understand that response. You must pick one of the four options shown above.")
tierfile = tier+".json"
print("Excellent! Let's get started with your team then!")
print()

#Helping the User Start a New Team and Selecting First Team Member
firstMemberGate = False
while not firstMemberGate:
    print("So, do you know which Pokemon you want to start your team with?")
    res = input("Input: (Y/N) ")
    if res == "Y":
        firstMemberGate = True
        print("Great! Innovation makes a great team!")
    elif res == "N":
        firstMemberGate = True
        print("That's ok. There are plenty of Pokemon to choose from. Let me give you a few suggestions.")
        for poke in TeamBuilder.rawCountTopFinds(tierfile,20):
            print("%s:\n\tPOP: %s" %(poke[0],poke[1]))
    else:
        print("Um... I don't understand your response ")
pokedex = Pokedex.loadPokedex()
teamMateNames = []
teamAdder()

#Adding Other 5 Members
for i in range(5):
    print("Ok, let me suggest some team-mates. How many suggestions would you like to see?")
    memberSelectGate = False
    while not memberSelectGate:
        try:
            teamSuggAmount = int(input("Input: (Int) "))
            memberSelectGate = True
        except:
            print("Um...I don't understand your response...")
    for t in TeamBuilder.findTeamMetaMatches(teamMateNames, tierfile, teamSuggAmount):
        print("%s:\n\tPOP: %s" % (t[0], t[1]))
    print()
    teamAdder()

print("Here is your team!")
for t in teamMateNames:
    print(t)
print()

#Switching Team Members If Needed
confirmTeamGate=False
while not confirmTeamGate:
    print("Are you happy with the selection?")
    res = input("Input: (Y/N) ")
    if res == "Y":
        confirmTeamGate = True
    elif res !="Y" and res!="N":
        print("Um...I don't understand that response...")
    else:
        #Finding Flip
        flipMemberGate = False
        while not flipMemberGate:
            print("Which Pokemon in your team would you like to swap?")
            flip = input("Input: (String) ")
            flipName = Pokedex.findPokemonSpecies(flip)
            if flipName in teamMateNames:
                flipMemberGate = True
            else:
                print("Pokemon %s isn't part of your team" % flip)
        #Showing Team Mate Options
        print("Ok, let me suggest some team-mates. How many suggestions would you like to see?")
        swapAmountGate = False
        while not swapAmountGate:
            try:
                swapAmount = int(input("Input: (Int) "))
                teamMateNamesprime = []
                for i in range(len(teamMateNames)):
                    teamMateNamesprime.append(teamMateNames[i])
                del teamMateNamesprime[teamMateNamesprime.index(flipName)]
                swapAmountGate = True
            except:
                print("Um...unfortunately I can't understand your request. Try again")
        for t in TeamBuilder.findTeamMetaMatches(teamMateNamesprime, tierfile, swapAmount):
            print("%s: %s" % (t[0], t[1]))
        print()
        #Finding Flop and Checking if it's another Mega
        flopMemberGate = False
        while not flopMemberGate:
            if "anythinggoes" not in tier:
                print("Which Pokemon in your team would you like to swap %s with? Note that your team can not have two or more Pokemon with the same National Pokedex number!" % flipName)
                flop = input("Input: (String) ")
            else:
                print("Which Pokemon in your team would you like to swap %s with?" % flipName)
                flop = input("Input: (String) ")
            flopName = Pokedex.findPokemonSpecies(flop)
            if flopName != None:
                data = MetaDex.findPokemonTierData(flopName,tierfile)
                if data!=None:
                    if "anythinggoes" not in tier:
                        numList = []
                        for str in teamMateNames:
                            numList.append(Pokedex.findPokemonNum(str))
                        if Pokedex.findPokemonNum(flopName) in numList:
                            print("Oh, you can not have two or more Pokemon with the same National Pokedex number! You must select another Pokemon.")
                        else:
                            forme = Pokedex.findPokemonForme(flopName)
                            if forme == "Mega":
                                megaChecks = []
                                for teamMate in teamMateNames:
                                    if Pokedex.findPokemonForme(teamMate) == "Mega":
                                        megaChecks.append(False)
                                    else:
                                        megaChecks.append(True)
                                if all(megaChecks):
                                    teamMateNames[teamMateNames.index(flipName)]=flopName
                                    print("Done! I switched %s with %s." % (flipName,flopName))
                                    flopMemberGate=True
                                else:
                                    print("Oh, I see that you're trying to add another mega to your team. I mean, this is techniaclly allowed, but I wouldn't suggest it. You can only use one mega per battle.")
                                    multiMegaGate = False
                                    while not multiMegaGate:
                                        print("Are you sure you want multiple megas in your team?")
                                        res = input("Input: (Y/N) ")
                                        if res == "Y":
                                            print("Alright, I'll add another mega then!")
                                            teamMateNames[teamMateNames.index(flipName)]=flopName
                                            print("Done! I switched %s with %s." % (flipName,flopName))
                                            flopMemberGate=True
                                            multiMegaGate = True
                                        elif res == "N":
                                            multiMegaGate = True
                                        else:
                                            print("Um...I don't understand your response...")
                            else:
                                teamMateNames[teamMateNames.index(flipName)]=flopName
                                print("Done! I switched %s with %s." % (flipName,flopName))
                                flopMemberGate=True
                    else:
                        forme = Pokedex.findPokemonForme(flopName)
                        if forme == "Mega":
                            megaChecks = []
                            for teamMate in teamMateNames:
                                if Pokedex.findPokemonForme(teamMate) == "Mega":
                                    megaChecks.append(False)
                                else:
                                    megaChecks.append(True)
                            if all(megaChecks):
                                teamMateNames[teamMateNames.index(flipName)] = flopName
                                print("Done! I switched %s with %s." % (flipName, flopName))
                                flopMemberGate = True
                            else:
                                print(
                                    "Oh, I see that you're trying to add another mega to your team. I mean, this is techniaclly allowed, but I wouldn't suggest it. You can only use one mega per battle.")
                                multiMegaGate = False
                                while not multiMegaGate:
                                    print("Are you sure you want multiple megas in your team?")
                                    res = input("Input: (Y/N) ")
                                    if res == "Y":
                                        print("Alright, I'll add another mega then!")
                                        teamMateNames[teamMateNames.index(flipName)] = flopName
                                        print("Done! I switched %s with %s." % (flipName, flopName))
                                        flopMemberGate = True
                                        multiMegaGate = True
                                    elif res == "N":
                                        multiMegaGate = True
                                    else:
                                        print("Um...I don't understand your response...")
                        else:
                            teamMateNames[teamMateNames.index(flipName)] = flopName
                            print("Done! I switched %s with %s." % (flipName, flopName))
                            flopMemberGate = True
                else:
                    print("Oh, I'm sorry. There seems to be a problem.")
                    print("Either Pokemon %s is not allowed in tier %s." % (flop, tier))
                    print("Or it might be that Pokemon %s is SO rare in tier %s that there isn't enough data on it" % (flop, tier))
                    print("Either way, I suggest chosing another Pokemon. That way I have the data necessary to help you")
            else:
                print("The inputted Pokemon is not an actual Pokemon! Try again")
print()
print("Excellent! Here is your team!")
for t in teamMateNames:
    print(t)
print()
print("Your team is coming along great. Let's move on to the individual team members")

#Make Dictionary with All Necessary Info
teamMatesDict = {}
for member in teamMateNames:
    dict={}
    dict["species"]=Pokedex.findPokemonSpecies(member)
    dict["ability"]=None
    dict["nature"]=None
    dict["baseStats"]={"hp":Pokedex.findPokemonHP(member),"atk":Pokedex.findPokemonAtk(member),"def":Pokedex.findPokemonDef(member),"spa":Pokedex.findPokemonSpA(member),"spd":Pokedex.findPokemonSpD(member),"spe":Pokedex.findPokemonSpe(member)}
    dict["ivs"]={"hp":31,"atk":31,"def":31,"spa":31,"spd":31,"spe":31}
    dict["evs"]={"hp":None,"atk":None,"def":None,"spa":None,"spd":None,"spe":None}
    dict["item"]=None
    dict["gender"]=None
    dict["item"]=None
    if member == "Rayquaza-Mega":
        dict["moves"]={"move1":"Dragon Ascent","move2":None,"move3":None,"move4":None}
    else:
        dict["moves"] = {"move1": None, "move2": None, "move3": None, "move4": None}
    dict["happiness"]=None
    dict["level"]=None
    dict["shiny"]=None
    teamMatesDict[member]=dict

#Iterate Over Every Team Member
for poke in teamMatesDict:
    spName = teamMatesDict[poke]["species"]
    if teamMateNames.index(poke)==0:
        print("Let's start with %s." % spName)
    else:
        print("Now let's take a look at %s." % spName)
    print("%s has the following base stats." % spName)
    for stat in teamMatesDict[poke]["baseStats"]:
        if stat == "hp":
            print("%s : %s" % (stat,teamMatesDict[poke]["baseStats"][stat]))
        else:
            print("%s: %s" % (stat,teamMatesDict[poke]["baseStats"][stat]))
    print()

    #Choosing Ability
    abilities = Pokedex.findPokemonAbilities(spName)
    metaAbilities = MetaDex.findPokemonTierAbilities(spName,tierfile)
    print("%s can have the following abilities." % spName)
    print("\t%s:\n\t\tDESC: %s\n\t\tPOP: %s" % (abilities["0"],Pokedex.findAbilityShortDesc(abilities["0"]),metaAbilities[Pokedex.findAbilityID(abilities["0"])]))
    if len(metaAbilities) > 1:
        if "1" in abilities:
            print("\t%s:\n\t\tDESC: %s\n\t\tPOP: %s" % (abilities["1"], Pokedex.findAbilityShortDesc(abilities["1"]),metaAbilities[Pokedex.findAbilityID(abilities["1"])]))
        if "S" in abilities and TeamBuilder.compress(abilities["S"]) in metaAbilities:
            print("Additionally, %s also has a special ability." % spName)
            print("\t%s:\n\t\tDESC: %s\n\t\tPOP: %s" % (abilities["S"], Pokedex.findAbilityShortDesc(abilities["S"]),metaAbilities[Pokedex.findAbilityID(abilities["S"])]))
        if "H" in abilities and TeamBuilder.compress(abilities["H"]) in metaAbilities:
            print("Additionally, %s also has the following hidden ability." % spName)
            print("\t%s:\n\t\tDESC: %s\n\t\tPOP: %s" % (abilities["H"], Pokedex.findAbilityShortDesc(abilities["H"]),metaAbilities[Pokedex.findAbilityID(abilities["H"])]))
        print()
        abilityGate = False
        while not abilityGate:
            print("What ability would you like %s to have?" % spName)
            inp = input("Input: (String) ")
            for s in ["0","1","S","H"]:
                abName = Pokedex.findAbilityName(inp)
                if s in abilities and abName == abilities[s]:
                    teamMatesDict[poke]["ability"]=abName
                    abilityGate = True
            if not abilityGate:
                print("I'm sorry, but %s is not an ability that %s can have." % (spName,inp))
    else:
        print("As you can see, %s only has one ability, so we don't have much choice here. I'll update your %s automatically, so you dont have to worry about that." % (spName,spName))
        teamMatesDict[poke]["ability"] = abilities["0"]
    print("Done! Your %s now has the ability %s" % (spName,teamMatesDict[poke]["ability"]))
    print()

    print("Now that we have that decided, let's move on to IV and Nature/EV spreads")

    #Choosing IVs
    print("First thing's first: I propose to give your %s the following IV spread: 31/31/31/31/31/31" % spName)
    print("This is by far the most common IV spread for Pokemon. However, if you have something more specific in mind, you might want a different IV spread")
    ivGate = False
    while not ivGate:
        print("Do you want to use this IV spread?")
        res = input("Input: (Y/N) ")
        if res == "Y":
            ivGate = True
        elif res != "N" and res != "Y":
            print("Um...I don't understand that response...")
        else:
            #Selecting Hidden Power
            hpGate = False
            while not hpGate:
                print("Would you like to give %s the move Hidden Power (Category: Special, Power: 60, Type: Depends on user's IVs)? \nRemember that Hidden Power CAN NOT have a Fairy or Normal typing." % spName)
                hidpowRes = input("Input: (Y/N) ")
                if hidpowRes == "Y":
                    ivTypeGate = False
                    while not ivTypeGate:
                        print("What type would you like Hidden Power to be?")
                        typeInput = input("Input: (String) ")
                        types = Pokedex.loadTypes()
                        tList = list(typeInput)
                        tList[0] = tList[0].capitalize()
                        typeInput = "".join(tList)
                        teamMatesDict[spName]["moves"]["move1"] = "Hidden Power "+typeInput
                        if typeInput in types and typeInput!="Normal" and typeInput!="Fairy":
                            print("Ok, here are a few IV spreads that result in Hidden Power having a %s typing." % typeInput)
                            for set in types[typeInput]["hp Sets"]:
                                print("\t %s:" % set)
                                for i in range(len(types[typeInput]["hp Sets"][set])):
                                    print("\t\t %s" % types[typeInput]["hp Sets"][set][i])
                                ivTypeGate = True
                        elif typeInput=="Fairy" or typeInput=="Normal":
                            print("I told you that Hidden Power can not have a Fairy or Normal typing! Didn't you pay attention?")
                        else:
                            print("Um...I don't understand that response...")
                    hpGate = True
                elif hidpowRes == "N":
                    hpGate = True
                else:
                    print("Um...I don't understand that response")

            #Choosing EVs
            print("What kind of IVs should %s have?" % spName)
            for string in ["hp","atk","def","spa","spd","spe"]:
                ivGate = False
                while not ivGate:
                    iv = input("%s: " % string)
                    try:
                        iv = int(iv)
                        if 0 <= iv <= 31:
                            teamMatesDict[spName]["ivs"][string] = iv
                            ivGate = True
                        else:
                            print("Oh, I'm sorry, but I can't give %s %s %s Ivs. Try again" % (spName, iv, string.capitalize()))
                    except:
                        print("Um...how can I give %s %s %s IVs? Try again" % (spName, iv, string.capitalize()))

            print("Your %s currently has the following IV spread." % spName)
            print("%s/%s/%s/%s/%s/%s" % (teamMatesDict[spName]["ivs"]["hp"],teamMatesDict[spName]["ivs"]["atk"],teamMatesDict[spName]["ivs"]["def"],teamMatesDict[spName]["ivs"]["spa"],teamMatesDict[spName]["ivs"]["spd"],teamMatesDict[spName]["ivs"]["spe"]))
    print("Great! Now your %s has the following IV spread: %s/%s/%s/%s/%s/%s." % (spName,teamMatesDict[spName]["ivs"]["hp"],teamMatesDict[spName]["ivs"]["atk"],teamMatesDict[spName]["ivs"]["def"],teamMatesDict[spName]["ivs"]["spa"],teamMatesDict[spName]["ivs"]["spd"],teamMatesDict[spName]["ivs"]["spe"]))
    print()

    #Choosing Natures
    print("Alright, it's time for Natures and EVs")
    print("%s has a few common Nature/EV spreads. How many would you like to see?" % spName)
    gate8 = False
    while not gate8:
        try:
            evAmount = int(input("Input: (Int) "))
            sortedSpreads = TeamBuilder.findPokemonMetaSpreads(spName, tierfile, evAmount)
            gate8 = True
        except:
            print("How can I show you that many Nature/EV spreads? Try again")
    for s in range(len(sortedSpreads)):
        print("\t%s:\n\t\tPOP: %s" % (sortedSpreads[s][0], sortedSpreads[s][1]))
    print()
    natureGate = False
    while not natureGate:
        print("What Nature would you like to give to %s?" % spName)
        res = input("Input: (String) ")
        rList = list(res)
        rList[0] = rList[0].capitalize()
        res = "".join(rList)
        if res in ["Hardy","Lonely","Adamant","Naughty","Brave","Bold","Docile","Impish","Lax","Relaxed","Modest","Mild","Bashful","Rash","Quiet","Calm","Gentle","Careful","Quirky","Sassy","Timid","Hasty","Jolly","Naive","Serious"]:
            teamMatesDict[spName]["nature"]=res
            natureGate = True
        else:
            print("Um...that's not a defined nature, so I can't assign that to %s. Try again." % spName)
    print("Excellent, now your %s has a %s nature!" % (spName,teamMatesDict[spName]["nature"]))
    print()

    #Choosing EVs
    print("And now it's time for EVs.")
    topNatureSpread = None
    for i in range(len(sortedSpreads)):
        if sortedSpreads[i][0].split(":")[0]==teamMatesDict[spName]["nature"]:
            topNatureSpread =sortedSpreads[i][0].split(":")[1]
            print("I'll start you off with the most common EV spread for your chosen Nature. In this case, that would be %s." %topNatureSpread)
            break
    if topNatureSpread == None:
        print("I couldn't immediately find any common EV spreads for your chosen Nature, but here is the most common EV spread currently in use: %s." %sortedSpreads[0][0].split(":")[1])
    parts = sortedSpreads[0][0].split(":")
    parts2 = parts[1].split("/")
    teamMatesDict[spName]["evs"]["hp"] = int(parts2[0])
    teamMatesDict[spName]["evs"]["atk"] = int(parts2[1])
    teamMatesDict[spName]["evs"]["def"] = int(parts2[2])
    teamMatesDict[spName]["evs"]["spa"] = int(parts2[3])
    teamMatesDict[spName]["evs"]["spd"] = int(parts2[4])
    teamMatesDict[spName]["evs"]["spe"] = int(parts2[5])
    evGate = False
    while not evGate:
        print("Do you want to use this EV spread?")
        res = input("Input: (Y/N) ")
        if res == "Y":
            evGate = True
        elif res != "N" and res != "Y":
            print("Um...I don't understand that response...")
        else:
            print("What kind of EVs should %s have? \nRemember, each Stat can effectively only have a maximum of 252 EVs, and the total can not effectively be larger than 508." % spName)
            available = 508
            for string in ["hp","atk","def","spa","spd","spe"]:
                evGate = False
                while not evGate:
                    print("Number of EVs available: %s" % available)
                    ev = input("%s: " % string)
                    try:
                        ev = int(ev)
                        if 0 <= ev <= 252:
                            if available - ev >= 0:
                                available = available - ev
                                teamMatesDict[spName]["evs"][string] = ev
                            else:
                                print("You exceeded the limit on your total EVs. Hey, I didn't make the rules...")
                        else:
                            print("Oh, I'm sorry, but I can't give %s %s HP EVs. Try again" % (spName, ev))
                    except:
                        print("Um...how can I give %s %s HP EVs? Try again" % (spName, ev))
            print("Your %s currently has the following IV spread." % spName)
            print("%s/%s/%s/%s/%s/%s" % (teamMatesDict[spName]["evs"]["hp"],teamMatesDict[spName]["evs"]["atk"],teamMatesDict[spName]["evs"]["def"],teamMatesDict[spName]["evs"]["spa"],teamMatesDict[spName]["evs"]["spd"],teamMatesDict[spName]["evs"]["spe"]))
    print("Great! Now your %s has the following EV spread: %s/%s/%s/%s/%s/%s." % (spName,teamMatesDict[spName]["evs"]["hp"],teamMatesDict[spName]["evs"]["atk"],teamMatesDict[spName]["evs"]["def"],teamMatesDict[spName]["evs"]["spa"],teamMatesDict[spName]["evs"]["spd"],teamMatesDict[spName]["evs"]["spe"]))
    print()

    #Selecting Gender
    print("Ok, now we have to change gears a little. Time to talk about your Pokemon's gender")
    if Pokedex.findPokemonGender(spName)!=None:
        print("Ah, this Pokemon has be a specific gender according to it's species. Don't worry, I'll take care of that")
        if Pokedex.findPokemonGender(spName)!="N":
            teamMatesDict[spName]["gender"]=Pokedex.findPokemonGender(spName)
    else:
        genderGate = False
        while not genderGate:
            print("Do you have a specific gender in mind for %s?" % spName)
            res = input("Input: (Y/N) ")
            if res == "N":
                print("Ok, I'll pick a gender at random for you then.")
                genPick = random.randrange(1,10)
                if genPick<=5:
                    teamMatesDict[spName]["gender"]="M"
                    genderGate = True
                else:
                    teamMatesDict[spName]["gender"]="F"
                    genderGate = True
            elif res == "Y":
                pickGenderGate = False
                while not pickGenderGate:
                    print("Which gender would you like to make your %s?" % spName)
                    pickRes = input("Input: (String) ")
                    if pickRes in ["M","m","Male","male","Man","man"]:
                        teamMatesDict[spName]["gender"] = "M"
                        pickGenderGate = True
                        genderGate = True
                    elif pickRes in ["F","f","Female","female","Woman","woman"]:
                        teamMatesDict[spName]["gender"] = "F"
                        pickGenderGate = True
                        genderGate = True
                    else:
                        print("Um...I don't understand that response")
            else:
                print("Um, I don't understand that response...")
    print("Done! Your %s is now has of the %s gender!" % (spName,teamMatesDict[spName]["gender"]))
    print()

    #Show Popular Moves
    print("Alright, now hey comes the REALLY important part: selecting moves.\tI'll show you a few of the most common moves that %s can have." % spName)
    moveset = MetaDex.findPokemonTierMoves(spName,tierfile)
    if len(moveset)==1:
        print("Oh, this Pokemon species can only learn 1 move! I set whatever moves I can, k?")
        moves[0] = Pokedex.findMoveName(list(moveset.keys())[0])
        moves[1] = None
        moves[2] = None
        moves[3] = None
    elif len(moveset)==2:
        print("Oh, this Pokemon species can only learn 2 moves! I set whatever moves I can, k?")
        moves[0] = Pokedex.findMoveName(list(moveset.keys())[0])
        moves[1] = Pokedex.findMoveName(list(moveset.keys())[1])
        moves[2] = None
        moves[3] = None
    elif len(moveset)==3:
        print("Oh, this Pokemon species can only learn 3 moves! I set whatever moves I can, k?")
        moves[0] = Pokedex.findMoveName(list(moveset.keys())[0])
        moves[1] = Pokedex.findMoveName(list(moveset.keys())[1])
        moves[2] = Pokedex.findMoveName(list(moveset.keys())[2])
        moves[3] = None
    elif len(moveset)==4:
        print("Oh, this Pokemon species can only learn 4 moves! I set whatever moves I can, k?")
        moves[0] = Pokedex.findMoveName(list(moveset.keys())[0])
        moves[1] = Pokedex.findMoveName(list(moveset.keys())[1])
        moves[2] = Pokedex.findMoveName(list(moveset.keys())[2])
        moves[3] = Pokedex.findMoveName(list(moveset.keys())[3])
    else:
        print("How many would you like to see?")
        showMovesGate = False
        while not showMovesGate:
            try:
                moveAmount = int(input("Input: (Int) "))
                sortedMoves = TeamBuilder.findPokemonMetaMoves(spName, tierfile, moveAmount)
                showMovesGate = True
            except:
                print("How can I show you that many Moves? Try again")
        for s in range(len(sortedMoves)):
            if sortedMoves[s][0] != "Nothing" and sortedMoves[s][0]!="":
                print("\t%s:\n\t\tCAT: %s,\n\t\tTYPE: %s,\n\t\tPP: %s,\n\t\tBASEPOW: %s,\n\t\tPOP: %s,\n\t\tDESC: %s" % (Pokedex.findMoveName(sortedMoves[s][0]), Pokedex.findMoveCategory(sortedMoves[s][0]), Pokedex.findMoveType(sortedMoves[s][0]),Pokedex.findMovePP(sortedMoves[s][0]),Pokedex.findMoveBasePower(sortedMoves[s][0]),sortedMoves[s][1],Pokedex.findMoveShortDesc(sortedMoves[s][0])))
            else:
                print("\tNothing:\n\t\tCAT: Nothing,\n\t\tTYPE: Nothing,\n\t\tPP: 0,\n\t\tBASEPOW: 0,\n\t\tPOP: 0,\n\t\tDESC: Does nothing")
        print()

        #Select All Moves
        moves = [teamMatesDict[spName]["moves"]["move1"], teamMatesDict[spName]["moves"]["move2"],teamMatesDict[spName]["moves"]["move3"], teamMatesDict[spName]["moves"]["move4"]]
        if teamMatesDict[spName]["moves"]["move1"] == None:
            move1Gate = False
            while not move1Gate:
                print("Which move would you like %s to have in move slot #1?" % spName)
                res = input("Input: (String) ")
                resName = Pokedex.findMoveName(res)
                if resName != None:
                    if Pokedex.findMoveID(res) in MetaDex.findPokemonTierMoves(spName, tierfile):
                        moves[0] = resName
                        move1Gate = True
                    else:
                        print("Oh, there seems to be a problem. Either %s can't learn this move, or it is used SO rarely that I couldn't find any useful data. In any case, try a different move." % spName)
                else:
                    print("I'm sorry, but that is not a valid move. Try again")
            print("Understood")
        else:
            print("Due to meeting various requirements, your first move for your %s has already been chosen. So that's already done!" % teamMatesDict[spName]["moves"]["move1"])
        for moveIndex in [2,3,4]:
            moveGate = False
            while not moveGate:
                print("Which move would you like %s to have in move slot #%s?" % (spName,moveIndex))
                res = input("Input: (String) ")
                if res in ["None", "none", "Null", "null"]:
                    moves[moveIndex] = None
                    moveGate = True
                else:
                    resName = Pokedex.findMoveName(res)
                    if resName != None:
                        if Pokedex.findMoveID(res) in MetaDex.findPokemonTierMoves(spName, tierfile):
                            if resName not in moves:
                                moves[moveIndex-1] = resName
                                moveGate = True
                            else:
                                print("Oh, you already have %s as a move for your %s. Please select a different move." % (
                                resName, spName))
                        else:
                            print("Oh, there seems to be a problem. Either %s can't learn this move, or it is used SO rarely that I couldn't find any useful data. In any case, try a different move." % spName)
                    else:
                        print("I'm sorry, but that is not a valid move. Try again")
            print("Understood")

    #Switching Moves Around
    movesCheckGate = False
    while not movesCheckGate:
        print("Your %s will have the following moves." % spName)
        print("Move 1: %s" % moves[0])
        print("Move 2: %s" % moves[1])
        print("Move 3: %s" % moves[2])
        print("Move 4: %s" % moves[3])
        print("Do you want to keep this moveset? Y/N")
        res = input("Input: (Y/N) ")
        if res == "Y":
            movesCheckGate = True
        elif res != "Y" and res != "N":
            print("Um...I don't understand that response...")
        else:
            #Selecting Flip
            flipMoveGate = False
            while not flipMoveGate:
                print("Which move would you like to swap?")
                flip = input("Input: (String) ")
                if flip in ["None", "none", "Null", "null"]:
                    flipName = None
                    flipMoveGate = True
                else:
                    flipName = Pokedex.findMoveName(flip)
                    if flipName in moves and flipName!= None:
                        flipMoveGate = True
                    else:
                        print("%s isn't part of your current moveset!" % flip)

            #Showing Move Options
            print("Ok, let me show you the most commonly-used moves again. How many suggestions would you like to see?")
            flipAmountGate = False
            while not flipAmountGate:
                try:
                    swapAmount = int(input("Input: (Int) "))
                    if swapAmount >= 0:
                        sortedMoves = TeamBuilder.findPokemonMetaMovesExc(spName, tierfile, swapAmount, moves)
                        flipAmountGate = True
                    else:
                        print("Well I can't suggest that many suggestions, now can I?")
                except:
                    print("Well that doesn't make any sense. Try again")
            for t in sortedMoves:
                print("\t%s:\n\t\tCAT: %s,\n\t\tTYPE: %s,\n\t\tPP: %s,\n\t\tBASEPOW: %s,\n\t\tPOP: %s,\n\t\tDESC: %s" % (Pokedex.findMoveName(t[0]), Pokedex.findMoveCategory(t[0]),Pokedex.findMoveType(t[0]), Pokedex.findMovePP(t[0]),Pokedex.findMoveBasePower(t[0]), t[1],Pokedex.findMoveShortDesc(t[0])))
            print()

            #Selecting Flop
            flopMoveGate = False
            while not flopMoveGate:
                print("Which move would you like to swap %s with?" % flipName)
                flop = input("Input: (String) ")
                if flop in ["None", "none", "Null", "null"]:
                    placeholder = moves.index(flipName)
                    moves[placeholder] = None
                    allNone = [False,False,False,False]
                    for i in range(len(moves)):
                        if moves[i] == None:
                            allNone[i] = True
                    if all(allNone):
                        print("Oh dear, it seems that you just made a completely empty moveset! That's not allowed in Pokemon: each Pokemon must have at least ONE move")
                        moves[placeholder] = flipName
                    else:
                        flopMoveGate = True
                else:
                    flopName = Pokedex.findMoveName(flop)
                    if flopName != None:
                        if Pokedex.findMoveID(flop) in MetaDex.findPokemonTierMoves(spName, tierfile):
                            if flopName not in moves:
                                if "Hidden Power" in flopName:
                                    print("Oh, I see you want to add Hidden Power to your arsenal. That's fine, but we will then need to change your IV's then.")
                                    maxIVs = Pokedex.findTypeHPSpreads(flopName[13])["max all"][0]
                                    maxIVList = maxIVs.split("/")
                                    try:
                                        teamMatesDict[spName]["ivs"]["hp"]=int(maxIVList[0])
                                        teamMatesDict[spName]["ivs"]["atk"] = int(maxIVList[1])
                                        teamMatesDict[spName]["ivs"]["def"] = int(maxIVList[2])
                                        teamMatesDict[spName]["ivs"]["spa"] = int(maxIVList[3])
                                        teamMatesDict[spName]["ivs"]["spd"] = int(maxIVList[4])
                                        teamMatesDict[spName]["ivs"]["spe"] = int(maxIVList[5])
                                        moves[moves.index(flipName)] = flopName
                                        print("I've set your IVs to be the maximum they can be and still compatible with %s.\nIf you don't like this selection, you can always change it later when you import your team into Pokemon Showdown." % flopName)
                                        flopMoveGate = True
                                    except:
                                        print("An error has occurred with the data. Huh, how did that escape me? Don't worry, its not your fault, but this is unexpected and could potentially be serious.\nI'm going to exist this program. Please contact my programmer immediately.")
                                        sys.exit()
                                else:
                                    moves[moves.index(flipName)] = flopName
                                    flopMoveGate = True
                            else:
                                print("Oh, you already have %s as a move for your %s. Please select a different move." % (flopName,spName))
                        else:
                            print("Oh, there seems to be a problem. Either %s can't learn this move, or it is used SO rarely that I couldn't find any useful data. In any case, try a different move." % spName)
                    else:
                        print("I'm sorry, but that is not a valid move. Try again")
    teamMatesDict[spName]["moves"]["move1"] = moves[0]
    teamMatesDict[spName]["moves"]["move2"] = moves[1]
    teamMatesDict[spName]["moves"]["move3"] = moves[2]
    teamMatesDict[spName]["moves"]["move4"] = moves[3]
    print("Excellent! Your %s now has the following moves!" % spName)
    print(teamMatesDict[spName]["moves"]["move1"])
    print(teamMatesDict[spName]["moves"]["move2"])
    print(teamMatesDict[spName]["moves"]["move3"])
    print(teamMatesDict[spName]["moves"]["move4"])
    print()

    #Selecting Items
    print("Alright, it's time to look at items.")
    if len(MetaDex.findPokemonTierItems(spName, tierfile))>1:
        if "Fling" in [teamMatesDict[spName]["moves"]["move1"],teamMatesDict[spName]["moves"]["move2"],teamMatesDict[spName]["moves"]["move3"],teamMatesDict[spName]["moves"]["move4"]]:
            print("Ah yes, your %s has the move Fling! Fling's power and effect depends on the user's item (the item is then used up). Here are a few interesting items and effects.\nFor the full list, check out Serebii: https://www.serebii.net/games/fling.shtml"% spName)
            print("\t%s:\n\t\tDESC: %s\n\t\tFLING'S POWER: %s\n\t\tFLING'S EFFECT: None\n" % (Pokedex.findItemName("iron ball"),Pokedex.findItemDesc("iron ball"),Pokedex.findItemFlingBasePower("iron ball")))
            print("\t%s:\n\t\tDESC: %s\n\t\tFLING'S POWER: %s\n\t\tFLING'S EFFECT: Burns opponent\n" % (Pokedex.findItemName("flame orb"), Pokedex.findItemDesc("flame orb"),Pokedex.findItemFlingBasePower("flame orb")))
            print("\t%s:\n\t\tDESC: %s\n\t\tFLING'S POWER: %s\n\t\tFLING'S EFFECT: Paralyses opponent\n" % (Pokedex.findItemName("light ball"), Pokedex.findItemDesc("light ball"),Pokedex.findItemFlingBasePower("light ball")))
            print("\t%s:\n\t\tDESC: %s\n\t\tFLING'S POWER: %s\n\t\tFLING'S EFFECT: Badly poisons opponent\n" % (Pokedex.findItemName("toxic orb"), Pokedex.findItemDesc("toxic orb"),Pokedex.findItemFlingBasePower("toxic orb")))
            print("\t%s:\n\t\tDESC: %s\n\t\tFLING'S POWER: %s\n\t\tFLING'S EFFECT: Flinches opponent\n" % (Pokedex.findItemName("king's rock"), Pokedex.findItemDesc("king's rock"),Pokedex.findItemFlingBasePower("king's rock")))
            print("\t%s:\n\t\tDESC: %s\n\t\tFLING'S POWER: %s\n\t\tFLING'S EFFECT: Restores Stat Changes on opponent\n" % (Pokedex.findItemName("white herb"), Pokedex.findItemDesc("white herb"),Pokedex.findItemFlingBasePower("white herb")))
            print("\t%s:\n\t\tDESC: %s\n\t\tFLING'S POWER: %s\n\t\tFLING'S EFFECT: Opponent recovers from any status problem\n" % (Pokedex.findItemName("lum berry"), Pokedex.findItemDesc("lum berry"),Pokedex.findItemFlingBasePower("lum berry")))

        if "Natural Gift" in [teamMatesDict[spName]["moves"]["move1"], teamMatesDict[spName]["moves"]["move2"],teamMatesDict[spName]["moves"]["move3"], teamMatesDict[spName]["moves"]["move4"]]:
            print("Ah yes, your %s has the move Natural Gift! Natural Gift's power and effect depends on the user's held berry (the berry is then used up). Here are a few interesting berries and effects.\nFor the full list, check out Serebii: https://www.serebii.net/games/naturalgift.shtml" % spName)
            print("As a special note, the power that Natural Gift gets from each berry varies from generation to generation. I will be displaying data from the most recent generation.")
            print("\t%s:\n\t\tDESC: %s\n\t\tNATURAL GIFT'S POWER: %s\n\t\tNATURAL GIFT'S POWER: %s \n" % (Pokedex.findItemName("roseliberry"), Pokedex.findItemDesc("roseliberry"),Pokedex.findItemNaturalGiftBasePower("roseliberry"),Pokedex.findItemNaturalGiftType("roseliberry")))
            print("\t%s:\n\t\tDESC: %s\n\t\tNATURAL GIFT'S POWER: %s\n\t\tNATURAL GIFT'S POWER: %s \n" % (Pokedex.findItemName("leppaberry"), Pokedex.findItemDesc("leppaberry"),Pokedex.findItemNaturalGiftBasePower("leppaberry"), Pokedex.findItemNaturalGiftType("leppaberry")))
            print("\t%s:\n\t\tDESC: %s\n\t\tNATURAL GIFT'S POWER: %s\n\t\tNATURAL GIFT'S POWER: %s \n" % (Pokedex.findItemName("aguavberry"), Pokedex.findItemDesc("aguavberry"),Pokedex.findItemNaturalGiftBasePower("aguavberry"), Pokedex.findItemNaturalGiftType("aguavberry")))
            print("\t%s:\n\t\tDESC: %s\n\t\tNATURAL GIFT'S POWER: %s\n\t\tNATURAL GIFT'S POWER: %s \n" % (Pokedex.findItemName("lumberry"), Pokedex.findItemDesc("lumberry"),Pokedex.findItemNaturalGiftBasePower("lumberry"), Pokedex.findItemNaturalGiftType("lumberry")))
            print("\t%s:\n\t\tDESC: %s\n\t\tNATURAL GIFT'S POWER: %s\n\t\tNATURAL GIFT'S POWER: %s \n" % (Pokedex.findItemName("watmelberry"), Pokedex.findItemDesc("watmelberry"),Pokedex.findItemNaturalGiftBasePower("watmelberry"), Pokedex.findItemNaturalGiftType("watmelberry")))
        print("I'm going to show the most popular items. How many should I suggest? ")
        itemAmountGate = False
        while not itemAmountGate:
            try:
                itemAmount = int(input("Input: (Int) "))
                itemAmountGate = True
            except:
                print("Um...how can I show that many items? Try again")
        sortedItems = TeamBuilder.findPokemonMetaItems(spName, tierfile, itemAmount)
        for s in sortedItems:
            print("\t%s:\n\t\tDESC: %s\n\t\tPOP: %s" % (Pokedex.findItemName(s[0]), Pokedex.findItemDesc(s[0]),s[1]))
            print()
        print()

        itemGate = False
        while not itemGate:
            if "vgc" in tier or "battlespot" in tier:
                print("Which item would you like to give to %s? Note that for the team that you are building, no two Pokemon may hold the same item!" % spName)
                itemRes = input("Input: (String) ")
            else:
                print("Which item would you like to give to %s?" % spName)
                itemRes = input("Input: (String) ")
            itemName = Pokedex.findItemName(itemRes)
            if itemName != None:
                if "vgc" in tier or "battlespot" in tier:
                    itemsList = []
                    for sp in teamMatesDict:
                        if teamMatesDict[sp]["item"] != None:
                            itemsList.append(teamMatesDict[sp]["item"])
                    if itemName in itemsList:
                        print("Oh, it seems that one of your Pokemon already holds that item. You must therefore select another item for your %s.\nYou can change edit this later on when you import your team into Pokemon Showdown" % spName)
                    else:
                        teamMatesDict[spName]["item"] = itemName
                        itemGate = True
                else:
                    teamMatesDict[spName]["item"]=itemName
                    itemGate = True
            else:
                print("I'm sorry, but that's not a registered item. Did you maybe spell it wrong?")
    else:
        print("Ah, I see that %s can only have one item. I'll automatically update your %s to hold that item." % (spName,spName))
        teamMatesDict[spName]["item"] = Pokedex.findItemName(list(MetaDex.findPokemonTierItems(spName, tierfile).keys())[1])
    print("Excellent! Your %s is now holding a %s!" % (spName, teamMatesDict[spName]["item"]))
    print()

    print("We are almost done with your %s. Just a few simple things to take care of." % spName)

    #Selecting Happiness
    print("Alright, let's move on to Happiness.")
    moves = [teamMatesDict[spName]["moves"]["move1"],teamMatesDict[spName]["moves"]["move2"],teamMatesDict[spName]["moves"]["move3"],teamMatesDict[spName]["moves"]["move4"]]
    if "Frustration" in moves and "Return" not in moves:
        print("Ah, yes. One of your moves is Frustration. This move has it's highest power when happiness is 0. I'll do that automatically for you!")
        teamMatesDict[spName]["happiness"] = 0
    elif "Return" in moves and "Frustration" not in moves:
        print("Ah, yes. One of your moves is Return.This move has it's highest power when happiness is maxed out. I'll do that automatically for you!")
        teamMatesDict[spName]["happiness"] = 255
    elif "Return" in moves and "Frustration" in moves:
        print("Oh hold on, you have both Return and Frustration as moves for your %s.\nThis isn't necessary. Return and Frustration are basically the same move, except where one increases in power as happiness goes up, the other decreases in power. \nI'll set Happiness to it's max setting, as this is the default, making Return the strongest of the two.\nI can't change the moveset now, but later when you import this team into Pokemon Showdown, remove Frustration and replace it with another move, k?"% spName)
        teamMatesDict[spName]["happiness"] = 255
    else:
        print("In your case, happiness does not affect your Pokemon at all. So I'll just set it to max, as this is it's default value.")
        teamMatesDict[spName]["happiness"] = 255
    print()

    #Selecting Level
    print("Ok, almost there. Time to chose what level your %s should be at." % spName)
    if "vgc" in tier or "battlespot" in tier:
        print("Remember, Pokemon in this team must be at level of 50 or under.")
        print("What level would like your Pokemon to be?")
        levelGate = False
        while not levelGate:
            try:
                res = int(input("Input: (Int) "))
                if 0 < res <= 50:
                    teamMatesDict[spName]["level"] = res
                    levelGate = True
                else:
                    print("That's impossible to do, try again!")
            except:
                print("Um...I don't understand that response...")
    else:
        evoLevel = Pokedex.findPokemonEvoLevel(spName)
        if evoLevel != None:
            print("Remember, your % evolves at level %s, so you must chose a level equal or greater than that" % (spName, evoLevel))
            print("What level would like your Pokemon to be?")
            levelGate = False
            while not levelGate:
                try:
                    res = int(input("Input: (Int) "))
                    if evoLevel <= res <= 100:
                        teamMatesDict[spName]["level"] = res
                        levelGate = True
                    else:
                        print("That's impossible to do, try again")
                except:
                    print("Um...I don't understand that response...")
        else:
            print("What level would like your Pokemon to be?")
            levelGate = False
            while not levelGate:
                try:
                    res = int(input("Input: (Int) "))
                    if 0 <= res <= 100:
                        teamMatesDict[spName]["level"] = res
                        levelGate = True
                    else:
                        print("That's impossible to do, try again")
                except:
                    print("Um...I don't understand that response...")
    print("Excellent! Your %s is now at Level %s" % (spName, teamMatesDict[spName]["level"]))
    print()

    #Selecting Shininess
    print("And last but probably the most important, shininess!")
    shinyGate = False
    while not shinyGate:
        if spName not in ["Celebi","Victini","Keldeo","Meloetta","Meloetta-Pirouette","Zygarde","Hoopa","Hoopa-Unbound","Volcanion","Tapu Koko", "Tapu Fini","Tapu Bulu","Tapu Lele","Cosmog","Cosmoem","Solgaleo","Lunala","Nihilego","Buzzwole","Pheromosa","Xurkitree","Celesteela","Kartana","Guzzlord","Necrozma","Magearna","Marshadow"]:
            print("Do you want %s to be shiny?" % spName)
            res = input("Input: (Y/N) ")
            if res == "Y":
                teamMatesDict[spName]["shiny"] = "Yes"
                shinyGate = True
            elif res == "N":
                teamMatesDict[spName]["shiny"] = "No"
                shinyGate = True
            else:
                print("Um...I don't understand that response...")
        else:
            print("I see that your %s can not be legally shiny. Maybe one day...")
            teamMatesDict[spName]["shiny"] = "No"
    print()
print()

#Writing Text File for a Team
print("And your done! You have constructed your team! Now let me convert this into a text file so that you can import your team into Pokemon Showdown without any problems.")
print("I'm going to put your team in the same location you put this program. If you can't find it, just search for it on your computer's search bar. I promise it's there.")
print()
now = datetime.datetime.now()
fileName = tier+"_"+str(now.day)+"-"+str(now.month)+"-"+str(now.year)+"_"+str(now.hour)+"-"+str(now.minute)+".txt"
file = open(fileName,"w")
for poke in teamMatesDict:
    if teamMatesDict[poke]["gender"] != None:
        if teamMatesDict[poke]["item"]!=None:
            file.write(teamMatesDict[poke]["species"]+" ("+teamMatesDict[poke]["gender"]+") @ "+teamMatesDict[poke]["item"]+"\n")
            print(teamMatesDict[poke]["species"]+" ("+teamMatesDict[poke]["gender"]+") @ "+teamMatesDict[poke]["item"])
        else:
            file.write(teamMatesDict[poke]["species"]+" ("+teamMatesDict[poke]["gender"]+")\n")
            print(teamMatesDict[poke]["species"]+" ("+teamMatesDict[poke]["gender"]+")")
    else:
        if teamMatesDict[poke]["item"]!=None:
            file.write(teamMatesDict[poke]["species"]+" @ "+teamMatesDict[poke]["item"]+"\n")
            print(teamMatesDict[poke]["species"]+" @ "+teamMatesDict[poke]["item"])
        else:
            file.write(teamMatesDict[poke]["species"]+"\n")
            print(teamMatesDict[poke]["species"])

    file.write("Ability: "+teamMatesDict[poke]["ability"]+"\n")
    print("Ability: "+teamMatesDict[poke]["ability"])

    file.write("Level: "+str(teamMatesDict[poke]["level"])+"\n")
    print("Level: "+str(teamMatesDict[poke]["level"]))

    if teamMatesDict[poke]["happiness"]!=255:
        file.write("Happiness: "+str(teamMatesDict[poke]["happiness"])+"\n")
        print("Happiness: " + str(teamMatesDict[poke]["happiness"]))

    if teamMatesDict[poke]["shiny"]=="Yes":
        file.write("Shiny: Yes\n")
        print("Shiny: Yes")

    evStringNeeded = False
    evString = ""
    if teamMatesDict[poke]["evs"]["hp"]!=0:
        evString = evString+str(teamMatesDict[poke]["evs"]["hp"])+" HP"
        evStringNeeded = True
    if teamMatesDict[poke]["evs"]["atk"]!=0:
        evString = evString+" / "+str(teamMatesDict[poke]["evs"]["atk"])+" Atk"
        evStringNeeded = True
    if teamMatesDict[poke]["evs"]["def"]!=0:
        evString = evString+" / "+str(teamMatesDict[poke]["evs"]["def"])+" Def"
        evStringNeeded = True
    if teamMatesDict[poke]["evs"]["spa"]!=0:
        evString = evString+" / "+str(teamMatesDict[poke]["evs"]["spa"])+" SpA"
        evStringNeeded = True
    if teamMatesDict[poke]["evs"]["spd"]!=0:
        evString = evString+" / "+str(teamMatesDict[poke]["evs"]["spd"])+" SpD"
        evStringNeeded = True
    if teamMatesDict[poke]["evs"]["spe"]!=0:
        evString = evString+" / "+str(teamMatesDict[poke]["evs"]["spe"])+" Spe"
        evStringNeeded = True
    if evStringNeeded == True:
        file.write("EVs: "+evString+"\n")
        print("EVs: "+evString)

    file.write(teamMatesDict[poke]["nature"]+" Nature\n")
    print(teamMatesDict[poke]["nature"]+" Nature")

    ivStringNeeded = False
    ivString = ""
    if teamMatesDict[poke]["ivs"]["hp"] != 31:
        ivString = ivString + str(teamMatesDict[poke]["ivs"]["hp"]) + " HP"
        ivStringNeeded = True
    if teamMatesDict[poke]["ivs"]["atk"] != 31:
        ivString = ivString + " / " + str(teamMatesDict[poke]["ivs"]["atk"]) + " Atk"
        ivStringNeeded = True
    if teamMatesDict[poke]["ivs"]["def"] != 31:
        ivString = ivString + " / " + str(teamMatesDict[poke]["ivs"]["def"]) + " Def"
        ivStringNeeded = True
    if teamMatesDict[poke]["ivs"]["spa"] != 31:
        ivString = ivString + " / " + str(teamMatesDict[poke]["ivs"]["spa"]) + " SpA"
        ivStringNeeded = True
    if teamMatesDict[poke]["ivs"]["spd"] != 31:
        ivString = ivString + " / " + str(teamMatesDict[poke]["ivs"]["spd"]) + " SpD"
        ivStringNeeded = True
    if teamMatesDict[poke]["ivs"]["spe"] != 31:
        ivString = ivString + " / " + str(teamMatesDict[poke]["ivs"]["spe"]) + " Spe"
        ivStringNeeded = True
    if ivStringNeeded == True:
        file.write("IVs: "+ivString+"\n")
        print("IVs: " + ivString)

    for move in ["move1","move2","move3","move4"]:
        if teamMatesDict[poke]["moves"][move]!=None:
            file.write("- " + teamMatesDict[poke]["moves"][move]+"\n")
            print("- " + teamMatesDict[poke]["moves"][move])
    file.write("\n")
    print()
file.close()
print("Ok, your team can be found in %s" % fileName)
print("So what you want to do is go to http://play.pokemonshowdown.com/")
print("Click on the 'Teambuilder' button.")
print("Click on the 'New Team' button.")
print("Click on the 'Import from text' button.")
print("Copy the entire text from the file I just sent you and paste it in the large input field.")
print("Click on the 'Import/Export' button on top.")
print("Your team will have been imported into the website!")
print("For extra measure, do you see that bar on the top left of your screen? It should read something like 'Untitled #'? This is where you can name your team!")
print("Under that, you should find the 'Format' option. Click it. A large window should appear.")
print("Select the format that most looks like %s (this is the tier/format you decided to build this team for)." % tier)
print("To check if everything went perfectingly in the team building process, click the 'Validate' button. A window should pop up.")
print("\tIf your team gets validated for your chosen format/tier, your all set.")
print("\tIf you do get an error, just follow the instructions given by the error message to correvct this. Revalidate your team and you should be ready to go!")
print()
print("NOTE: Your imported team will be preserved on the website via cookies. Therefore, you can come back later to Pokemon Showdown, and your team will still be there!")
print("However, if you delete the cookies stored on your computer, you team will disappear. Don't worry. All you have to dude is just import your team from the file we just made today.")
print()
print("If you want to test your team in an actual battle, click on the Home tab")
print("Before you can participate in an actual battle, you will need a Pokemon Showdown account.\n\tIf you don't have one already, making one is very easy and takes two seconds: all it requires is a username and a password.\n\tIf you already have an account, make sure you are signed in")
print("Now that you are signed in, click on the 'Format' option on the left of the screen. A large window will appear.")
print("Select the format that most looks like %s (this is the tier/format you decided to build this team for)." % tier)
print("Now that the website knows which type of battle you want to participate in, it will show you your teams (or one of them if you have multiple.)")
print("Select the team you wish to battle with.")
print("\tIf the website doesn't show the team you wish to battle with, it means that your team hasn't been validated for that format.\n\tYou must then go back to the Teambuilder, select your team, and validate it for the format/tier you wish to battle in.")
print("Alright, your all set! Just press the 'Battle!' button and have fun!\n\tNote, it may take a few moments for the servers to find you an opponent. Please be patient.")
print("glhf! Good luck and have fun!")
from tkinter import *
import Pokedex, MetaDex, TeamBuilder, random

def AI(shell, inputEvent):
    shell.yes = ["Y", "y", "Yes", "yes", "YES"]
    shell.no = ["N", "n", "No", "no", "NO"]

    shell.respond("Hello! I'm Al, here to help build your personal competitive Pokemon team!")
    shell.respond(
        "The great thing is, after we have built your team, I'll automatically export your team so you can easily import it into Pokemon Showdown, a Competitive Pokemon Battle Simulator used by hundreds of people every day!")
    shell.respond("Let's get started!")
    # TODO: implement personal names and inout of user names

    # Display All Tiers Downloaded Tiers
    shell.respond("First, we need to decide which tier this team will be used in.")
    tiers = MetaDex.getTiers()
    for t in range(len(tiers)):
        tList = list(tiers[t])
        cut = tList.index("-")
        tiers[t] = "".join(tList)[:cut]
    isDone = False
    while not isDone:
        isDone = True
        for t in range(len(tiers)):
            for s in range(len(tiers) - 1, t, -1):
                if tiers[s] == tiers[t]:
                    del tiers[s]
                    isDone = False

    # Chosing a Tier
    shell.respond("You have the following tiers to choose from:")
    tiersString = ""
    for t in tiers:
        tiersString += t + "\n    "
    shell.respond(tiersString[:-5])
    chooseTierGate = False
    while not chooseTierGate:
        shell.respond("Which tier would you like to work in? (String)")
        inputEvent.wait()
        inputEvent.clear()
        if shell.input_get in tiers:
            shell.tier = shell.input_get
            confirmTierGate = False
            while not confirmTierGate:
                shell.respond("You would like to build a team for %s? (Y/N)" % shell.tier)
                inputEvent.wait()
                inputEvent.clear()
                if shell.input_get in shell.yes:
                    chooseTierGate = True
                    confirmTierGate = True
                elif shell.input_get in shell.no:
                    confirmTierGate = True
                else:
                    shell.respond("Um...I don't understand your response...")
        else:
            shell.respond("Um...I don't understand your response...")

    # Select Level of Competitiveness
    shell.respond(
        "Ok, now how hard core do you want to make this team? You have 4 options.\n    Fun\n    Serious\n    Hard Core\n    Champion")
    tierSeverityGate = False
    while not tierSeverityGate:
        shell.respond("So, what will it be? (String)")
        inputEvent.wait()
        if shell.input_get in ["fun", "Fun"]:
            shell.tier = shell.tier + "-0"
            tierSeverityGate = True
        elif shell.input_get in ["serious", "Serious"]:
            shell.tier = shell.tier + "-1500"
            tierSeverityGate = True
        elif shell.input_get in ["hard core", "hard Core", "Hard Core", "Hard Core", "hardcore", "hardCore", "Hardcore",
                                "HardCore"]:
            if "ou" in shell.tier:
                shell.tier = shell.tier + "-1695"
            else:
                shell.tier = shell.tier + "-1630"
            tierSeverityGate = True
        elif shell.input_get in ["champion", "Champion"]:
            if "ou" in shell.tier:
                shell.tier = shell.tier + "-1825"
            else:
                shell.tier = shell.tier + "-1760"
            tierSeverityGate = True
        else:
            shell.respond("Um, I don't understand that response. You must pick one of the four options shown above.")
    shell.tierfile = shell.tier + ".json"
    shell.respond("Excellent! Let's get started with your team then!")

    # Helping the User Start a New Team and Selecting First Team Member
    firstMemberGate = False
    while not firstMemberGate:
        shell.respond("So, do you know which Pokemon you want to start your team with? (Y/N)")
        inputEvent.wait()
        inputEvent.clear()
        if shell.input_get in shell.yes:
            firstMemberGate = True
            shell.respond("Great! Innovation makes a great team!")
        elif shell.input_get in shell.no:
            firstMemberGate = True
            shell.respond("That's ok. There are plenty of Pokemon to choose from. Let me give you a few suggestions.")
            text = ""
            for poke in TeamBuilder.rawCountTopFinds(shell.tierfile, 20):
                pokeData = Pokedex.findPokemonData(poke[0])
                if len(pokeData["types"]) == 1:
                    text += poke[0] + ":\n\tTYPE: " + pokeData["types"][0] + "\n\tSTATS: " + str(
                        pokeData["baseStats"]["hp"]) + "/" + str(pokeData["baseStats"]["atk"]) + "/" + str(
                        pokeData["baseStats"]["def"]) + "/" + str(pokeData["baseStats"]["spa"]) + "/" + str(
                        pokeData["baseStats"]["spd"]) + "/" + str(pokeData["baseStats"]["spe"]) + "\n\tPOP: " + str(
                        poke[1]) + "\n\n    "
                elif len(pokeData["types"]) == 2:
                    text += poke[0] + ":\n\tTYPE: " + pokeData["types"][0] + ", " + pokeData["types"][
                        1] + "\n\tSTATS: " + str(pokeData["baseStats"]["hp"]) + "/" + str(
                        pokeData["baseStats"]["atk"]) + "/" + str(pokeData["baseStats"]["def"]) + "/" + str(
                        pokeData["baseStats"]["spa"]) + "/" + str(pokeData["baseStats"]["spd"]) + "/" + str(
                        pokeData["baseStats"]["spe"]) + "\n\tPOP: " + str(poke[1]) + "\n\n    "
            shell.respond(text[:-5])
        else:
            shell.respond("Um... I don't understand your response ")
    pokedex = Pokedex.loadPokedex()
    shell.teamMateNames = []
    shell.teamAdder(inputEvent)

    # Adding Other 5 Members
    for i in range(5):
        # TODO: include the species clause when showing new pokes
        shell.respond("Ok, let me suggest some team-mates. How many suggestions would you like to see? (Int)")
        memberSelectGate = False
        while not memberSelectGate:
            try:
                inputEvent.wait()
                inputEvent.clear()
                teamSuggAmount = int(shell.input_get)
                memberSelectGate = True
            except:
                shell.respond("Um...I don't understand your response...")
                # TODO: implement ID checks for species clause
        text = ""
        for poke in TeamBuilder.findTeamMetaMatches(shell.teamMateNames, shell.tierfile, teamSuggAmount):
            # TODO: fix this
            pokeData = Pokedex.findPokemonData(poke[0])
            if len(pokeData["types"]) == 1:
                text += poke[0] + ":\n\tTYPE: " + pokeData["types"][0] + "\n\tSTATS: " + str(
                    pokeData["baseStats"]["hp"]) + "/" + str(pokeData["baseStats"]["atk"]) + "/" + str(
                    pokeData["baseStats"]["def"]) + "/" + str(pokeData["baseStats"]["spa"]) + "/" + str(
                    pokeData["baseStats"]["spd"]) + "/" + str(pokeData["baseStats"]["spe"]) + "\n\tPOP: " + str(
                    poke[1]) + "\n\n    "
            elif len(pokeData["types"]) == 2:
                text += poke[0] + ":\n\tTYPE: " + pokeData["types"][0] + ", " + pokeData["types"][
                    1] + "\n\tSTATS: " + str(pokeData["baseStats"]["hp"]) + "/" + str(
                    pokeData["baseStats"]["atk"]) + "/" + str(pokeData["baseStats"]["def"]) + "/" + str(
                    pokeData["baseStats"]["spa"]) + "/" + str(pokeData["baseStats"]["spd"]) + "/" + str(
                    pokeData["baseStats"]["spe"]) + "\n\tPOP: " + str(poke[1]) + "\n\n    "

                # text+=t[0]+":\n\tPOP: "+str(t[1])+"\n\n    "
        shell.respond(text[:-5])
        shell.teamAdder(inputEvent)

    # Switching Team Members If Needed
    confirmTeamGate = False
    while not confirmTeamGate:
        text = ""
        text += "Here is your team!"
        for t in shell.teamMateNames:
            text += "\n    " + t
        shell.respond(text)
        shell.respond("Are you happy with the selection? (Y/N)")
        inputEvent.wait()
        inputEvent.clear()
        if shell.input_get in shell.yes:
            confirmTeamGate = True
        elif shell.input_get not in shell.yes and shell.input_get not in shell.no:
            shell.respond("Um...I don't understand that response...")
        else:
            # Finding Flip
            flipMemberGate = False
            while not flipMemberGate:
                shell.respond("Which Pokemon in your team would you like to swap? (String)")
                inputEvent.wait()
                inputEvent.clear()
                flip = shell.input_get
                flipName = Pokedex.findPokemonSpecies(flip)
                if flipName in shell.teamMateNames:
                    flipMemberGate = True
                else:
                    shell.respond("Pokemon %s isn't part of your team" % flip)
            # Showing Team Mate Options
            shell.respond("Ok, let me suggest some team-mates. How many suggestions would you like to see? (Int)")
            swapAmountGate = False
            while not swapAmountGate:
                try:
                    inputEvent.wait()
                    inputEvent.clear()
                    swapAmount = int(shell.input_get)
                    teamMateNamesprime = []
                    for i in range(len(shell.teamMateNames)):
                        teamMateNamesprime.append(shell.teamMateNames[i])
                    del teamMateNamesprime[teamMateNamesprime.index(flipName)]
                    swapAmountGate = True
                except:
                    shell.respond("Um...unfortunately I can't understand your request. Try again")
            text = ""
            for poke in TeamBuilder.findTeamMetaMatches(teamMateNamesprime, shell.tierfile, swapAmount):
                pokeData = Pokedex.findPokemonData(poke[0])
                if len(pokeData["types"]) == 1:
                    text += poke[0] + ":\n\tTYPE: " + pokeData["types"][0] + "\n\tSTATS: " + str(
                        pokeData["baseStats"]["hp"]) + "/" + str(pokeData["baseStats"]["atk"]) + "/" + str(
                        pokeData["baseStats"]["def"]) + "/" + str(pokeData["baseStats"]["spa"]) + "/" + str(
                        pokeData["baseStats"]["spd"]) + "/" + str(pokeData["baseStats"]["spe"]) + "\n\tPOP: " + str(
                        poke[1]) + "\n\n    "
                elif len(pokeData["types"]) == 2:
                    text += poke[0] + ":\n\tTYPE: " + pokeData["types"][0] + ", " + pokeData["types"][
                        1] + "\n\tSTATS: " + str(pokeData["baseStats"]["hp"]) + "/" + str(
                        pokeData["baseStats"]["atk"]) + "/" + str(pokeData["baseStats"]["def"]) + "/" + str(
                        pokeData["baseStats"]["spa"]) + "/" + str(pokeData["baseStats"]["spd"]) + "/" + str(
                        pokeData["baseStats"]["spe"]) + "\n\tPOP: " + str(poke[1]) + "\n\n    "
                    # text+=t[0]+": "+str(t[1])+"\n\n    "
            shell.respond(text)
            # Finding Flop and Checking if it's another Mega
            flopMemberGate = False
            while not flopMemberGate:
                if "anythinggoes" not in shell.tier:
                    shell.respond(
                        "Which Pokemon in your team would you like to swap %s with? Note that your team can not have two or more Pokemon with the same National Pokedex number!" % flipName)
                    inputEvent.wait()
                    inputEvent.clear()
                    flop = shell.input_get
                else:
                    shell.respond("Which Pokemon in your team would you like to swap %s with?" % flipName)
                    inputEvent.wait()
                    inputEvent.clear()
                    flop = shell.input_get
                flopName = Pokedex.findPokemonSpecies(flop)
                if flopName != None:
                    data = MetaDex.findPokemonTierData(flopName, shell.tierfile)
                    if data != None:
                        if "anythinggoes" not in shell.tier:
                            numList = []
                            for s in shell.teamMateNames:
                                numList.append(Pokedex.findPokemonNum(s))
                            if Pokedex.findPokemonNum(flopName) in numList:
                                shell.respond(
                                    "Oh, you can not have two or more Pokemon with the same National Pokedex number! You must select another Pokemon.")
                            else:
                                forme = Pokedex.findPokemonForme(flopName)
                                if forme == "Mega":
                                    megaChecks = []
                                    for teamMate in shell.teamMateNames:
                                        if Pokedex.findPokemonForme(teamMate) == "Mega":
                                            megaChecks.append(False)
                                        else:
                                            megaChecks.append(True)
                                    if all(megaChecks):
                                        shell.teamMateNames[shell.teamMateNames.index(flipName)] = flopName
                                        shell.respond("Done! I switched %s with %s." % (flipName, flopName))
                                        flopMemberGate = True
                                    else:
                                        shell.respond(
                                            "Oh, I see that you're trying to add another mega to your team. I mean, this is techniaclly allowed, but I wouldn't suggest it. You can only use one mega per battle.")
                                        multiMegaGate = False
                                        while not multiMegaGate:
                                            shell.respond("Are you sure you want multiple megas in your team?")
                                            inputEvent.wait()
                                            inputEvent.clear()
                                            if shell.input_get in shell.yes:
                                                shell.respond("Alright, I'll add another mega then!")
                                                shell.teamMateNames[shell.teamMateNames.index(flipName)] = flopName
                                                shell.respond("Done! I switched %s with %s." % (flipName, flopName))
                                                flopMemberGate = True
                                                multiMegaGate = True
                                            elif shell.input_get in shell.no:
                                                multiMegaGate = True
                                            else:
                                                shell.respond("Um...I don't understand your response...")
                                else:
                                    shell.teamMateNames[shell.teamMateNames.index(flipName)] = flopName
                                    shell.respond("Done! I switched %s with %s." % (flipName, flopName))
                                    flopMemberGate = True
                        else:
                            forme = Pokedex.findPokemonForme(flopName)
                            if forme == "Mega":
                                megaChecks = []
                                for teamMate in shell.teamMateNames:
                                    if Pokedex.findPokemonForme(teamMate) == "Mega":
                                        megaChecks.append(False)
                                    else:
                                        megaChecks.append(True)
                                if all(megaChecks):
                                    shell.teamMateNames[shell.teamMateNames.index(flipName)] = flopName
                                    shell.respond("Done! I switched %s with %s." % (flipName, flopName))
                                    flopMemberGate = True
                                else:
                                    shell.respond(
                                        "Oh, I see that you're trying to add another mega to your team. I mean, this is techniaclly allowed, but I wouldn't suggest it. You can only use one mega per battle.")
                                    multiMegaGate = False
                                    while not multiMegaGate:
                                        shell.respond("Are you sure you want multiple megas in your team?")
                                        inputEvent.wait()
                                        inputEvent.clear()
                                        if shell.input_get in shell.yes:
                                            shell.respond("Alright, I'll add another mega then!")
                                            shell.teamMateNames[shell.teamMateNames.index(flipName)] = flopName
                                            shell.respond("Done! I switched %s with %s." % (flipName, flopName))
                                            flopMemberGate = True
                                            multiMegaGate = True
                                        elif shell.input_get in shell.no:
                                            multiMegaGate = True
                                        else:
                                            shell.respond("Um...I don't understand your response...")
                            else:
                                shell.teamMateNames[shell.teamMateNames.index(flipName)] = flopName
                                shell.respond("Done! I switched %s with %s." % (flipName, flopName))
                                flopMemberGate = True
                    else:
                        shell.respond("Oh, I'm sorry. There seems to be a problem.")
                        shell.respond("Either Pokemon %s is not allowed in tier %s." % (flop, shell.tier))
                        shell.respond(
                            "Or it might be that Pokemon %s is SO rare in tier %s that there isn't enough data on it" % (
                            flop, shell.tier))
                        shell.respond(
                            "Either way, I suggest chosing another Pokemon. That way I have the data necessary to help you")
                else:
                    shell.respond("The inputted Pokemon is not an actual Pokemon! Try again")
    shell.respond("Your team is coming along great. Let's move on to the individual team members.")

    # Make Dictionary with All Necessary Info
    for member in shell.teamMateNames:
        dict = {}
        dict["species"] = Pokedex.findPokemonSpecies(member)
        dict["ability"] = None
        dict["nature"] = None
        dict["baseStats"] = {"hp": Pokedex.findPokemonHP(member), "atk": Pokedex.findPokemonAtk(member),
                             "def": Pokedex.findPokemonDef(member), "spa": Pokedex.findPokemonSpA(member),
                             "spd": Pokedex.findPokemonSpD(member), "spe": Pokedex.findPokemonSpe(member)}
        dict["ivs"] = {"hp": 31, "atk": 31, "def": 31, "spa": 31, "spd": 31, "spe": 31}
        dict["evs"] = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0}
        dict["item"] = None
        dict["gender"] = None
        if member == "Rayquaza-Mega":
            dict["moves"] = {"move1": "Dragon Ascent", "move2": None, "move3": None, "move4": None}
        else:
            dict["moves"] = {"move1": None, "move2": None, "move3": None, "move4": None}
        dict["happiness"] = None
        dict["level"] = 100
        dict["shiny"] = None
        shell.teamMatesDict[member] = dict

    pokemon1_menu = Menu(shell.the_menu, tearoff=0)
    pokemon1_menu.add_command(label="View", command=lambda: shell.switch(shell.teamMateNames[0]))
    # pokemon1_menu.add_command(label="Delete",command=lambda:shell.delete(shell.teamMateNames[0]))
    shell.the_menu.add_cascade(label=shell.teamMateNames[0], menu=pokemon1_menu)

    pokemon2_menu = Menu(shell.the_menu, tearoff=0)
    pokemon2_menu.add_command(label="View", command=lambda: shell.switch(shell.teamMateNames[1]))
    # pokemon2_menu.add_command(label="Delete", command=lambda:shell.delete(shell.teamMateNames[1]))
    shell.the_menu.add_cascade(label=shell.teamMateNames[1], menu=pokemon2_menu)

    pokemon3_menu = Menu(shell.the_menu, tearoff=0)
    pokemon3_menu.add_command(label="View", command=lambda: shell.switch(shell.teamMateNames[2]))
    # pokemon3_menu.add_command(label="Delete", command=lambda:shell.delete(shell.teamMateNames[2]))
    shell.the_menu.add_cascade(label=shell.teamMateNames[2], menu=pokemon3_menu)

    pokemon4_menu = Menu(shell.the_menu, tearoff=0)
    pokemon4_menu.add_command(label="View", command=lambda: shell.switch(shell.teamMateNames[3]))
    # pokemon4_menu.add_command(label="Delete", command=lambda:shell.delete(shell.teamMateNames[3]))
    shell.the_menu.add_cascade(label=shell.teamMateNames[3], menu=pokemon4_menu)

    pokemon5_menu = Menu(shell.the_menu, tearoff=0)
    pokemon5_menu.add_command(label="View", command=lambda: shell.switch(shell.teamMateNames[4]))
    # pokemon5_menu.add_command(label="Delete", command=lambda:shell.delete(shell.teamMateNames[4]))
    shell.the_menu.add_cascade(label=shell.teamMateNames[4], menu=pokemon5_menu)

    pokemon6_menu = Menu(shell.the_menu, tearoff=0)
    pokemon6_menu.add_command(label="View", command=lambda: shell.switch(shell.teamMateNames[5]))
    # pokemon6_menu.add_command(label="Delete", command=lambda:shell.delete(shell.teamMateNames[5]))
    shell.the_menu.add_cascade(label=shell.teamMateNames[5], menu=pokemon6_menu)

    shell.respond("I have uploaded your team members into the panel to your left. Have a look around!")

    # Iterate Over Every Team Member
    for poke in shell.teamMatesDict:
        spName = shell.teamMatesDict[poke]["species"]
        shell.switch(spName)
        if shell.teamMateNames.index(poke) == 0:
            shell.respond("Let's start with %s." % spName)
        else:
            shell.respond("Now let's take a look at %s." % spName)
        text = ""
        text += spName + " has the following base stats.\n    "
        for stat in shell.teamMatesDict[poke]["baseStats"]:
            if stat == "hp":
                text += stat + " : " + str(shell.teamMatesDict[poke]["baseStats"][stat]) + "\n    "
            else:
                text += stat + ": " + str(shell.teamMatesDict[poke]["baseStats"][stat]) + "\n    "
        shell.respond(text[:-5])

        # Choosing Ability
        abilities = Pokedex.findPokemonAbilities(spName)
        metaAbilities = MetaDex.findPokemonTierAbilities(spName, shell.tierfile)
        text = ""
        text += shell.cut(spName + " can have the following abilities:")
        text += "\n\t" + abilities["0"] + ":" + shell.cut(
            "\n\t    DESC: " + Pokedex.findAbilityShortDesc(abilities["0"])) + "\n\t    POP: " + str(
            metaAbilities[Pokedex.findAbilityID(abilities["0"])])
        if len(metaAbilities) > 1:
            if "1" in abilities:
                text += "\n\t" + abilities["1"] + ":" + shell.cut(
                    "\n\t    DESC: " + Pokedex.findAbilityShortDesc(abilities["1"])) + "\n\t    POP: " + str(
                    metaAbilities[Pokedex.findAbilityID(abilities["1"])])
            if "S" in abilities and TeamBuilder.compress(abilities["S"]) in metaAbilities:
                text += shell.cut("\n\tAdditionally, " + spName + " also has a special ability:")
                text += "\n\t" + abilities["S"] + ":" + shell.cut(
                    "\n\t    DESC: " + Pokedex.findAbilityShortDesc(abilities["S"])) + "\n\t    POP: " + str(
                    metaAbilities[Pokedex.findAbilityID(abilities["S"])])
                if TeamBuilder.compress(abilities["S"]) not in list(metaAbilities.keys()):
                    text += shell.cut("\n    Unfortunately, this ability is not allowed in " + shell.tier)
                else:
                    # TODO fix this
                    pass
            if "H" in abilities and TeamBuilder.compress(abilities["H"]) in metaAbilities:
                text += shell.cut("\n    Additionally, " + spName + " also has a Hidden ability:")
                text += "\n\t" + abilities["H"] + ":" + shell.cut(
                    "\n\t    DESC: " + Pokedex.findAbilityShortDesc(abilities["H"])) + "\n\t    POP: " + str(
                    metaAbilities[Pokedex.findAbilityID(abilities["H"])])
                if TeamBuilder.compress(abilities["H"]) not in list(metaAbilities.keys()):
                    text += shell.cut("\n    Unfortunately, this ability is not allowed in " + shell.tier)
                else:
                    # TODO fix this
                    pass
            shell.respond(text)
            abilityGate = False
            while not abilityGate:
                shell.respond("What ability would you like %s to have?" % spName)
                inputEvent.wait()
                inputEvent.clear()
                for s in ["0", "1", "S", "H"]:
                    abName = Pokedex.findAbilityName(shell.input_get)
                    if s in abilities and abName == abilities[s]:
                        if TeamBuilder.compress(abilities[s]) in metaAbilities:
                            shell.teamMatesDict[poke]["ability"] = abName
                            abilityGate = True
                if not abilityGate:
                    shell.respond("I'm sorry, but %s is not an ability that %s can have in tier %s." % (
                    spName, shell.input_get, shell.tier))
        else:
            shell.respond(text)
            shell.respond(
                "As you can see, %s only has one ability, so we don't have much choice here. I'll update your %s automatically, so you dont have to worry about that." % (
                    spName, spName))
            shell.teamMatesDict[poke]["ability"] = abilities["0"]
        shell.respond("Done! Your %s now has the ability %s" % (spName, shell.teamMatesDict[poke]["ability"]))
        shell.update(spName, "ability")

        shell.respond("Now that we have that decided, let's move on to IV and Nature/EV spreads")

        # Choosing IVs
        shell.respond(
            "First thing's first: I propose to give your %s the following IV spread: 31/31/31/31/31/31" % spName)
        shell.respond(
            "This is by far the most common IV spread for Pokemon. However, if you have something more specific in mind, you might want a different IV spread")
        ivGate = False
        while not ivGate:
            shell.respond("Do you want to use this IV spread?")
            inputEvent.wait()
            inputEvent.clear()
            if shell.input_get in shell.yes:
                ivGate = True
            elif shell.input_get not in shell.yes and shell.input_get not in shell.no:
                shell.respond("Um...I don't understand that response...")
            else:
                # Selecting Hidden Power
                hpGate = False
                while not hpGate:
                    shell.respond(
                        "Would you like to give %s the move Hidden Power (Category: Special, Power: 60, Type: Depends on user's IVs)? \nRemember that Hidden Power CAN NOT have a Fairy or Normal typing." % spName)
                    inputEvent.wait()
                    inputEvent.clear()
                    if shell.input_get in shell.yes:
                        ivTypeGate = False
                        while not ivTypeGate:
                            shell.respond("What type would you like Hidden Power to be?")
                            inputEvent.wait()
                            inputEvent.clear()
                            typeInput = shell.input_get
                            types = Pokedex.loadTypes()
                            tList = list(typeInput)
                            tList[0] = tList[0].capitalize()
                            typeInput = "".join(tList)
                            shell.teamMatesDict[spName]["moves"]["move1"] = "Hidden Power " + typeInput
                            if typeInput in types and typeInput != "Normal" and typeInput != "Fairy":
                                text = ""
                                text += "Ok, here are a few IV spreads that result in Hidden Power having a typeInput typing."
                                for set in types[typeInput]["hp Sets"]:
                                    text += "\n\t" + set + ":"
                                    for i in range(len(types[typeInput]["hp Sets"][set])):
                                        text += "\n\t    " + types[typeInput]["hp Sets"][set][i]
                                    ivTypeGate = True
                                shell.respond(text)
                            elif typeInput == "Fairy" or typeInput == "Normal":
                                shell.respond(
                                    "I told you that Hidden Power can not have a Fairy or Normal typing! Didn't you pay attention?")
                            else:
                                shell.respond("Um...I don't understand that response...")
                        hpGate = True
                    elif shell.input_get in shell.no:
                        hpGate = True
                    else:
                        shell.respond("Um...I don't understand that response")

                # Choosing IVs
                shell.respond("What kind of IVs should %s have?" % spName)
                for string in ["hp", "atk", "def", "spa", "spd", "spe"]:
                    ivChoiceGate = False
                    while not ivChoiceGate:
                        shell.respond(string + ":")
                        inputEvent.wait()
                        inputEvent.clear()
                        iv = shell.input_get
                        try:
                            iv = int(iv)
                            if 0 <= iv <= 31:
                                shell.teamMatesDict[spName]["ivs"][string] = iv
                                ivChoiceGate = True
                            else:
                                shell.respond("Oh, I'm sorry, but I can't give %s %s %s Ivs. Try again" % (
                                    spName, iv, string.capitalize()))
                        except:
                            shell.respond(
                                "Um...how can I give %s %s %s IVs? Try again" % (spName, iv, string.capitalize()))

                shell.respond("Your %s currently has the following IV spread." % spName)
                shell.respond("%s/%s/%s/%s/%s/%s" % (
                    shell.teamMatesDict[spName]["ivs"]["hp"], shell.teamMatesDict[spName]["ivs"]["atk"],
                    shell.teamMatesDict[spName]["ivs"]["def"], shell.teamMatesDict[spName]["ivs"]["spa"],
                    shell.teamMatesDict[spName]["ivs"]["spd"], shell.teamMatesDict[spName]["ivs"]["spe"]))
        shell.respond("Great! Now your %s has the following IV spread: %s/%s/%s/%s/%s/%s." % (
            spName, shell.teamMatesDict[spName]["ivs"]["hp"], shell.teamMatesDict[spName]["ivs"]["atk"],
            shell.teamMatesDict[spName]["ivs"]["def"], shell.teamMatesDict[spName]["ivs"]["spa"],
            shell.teamMatesDict[spName]["ivs"]["spd"], shell.teamMatesDict[spName]["ivs"]["spe"]))
        shell.update(spName, "ivs")

        # Choosing Natures
        # TODO: what nature is what? fix
        shell.respond("Alright, it's time for Natures and EVs")
        shell.respond("%s has a few common Nature/EV spreads. How many would you like to see? (Int)" % spName)
        gate8 = False
        while not gate8:
            try:
                inputEvent.wait()
                inputEvent.clear()
                evAmount = int(shell.input_get)
                sortedSpreads = TeamBuilder.findPokemonMetaSpreads(spName, shell.tierfile, evAmount)
                gate8 = True
            except:
                shell.respond("How can I show you that many Nature/EV spreads? Try again")
        text = ""
        for s in range(len(sortedSpreads)):
            text += sortedSpreads[s][0] + ":\n\tPOP: " + str(sortedSpreads[s][1]) + "\n    "
        shell.respond(text[:-5])
        natureGate = False
        while not natureGate:
            shell.respond("What Nature would you like to give to %s? (String)" % spName)
            inputEvent.wait()
            inputEvent.clear()
            res = shell.input_get
            rList = list(res)
            rList[0] = rList[0].capitalize()
            res = "".join(rList)
            if res in ["Hardy", "Lonely", "Adamant", "Naughty", "Brave", "Bold", "Docile", "Impish", "Lax",
                       "Relaxed", "Modest", "Mild", "Bashful", "Rash", "Quiet", "Calm", "Gentle", "Careful",
                       "Quirky", "Sassy", "Timid", "Hasty", "Jolly", "Naive", "Serious"]:
                shell.teamMatesDict[spName]["nature"] = res
                natureGate = True
            else:
                shell.respond("Um...that's not a defined nature, so I can't assign that to %s. Try again." % spName)
        shell.respond("Excellent, now your %s has a %s nature!" % (spName, shell.teamMatesDict[spName]["nature"]))
        shell.update(spName, "nature")

        # Choosing EVs
        shell.respond("And now it's time for EVs.")
        topNatureSpread = None
        for i in range(len(sortedSpreads)):
            if sortedSpreads[i][0].split(":")[0] == shell.teamMatesDict[spName]["nature"]:
                topNatureSpread = sortedSpreads[i][0].split(":")[1]
                shell.respond(
                    "I'll start you off with the most common EV spread for your chosen Nature. In this case, that would be %s." % topNatureSpread)
                break
        if topNatureSpread == None:
            topNatureSpread = sortedSpreads[0][0].split(":")[1]
            shell.respond(
                "I couldn't immediately find any common EV spreads for your chosen Nature, but here is the most common EV spread currently in use: %s." % topNatureSpread)
        parts2 = topNatureSpread.split("/")
        shell.teamMatesDict[spName]["evs"]["hp"] = int(parts2[0])
        shell.teamMatesDict[spName]["evs"]["atk"] = int(parts2[1])
        shell.teamMatesDict[spName]["evs"]["def"] = int(parts2[2])
        shell.teamMatesDict[spName]["evs"]["spa"] = int(parts2[3])
        shell.teamMatesDict[spName]["evs"]["spd"] = int(parts2[4])
        shell.teamMatesDict[spName]["evs"]["spe"] = int(parts2[5])
        evGate = False
        while not evGate:
            shell.respond("Do you want to use this EV spread?")
            inputEvent.wait()
            inputEvent.clear()
            if shell.input_get in shell.yes:
                evGate = True
            elif shell.input_get not in shell.no and shell.input_get not in shell.yes:
                shell.respond("Um...I don't understand that response...")
            else:
                shell.respond(
                    "What kind of EVs should %s have? \nRemember, each Stat can effectively only have a maximum of 252 EVs, and the total can not effectively be larger than 508." % spName)
                available = 508
                for string in ["hp", "atk", "def", "spa", "spd", "spe"]:
                    evChoiceGate = False
                    while not evChoiceGate:
                        shell.respond("Number of EVs available: %s" % available)
                        shell.respond(string + ":")
                        inputEvent.wait()
                        inputEvent.clear()
                        try:
                            ev = int(shell.input_get)
                            if 0 <= ev <= 252:
                                if available - ev >= 0:
                                    available = available - ev
                                    shell.teamMatesDict[spName]["evs"][string] = ev
                                    evChoiceGate = True
                                else:
                                    shell.respond(
                                        "You exceeded the limit on your total EVs. Hey, I didn't make the rules...")
                            else:
                                shell.respond("Oh, I'm sorry, but I can't give %s %s HP EVs. Try again" % (spName, ev))
                        except:
                            shell.respond("Um...how can I give %s %s HP EVs? Try again" % (spName, ev))
                shell.respond("Your %s currently has the following IV spread." % spName)
                shell.respond("%s/%s/%s/%s/%s/%s" % (
                    shell.teamMatesDict[spName]["evs"]["hp"], shell.teamMatesDict[spName]["evs"]["atk"],
                    shell.teamMatesDict[spName]["evs"]["def"], shell.teamMatesDict[spName]["evs"]["spa"],
                    shell.teamMatesDict[spName]["evs"]["spd"], shell.teamMatesDict[spName]["evs"]["spe"]))
        shell.respond("Great! Now your %s has the following EV spread: %s/%s/%s/%s/%s/%s." % (
            spName, shell.teamMatesDict[spName]["evs"]["hp"], shell.teamMatesDict[spName]["evs"]["atk"],
            shell.teamMatesDict[spName]["evs"]["def"], shell.teamMatesDict[spName]["evs"]["spa"],
            shell.teamMatesDict[spName]["evs"]["spd"], shell.teamMatesDict[spName]["evs"]["spe"]))
        shell.update(spName, "evs")

        # Selecting Gender
        shell.respond("Ok, now we have to change gears a little. Time to talk about your Pokemon's gender")
        if Pokedex.findPokemonGender(spName) != None:
            shell.respond(
                "Ah, this Pokemon has be a specific gender according to it's species. Don't worry, I'll take care of that")
            if Pokedex.findPokemonGender(spName) != "N":
                shell.teamMatesDict[spName]["gender"] = Pokedex.findPokemonGender(spName)
        else:
            genderGate = False
            while not genderGate:
                shell.respond("Do you have a specific gender in mind for %s? (Y/N)" % spName)
                inputEvent.wait()
                inputEvent.clear()
                if shell.input_get in shell.no:
                    shell.respond("Ok, I'll pick a gender at random for you then.")
                    genPick = random.randrange(1, 10)
                    if genPick <= 5:
                        shell.teamMatesDict[spName]["gender"] = "M"
                        genderGate = True
                    else:
                        shell.teamMatesDict[spName]["gender"] = "F"
                        genderGate = True
                elif shell.input_get in shell.yes:
                    pickGenderGate = False
                    while not pickGenderGate:
                        shell.respond("Which gender would you like to make your %s? (String)" % spName)
                        inputEvent.wait()
                        inputEvent.clear()
                        if shell.input_get in ["M", "m", "Male", "male", "Man", "man"]:
                            shell.teamMatesDict[spName]["gender"] = "M"
                            pickGenderGate = True
                            genderGate = True
                        elif shell.input_get in ["F", "f", "Female", "female", "Woman", "woman"]:
                            shell.teamMatesDict[spName]["gender"] = "F"
                            pickGenderGate = True
                            genderGate = True
                        else:
                            shell.respond("Um...I don't understand that response")
                else:
                    shell.respond("Um, I don't understand that response...")
        shell.respond("Done! Your %s is now has of the %s gender!" % (spName, shell.teamMatesDict[spName]["gender"]))
        shell.update(spName, "gender")

        # Show Popular Moves
        shell.respond(
            "Alright, now hey comes the REALLY important part: selecting moves.\tI'll show you a few of the most common moves that %s can have." % spName)
        moves = [shell.teamMatesDict[spName]["moves"]["move1"], shell.teamMatesDict[spName]["moves"]["move2"],
                 shell.teamMatesDict[spName]["moves"]["move3"], shell.teamMatesDict[spName]["moves"]["move4"]]
        moveset = MetaDex.findPokemonTierMoves(spName, shell.tierfile)
        # TODO: implement hidden powers
        if len(moveset) == 1:
            shell.respond("Oh, this Pokemon species can only learn 1 move! I set whatever moves I can, k?")
            moves[0] = Pokedex.findMoveName(list(moveset.keys())[0])
            moves[1] = None
            moves[2] = None
            moves[3] = None
        elif len(moveset) == 2:
            shell.respond("Oh, this Pokemon species can only learn 2 moves! I set whatever moves I can, k?")
            moves[0] = Pokedex.findMoveName(list(moveset.keys())[0])
            moves[1] = Pokedex.findMoveName(list(moveset.keys())[1])
            moves[2] = None
            moves[3] = None
        elif len(moveset) == 3:
            shell.respond("Oh, this Pokemon species can only learn 3 moves! I set whatever moves I can, k?")
            moves[0] = Pokedex.findMoveName(list(moveset.keys())[0])
            moves[1] = Pokedex.findMoveName(list(moveset.keys())[1])
            moves[2] = Pokedex.findMoveName(list(moveset.keys())[2])
            moves[3] = None
        elif len(moveset) == 4:
            shell.respond("Oh, this Pokemon species can only learn 4 moves! I set whatever moves I can, k?")
            moves[0] = Pokedex.findMoveName(list(moveset.keys())[0])
            moves[1] = Pokedex.findMoveName(list(moveset.keys())[1])
            moves[2] = Pokedex.findMoveName(list(moveset.keys())[2])
            moves[3] = Pokedex.findMoveName(list(moveset.keys())[3])
        else:
            shell.respond("How many would you like to see? (Int)")
            showMovesGate = False
            while not showMovesGate:
                try:
                    inputEvent.wait()
                    inputEvent.clear()
                    moveAmount = int(shell.input_get)
                    sortedMoves = TeamBuilder.findPokemonMetaMoves(spName, shell.tierfile, moveAmount)
                    showMovesGate = True
                except:
                    shell.respond("How can I show you that many Moves? Try again")
            text = ""
            for s in range(len(sortedMoves)):
                if sortedMoves[s][0] != "Nothing" and sortedMoves[s][0] != "":
                    moveData = Pokedex.findMoveData(sortedMoves[s][0])
                    text += moveData["name"] + ":\n\tCAT: " + moveData["category"] + ",\n\tTYPE: " + moveData[
                        "type"] + ",\n\tPP: " + str(moveData["pp"]) + ",\n\tACC: " + str(
                        moveData["accuracy"]) + ",\n\tBASEPOW: " + str(moveData["basePower"]) + "," + shell.cut(
                        "\n\tDESC: " + moveData["shortDesc"]) + "\n\tPOP: " + str(sortedMoves[s][1]) + "\n    "
                else:
                    text += "Nothing:\n\tCAT: Nothing,\n\tTYPE: Nothing,\n\tPP: 0,\n\tACC: 0,\n\tBASEPOW: 0,\n\tDESC: Does nothing.\n\tPOP: 0\n    "
            shell.respond(text)

        for moveIndex in [1, 2, 3, 4]:
            if moves[moveIndex - 1] == None:
                moveGate = False
                while not moveGate:
                    shell.respond(
                        "Which move would you like %s to have in move slot #%s? (String)" % (spName, moveIndex))
                    inputEvent.wait()
                    inputEvent.clear()
                    if moveIndex != 1 and shell.input_get in ["None", "none", "Null", "null"]:
                        moves[moveIndex - 1] = None
                        moveGate = True
                    else:
                        resName = Pokedex.findMoveName(shell.input_get)
                        if resName != None:
                            if Pokedex.findMoveID(shell.input_get) in MetaDex.findPokemonTierMoves(spName,
                                                                                                  shell.tierfile):
                                if resName not in moves:
                                    moves[moveIndex - 1] = resName
                                    moveGate = True
                                else:
                                    shell.respond(
                                        "Oh, you already have %s as a move for your %s. Please select a different move." % (
                                        resName, spName))
                            else:
                                shell.respond(
                                    "Oh, there seems to be a problem. Either %s can't learn this move, or it is used SO rarely that I couldn't find any useful data. In any case, try a different move." % spName)
                        else:
                            shell.respond("I'm sorry, but that is not a valid move. Try again")
                shell.respond("Understood")
            else:
                shell.respond(
                    "Due to meeting various requirements, this move for your %s has already been chosen to be %s. So that's already done!" % (
                    spName, moves[moveIndex - 1]))

        # Switching Moves Around
        movesCheckGate = False
        while not movesCheckGate:
            text = ""
            text += "Your " + spName + " will have the following moves."
            text += "\n\tMove 1: " + moves[0]
            text += "\n\tMove 2: " + moves[1]
            text += "\n\tMove 3: " + moves[2]
            text += "\n\tMove 4: " + moves[3]
            text += "\n    Do you want to keep this moveset? Y/N"
            shell.respond(text)
            inputEvent.wait()
            inputEvent.clear()
            if shell.input_get in shell.yes:
                movesCheckGate = True
            elif shell.input_get not in shell.yes and shell.input_get not in shell.no:
                shell.respond("Um...I don't understand that response...")
            else:
                # Selecting Flip
                flipMoveGate = False
                while not flipMoveGate:
                    shell.respond("Which move would you like to swap?")
                    inputEvent.wait()
                    inputEvent.clear()
                    flip = shell.input_get
                    if flip in ["None", "none", "Null", "null"]:
                        flipName = None
                        flipMoveGate = True
                    else:
                        flipName = Pokedex.findMoveName(flip)
                        if flipName in moves and flipName != None:
                            flipMoveGate = True
                        else:
                            shell.respond("%s isn't part of your current moveset!" % flip)

                # Showing Move Options
                shell.respond(
                    "Ok, let me show you the most commonly-used moves again. How many suggestions would you like to see?")
                flipAmountGate = False
                while not flipAmountGate:
                    try:
                        inputEvent.wait()
                        inputEvent.clear()
                        swapAmount = int(shell.input_get)
                        if swapAmount >= 0:
                            # TODO: Implement the inability to chose already chosen moves
                            sortedMoves = TeamBuilder.findPokemonMetaMovesExc(spName, shell.tierfile, swapAmount, moves)
                            flipAmountGate = True
                        else:
                            shell.respond("Well I can't suggest that many suggestions, now can I?")
                    except:
                        shell.respond("Well that doesn't make any sense. Try again")
                text = ""
                for t in sortedMoves:
                    if t[0] != "Nothing" and t[0] != "":
                        moveData = Pokedex.findMoveData(t[0])
                        text += moveData["name"] + ":\n\tCAT: " + moveData["category"] + ",\n\tTYPE: " + moveData[
                            "type"] + ",\n\tPP: " + str(moveData["pp"]) + ",\n\tACC: " + str(
                            moveData["accuracy"]) + ",\n\tBASEPOW: " + str(moveData["basePower"]) + "," + shell.cut(
                            "\n\tDESC: " + moveData["shortDesc"]) + "\n\tPOP: " + str(t[1]) + "\n    "
                    else:
                        text += "Nothing:\n\tCAT: Nothing,\n\tTYPE: Nothing,\n\tPP: 0,\n\tACC: 0,\n\tBASEPOW: 0,\n\tDESC: Does nothing.\n\tPOP: 0\n    "
                shell.respond(text)

                # Selecting Flop
                flopMoveGate = False
                while not flopMoveGate:
                    shell.respond("Which move would you like to swap %s with?" % flipName)
                    inputEvent.wait()
                    inputEvent.clear()
                    flop = shell.input_get
                    if flop in ["None", "none", "Null", "null"]:
                        placeholder = moves.index(flipName)
                        moves[placeholder] = None
                        allNone = [False, False, False, False]
                        for i in range(len(moves)):
                            if moves[i] == None:
                                allNone[i] = True
                        if all(allNone):
                            shell.respond(
                                "Oh dear, it seems that you just made a completely empty moveset! That's not allowed in Pokemon: each Pokemon must have at least ONE move")
                            moves[placeholder] = flipName
                        else:
                            flopMoveGate = True
                    else:
                        flopName = Pokedex.findMoveName(flop)
                        if flopName != None:
                            if Pokedex.findMoveID(flop) in MetaDex.findPokemonTierMoves(spName, shell.tierfile):
                                if flopName not in moves:
                                    if "Hidden Power" in flopName:
                                        shell.respond(
                                            "Oh, I see you want to add Hidden Power to your arsenal. That's fine, but we will then need to change your IV's then.")
                                        maxIVs = Pokedex.findTypeHPSpreads(flopName[13])["max all"][0]
                                        maxIVList = maxIVs.split("/")
                                        try:
                                            shell.teamMatesDict[spName]["ivs"]["hp"] = int(maxIVList[0])
                                            shell.teamMatesDict[spName]["ivs"]["atk"] = int(maxIVList[1])
                                            shell.teamMatesDict[spName]["ivs"]["def"] = int(maxIVList[2])
                                            shell.teamMatesDict[spName]["ivs"]["spa"] = int(maxIVList[3])
                                            shell.teamMatesDict[spName]["ivs"]["spd"] = int(maxIVList[4])
                                            shell.teamMatesDict[spName]["ivs"]["spe"] = int(maxIVList[5])
                                            moves[moves.index(flipName)] = flopName
                                            shell.respond(
                                                "I've set your IVs to be the maximum they can be and still compatible with %s.\nIf you don't like this selection, you can always change it later when you import your team into Pokemon Showdown." % flopName)
                                            flopMoveGate = True
                                        except:
                                            shell.respond(
                                                "An error has occurred with the data. Huh, how did that escape me? Don't worry, its not your fault, but this is unexpected and could potentially be serious.\nI'm going to exist this program. Please contact my programmer immediately.")
                                            sys.exit()
                                    else:
                                        moves[moves.index(flipName)] = flopName
                                        flopMoveGate = True
                                else:
                                    shell.respond(
                                        "Oh, you already have %s as a move for your %s. Please select a different move." % (
                                        flopName, spName))
                            else:
                                shell.respond(
                                    "Oh, there seems to be a problem. Either %s can't learn this move, or it is used SO rarely that I couldn't find any useful data. In any case, try a different move." % spName)
                        else:
                            shell.respond("I'm sorry, but that is not a valid move. Try again")
        shell.teamMatesDict[spName]["moves"]["move1"] = moves[0]
        shell.teamMatesDict[spName]["moves"]["move2"] = moves[1]
        shell.teamMatesDict[spName]["moves"]["move3"] = moves[2]
        shell.teamMatesDict[spName]["moves"]["move4"] = moves[3]
        shell.respond("Excellent! Your %s now has moves!" % spName)
        shell.update(spName, "moves")

        # Selecting Items
        shell.respond("Alright, it's time to look at items.")
        if len(MetaDex.findPokemonTierItems(spName, shell.tierfile)) > 1:
            if "Fling" in [shell.teamMatesDict[spName]["moves"]["move1"], shell.teamMatesDict[spName]["moves"]["move2"],
                           shell.teamMatesDict[spName]["moves"]["move3"], shell.teamMatesDict[spName]["moves"]["move4"]]:
                text = ""
                text += "Ah yes, your " + spName + " has the move Fling! Fling's power and effect depends on the user's item (the item is then used up). Here are a few interesting items and effects.\nFor the full list, check out Serebii: https://www.serebii.net/games/fling.shtml"
                text += "\n    Iron Ball:\n\tFLING'S POWER: " + str(
                    Pokedex.findItemFlingBasePower("iron ball")) + "\n\tFLING'S EFFECT: None"
                text += "\n    Flame Orb:\n\tFLING'S POWER: " + str(
                    Pokedex.findItemFlingBasePower("flame orb")) + "\n\tFLING'S EFFECT: Burns opponent"
                text += "\n    Light Ball:\n\tFLING'S POWER: " + str(
                    Pokedex.findItemFlingBasePower("light ball")) + "\n\tFLING'S EFFECT: Paralyses opponent"
                text += "\n    Toxic Orb:\n\tFLING'S POWER: " + str(
                    Pokedex.findItemFlingBasePower("toxic orb")) + "\n\tFLING'S EFFECT: Badly poisons opponent"
                text += "\n    King's Rock:\n\tFLING'S POWER: " + str(
                    Pokedex.findItemFlingBasePower("king's rock")) + "\n\tFLING'S EFFECT: Flinches opponent"
                text += "\n    White Herb:\n\tFLING'S POWER: " + str(
                    Pokedex.findItemFlingBasePower("white herb")) + shell.cut(
                    "\n\tFLING'S EFFECT: Restores Stat Changes on opponent")
                text += "\n    Lum Berry:\n\tFLING'S POWER: " + str(
                    Pokedex.findItemFlingBasePower("lum berry")) + shell.cut(
                    "\n\tFLING'S EFFECT: Opponent recovers from any status problem")
                shell.respond(text)

            if "Natural Gift" in [shell.teamMatesDict[spName]["moves"]["move1"],
                                  shell.teamMatesDict[spName]["moves"]["move2"],
                                  shell.teamMatesDict[spName]["moves"]["move3"],
                                  shell.teamMatesDict[spName]["moves"]["move4"]]:
                text = ""
                text += "Ah yes, your " + spName + " has the move Natural Gift! Natural Gift's power and effect depends on the user's held berry (the berry is then used up). Here are a few interesting berries and effects.\nFor the full list, check out Serebii: https://www.serebii.net/games/naturalgift.shtml"
                text += "\n    As a special note, the power that Natural Gift gets from each berry varies from generation to generation. I will be displaying data from the most recent generation."
                text += "\n    Roseli Berry:\n\tNATURAL GIFT'S POWER: " + str(Pokedex.findItemNaturalGiftBasePower(
                    "roseliberry")) + "\n\tNATURAL GIFT'S TYPE: " + Pokedex.findItemNaturalGiftType("roseliberry")
                text += "\n    Leppa Berry:\n\tNATURAL GIFT'S POWER: " + str(Pokedex.findItemNaturalGiftBasePower(
                    "leppaberry")) + "\n\tNATURAL GIFT'S TYPE: " + Pokedex.findItemNaturalGiftType("leppaberry")
                text += "\n    Aguav Berry:\n\tNATURAL GIFT'S POWER: " + str(Pokedex.findItemNaturalGiftBasePower(
                    "aguavberry")) + "\n\tNATURAL GIFT'S TYPE: " + Pokedex.findItemNaturalGiftType("aguavberry")
                text += "\n    Lum Berry:\n\tNATURAL GIFT'S POWER: " + str(Pokedex.findItemNaturalGiftBasePower(
                    "lumberry")) + "\n\tNATURAL GIFT'S Type: " + Pokedex.findItemNaturalGiftType("lumberry")
                text += "\n    Watmel Berry:\n\tNATURAL GIFT'S POWER: " + str(Pokedex.findItemNaturalGiftBasePower(
                    "watmelberry")) + "\n\tNATURAL GIFT'S Type: " + Pokedex.findItemNaturalGiftType("watmelberry")
                shell.respond(text)

            shell.respond("I'm going to show the most popular items. How many should I suggest? (Int)")
            itemAmountGate = False
            while not itemAmountGate:
                try:
                    inputEvent.wait()
                    inputEvent.clear()
                    itemAmount = int(shell.input_get)
                    itemAmountGate = True
                except:
                    shell.respond("Um...how can I show that many items? Try again")
            sortedItems = TeamBuilder.findPokemonMetaItems(spName, shell.tierfile, itemAmount)
            text = ""
            for s in sortedItems:
                itemData = Pokedex.findItemData(s[0])
                text += itemData["name"] + ":" + shell.cut("\n\tDESC: " + itemData["desc"]) + "\n\tPOP: " + str(
                    s[1]) + "\n    "
            shell.respond(text)
            itemGate = False
            while not itemGate:
                if "vgc" in shell.tier or "battlespot" in shell.tier:
                    shell.respond(
                        "Which item would you like to give to %s? Note that for the team that you are building, no two Pokemon may hold the same item!" % spName)
                    inputEvent.wait()
                    inputEvent.clear()
                else:
                    shell.respond("Which item would you like to give to %s?" % spName)
                    inputEvent.wait()
                    inputEvent.clear()
                itemName = Pokedex.findItemName(shell.input_get)
                if itemName != None:
                    if "vgc" in shell.tier or "battlespot" in shell.tier:
                        itemsList = []
                        for sp in shell.teamMatesDict:
                            if shell.teamMatesDict[sp]["item"] != None:
                                itemsList.append(shell.teamMatesDict[sp]["item"])
                        if itemName in itemsList:
                            shell.respond(
                                "Oh, it seems that one of your Pokemon already holds that item. You must therefore select another item for your %s.\nYou can change edit this later on when you import your team into Pokemon Showdown" % spName)
                        else:
                            shell.teamMatesDict[spName]["item"] = itemName
                            itemGate = True
                    else:
                        shell.teamMatesDict[spName]["item"] = itemName
                        itemGate = True
                else:
                    shell.respond("I'm sorry, but that's not a registered item. Did you maybe spell it wrong?")
        else:
            shell.respond(
                "Ah, I see that %s can only have one item. I'll automatically update your %s to hold that item." % (
                    spName, spName))
            shell.teamMatesDict[spName]["item"] = Pokedex.findItemName(
                list(MetaDex.findPokemonTierItems(spName, shell.tierfile).keys())[0])
        shell.respond("Excellent! Your %s is now holding a %s!" % (spName, shell.teamMatesDict[spName]["item"]))
        shell.update(spName, "item")

        shell.respond("We are almost done with your %s. Just a few simple things to take care of." % spName)

        # Selecting Happiness
        shell.respond("Alright, let's move on to Happiness.")
        moves = [shell.teamMatesDict[spName]["moves"]["move1"], shell.teamMatesDict[spName]["moves"]["move2"],
                 shell.teamMatesDict[spName]["moves"]["move3"], shell.teamMatesDict[spName]["moves"]["move4"]]
        if "Frustration" in moves and "Return" not in moves:
            shell.respond(
                "Ah, yes. One of your moves is Frustration. This move has it's highest power when happiness is 0. I'll do that automatically for you!")
            shell.teamMatesDict[spName]["happiness"] = 0
        elif "Return" in moves and "Frustration" not in moves:
            shell.respond(
                "Ah, yes. One of your moves is Return.This move has it's highest power when happiness is maxed out. I'll do that automatically for you!")
            shell.teamMatesDict[spName]["happiness"] = 255
        elif "Return" in moves and "Frustration" in moves:
            shell.respond(
                "Oh hold on, you have both Return and Frustration as moves for your %s.\nThis isn't necessary. Return and Frustration are basically the same move, except where one increases in power as happiness goes up, the other decreases in power. \nI'll set Happiness to it's max setting, as this is the default, making Return the strongest of the two.\nI can't change the moveset now, but later when you import this team into Pokemon Showdown, remove Frustration and replace it with another move, k?" % spName)
            shell.teamMatesDict[spName]["happiness"] = 255
        else:
            shell.respond(
                "In your case, happiness does not affect your Pokemon at all. So I'll just set it to max, as this is it's default value.")
            shell.teamMatesDict[spName]["happiness"] = 255
        shell.update(spName, "happiness")

        # Selecting Level
        shell.respond("Ok, almost there. Time to chose what level your %s should be at." % spName)
        if "vgc" in shell.tier or "battlespot" in shell.tier:
            shell.respond("Remember, Pokemon in this team must be at level of 50 or under.")
            evoLevel = Pokedex.findPokemonEvoLevel(spName)
            if evoLevel != None and evoLevel < 50:
                shell.respond(
                    "Also, your %s evolves at level %s, so you must chose a level equal or greater than that" % (
                        spName, evoLevel))
                shell.respond("What level would like your Pokemon to be? (Int)")
                levelGate = False
                while not levelGate:
                    try:
                        inputEvent.wait()
                        inputEvent.clear()
                        if evoLevel < int(shell.input_get) <= 50:
                            shell.teamMatesDict[spName]["level"] = int(shell.input_get)
                            levelGate = True
                        else:
                            shell.respond("That's impossible to do, try again!")
                    except:
                        shell.respond("Um...I don't understand that response...")
            elif evoLevel != None and evoLevel <= 50:
                shell.respond(
                    "Oh, it seems that this Pokemon can oly be level 50. Not to worry, I'll autmatically update that for you!")
                shell.teamMatesDict[spName]["level"] = 50
                levelGate = True
            else:
                shell.respond("What level would like your Pokemon to be? (Int)")
                levelGate = False
                while not levelGate:
                    try:
                        inputEvent.wait()
                        inputEvent.clear()
                        if 0 < int(shell.input_get) <= 50:
                            shell.teamMatesDict[spName]["level"] = int(shell.input_get)
                            levelGate = True
                        else:
                            shell.respond("That's impossible to do, try again!")
                    except:
                        shell.respond("Um...I don't understand that response...")
        else:
            evoLevel = Pokedex.findPokemonEvoLevel(spName)
            if evoLevel != None:
                shell.respond(
                    "Remember, your %s evolves at level %s, so you must chose a level equal or greater than that" % (
                        spName, evoLevel))
                shell.respond("What level would like your Pokemon to be?")
                levelGate = False
                while not levelGate:
                    try:
                        inputEvent.wait()
                        inputEvent.clear()
                        if evoLevel <= int(shell.input_get) <= 100:
                            shell.teamMatesDict[spName]["level"] = int(shell.input_get)
                            levelGate = True
                        else:
                            shell.respond("That's impossible to do, try again")
                    except:
                        shell.respond("Um...I don't understand that response...")
            else:
                shell.respond("What level would like your Pokemon to be? (Int)")
                levelGate = False
                while not levelGate:
                    try:
                        inputEvent.wait()
                        inputEvent.clear()
                        if 0 <= int(shell.input_get) <= 100:
                            shell.teamMatesDict[spName]["level"] = int(shell.input_get)
                            levelGate = True
                        else:
                            shell.respond("That's impossible to do, try again")
                    except:
                        shell.respond("Um...I don't understand that response...")
        shell.respond("Excellent! Your %s is now at Level %s" % (spName, shell.teamMatesDict[spName]["level"]))
        shell.update(spName, "level")

        # Selecting Shininess
        shell.respond("And last but probably the most important, shininess!")
        shinyGate = False
        while not shinyGate:
            if spName not in ["Celebi", "Victini", "Keldeo", "Meloetta", "Meloetta-Pirouette", "Zygarde", "Hoopa",
                              "Hoopa-Unbound", "Volcanion", "Tapu Koko", "Tapu Fini", "Tapu Bulu", "Tapu Lele",
                              "Cosmog", "Cosmoem", "Solgaleo", "Lunala", "Nihilego", "Buzzwole", "Pheromosa",
                              "Xurkitree", "Celesteela", "Kartana", "Guzzlord", "Necrozma", "Magearna",
                              "Marshadow"]:
                shell.respond("Do you want %s to be shiny? (Y/N)" % spName)
                inputEvent.wait()
                inputEvent.clear()
                if shell.input_get in shell.yes:
                    shell.teamMatesDict[spName]["shiny"] = "Yes"
                    shinyGate = True
                elif shell.input_get in shell.no:
                    shell.teamMatesDict[spName]["shiny"] = "No"
                    shinyGate = True
                else:
                    shell.respond("Um...I don't understand that response...")
            else:
                shell.respond("I see that your %s can not be legally shiny. Maybe one day..." % spName)
                shell.teamMatesDict[spName]["shiny"] = "No"
                shinyGate = True
        shell.update(spName, "shiny")

        if shell.teamMateNames.index(spName) < 5:
            finalGate = False
            while not finalGate:
                shell.respond(
                    "Alright, this Pokemon is done! Type 'Next' when you are ready to move on to the next member of your team.")
                inputEvent.wait()
                inputEvent.clear()
                if shell.input_get in ["Next", "next", "NEXT"]:
                    finalGate = True
        else:
            shell.respond("And we are done! You have just successfulling made your very own competitive Pokemon team!")
            doneGate = False
            while not doneGate:
                shell.respond("When you are completely done, type 'Done' so I can export your team.")
                inputEvent.wait()
                inputEvent.clear()
                if shell.input_get in ["Done", "done", "DONE"]:
                    shell.export()
                    doneGate = True
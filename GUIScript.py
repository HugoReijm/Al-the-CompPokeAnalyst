from tkinter import *
import Pokedex, MetaDex, Tools, random, datetime, os

def AI(shell):
    shell.yes = ["Y", "y", "Yes", "yes", "YES"]
    shell.no = ["N", "n", "No", "no", "NO"]

    #shell.respond("Hello! I'm Al, here to help build your personal competitive Pokemon team!")
    #shell.respond("The great thing is, after we have built your team, I'll automatically export your team so you can easily import it into Pokemon Showdown, a Competitive Pokemon Battle Simulator used by hundreds of people every day!")
    #shell.respond("Let's get started!")
    # TODO: implement personal names and inout of user names

    #chooseTier(shell)
    #CLEAR THIS
    shell.tier = "gen7doublesou-1695"
    shell.tierfile = shell.tier+".json"

    # Helping the User Start a New Team and Selecting First Team Member
    #firstMemberGate = False
    #while not firstMemberGate:
    #    shell.respond("So, do you know which Pokemon you want to start your team with? (Y/N)")
    #    shell.inputEvent.wait()
    #    if shell.input_get in shell.yes:
    #        firstMemberGate = True
    #        shell.respond("Great! Innovation makes a great team!")
    #    elif shell.input_get in shell.no:
    #        firstMemberGate = True
    #        shell.respond("That's ok. There are plenty of Pokemon to choose from. Let me give you a few suggestions.")
    #        text = ""
    #        for poke in Tools.rawCountTopFinds(shell.tierfile, 20):
    #            pokeData = Pokedex.findPokemonData(poke[0])
    #            if len(pokeData["types"]) == 1:
    #                text += poke[0] + ":\n\tTYPE: " + pokeData["types"][0] + "\n\tSTATS: " + str(
    #                    pokeData["baseStats"]["hp"]) + "/" + str(pokeData["baseStats"]["atk"]) + "/" + str(
    #                    pokeData["baseStats"]["def"]) + "/" + str(pokeData["baseStats"]["spa"]) + "/" + str(
    #                    pokeData["baseStats"]["spd"]) + "/" + str(pokeData["baseStats"]["spe"]) + "\n\tPOP: " + str(
    #                    poke[1]) + "\n\n    "
    #            elif len(pokeData["types"]) == 2:
    #                text += poke[0] + ":\n\tTYPE: " + pokeData["types"][0] + ", " + pokeData["types"][
    #                    1] + "\n\tSTATS: " + str(pokeData["baseStats"]["hp"]) + "/" + str(
    #                    pokeData["baseStats"]["atk"]) + "/" + str(pokeData["baseStats"]["def"]) + "/" + str(
    #                    pokeData["baseStats"]["spa"]) + "/" + str(pokeData["baseStats"]["spd"]) + "/" + str(
    #                    pokeData["baseStats"]["spe"]) + "\n\tPOP: " + str(poke[1]) + "\n\n    "
    #        shell.respond(text[:-5])
    #    else:
    #        shell.respond("Um... I don't understand your response ")
    #shell.teamMateNames = []
    #teamAdder(shell)

    # Adding Other 5 Members
    #for i in range(5):
    #    showMemberOptions(shell)
    #    teamAdder(shell)

    #switchMembers(shell)

    # CLEAR THIS
    shell.teamMateNames = ["Zapdos","Landorus-Therian", "Heatran", "Ninetales-Alola", "Sandslash-Alola", "Tapu Fini"]

    #TODO: oh, something interesting...apparently having multiple of the same species messes with the program, cause it then works on all individuals simultaneously
    #shell.teamMateNames = ["Blissey","Blissey","Blissey","Blissey","Blissey","Blissey"]

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
        dict["happiness"] = 255
        if "battlespot" in shell.tier or "vgc" in shell.tier:
            dict["level"] = 50
        else:
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

    shell.analyzer.update(shell, "species")
    shell.analyzer.update(shell, "stats")
    shell.analyzer.update(shell, "physpec Offense")
    shell.analyzer.update(shell, "physpec Defense")
    shell.toplevel.deiconify()
    #shell.toplevel.iconify()

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

        chooseAbility(shell,poke)

        shell.respond("Now that we have that decided, let's move on to IV spreads. Remember that if you want %s to have a certain Hidden Power, you can do that here or when selecting moves." % spName)

        # Choosing IVs
        chooseIVs(shell,poke)

        # Choosing Natures and EVs
        chooseNatureEVs(shell,poke)

        # Selecting Gender
        shell.respond("Ok, now we have to change gears a little. Time to talk about your Pokemon's gender")
        chooseGender(shell,poke)

        # Show Popular Moves
        shell.respond("Alright, now hey comes the REALLY important part: selecting moves.\tI'll show you a few of the most common moves that %s can have." % spName)
        chooseMoves(shell,poke)

        # Selecting Items
        shell.respond("Alright, it's time to look at items.")
        chooseItem(shell,poke)

        shell.respond("We are almost done with your %s. Just a few simple things to take care of." % spName)

        # Selecting Happiness
        shell.respond("Alright, let's move on to Happiness.")
        chooseHappiness(shell,poke)

        # Selecting Level
        shell.respond("Ok, almost there. Time to chose what level your %s should be at." % spName)
        chooseLevel(shell,poke)

        # Selecting Shininess
        shell.respond("And last but probably the most important, shininess!")
        chooseShiny(shell,poke)

        if shell.teamMateNames.index(spName) < 5:
            checkMember(shell,poke)
        else:
            finalCheck(shell)
            shell.respond("And we are done! You have just successfulling made your very own competitive Pokemon team!")
            doneGate = False
            while not doneGate:
                shell.respond("When you are completely done, type 'Done' so I can export your team.")
                shell.inputEvent.wait()
                if shell.input_get in ["Done", "done", "DONE"]:
                    export(shell)
                    doneGate = True

def chooseTier(shell):
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
        shell.inputEvent.wait()
        if shell.input_get in tiers:
            shell.tier = shell.input_get
            confirmTierGate = False
            while not confirmTierGate:
                shell.respond("You would like to build a team for %s? (Y/N)" % shell.tier)
                shell.inputEvent.wait()
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
        shell.inputEvent.wait()
        if shell.input_get in ["fun", "Fun"]:
            shell.tier = shell.tier + "-0"
            tierSeverityGate = True
        elif shell.input_get in ["serious", "Serious"]:
            shell.tier = shell.tier + "-1500"
            tierSeverityGate = True
        elif shell.input_get in ["hard core", "hard Core", "Hard Core", "Hard Core", "hardcore", "hardCore",
                                 "Hardcore",
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
            shell.respond(
                "Um, I don't understand that response. You must pick one of the four options shown above.")
    shell.tierfile = shell.tier + ".json"
    shell.respond("Excellent! Let's get started with your team then!")
    
def teamAdder(shell):
    teamAdderGate = False
    while not teamAdderGate:
        if len(shell.teamMateNames) == 0:
            shell.respond("Which Pokemon would you like to start your team with?")
            shell.inputEvent.wait()
        else:
            if "anythinggoes" not in shell.tier:
                shell.respond("Which Pokemon would you like to add to your team? Note that your team can not have two or more Pokemon with the same National Pokedex number!")
                shell.inputEvent.wait()
            else:
                shell.respond("Which Pokemon would you like to add to your team?")
                shell.inputEvent.wait()
        species = Pokedex.findPokemonSpecies(shell.input_get)
        if species != None:
            if MetaDex.findPokemonTierData(species, shell.tierfile) != None:
                if "anythinggoes" not in shell.tier:
                    numList = []
                    for s in shell.teamMateNames:
                        numList.append(Pokedex.findPokemonNum(s))
                    if Pokedex.findPokemonNum(species) in numList:
                        shell.respond("Oh, you can not have two or more Pokemon with the same National Pokedex number! You must select another Pokemon.")
                    else:
                        forme = Pokedex.findPokemonForme(species)
                        if forme == "Mega":
                            megaCheck=True
                            for teamMate in shell.teamMateNames:
                                if Pokedex.findPokemonForme(teamMate) == "Mega":
                                    megaCheck=False
                                    break
                            if megaCheck:
                                shell.teamMateNames.append(species)
                                teamAdderGate = True
                            else:
                                shell.respond("Oh, I see that you're trying to add another mega to your team. I mean, this is technically allowed, but I wouldn't suggest it. You can only use one mega per battle.")
                                multiMegaGate = False
                                while not multiMegaGate:
                                    shell.respond("Are you sure you want multiple megas in your team?")
                                    shell.inputEvent.wait()
                                    if shell.input_get in shell.yes:
                                        shell.respond("Alright, I'll add another mega then!")
                                        shell.teamMateNames.append(species)
                                        multiMegaGate = True
                                        teamAdderGate = True
                                    elif shell.input_get in shell.no:
                                        multiMegaGate = True
                                    else:
                                        shell.respond("Um...I don't understand your response...")
                        else:
                            shell.teamMateNames.append(species)
                            teamAdderGate = True
                else:
                    forme = Pokedex.findPokemonForme(species)
                    if forme == "Mega":
                        megaCheck=True
                        for teamMate in shell.teamMateNames:
                            if Pokedex.findPokemonForme(teamMate) == "Mega":
                                megaCheck=False
                                break
                        if megaCheck:
                            shell.teamMateNames.append(species)
                            teamAdderGate = True
                        else:
                            shell.respond(
                                "Oh, I see that you're trying to add another mega to your team. I mean, this is technically allowed, but I wouldn't suggest it. You can only use one mega per battle.")
                            multiMegaGate = False
                            while not multiMegaGate:
                                shell.respond("Are you sure you want multiple megas in your team?")
                                shell.inputEvent.wait()
                                if shell.input_get in shell.yes:
                                    shell.respond("Alright, I'll add another mega then!")
                                    shell.teamMateNames.append(species)
                                    multiMegaGate = True
                                    teamAdderGate = True
                                elif shell.input_get in shell.no:
                                    multiMegaGate = True
                                else:
                                    shell.respond("Um...I don't understand your response...")
                    else:
                        shell.teamMateNames.append(species)
                        teamAdderGate = True
            else:
                shell.respond("Oh, I'm sorry. There seems to be a problem.")
                shell.respond("Either Pokemon %s is not allowed in tier %s." % (species, shell.tier))
                shell.respond("Or it might be that Pokemon %s is SO rare in tier %s that there isn't enough data on it" % (species, shell.tier))
                shell.respond("Either way, I suggest chosing another Pokemon. That way I have the data necessary to help you")
        else:
            shell.respond("Um...I don't understand your response...")

def teamAdjuster(shell,index):
    teamAdderGate = False
    while not teamAdderGate:
        if "anythinggoes" not in shell.tier:
            shell.respond("Which Pokemon would you like to add to your team? Note that your team can not have two or more Pokemon with the same National Pokedex number!")
            shell.inputEvent.wait()
        else:
            shell.respond("Which Pokemon would you like to add to your team?")
            shell.inputEvent.wait()
        species = Pokedex.findPokemonSpecies(shell.input_get)
        if species != None:
            if MetaDex.findPokemonTierData(species, shell.tierfile) != None:
                if "anythinggoes" not in shell.tier:
                    numList = []
                    for s in shell.teamMateNames:
                        numList.append(Pokedex.findPokemonNum(s))
                    if Pokedex.findPokemonNum(species) in numList:
                        shell.respond("Oh, you can not have two or more Pokemon with the same National Pokedex number! You must select another Pokemon.")
                    else:
                        forme = Pokedex.findPokemonForme(species)
                        if forme == "Mega":
                            megaCheck = True
                            for teamMate in shell.teamMateNames:
                                if Pokedex.findPokemonForme(teamMate) == "Mega":
                                    megaCheck=False
                                    break
                            if megaCheck:
                                shell.teamMateNames[index]=species
                                teamAdderGate = True
                            else:
                                shell.respond("Oh, I see that you're trying to add another mega to your team. I mean, this is technically allowed, but I wouldn't suggest it. You can only use one mega per battle.")
                                multiMegaGate = False
                                while not multiMegaGate:
                                    shell.respond("Are you sure you want multiple megas in your team?")
                                    shell.inputEvent.wait()
                                    if shell.input_get in shell.yes:
                                        shell.respond("Alright, I'll add another mega then!")
                                        shell.teamMateNames[index]=species
                                        multiMegaGate = True
                                        teamAdderGate = True
                                    elif shell.input_get in shell.no:
                                        multiMegaGate = True
                                    else:
                                        shell.respond("Um...I don't understand your response...")
                        else:
                            shell.teamMateNames[index]=species
                            teamAdderGate = True
                else:
                    forme = Pokedex.findPokemonForme(species)
                    if forme == "Mega":
                        megaCheck=True
                        for teamMate in shell.teamMateNames:
                            if Pokedex.findPokemonForme(teamMate) == "Mega":
                                megaCheck=False
                                break
                        if megaCheck:
                            shell.teamMateNames[index]=species
                            teamAdderGate = True
                        else:
                            shell.respond(
                                "Oh, I see that you're trying to add another mega to your team. I mean, this is technically allowed, but I wouldn't suggest it. You can only use one mega per battle.")
                            multiMegaGate = False
                            while not multiMegaGate:
                                shell.respond("Are you sure you want multiple megas in your team?")
                                shell.inputEvent.wait()
                                if shell.input_get in shell.yes:
                                    shell.respond("Alright, I'll add another mega then!")
                                    shell.teamMateNames[index]=species
                                    multiMegaGate = True
                                    teamAdderGate = True
                                elif shell.input_get in shell.no:
                                    multiMegaGate = True
                                else:
                                    shell.respond("Um...I don't understand your response...")
                    else:
                        shell.teamMateNames[index]=species
                        teamAdderGate = True
            else:
                shell.respond("Oh, I'm sorry. There seems to be a problem.")
                shell.respond("Either Pokemon %s is not allowed in tier %s." % (species, shell.tier))
                shell.respond("Or it might be that Pokemon %s is SO rare in tier %s that there isn't enough data on it" % (species, shell.tier))
                shell.respond("Either way, I suggest chosing another Pokemon. That way I have the data necessary to help you")
        else:
            shell.respond("Um...I don't understand your response...")

def showMemberOptions(shell):
    # TODO: include the species clause when showing new pokes
    shell.respond("Ok, let me suggest some team-mates. How many suggestions would you like to see? (Int)")
    memberSelectGate = False
    while not memberSelectGate:
        try:
            shell.inputEvent.wait()
            teamSuggAmount = int(shell.input_get)
            memberSelectGate = True
        except:
            shell.respond("Um...I don't understand your response...")
            # TODO: implement ID checks for species clause
    text = ""
    for poke in Tools.findTeamMetaMatches(shell.teamMateNames, shell.tierfile, teamSuggAmount):
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

def switchMembers(shell):
    # Switching Team Members If Needed
    confirmTeamGate = False
    while not confirmTeamGate:
        text = ""
        text += "Here is your team!"
        for t in shell.teamMateNames:
            text += "\n    " + t
        shell.respond(text)
        shell.respond("Are you happy with the selection? (Y/N)")
        shell.inputEvent.wait()
        if shell.input_get in shell.yes:
            confirmTeamGate = True
        elif shell.input_get not in shell.yes and shell.input_get not in shell.no:
            shell.respond("Um...I don't understand that response...")
        else:
            # Finding Flip
            flipMemberGate = False
            while not flipMemberGate:
                shell.respond("Which Pokemon in your team would you like to swap? (String)")
                shell.inputEvent.wait()
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
                    shell.inputEvent.wait()
                    swapAmount = int(shell.input_get)
                    teamMateNamesprime = []
                    for i in range(len(shell.teamMateNames)):
                        teamMateNamesprime.append(shell.teamMateNames[i])
                    del teamMateNamesprime[teamMateNamesprime.index(flipName)]
                    swapAmountGate = True
                except:
                    shell.respond("Um...unfortunately I can't understand your request. Try again")
            text = ""
            for poke in Tools.findTeamMetaMatches(teamMateNamesprime, shell.tierfile, swapAmount):
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
                    shell.inputEvent.wait()
                    flop = shell.input_get
                else:
                    shell.respond("Which Pokemon in your team would you like to swap %s with?" % flipName)
                    shell.inputEvent.wait()
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
                                            shell.inputEvent.wait()
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
                                        shell.inputEvent.wait()
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

def chooseAbility(shell,poke):
    # Choosing Ability
    spName = shell.teamMatesDict[poke]["species"]
    abilities = Pokedex.findPokemonAbilities(spName)
    metaAbilities = MetaDex.findPokemonTierAbilities(spName, shell.tierfile)
    text = ""
    text += shell.cut(spName + " can have the following abilities:")
    #TODO: it is possible to have an ability that isnt found in the metadex (example: snowcloak for alolan ninetales in gen7doublesou-1695)
    if Tools.compress(abilities["0"]) in metaAbilities:
        text += "\n\t" + abilities["0"] + ":" + shell.cut(
            "\n\t    DESC: " + Pokedex.findAbilityShortDesc(abilities["0"])) + "\n\t    POP: " + str(
            metaAbilities[Pokedex.findAbilityID(abilities["0"])])
    else:
        text += "\n\t" + abilities["0"] + ":" + shell.cut(
            "\n\t    DESC: " + Pokedex.findAbilityShortDesc(abilities["0"])) + "\n\t    POP: 0.0"
    if len(abilities) > 1:
        if "1" in abilities:
            if Tools.compress(abilities["1"]) in metaAbilities:
                text += "\n\t" + abilities["1"] + ":" + shell.cut(
                    "\n\t    DESC: " + Pokedex.findAbilityShortDesc(abilities["1"])) + "\n\t    POP: " + str(
                    metaAbilities[Pokedex.findAbilityID(abilities["1"])])
            else:
                text += "\n\t" + abilities["1"] + ":" + shell.cut(
                    "\n\t    DESC: " + Pokedex.findAbilityShortDesc(abilities["1"])) + "\n\t    POP: 0.0"
        if "S" in abilities:
            text += shell.cut("\n\tAdditionally, " + spName + " also has a special ability:")
            if Tools.compress(abilities["S"]) in metaAbilities:
                text += "\n\t" + abilities["S"] + ":" + shell.cut(
                    "\n\t    DESC: " + Pokedex.findAbilityShortDesc(abilities["S"])) + "\n\t    POP: " + str(
                    metaAbilities[Pokedex.findAbilityID(abilities["S"])])
            else:
                text += "\n\t" + abilities["S"] + ":" + shell.cut(
                    "\n\t    DESC: " + Pokedex.findAbilityShortDesc(abilities["S"])) + "\n\t    POP: 0.0"
        if "H" in abilities:
            text += shell.cut("\n    Additionally, " + spName + " also has a Hidden ability:")
            if Tools.compress(abilities["H"]) in metaAbilities:
                text += "\n\t" + abilities["H"] + ":" + shell.cut(
                    "\n\t    DESC: " + Pokedex.findAbilityShortDesc(abilities["H"])) + "\n\t    POP: " + str(
                    metaAbilities[Pokedex.findAbilityID(abilities["H"])])
            else:
                text += "\n\t" + abilities["H"] + ":" + shell.cut(
                    "\n\t    DESC: " + Pokedex.findAbilityShortDesc(abilities["H"])) + "\n\t    POP: 0.0"
        shell.respond(text)
        abilityGate = False
        while not abilityGate:
            shell.respond("What ability would you like %s to have?" % spName)
            shell.inputEvent.wait()
            abName = Pokedex.findAbilityName(shell.input_get)
            for s in ["0", "1", "S", "H"]:
                if s in abilities and abName == abilities[s]:
                    if Tools.compress(abilities[s]) in metaAbilities:
                        shell.teamMatesDict[poke]["ability"] = abName
                        abilityGate = True
                        break
            if not abilityGate:
                shell.respond("Oh, something interesting has occurred: either %s can't have the ability %s in tier %s OR its so rare that I can't find ANY data on it. Since I can't tell, its best that you just choose a different ability." % (spName,abName,shell.tier))
    else:
        shell.respond(text)
        shell.respond(
            "As you can see, %s only has one ability, so we don't have much choice here. I'll update your %s automatically, so you dont have to worry about that." % (
                spName, spName))
        shell.teamMatesDict[poke]["ability"] = abilities["0"]
    shell.respond("Done! Your %s now has the ability %s" % (spName, shell.teamMatesDict[poke]["ability"]))
    shell.update(spName, "ability")

def chooseIVs(shell,poke):
    spName = shell.teamMatesDict[poke]["species"]
    shell.respond(
        "First thing's first: I propose to give your %s the following IV spread: 31/31/31/31/31/31" % spName)
    shell.respond(
        "This is by far the most common IV spread for Pokemon. However, if you have something more specific in mind, you might want a different IV spread")
    ivGate = False
    while not ivGate:
        shell.respond("Do you want to use this IV spread?")
        shell.inputEvent.wait()
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
                shell.inputEvent.wait()
                if shell.input_get in shell.yes:
                    ivTypeGate = False
                    while not ivTypeGate:
                        shell.respond("What type would you like Hidden Power to be?")
                        shell.inputEvent.wait()
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
                    shell.inputEvent.wait()
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

def chooseNatureEVs(shell,poke):
    spName = shell.teamMatesDict[poke]["species"]
    shell.respond("Alright, it's time for Natures and EVs")
    shell.respond("%s has a few common Nature/EV spreads. How many would you like to see? (Int)" % spName)
    gate8 = False
    while not gate8:
        try:
            shell.inputEvent.wait()
            evAmount = int(shell.input_get)
            sortedSpreads = Tools.findPokemonMetaSpreads(spName, shell.tierfile, evAmount)
            gate8 = True
        except:
            shell.respond("How can I show you that many Nature/EV spreads? Try again")
    text = ""
    for s in range(len(sortedSpreads)):
        text += sortedSpreads[s][0] + ":\n\tPOP: " + str(sortedSpreads[s][1]) + "\n    "
    shell.respond(text[:-5])
    # TODO: what nature is what? fix
    natureGate = False
    while not natureGate:
        shell.respond("What Nature would you like to give to %s? (String)" % spName)
        shell.inputEvent.wait()
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
        shell.inputEvent.wait()
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
                    shell.inputEvent.wait()
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

def chooseGender(shell,poke):
    spName = shell.teamMatesDict[poke]["species"]
    if Pokedex.findPokemonGender(spName) != None:
        shell.respond(
            "Ah, this Pokemon has be a specific gender according to it's species. Don't worry, I'll take care of that")
        if Pokedex.findPokemonGender(spName) != "N":
            shell.teamMatesDict[spName]["gender"] = Pokedex.findPokemonGender(spName)
    else:
        genderGate = False
        while not genderGate:
            shell.respond("Do you have a specific gender in mind for %s? (Y/N)" % spName)
            shell.inputEvent.wait()
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
                    shell.inputEvent.wait()
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
    if shell.teamMatesDict[spName]["gender"] == "M":
        shell.respond("Done! Your %s is now a Male!" % spName)
    elif shell.teamMatesDict[spName]["gender"] == "F":
        shell.respond("Done! Your %s is now a Female!" % spName)
    else:
        shell.respond("Done! Your %s has no gender at all!" % spName)
    shell.update(spName, "gender")

def chooseMoves(shell,poke):
    spName = shell.teamMatesDict[poke]["species"]
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
        shell.respond("How many moves would you like to see? (Int)")
        showMovesGate = False
        while not showMovesGate:
            try:
                shell.inputEvent.wait()
                moveAmount = int(shell.input_get)
                sortedMoves = Tools.findPokemonMetaMoves(spName, shell.tierfile, moveAmount)
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
                shell.inputEvent.wait()
                if moveIndex != 1 and shell.input_get in ["None", "none", "Null", "null"]:
                    moves[moveIndex - 1] = None
                    moveGate = True
                else:
                    resName = Pokedex.findMoveName(shell.input_get)
                    if resName != None:
                        id = Pokedex.findMoveID(resName)
                        if "hiddenpower" in id:
                            id = Tools.compress(resName)
                        if id in MetaDex.findPokemonTierMoves(spName,shell.tierfile):
                            if resName not in moves:
                                if "Hidden Power" in resName:
                                    shell.respond("Oh, I see you want to add Hidden Power to your arsenal. That's fine, but we will then need to change your IV's then.")
                                    maxIVs = Pokedex.findTypeHPSpreads(resName[13:])["max all"][0]
                                    maxIVList = maxIVs.split("/")
                                    try:
                                        shell.teamMatesDict[spName]["ivs"]["hp"] = int(maxIVList[0])
                                        shell.teamMatesDict[spName]["ivs"]["atk"] = int(maxIVList[1])
                                        shell.teamMatesDict[spName]["ivs"]["def"] = int(maxIVList[2])
                                        shell.teamMatesDict[spName]["ivs"]["spa"] = int(maxIVList[3])
                                        shell.teamMatesDict[spName]["ivs"]["spd"] = int(maxIVList[4])
                                        shell.teamMatesDict[spName]["ivs"]["spe"] = int(maxIVList[5])
                                        moves[moveIndex-1] = resName
                                        shell.update(spName,"ivs")
                                        shell.respond("I've set your IVs to be the maximum they can be and still compatible with %s.\nIf you don't like this selection, you can always change it later when you import your team into Pokemon Showdown." % resName)
                                        moveGate = True
                                    except:
                                        shell.respond("An error has occurred with the data. Huh, how did that escape me? Don't worry, its not your fault, but this is unexpected and could potentially be serious.\nI'm going to exit this program. Please contact my programmer immediately.")
                                        #TODO: this doesnt work. fix that
                                        sys.exit()
                                else:
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
            shell.respond("Registered")
        else:
            shell.respond(
                "Due to meeting various requirements, this move for your %s has already been chosen to be %s. So that's already done!" % (
                    spName, moves[moveIndex - 1]))

    # Switching Moves Around
    movesCheckGate = False
    while not movesCheckGate:
        text = ""
        text += "Your " + spName + " will have the following moves."
        if moves[0] != None:
            text += "\n\tMove 1: " + moves[0]
        else:
            text += "\n\tMove 1: None"
        if moves[1] != None:
            text += "\n\tMove 2: " + moves[1]
        else:
            text += "\n\tMove 2: None"
        if moves[2] != None:
            text += "\n\tMove 3: " + moves[2]
        else:
            text += "\n\tMove 3: None"
        if moves[3] != None:
            text += "\n\tMove 4: " + moves[3]
        else:
            text += "\n\tMove 4: None"
        text += "\n    Do you want to keep this moveset? Y/N"
        shell.respond(text)
        shell.inputEvent.wait()
        if shell.input_get in shell.yes:
            movesCheckGate = True
        elif shell.input_get not in shell.yes and shell.input_get not in shell.no:
            shell.respond("Um...I don't understand that response...")
        else:
            # Selecting Flip
            flipMoveGate = False
            while not flipMoveGate:
                shell.respond("Which move would you like to swap?")
                shell.inputEvent.wait()
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
                    shell.inputEvent.wait()
                    swapAmount = int(shell.input_get)
                    if swapAmount >= 0:
                        # TODO: Implement the inability to chose already chosen moves
                        sortedMoves = Tools.findPokemonMetaMovesExc(spName, shell.tierfile, swapAmount, moves)
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
                shell.inputEvent.wait()
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
                        id = Pokedex.findMoveID(flop)
                        if "hiddenpower" in id:
                            id = Tools.compress(flopName)
                        if id in MetaDex.findPokemonTierMoves(spName, shell.tierfile):
                            if flopName not in moves:
                                if "Hidden Power" in flopName:
                                    shell.respond(
                                        "Oh, I see you want to add Hidden Power to your arsenal. That's fine, but we will then need to change your IV's then.")
                                    maxIVs = Pokedex.findTypeHPSpreads(flopName[13:])["max all"][0]
                                    maxIVList = maxIVs.split("/")
                                    try:
                                        shell.teamMatesDict[spName]["ivs"]["hp"] = int(maxIVList[0])
                                        shell.teamMatesDict[spName]["ivs"]["atk"] = int(maxIVList[1])
                                        shell.teamMatesDict[spName]["ivs"]["def"] = int(maxIVList[2])
                                        shell.teamMatesDict[spName]["ivs"]["spa"] = int(maxIVList[3])
                                        shell.teamMatesDict[spName]["ivs"]["spd"] = int(maxIVList[4])
                                        shell.teamMatesDict[spName]["ivs"]["spe"] = int(maxIVList[5])
                                        moves[moves.index(flipName)] = flopName
                                        shell.update(spName,"ivs")
                                        shell.respond(
                                            "I've set your IVs to be the maximum they can be and still compatible with %s.\nIf you don't like this selection, you can always change it later when you import your team into Pokemon Showdown." % flopName)
                                        flopMoveGate = True
                                    except:
                                        shell.respond(
                                            "An error has occurred with the data. Huh, how did that escape me? Don't worry, its not your fault, but this is unexpected and could potentially be serious.\nI'm going to exit this program. Please contact my programmer immediately.")
                                        #TODO: this doesnt work. fix this
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

def chooseItem(shell,poke):
    spName = shell.teamMatesDict[poke]["species"]
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
                shell.inputEvent.wait()
                itemAmount = int(shell.input_get)
                itemAmountGate = True
            except:
                shell.respond("Um...how can I show that many items? Try again")
        sortedItems = Tools.findPokemonMetaItems(spName, shell.tierfile, itemAmount)
        text = ""
        for s in sortedItems:
            itemData = Pokedex.findItemData(s[0])
            text += itemData["name"] + ":" + shell.cut("\n\tDESC: " + itemData["desc"]) + "\n\tPOP: " + str(s[1]) + "\n    "
        shell.respond(text)
        itemGate = False
        while not itemGate:
            if "vgc" in shell.tier or "battlespot" in shell.tier:
                shell.respond(
                    "Which item would you like to give to %s? Note that for the team that you are building, no two Pokemon may hold the same item!" % spName)
                shell.inputEvent.wait()
            else:
                shell.respond("Which item would you like to give to %s?" % spName)
                shell.inputEvent.wait()
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

def chooseHappiness(shell,poke):
    spName = shell.teamMatesDict[poke]["species"]
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
            "In your case, happiness does not affect your Pokemon at all. So I'll just set it to max, as this is it's default value. If you REALLy want to change it, you can do so later.")
        shell.teamMatesDict[spName]["happiness"] = 255
    shell.update(spName, "happiness")

def chooseLevel(shell,poke):
    spName = shell.teamMatesDict[poke]["species"]
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
                    shell.inputEvent.wait()
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
                    shell.inputEvent.wait()
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
                    shell.inputEvent.wait()
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
                    shell.inputEvent.wait()
                    if 0 <= int(shell.input_get) <= 100:
                        shell.teamMatesDict[spName]["level"] = int(shell.input_get)
                        levelGate = True
                    else:
                        shell.respond("That's impossible to do, try again")
                except:
                    shell.respond("Um...I don't understand that response...")
    shell.respond("Excellent! Your %s is now at Level %s" % (spName, shell.teamMatesDict[spName]["level"]))
    shell.update(spName, "level")

def chooseShiny(shell,poke):
    spName = shell.teamMatesDict[poke]["species"]
    shinyGate = False
    while not shinyGate:
        if spName not in ["Celebi", "Victini", "Keldeo", "Meloetta", "Meloetta-Pirouette", "Zygarde", "Hoopa",
                          "Hoopa-Unbound", "Volcanion", "Tapu Koko", "Tapu Fini", "Tapu Bulu", "Tapu Lele",
                          "Cosmog", "Cosmoem", "Solgaleo", "Lunala", "Nihilego", "Buzzwole", "Pheromosa",
                          "Xurkitree", "Celesteela", "Kartana", "Guzzlord", "Necrozma", "Magearna",
                          "Marshadow"]:
            shell.respond("Do you want %s to be shiny? (Y/N)" % spName)
            shell.inputEvent.wait()
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

def checkMember(shell,poke):
    spName = shell.teamMatesDict[poke]["species"]
    shell.respond("And we're done! your %s is finished! Take a moment to look at your %s and how it fits with your team." % (spName,spName))
    finalMemberGate=False
    while not finalMemberGate:
        shell.respond("Would you like to change anything? (Y/N)")
        shell.inputEvent.wait()
        if shell.input_get in shell.no:
            finalMemberGate=True
        elif shell.input_get not in shell.yes and shell.input_get not in shell.no:
            shell.respond("Um...I don't understand your response")
        else:
            finalMemberChangeGate=False
            while not finalMemberChangeGate:
                text = "What would you like to change? Please input one of the following options."
                text += "\n    Species (Basically starting over)"
                text += "\n    Ability"
                text += "\n    IVs"
                text += "\n    Nature and EVs"
                text += "\n    Moves"
                text += "\n    Item"
                text += "\n    Gender"
                text += "\n    Happiness"
                text += "\n    Level"
                text += "\n    Shininess"
                text += "\n    Nothing"
                shell.respond(text)
                shell.inputEvent.wait()
                if Tools.compress(shell.input_get) == "species":
                    #TODO: rename tab and switch CORRECTLY. encountering a problem because your deleting the teamMatesDict entry
                    index = shell.teamMateNames.index(poke)
                    shell.delete(poke)
                    del shell.teamMatesDict[poke]

                    showMemberOptions(shell)
                    teamAdjuster(shell,index)

                    member = shell.teamMateNames[index]
                    shell.the_menu.entryconfigure("None", label=member)
                    shell.the_menu.entryconfigure(member, state="normal")
                    shell.teamMatesDict[member] = {}
                    shell.teamMatesDict[member]["species"] = Pokedex.findPokemonSpecies(member)
                    shell.teamMatesDict[member]["ability"] = None
                    shell.teamMatesDict[member]["nature"] = None
                    shell.teamMatesDict[member]["baseStats"] = {"hp": Pokedex.findPokemonHP(member), "atk": Pokedex.findPokemonAtk(member),
                                         "def": Pokedex.findPokemonDef(member), "spa": Pokedex.findPokemonSpA(member),
                                         "spd": Pokedex.findPokemonSpD(member), "spe": Pokedex.findPokemonSpe(member)}
                    shell.teamMatesDict[member]["ivs"] = {"hp": 31, "atk": 31, "def": 31, "spa": 31, "spd": 31, "spe": 31}
                    shell.teamMatesDict[member]["evs"] = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0}
                    shell.teamMatesDict[member]["item"] = None
                    shell.teamMatesDict[member]["gender"] = None
                    if member == "Rayquaza-Mega":
                        shell.teamMatesDict[member]["moves"] = {"move1": "Dragon Ascent", "move2": None, "move3": None, "move4": None}
                    else:
                        shell.teamMatesDict[member]["moves"] = {"move1": None, "move2": None, "move3": None, "move4": None}
                    shell.teamMatesDict[member]["happiness"] = 255
                    if "battlespot" in shell.tier or "vgc" in shell.tier:
                        shell.teamMatesDict[member]["level"] = 50
                    else:
                        shell.teamMatesDict[member]["level"] = 100
                    shell.teamMatesDict[member]["shiny"] = None

                    spName = shell.teamMatesDict[member]["species"]
                    shell.switch(spName)
                    shell.respond("Let's start with %s." % spName)
                    text = ""
                    text += spName + " has the following base stats.\n    "
                    for stat in shell.teamMatesDict[member]["baseStats"]:
                        if stat == "hp":
                            text += stat + " : " + str(shell.teamMatesDict[member]["baseStats"][stat]) + "\n    "
                        else:
                            text += stat + ": " + str(shell.teamMatesDict[member]["baseStats"][stat]) + "\n    "
                    shell.respond(text[:-5])

                    chooseAbility(shell, member)

                    shell.respond("Now that we have that decided, let's move on to IV and Nature/EV spreads")

                    # Choosing IVs
                    chooseIVs(shell, member)

                    # Choosing Natures and EVs
                    chooseNatureEVs(shell, member)

                    # Selecting Gender
                    shell.respond("Ok, now we have to change gears a little. Time to talk about your Pokemon's gender")
                    chooseGender(shell, member)

                    # Show Popular Moves
                    shell.respond("Alright, now hey comes the REALLY important part: selecting moves.\tI'll show you a few of the most common moves that %s can have." % spName)
                    chooseMoves(shell, member)

                    # Selecting Items
                    shell.respond("Alright, it's time to look at items.")
                    chooseItem(shell, member)

                    shell.respond("We are almost done with your %s. Just a few simple things to take care of." % spName)

                    # Selecting Happiness
                    shell.respond("Alright, let's move on to Happiness.")
                    chooseHappiness(shell,member)

                    # Selecting Level
                    shell.respond("Ok, almost there. Time to chose what level your %s should be at." % spName)
                    chooseLevel(shell, member)

                    # Selecting Shininess
                    shell.respond("And last but probably the most important, shininess!")
                    chooseShiny(shell, member)

                    finalMemberChangeGate = True
                elif Tools.compress(shell.input_get) == "ability":
                    shell.teamMatesDict[poke]["ability"] = None
                    chooseAbility(shell,poke)
                    finalMemberChangeGate = True
                elif Tools.compress(shell.input_get) == "ivs":
                    shell.teamMatesDict[poke]["ivs"] = {"hp": 31, "atk": 31, "def": 31, "spa": 31, "spd": 31, "spe": 31}
                    chooseIVs(shell,poke)
                    finalMemberChangeGate = True
                elif Tools.compress(shell.input_get) == "natureandevs":
                    shell.teamMatesDict[poke]["nature"] = None
                    shell.teamMatesDict[poke]["evs"] = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0}
                    chooseNatureEVs(shell,poke)
                    finalMemberChangeGate = True
                elif Tools.compress(shell.input_get) == "moves":
                    if poke == "Rayquaza-Mega":
                        shell.teamMatesDict[poke]["moves"] = {"move1": "Dragon Ascent", "move2": None, "move3": None, "move4": None}
                    else:
                        shell.teamMatesDict[poke]["moves"] = {"move1": None, "move2": None, "move3": None, "move4": None}
                    chooseMoves(shell,poke)
                    finalMemberChangeGate = True
                elif Tools.compress(shell.input_get) == "item":
                    shell.teamMatesDict[poke]["item"] = None
                    chooseItem(shell,poke)
                    finalMemberChangeGate = True
                elif Tools.compress(shell.input_get) == "gender":
                    shell.teamMatesDict[poke]["gender"] = None
                    chooseGender(shell,poke)
                    finalMemberChangeGate = True
                elif Tools.compress(shell.input_get) == "happiness":
                    shell.teamMatesDict[poke]["happiness"] = 255
                    spName = shell.teamMatesDict[poke]["species"]
                    moves = [shell.teamMatesDict[spName]["moves"]["move1"],
                             shell.teamMatesDict[spName]["moves"]["move2"],
                             shell.teamMatesDict[spName]["moves"]["move3"],
                             shell.teamMatesDict[spName]["moves"]["move4"]]
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
                        happinessGate = False
                        while not happinessGate:
                            shell.respond(
                                "In your case, happiness does not affect your Pokemon at all. What would you like it's Happiness to be? Remember that Happiness ranges between 0 and 255 (Int)")
                            shell.inputEvent.wait()
                            try:
                                h = int(shell.input_get)
                                if 0 <= h <= 255:
                                    shell.teamMatesDict[spName]["happiness"] = h
                                    shell.respond("Excellent! Your %s has a Happiness of %s" % (spName,shell.teamMatesDict[spName]["happiness"]))
                                    happinessGate = True
                                else:
                                    shell.respond(
                                        "I'm sorry, but Happiness can only range between 0 and 255. Try again.")
                            except:
                                shell.respond("Um...I don't understand your response")
                    shell.update(spName, "happiness")
                    finalMemberChangeGate = True
                elif Tools.compress(shell.input_get) == "level":
                    if "battlespot" in shell.tier and "vgc" in shell.tier:
                        shell.teamMatesDict[poke]["level"] = 50
                    else:
                        shell.teamMatesDict[poke]["level"] = 100
                    chooseLevel(shell, poke)
                    finalMemberChangeGate = True
                elif Tools.compress(shell.input_get) == "shininess":
                    shell.teamMatesDict[poke]["shiny"] = None
                    chooseShiny(shell,poke)
                    finalMemberChangeGate = True
                elif Tools.compress(shell.input_get) == "nothing":
                    finalMemberChangeGate = True
                    finalMemberGate = True
                else:
                    shell.respond("Um...I don't understand your response")

def finalCheck(shell):
    finalGate = False
    while not finalGate:
        shell.respond("Would you like to change anything about your team? (Y/N)")
        shell.inputEvent.wait()
        if shell.input_get in shell.no:
            finalGate = True
        elif shell.input_get not in shell.yes and shell.input_get not in shell.no:
            shell.respond("Um...I don't understand your response")
        else:
            memberChangeGate = False
            while not memberChangeGate:
                shell.respond("Which team member would you like to change? (String)")
                shell.inputEvent.wait()
                compressedNames = []
                for name in shell.teamMateNames:
                    compressedNames.append(Tools.compress(name))
                if Tools.compress(shell.input_get) in compressedNames:
                    poke = shell.teamMateNames[compressedNames.index(Tools.compress(shell.input_get))]
                    checkMember(shell,poke)
                    memberChangeGate=True
                else:
                    shell.respond("Um...I don't understand your response")

def export(shell):
    shell.respond("I'm going to put your team in the same location you put this program. If you can't find it, just search for it on your computer's search bar. I promise it's there.")
    now = datetime.datetime.now()
    fileName = shell.tier + "_" + str(now.day) + "-" + str(now.month) + "-" + str(now.year) + "_" + str(
        now.hour) + "-" + str(now.minute) + ".txt"
    file = open(os.path.dirname(os.path.realpath(__file__))+"/"+fileName, "w")
    for poke in shell.teamMatesDict:
        if shell.teamMatesDict[poke]["gender"] != None:
            if shell.teamMatesDict[poke]["item"] != None:
                file.write(shell.teamMatesDict[poke]["species"] + " (" + shell.teamMatesDict[poke]["gender"] + ") @ " +
                           shell.teamMatesDict[poke]["item"] + "\n")
                # shell.respond(teamMatesDict[poke]["species"]+" ("+teamMatesDict[poke]["gender"]+") @ "+teamMatesDict[poke]["item"])
            else:
                file.write(shell.teamMatesDict[poke]["species"] + " (" + shell.teamMatesDict[poke]["gender"] + ")\n")
                # shell.respond(teamMatesDict[poke]["species"]+" ("+teamMatesDict[poke]["gender"]+")")
        else:
            if shell.teamMatesDict[poke]["item"] != None:
                file.write(shell.teamMatesDict[poke]["species"] + " @ " + shell.teamMatesDict[poke]["item"] + "\n")
                # shell.respond(teamMatesDict[poke]["species"]+" @ "+teamMatesDict[poke]["item"])
            else:
                file.write(shell.teamMatesDict[poke]["species"] + "\n")
                # shell.respond(teamMatesDict[poke]["species"])

        if shell.teamMatesDict[poke]["ability"] != None:
            file.write("Ability: " + shell.teamMatesDict[poke]["ability"] + "\n")
        # shell.respond("Ability: "+teamMatesDict[poke]["ability"])

        if shell.teamMatesDict[poke]["level"] != None:
            file.write("Level: " + str(shell.teamMatesDict[poke]["level"]) + "\n")
        # shell.respond("Level: "+str(teamMatesDict[poke]["level"]))

        if shell.teamMatesDict[poke]["happiness"] != 255 and shell.teamMatesDict[poke]["happiness"] != None:
            file.write("Happiness: " + str(shell.teamMatesDict[poke]["happiness"]) + "\n")
            # shell.respond("Happiness: " + str(teamMatesDict[poke]["happiness"]))

        if shell.teamMatesDict[poke]["shiny"] == "Yes":
            file.write("Shiny: Yes\n")
            # shell.respond("Shiny: Yes")

        evStringNeeded = False
        evString = ""
        if shell.teamMatesDict[poke]["evs"]["hp"] != 0:
            evString = evString + str(shell.teamMatesDict[poke]["evs"]["hp"]) + " HP"
            evStringNeeded = True
        if shell.teamMatesDict[poke]["evs"]["atk"] != 0:
            evString = evString + " / " + str(shell.teamMatesDict[poke]["evs"]["atk"]) + " Atk"
            evStringNeeded = True
        if shell.teamMatesDict[poke]["evs"]["def"] != 0:
            evString = evString + " / " + str(shell.teamMatesDict[poke]["evs"]["def"]) + " Def"
            evStringNeeded = True
        if shell.teamMatesDict[poke]["evs"]["spa"] != 0:
            evString = evString + " / " + str(shell.teamMatesDict[poke]["evs"]["spa"]) + " SpA"
            evStringNeeded = True
        if shell.teamMatesDict[poke]["evs"]["spd"] != 0:
            evString = evString + " / " + str(shell.teamMatesDict[poke]["evs"]["spd"]) + " SpD"
            evStringNeeded = True
        if shell.teamMatesDict[poke]["evs"]["spe"] != 0:
            evString = evString + " / " + str(shell.teamMatesDict[poke]["evs"]["spe"]) + " Spe"
            evStringNeeded = True
        if evStringNeeded == True:
            file.write("EVs: " + evString + "\n")
            # shell.respond("EVs: "+evString)

        file.write(shell.teamMatesDict[poke]["nature"] + " Nature\n")
        # shell.respond(teamMatesDict[poke]["nature"]+" Nature")

        ivStringNeeded = False
        ivString = ""
        if shell.teamMatesDict[poke]["ivs"]["hp"] != 31:
            ivString = ivString + str(shell.teamMatesDict[poke]["ivs"]["hp"]) + " HP"
            ivStringNeeded = True
        if shell.teamMatesDict[poke]["ivs"]["atk"] != 31:
            ivString = ivString + " / " + str(shell.teamMatesDict[poke]["ivs"]["atk"]) + " Atk"
            ivStringNeeded = True
        if shell.teamMatesDict[poke]["ivs"]["def"] != 31:
            ivString = ivString + " / " + str(shell.teamMatesDict[poke]["ivs"]["def"]) + " Def"
            ivStringNeeded = True
        if shell.teamMatesDict[poke]["ivs"]["spa"] != 31:
            ivString = ivString + " / " + str(shell.teamMatesDict[poke]["ivs"]["spa"]) + " SpA"
            ivStringNeeded = True
        if shell.teamMatesDict[poke]["ivs"]["spd"] != 31:
            ivString = ivString + " / " + str(shell.teamMatesDict[poke]["ivs"]["spd"]) + " SpD"
            ivStringNeeded = True
        if shell.teamMatesDict[poke]["ivs"]["spe"] != 31:
            ivString = ivString + " / " + str(shell.teamMatesDict[poke]["ivs"]["spe"]) + " Spe"
            ivStringNeeded = True
        if ivStringNeeded == True:
            file.write("IVs: " + ivString + "\n")
            # shell.respond("IVs: " + ivString)

        for move in ["move1", "move2", "move3", "move4"]:
            if shell.teamMatesDict[poke]["moves"][move] != None:
                file.write("- " + shell.teamMatesDict[poke]["moves"][move] + "\n")
                # shell.respond("- " + teamMatesDict[poke]["moves"][move])
        file.write("\n")
    file.close()
    shell.respond("Ok, your team can be found in %s" % fileName)
    shell.respond("So what you want to do is go to http://play.pokemonshowdown.com/")
    shell.respond("Click on the 'Teambuilder' button.")
    shell.respond("Click on the 'New Team' button.")
    shell.respond("Click on the 'Import from text' button.")
    shell.respond("Copy the entire text from the file I just sent you and paste it in the large input field.")
    shell.respond("Click on the 'Import/Export' button on top.")
    shell.respond("Your team will have been imported into the website!")
    shell.respond("For extra measure, do you see that bar on the top left of your screen? It should read something like 'Untitled #'? This is where you can name your team!")
    shell.respond("Under that, you should find the 'Format' option. Click it. A large window should appear.")
    shell.respond("Select the format that most looks like %s (this is the tier/format you decided to build this team for)." % shell.tier)
    shell.respond("To check if everything went perfectingly in the team building process, click the 'Validate' button. A window should pop up.")
    shell.respond("If your team gets validated for your chosen format/tier, your all set.")
    shell.respond("If you do get an error, just follow the instructions given by the error message to correvct this. Revalidate your team and you should be ready to go!")
    shell.respond("NOTE: Your imported team will be preserved on the website via cookies. Therefore, you can come back later to Pokemon Showdown, and your team will still be there!")
    shell.respond("However, if you delete the cookies stored on your computer, you team will disappear. Don't worry. All you have to dude is just import your team from the file we just made today.")
    shell.respond("If you want to test your team in an actual battle, click on the Home tab")
    shell.respond("Before you can participate in an actual battle, you will need a Pokemon Showdown account.If you don't have one already, making one is very easy and takes two seconds: all it requires is a username and a password. If you already have an account, make sure you are signed in")
    shell.respond("Now that you are signed in, click on the 'Format' option on the left of the screen. A large window will appear.")
    shell.respond("Select the format that most looks like %s (this is the tier/format you decided to build this team for)." % shell.tier)
    shell.respond("Now that the website knows which type of battle you want to participate in, it will show you your teams (or one of them if you have multiple.)")
    shell.respond("Select the team you wish to battle with.")
    shell.respond("If the website doesn't show the team you wish to battle with, it means that your team hasn't been validated for that format. You must then go back to the Teambuilder, select your team, and validate it for the format/tier you wish to battle in.")
    shell.respond("Alright, your all set! Just press the 'Battle!' button and have fun! Note, it may take a few moments for the servers to find you an opponent. Please be patient.")
    shell.respond("glhf! Good luck and have fun!")
from tkinter import *
from tkinter import ttk
import math,Pokedex,Tools,threading,os,glob,GUIScript,TeamAnalyzer
import urllib.request

class AL:
    @staticmethod
    def atkNatureColor(nature):
        if nature in ["Lonely","Adamant","Naughty","Brave"]:
            return "firebrick2"
        elif nature in ["Bold","Modest","Calm","Timid"]:
            return "dodger blue"
        else:
            return "lawn green"

    @staticmethod
    def defNatureColor(nature):
        if nature in ["Bold","Lax","Impish","Relaxed"]:
            return "firebrick2"
        elif nature in ["Lonely","Mild","Gentle","Hasty"]:
            return "dodger blue"
        else:
            return "lawn green"

    @staticmethod
    def spaNatureColor(nature):
        if nature in ["Modest","Mild","Rash","Quiet"]:
            return "firebrick2"
        elif nature in ["Adamant","Impish","Careful","Jolly"]:
            return "dodger blue"
        else:
            return "lawn green"

    @staticmethod
    def spdNatureColor(nature):
        if nature in ["Calm","Gentle","Careful","Sassy"]:
            return "firebrick2"
        elif nature in ["Naughty","Lax","Rash","Naive"]:
            return "dodger blue"
        else:
            return "lawn green"

    @staticmethod
    def speNatureColor(nature):
        if nature in ["Timid", "Hasty", "Jolly", "Naive"]:
            return "firebrick2"
        elif nature in ["Brave", "Relaxed", "Quiet", "Sassy"]:
            return "dodger blue"
        else:
            return "lawn green"

    @staticmethod
    def hpStatCalc(base,evs,ivs,level):
        return math.floor(((2*base+ivs+math.floor(evs/4))*level)/100)+level+10

    @staticmethod
    def atkStatCalc(base,evs,ivs,level,nature):
        if nature in ["Lonely", "Adamant", "Naughty", "Brave"]:
            return math.floor((math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5) * 1.1)
        elif nature in ["Bold", "Modest", "Calm", "Timid"]:
            return math.floor((math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5) * 0.9)
        else:
            return math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5

    @staticmethod
    def defStatCalc(base,evs,ivs,level,nature):
        if nature in ["Bold", "Lax", "Impish", "Relaxed"]:
            return math.floor((math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5) * 1.1)
        elif nature in ["Lonely", "Mild", "Gentle", "Hasty"]:
            return math.floor((math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5) * 0.9)
        else:
            return math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5

    @staticmethod
    def spaStatCalc(base,evs,ivs,level,nature):
        if nature in ["Modest", "Mild", "Rash", "Quiet"]:
            return math.floor((math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5) * 1.1)
        elif nature in ["Adamant", "Impish", "Careful", "Jolly"]:
            return math.floor((math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5) * 0.9)
        else:
            return math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5

    @staticmethod
    def spdStatCalc(base,evs,ivs,level,nature):
        if nature in ["Calm", "Gentle", "Careful", "Sassy"]:
            return math.floor((math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5) * 1.1)
        elif nature in ["Naughty", "Lax", "Rash", "Naive"]:
            return math.floor((math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5) * 0.9)
        else:
            return math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5

    @staticmethod
    def speStatCalc(base,evs,ivs,level,nature):
        if nature in ["Timid", "Hasty", "Jolly", "Naive"]:
            return math.floor((math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5) * 1.1)
        elif nature in ["Brave", "Relaxed", "Quiet", "Sassy"]:
            return math.floor((math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5) * 0.9)
        else:
            return math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5

    @staticmethod
    def get_picture_name(icon, species):
        pokemonData = Pokedex.findPokemonData(species)
        num = str(pokemonData['num'])
        while len(num) < 3:
            num = '0' + num
        if 'forme' in pokemonData:
            num += '-'
            forme = Tools.compress(pokemonData['forme'])

            if forme in ['alola', 'ash', 'black', 'mega', 'midnight', 'pompom', 'school', 'sensu', 'unbound']:
                forme = forme[0]

            elif forme in ['megax', 'megay']:
                forme = 'm' + forme[-1]

            elif forme in ['heat', 'wash']:
                forme = forme[0]
                if icon:
                    num = num[:-1]

            elif forme in ['therian', 'trash']:
                forme = 's'

            elif num in ['773-'] and icon:
                num = num[:-1]
                forme = ''

            elif num in ['778-']:
                if icon:
                    num = num[:-1]
                    forme = ''
                else:
                    forme = forme[0]

            num += forme
        return num

    def download_picture(self, name, icon):
        if icon:
            print('Downloading icon', name)
            url = 'http://www.serebii.net/pokedex-sm/icon/'
        else:
            print('Downloading picture', name)
            url = 'http://www.serebii.net/sunmoon/pokemon/'
        url += name + '.png'
        print(url)
        try:
            urllib.request.urlretrieve(url, name + '.png')
            return True
        except:
            print('failed to download', name)
            return False

    def request_picture(self,name,icon=False):
        if icon:
            os.chdir(os.path.dirname(os.path.realpath(__file__))+'/data/images/Icons')
        else:
            os.chdir(os.path.dirname(os.path.realpath(__file__))+'/data/images/Larges')

        pkmn_list = []
        for file in glob.glob("*.png"):
            pkmn_list.append(file[:-4])

        picture_available = True
        if name not in pkmn_list:
            picture_available = self.download_picture(name, icon)

        os.chdir('../..')

        return picture_available

    def respond(self,text):
        self.messages.config(state=NORMAL)
        self.messages.insert(END, 'Al: %s\n\n' % text)
        self.messages.see(END)
        self.messages.config(state=DISABLED)

    def showAnalyzer(self):
        pass
        #if self.toplevel:
        #   if self.toplevel.state() in ["iconic","icon","withdrawn"]:
        #       self.toplevel.deiconify()
    
    def updateAnalyzer(self, option):
        if option in ["species","moves","stats","physpec Offense","physpec Defense","advice"]:
            self.analyzer.update(self, option)
        elif option == "threats":
            self.analyzer.threats(self)
        elif option == "checkAndCounters":
            self.analyzer.checkAndCounters(self)
        else:
            print("Whoops, something went wrong with the options for the team analyzer")
            print(option)
    
    def switch(self,name):
        self.current = self.teamMatesDict[name]
        self.spriteCanvas.delete("all")
        if self.current["species"] != None:
            filename = self.get_picture_name(True,name)
            if self.request_picture(filename,True):
                self.spriteCanvas.spriteFile = PhotoImage(file=os.path.dirname(os.path.realpath(__file__))+"/data/images/icons/"+filename+".png")
                self.spriteCanvas.spriteFile = self.spriteCanvas.spriteFile.zoom(80)
                self.spriteCanvas.spriteFile = self.spriteCanvas.spriteFile.subsample(int(self.spriteCanvas.spriteFile.width() / 80))
                self.spriteCanvas.create_image(2,2, anchor=NW, image=self.spriteCanvas.spriteFile)
            else:
                self.spriteCanvas.spriteFile = PhotoImage(file=os.path.dirname(os.path.realpath(__file__)) + "/data/images/icons/Pokeball.png")
                self.spriteCanvas.spriteFile = self.spriteCanvas.spriteFile.zoom(7)
                self.spriteCanvas.spriteFile = self.spriteCanvas.spriteFile.subsample(int(self.spriteCanvas.spriteFile.width() / 80))
                self.spriteCanvas.create_image(1, 1, anchor=NW, image=self.spriteCanvas.spriteFile)
        self.speciesLabelText.set(self.current["species"])
        if self.current["species"] != None:
            types = Pokedex.findPokemonTypes(self.current["species"])
            if len(types) == 2:
                self.typeLabelText.set(types[0] + ", " + types[1])
            else:
                self.typeLabelText.set(types[0])
        else:
            self.typeLabelText.set(None)
        self.abilityLabelText.set(self.current["ability"])
        self.itemLabelText.set(self.current["item"])
        self.levelLabelText.set(self.current["level"])
        self.genderLabelText.set(self.current["gender"])
        self.happinessLabelText.set(self.current["happiness"])
        self.shinyLabelText.set(self.current["shiny"])
        self.hpBS.set(str(self.current["baseStats"]["hp"]))
        self.atkBS.set(str(self.current["baseStats"]["atk"]))
        self.defBS.set(str(self.current["baseStats"]["def"]))
        self.spaBS.set(str(self.current["baseStats"]["spa"]))
        self.spdBS.set(str(self.current["baseStats"]["spd"]))
        self.speBS.set(str(self.current["baseStats"]["spe"]))
        self.hpIV.set(str(self.current["ivs"]["hp"]))
        self.atkIV.set(str(self.current["ivs"]["atk"]))
        self.defIV.set(str(self.current["ivs"]["def"]))
        self.spaIV.set(str(self.current["ivs"]["spa"]))
        self.spdIV.set(str(self.current["ivs"]["spd"]))
        self.speIV.set(str(self.current["ivs"]["spe"]))
        self.hpEV.set(str(self.current["evs"]["hp"]))
        self.atkEV.set(str(self.current["evs"]["atk"]))
        self.defEV.set(str(self.current["evs"]["def"]))
        self.spaEV.set(str(self.current["evs"]["spa"]))
        self.spdEV.set(str(self.current["evs"]["spd"]))
        self.speEV.set(str(self.current["evs"]["spe"]))
        if self.current["species"]!=None:
            self.hpStatCanvas.coords(self.hpStatBar, 0, 5, int(
                self.hpStatCalc(self.current["baseStats"]["hp"], self.current["evs"]["hp"], self.current["ivs"]["hp"],
                                self.current["level"]) / 4), 16)
            self.atkStatCanvas.coords(self.atkStatBar, 0, 5, int(
                self.atkStatCalc(self.current["baseStats"]["atk"], self.current["evs"]["atk"], self.current["ivs"]["atk"],
                                 self.current["level"], self.current["nature"]) / 4), 16)
            self.atkStatCanvas.itemconfig(self.atkStatBar, fill=self.atkNatureColor(self.current["nature"]))
            self.defStatCanvas.coords(self.defStatBar, 0, 5, int(
                self.defStatCalc(self.current["baseStats"]["def"], self.current["evs"]["def"], self.current["ivs"]["def"],
                                 self.current["level"], self.current["nature"]) / 4), 16)
            self.defStatCanvas.itemconfig(self.defStatBar, fill=self.defNatureColor(self.current["nature"]))
            self.spaStatCanvas.coords(self.spaStatBar, 0, 5, int(
                self.spaStatCalc(self.current["baseStats"]["spa"], self.current["evs"]["spa"], self.current["ivs"]["spa"],
                                 self.current["level"], self.current["nature"]) / 4), 16)
            self.spaStatCanvas.itemconfig(self.spaStatBar, fill=self.spaNatureColor(self.current["nature"]))
            self.spdStatCanvas.coords(self.spdStatBar, 0, 5, int(
                self.spdStatCalc(self.current["baseStats"]["spd"], self.current["evs"]["spd"], self.current["ivs"]["spd"],
                                 self.current["level"], self.current["nature"]) / 4), 16)
            self.spdStatCanvas.itemconfig(self.spdStatBar, fill=self.spdNatureColor(self.current["nature"]))
            self.speStatCanvas.coords(self.speStatBar, 0, 5, int(
                self.speStatCalc(self.current["baseStats"]["spe"], self.current["evs"]["spe"], self.current["ivs"]["spe"],
                                 self.current["level"], self.current["nature"]) / 4), 16)
            self.speStatCanvas.itemconfig(self.speStatBar, fill=self.speNatureColor(self.current["nature"]))
            self.hpTotal.set(str(self.hpStatCalc(self.current["baseStats"]["hp"], self.current["evs"]["hp"], self.current["ivs"]["hp"],self.current["level"])))
            self.atkTotal.set(str(self.atkStatCalc(self.current["baseStats"]["atk"], self.current["evs"]["atk"], self.current["ivs"]["atk"],self.current["level"], self.current["nature"])))
            self.defTotal.set(str(self.defStatCalc(self.current["baseStats"]["def"], self.current["evs"]["def"], self.current["ivs"]["def"],self.current["level"], self.current["nature"])))
            self.spaTotal.set(str(self.spaStatCalc(self.current["baseStats"]["spa"], self.current["evs"]["spa"], self.current["ivs"]["spa"],self.current["level"], self.current["nature"])))
            self.spdTotal.set(str(self.spdStatCalc(self.current["baseStats"]["spd"], self.current["evs"]["spd"], self.current["ivs"]["spd"],self.current["level"], self.current["nature"])))
            self.speTotal.set(str(self.speStatCalc(self.current["baseStats"]["spe"], self.current["evs"]["spe"], self.current["ivs"]["spe"],self.current["level"], self.current["nature"])))
        else:
            self.hpStatCanvas.coords(self.hpStatBar, 0, 5, 0, 16)
            self.atkStatCanvas.coords(self.atkStatBar, 0, 5, 0, 16,fill="lawn green")
            #self.atkStatCanvas.itemconfig(self.atkStatBar, fill="lawn green")
            self.defStatCanvas.coords(self.defStatBar, 0, 5, 0, 16,fill="lawn green")
            #self.defStatCanvas.itemconfig(self.defStatBar, fill="lawn green")
            self.spaStatCanvas.coords(self.spaStatBar, 0, 5, 0, 16,fill="lawn green")
            #self.spaStatCanvas.itemconfig(self.spaStatBar, fill="lawn green")
            self.spdStatCanvas.coords(self.spdStatBar, 0, 5, 0, 16,fill="lawn green")
            #self.spdStatCanvas.itemconfig(self.spdStatBar, fill="lawn green")
            self.speStatCanvas.coords(self.speStatBar, 0, 5, 0, 16,fill="lawn green")
            #self.speStatCanvas.itemconfig(self.speStatBar, fill="lawn green")
            self.hpTotal.set(str(0))
            self.atkTotal.set(str(0))
            self.defTotal.set(str(0))
            self.spaTotal.set(str(0))
            self.spdTotal.set(str(0))
            self.speTotal.set(str(0))
        self.move1Name.set(self.current["moves"]["move1"])
        self.move2Name.set(self.current["moves"]["move2"])
        self.move3Name.set(self.current["moves"]["move3"])
        self.move4Name.set(self.current["moves"]["move4"])
        move1Data = Pokedex.findMoveData(self.current["moves"]["move1"])
        move2Data = Pokedex.findMoveData(self.current["moves"]["move2"])
        move3Data = Pokedex.findMoveData(self.current["moves"]["move3"])
        move4Data = Pokedex.findMoveData(self.current["moves"]["move4"])
        if move1Data != None:
            self.move1Cat.set(move1Data["category"])
            self.move1Type.set(move1Data["type"])
            self.move1BasePower.set(str(move1Data["basePower"]))
            self.move1PP.set(str(move1Data["pp"]))
            if move1Data["accuracy"] != True:
                self.move1Acc.set(str(move1Data["accuracy"]) + "%")
            else:
                self.move1Acc.set("100%")
        else:
            self.move1Cat.set("N/A")
            self.move1Type.set("N/A")
            self.move1BasePower.set("N/A")
            self.move1PP.set("N/A")
            self.move1Acc.set("N/A")

        if move2Data != None:
            self.move2Cat.set(move2Data["category"])
            self.move2Type.set(move2Data["type"])
            self.move2BasePower.set(str(move2Data["basePower"]))
            self.move2PP.set(str(move2Data["pp"]))
            if move2Data["accuracy"] != True:
                self.move2Acc.set(str(move2Data["accuracy"]) + "%")
            else:
                self.move2Acc.set("100%")
        else:
            self.move2Cat.set("N/A")
            self.move2Type.set("N/A")
            self.move2BasePower.set("N/A")
            self.move2PP.set("N/A")
            self.move2Acc.set("N/A")

        if move3Data != None:
            self.move3Cat.set(move3Data["category"])
            self.move3Type.set(move3Data["type"])
            self.move3BasePower.set(str(move3Data["basePower"]))
            self.move3PP.set(str(move3Data["pp"]))
            if move3Data["accuracy"] != True:
                self.move3Acc.set(str(move3Data["accuracy"]) + "%")
            else:
                self.move3Acc.set("100%")
        else:
            self.move3Cat.set("N/A")
            self.move3Type.set("N/A")
            self.move3BasePower.set("N/A")
            self.move3PP.set("N/A")
            self.move3Acc.set("N/A")

        if move4Data != None:
            self.move4Cat.set(move4Data["category"])
            self.move4Type.set(move4Data["type"])
            self.move4BasePower.set(str(move4Data["basePower"]))
            self.move4PP.set(str(move4Data["pp"]))
            if move4Data["accuracy"] != True:
                self.move4Acc.set(str(move4Data["accuracy"]) + "%")
            else:
                self.move4Acc.set("100%")
        else:
            self.move4Cat.set("N/A")
            self.move4Type.set("N/A")
            self.move4BasePower.set("N/A")
            self.move4PP.set("N/A")
            self.move4Acc.set("N/A")

        #print("switch: %s" % self.current["index"])

    def update(self,option):
        if option=="types":
            self.updateAnalyzer("species")
            types = Pokedex.findPokemonTypes(self.current["species"])
            if len(types) == 2:
                self.typeLabelText.set(types[0] + ", " + types[1])
            else:
                self.typeLabelText.set(types[0])
        elif option == "ability":
            self.abilityLabelText.set(self.current["ability"])
        elif option == "item":
            self.itemLabelText.set(self.current["item"])
        elif option == "level":
            self.updateAnalyzer("stats")
            self.updateAnalyzer("physpec Offense")
            self.updateAnalyzer("physpec Defense")
            self.levelLabelText.set(self.current["level"])
            self.hpStatCanvas.coords(self.hpStatBar, 0, 5, int(
                self.hpStatCalc(self.current["baseStats"]["hp"], self.current["evs"]["hp"], self.current["ivs"]["hp"],
                                self.current["level"]) / 4), 16)
            self.atkStatCanvas.coords(self.atkStatBar, 0, 5, int(
                self.atkStatCalc(self.current["baseStats"]["atk"], self.current["evs"]["atk"],
                                 self.current["ivs"]["atk"],
                                 self.current["level"], self.current["nature"]) / 4), 16)
            self.atkStatCanvas.itemconfig(self.atkStatBar, fill=self.atkNatureColor(self.current["nature"]))
            self.defStatCanvas.coords(self.defStatBar, 0, 5, int(
                self.defStatCalc(self.current["baseStats"]["def"], self.current["evs"]["def"],
                                 self.current["ivs"]["def"],
                                 self.current["level"], self.current["nature"]) / 4), 16)
            self.defStatCanvas.itemconfig(self.defStatBar, fill=self.defNatureColor(self.current["nature"]))
            self.spaStatCanvas.coords(self.spaStatBar, 0, 5, int(
                self.spaStatCalc(self.current["baseStats"]["spa"], self.current["evs"]["spa"],
                                 self.current["ivs"]["spa"],
                                 self.current["level"], self.current["nature"]) / 4), 16)
            self.spaStatCanvas.itemconfig(self.spaStatBar, fill=self.spaNatureColor(self.current["nature"]))
            self.spdStatCanvas.coords(self.spdStatBar, 0, 5, int(
                self.spdStatCalc(self.current["baseStats"]["spd"], self.current["evs"]["spd"],
                                 self.current["ivs"]["spd"],
                                 self.current["level"], self.current["nature"]) / 4), 16)
            self.spdStatCanvas.itemconfig(self.spdStatBar, fill=self.spdNatureColor(self.current["nature"]))
            self.speStatCanvas.coords(self.speStatBar, 0, 5, int(
                self.speStatCalc(self.current["baseStats"]["spe"], self.current["evs"]["spe"],
                                 self.current["ivs"]["spe"],
                                 self.current["level"], self.current["nature"]) / 4), 16)
            self.speStatCanvas.itemconfig(self.speStatBar, fill=self.speNatureColor(self.current["nature"]))
            self.hpTotal.set(str(
                self.hpStatCalc(self.current["baseStats"]["hp"], self.current["evs"]["hp"], self.current["ivs"]["hp"],
                                self.current["level"])))
            self.atkTotal.set(str(
                self.atkStatCalc(self.current["baseStats"]["atk"], self.current["evs"]["atk"],
                                 self.current["ivs"]["atk"],
                                 self.current["level"], self.current["nature"])))
            self.defTotal.set(str(
                self.defStatCalc(self.current["baseStats"]["def"], self.current["evs"]["def"],
                                 self.current["ivs"]["def"],
                                 self.current["level"], self.current["nature"])))
            self.spaTotal.set(str(
                self.spaStatCalc(self.current["baseStats"]["spa"], self.current["evs"]["spa"],
                                 self.current["ivs"]["spa"],
                                 self.current["level"], self.current["nature"])))
            self.spdTotal.set(str(
                self.spdStatCalc(self.current["baseStats"]["spd"], self.current["evs"]["spd"],
                                 self.current["ivs"]["spd"],
                                 self.current["level"], self.current["nature"])))
            self.speTotal.set(str(
                self.speStatCalc(self.current["baseStats"]["spe"], self.current["evs"]["spe"],
                                 self.current["ivs"]["spe"],
                                 self.current["level"], self.current["nature"])))
        elif option == "gender":
            self.genderLabelText.set(self.current["gender"])
        elif option == "happiness":
            self.happinessLabelText.set(self.current["happiness"])
            if self.current["moves"]["move1"] == "Frustration":
                self.move1BasePower.set(str(math.min(round((255 - self.current["happiness"]) / 2.5), 1)))
            elif self.current["moves"]["move1"] == "Return":
                self.move1BasePower.set(str(math.min(round((self.current["happiness"]) / 2.5), 1)))
            if self.current["moves"]["move2"] == "Frustration":
                self.move2BasePower.set(str(math.min(round((255 - self.current["happiness"]) / 2.5), 1)))
            elif self.current["moves"]["move2"] == "Return":
                self.move2BasePower.set(str(math.min(round((self.current["happiness"]) / 2.5), 1)))
            if self.current["moves"]["move3"] == "Frustration":
                self.move3BasePower.set(str(math.min(round((255 - self.current["happiness"]) / 2.5), 1)))
            elif self.current["moves"]["move3"] == "Return":
                self.move3BasePower.set(str(math.min(round((self.current["happiness"]) / 2.5), 1)))
            if self.current["moves"]["move4"] == "Frustration":
                self.move4BasePower.set(str(math.min(round((255 - self.current["happiness"]) / 2.5), 1)))
            elif self.current["moves"]["move4"] == "Return":
                self.move4BasePower.set(str(math.min(round((self.current["happiness"]) / 2.5), 1)))
        elif option == "shiny":
            self.shinyLabelText.set(self.current["shiny"])
        elif option == "ivs":
            self.updateAnalyzer("stats")
            self.updateAnalyzer("physpec Offense")
            self.updateAnalyzer("physpec Defense")
            self.hpIV.set(str(self.current["ivs"]["hp"]))
            self.atkIV.set(str(self.current["ivs"]["atk"]))
            self.defIV.set(str(self.current["ivs"]["def"]))
            self.spaIV.set(str(self.current["ivs"]["spa"]))
            self.spdIV.set(str(self.current["ivs"]["spd"]))
            self.speIV.set(str(self.current["ivs"]["spe"]))
            self.hpStatCanvas.coords(self.hpStatBar, 0, 5, int(
                self.hpStatCalc(self.current["baseStats"]["hp"], self.current["evs"]["hp"], self.current["ivs"]["hp"],
                                self.current["level"]) / 4), 16)
            self.atkStatCanvas.coords(self.atkStatBar, 0, 5, int(
                self.atkStatCalc(self.current["baseStats"]["atk"], self.current["evs"]["atk"],
                                 self.current["ivs"]["atk"],
                                 self.current["level"], self.current["nature"]) / 4), 16)
            self.atkStatCanvas.itemconfig(self.atkStatBar, fill=self.atkNatureColor(self.current["nature"]))
            self.defStatCanvas.coords(self.defStatBar, 0, 5, int(
                self.defStatCalc(self.current["baseStats"]["def"], self.current["evs"]["def"],
                                 self.current["ivs"]["def"],
                                 self.current["level"], self.current["nature"]) / 4), 16)
            self.defStatCanvas.itemconfig(self.defStatBar, fill=self.defNatureColor(self.current["nature"]))
            self.spaStatCanvas.coords(self.spaStatBar, 0, 5, int(
                self.spaStatCalc(self.current["baseStats"]["spa"], self.current["evs"]["spa"],
                                 self.current["ivs"]["spa"],
                                 self.current["level"], self.current["nature"]) / 4), 16)
            self.spaStatCanvas.itemconfig(self.spaStatBar, fill=self.spaNatureColor(self.current["nature"]))
            self.spdStatCanvas.coords(self.spdStatBar, 0, 5, int(
                self.spdStatCalc(self.current["baseStats"]["spd"], self.current["evs"]["spd"],
                                 self.current["ivs"]["spd"],
                                 self.current["level"], self.current["nature"]) / 4), 16)
            self.spdStatCanvas.itemconfig(self.spdStatBar, fill=self.spdNatureColor(self.current["nature"]))
            self.speStatCanvas.coords(self.speStatBar, 0, 5, int(
                self.speStatCalc(self.current["baseStats"]["spe"], self.current["evs"]["spe"],
                                 self.current["ivs"]["spe"],
                                 self.current["level"], self.current["nature"]) / 4), 16)
            self.speStatCanvas.itemconfig(self.speStatBar, fill=self.speNatureColor(self.current["nature"]))
            self.hpTotal.set(str(
                self.hpStatCalc(self.current["baseStats"]["hp"], self.current["evs"]["hp"], self.current["ivs"]["hp"],
                                self.current["level"])))
            self.atkTotal.set(str(
                self.atkStatCalc(self.current["baseStats"]["atk"], self.current["evs"]["atk"],
                                 self.current["ivs"]["atk"],
                                 self.current["level"], self.current["nature"])))
            self.defTotal.set(str(
                self.defStatCalc(self.current["baseStats"]["def"], self.current["evs"]["def"],
                                 self.current["ivs"]["def"],
                                 self.current["level"], self.current["nature"])))
            self.spaTotal.set(str(
                self.spaStatCalc(self.current["baseStats"]["spa"], self.current["evs"]["spa"],
                                 self.current["ivs"]["spa"],
                                 self.current["level"], self.current["nature"])))
            self.spdTotal.set(str(
                self.spdStatCalc(self.current["baseStats"]["spd"], self.current["evs"]["spd"],
                                 self.current["ivs"]["spd"],
                                 self.current["level"], self.current["nature"])))
            self.speTotal.set(str(
                self.speStatCalc(self.current["baseStats"]["spe"], self.current["evs"]["spe"],
                                 self.current["ivs"]["spe"],
                                 self.current["level"], self.current["nature"])))
        elif option == "nature":
            self.updateAnalyzer("stats")
            self.updateAnalyzer("physpec Offense")
            self.updateAnalyzer("physpec Defense")
            self.atkStatCanvas.itemconfig(self.atkStatBar, fill=self.atkNatureColor(self.current["nature"]))
            self.defStatCanvas.itemconfig(self.defStatBar, fill=self.defNatureColor(self.current["nature"]))
            self.spaStatCanvas.itemconfig(self.spaStatBar, fill=self.spaNatureColor(self.current["nature"]))
            self.spdStatCanvas.itemconfig(self.spdStatBar, fill=self.spdNatureColor(self.current["nature"]))
            self.speStatCanvas.itemconfig(self.speStatBar, fill=self.speNatureColor(self.current["nature"]))
        elif option == "evs":
            self.updateAnalyzer("stats")
            self.updateAnalyzer("physpec Offense")
            self.updateAnalyzer("physpec Defense")
            self.hpEV.set(str(self.current["evs"]["hp"]))
            self.atkEV.set(str(self.current["evs"]["atk"]))
            self.defEV.set(str(self.current["evs"]["def"]))
            self.spaEV.set(str(self.current["evs"]["spa"]))
            self.spdEV.set(str(self.current["evs"]["spd"]))
            self.speEV.set(str(self.current["evs"]["spe"]))
            self.hpStatCanvas.coords(self.hpStatBar, 0, 5, int(
                self.hpStatCalc(self.current["baseStats"]["hp"], self.current["evs"]["hp"], self.current["ivs"]["hp"],
                                self.current["level"]) / 4), 16)
            self.atkStatCanvas.coords(self.atkStatBar, 0, 5, int(
                self.atkStatCalc(self.current["baseStats"]["atk"], self.current["evs"]["atk"],
                                 self.current["ivs"]["atk"],
                                 self.current["level"], self.current["nature"]) / 4), 16)
            self.atkStatCanvas.itemconfig(self.atkStatBar, fill=self.atkNatureColor(self.current["nature"]))
            self.defStatCanvas.coords(self.defStatBar, 0, 5, int(
                self.defStatCalc(self.current["baseStats"]["def"], self.current["evs"]["def"],
                                 self.current["ivs"]["def"],
                                 self.current["level"], self.current["nature"]) / 4), 16)
            self.defStatCanvas.itemconfig(self.defStatBar, fill=self.defNatureColor(self.current["nature"]))
            self.spaStatCanvas.coords(self.spaStatBar, 0, 5, int(
                self.spaStatCalc(self.current["baseStats"]["spa"], self.current["evs"]["spa"],
                                 self.current["ivs"]["spa"],
                                 self.current["level"], self.current["nature"]) / 4), 16)
            self.spaStatCanvas.itemconfig(self.spaStatBar, fill=self.spaNatureColor(self.current["nature"]))
            self.spdStatCanvas.coords(self.spdStatBar, 0, 5, int(
                self.spdStatCalc(self.current["baseStats"]["spd"], self.current["evs"]["spd"],
                                 self.current["ivs"]["spd"],
                                 self.current["level"], self.current["nature"]) / 4), 16)
            self.spdStatCanvas.itemconfig(self.spdStatBar, fill=self.spdNatureColor(self.current["nature"]))
            self.speStatCanvas.coords(self.speStatBar, 0, 5, int(
                self.speStatCalc(self.current["baseStats"]["spe"], self.current["evs"]["spe"],
                                 self.current["ivs"]["spe"],
                                 self.current["level"], self.current["nature"]) / 4), 16)
            self.speStatCanvas.itemconfig(self.speStatBar, fill=self.speNatureColor(self.current["nature"]))
            self.hpTotal.set(str(
                self.hpStatCalc(self.current["baseStats"]["hp"], self.current["evs"]["hp"], self.current["ivs"]["hp"],
                                self.current["level"])))
            self.atkTotal.set(str(
                self.atkStatCalc(self.current["baseStats"]["atk"], self.current["evs"]["atk"],
                                 self.current["ivs"]["atk"],
                                 self.current["level"], self.current["nature"])))
            self.defTotal.set(str(
                self.defStatCalc(self.current["baseStats"]["def"], self.current["evs"]["def"],
                                 self.current["ivs"]["def"],
                                 self.current["level"], self.current["nature"])))
            self.spaTotal.set(str(
                self.spaStatCalc(self.current["baseStats"]["spa"], self.current["evs"]["spa"],
                                 self.current["ivs"]["spa"],
                                 self.current["level"], self.current["nature"])))
            self.spdTotal.set(str(
                self.spdStatCalc(self.current["baseStats"]["spd"], self.current["evs"]["spd"],
                                 self.current["ivs"]["spd"],
                                 self.current["level"], self.current["nature"])))
            self.speTotal.set(str(
                self.speStatCalc(self.current["baseStats"]["spe"], self.current["evs"]["spe"],
                                 self.current["ivs"]["spe"],
                                 self.current["level"], self.current["nature"])))
        elif option == "moves":
            self.updateAnalyzer("moves")
            self.updateAnalyzer("physpec Offense")
            self.move1Name.set(self.current["moves"]["move1"])
            self.move2Name.set(self.current["moves"]["move2"])
            self.move3Name.set(self.current["moves"]["move3"])
            self.move4Name.set(self.current["moves"]["move4"])
            move1Data = Pokedex.findMoveData(self.current["moves"]["move1"])
            move2Data = Pokedex.findMoveData(self.current["moves"]["move2"])
            move3Data = Pokedex.findMoveData(self.current["moves"]["move3"])
            move4Data = Pokedex.findMoveData(self.current["moves"]["move4"])
            if move1Data != None:
                self.move1Cat.set(move1Data["category"])
                self.move1Type.set(move1Data["type"])
                if self.current["moves"]["move1"] == "Frustration":
                    self.move1BasePower.set(str(math.min(round((255-self.current["happiness"])/2.5),1)))
                elif self.current["moves"]["move1"] == "Return":
                    self.move1BasePower.set(str(math.min(round((self.current["happiness"])/2.5),1)))
                else:
                    self.move1BasePower.set(str(move1Data["basePower"]))
                self.move1PP.set(str(move1Data["pp"]))
                if move1Data["accuracy"] != True:
                    self.move1Acc.set(str(move1Data["accuracy"]) + "%")
                else:
                    self.move1Acc.set("100%")
            else:
                self.move1Cat.set("N/A")
                self.move1Type.set("N/A")
                self.move1BasePower.set("N/A")
                self.move1PP.set("N/A")
                self.move1Acc.set("N/A")

            if move2Data != None:
                self.move2Cat.set(move2Data["category"])
                self.move2Type.set(move2Data["type"])
                if self.current["moves"]["move2"] == "Frustration":
                    self.move2BasePower.set(str(math.min(round((255-self.current["happiness"])/2.5),1)))
                elif self.current["moves"]["move2"] == "Return":
                    self.move2BasePower.set(str(math.min(round((self.current["happiness"])/2.5),1)))
                else:
                    self.move2BasePower.set(str(move2Data["basePower"]))
                self.move2PP.set(str(move2Data["pp"]))
                if move2Data["accuracy"] != True:
                    self.move2Acc.set(str(move2Data["accuracy"]) + "%")
                else:
                    self.move2Acc.set("100%")
            else:
                self.move2Cat.set("N/A")
                self.move2Type.set("N/A")
                self.move2BasePower.set("N/A")
                self.move2PP.set("N/A")
                self.move2Acc.set("N/A")

            if move3Data != None:
                self.move3Cat.set(move3Data["category"])
                self.move3Type.set(move3Data["type"])
                if self.current["moves"]["move3"] == "Frustration":
                    self.move3BasePower.set(str(math.min(round((255-self.current["happiness"])/2.5),1)))
                elif self.current["moves"]["move3"] == "Return":
                    self.move3BasePower.set(str(math.min(round((self.current["happiness"])/2.5),1)))
                else:
                    self.move3BasePower.set(str(move3Data["basePower"]))
                self.move3PP.set(str(move3Data["pp"]))
                if move3Data["accuracy"] != True:
                    self.move3Acc.set(str(move3Data["accuracy"]) + "%")
                else:
                    self.move3Acc.set("100%")
            else:
                self.move3Cat.set("N/A")
                self.move3Type.set("N/A")
                self.move3BasePower.set("N/A")
                self.move3PP.set("N/A")
                self.move3Acc.set("N/A")

            if move4Data != None:
                self.move4Cat.set(move4Data["category"])
                self.move4Type.set(move4Data["type"])
                if self.current["moves"]["move4"] == "Frustration":
                    self.move4BasePower.set(str(math.min(round((255-self.current["happiness"])/2.5),1)))
                elif self.current["moves"]["move4"] == "Return":
                    self.move4BasePower.set(str(math.min(round((self.current["happiness"])/2.5),1)))
                else:
                    self.move4BasePower.set(str(move4Data["basePower"]))
                self.move4PP.set(str(move4Data["pp"]))
                if move4Data["accuracy"] != True:
                    self.move4Acc.set(str(move4Data["accuracy"]) + "%")
                else:
                    self.move4Acc.set("100%")
            else:
                self.move4Cat.set("N/A")
                self.move4Type.set("N/A")
                self.move4BasePower.set("N/A")
                self.move4PP.set("N/A")
                self.move4Acc.set("N/A")
        else:
            print("whoops, you should fix "+option)
        #print(self.current["index"])

    def delete(self,name):
        #del self.teamMateNames[self.teamMateNames.index(name)]
        self.teamMatesDict[name]["species"] = None
        self.teamMatesDict[name]["ability"] = None
        self.teamMatesDict[name]["nature"] = None
        self.teamMatesDict[name]["baseStats"] = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0}
        self.teamMatesDict[name]["ivs"] = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0}
        self.teamMatesDict[name]["evs"] = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0}
        self.teamMatesDict[name]["item"] = None
        self.teamMatesDict[name]["gender"] = None
        self.teamMatesDict[name]["moves"] = {"move1": None, "move2": None, "move3": None, "move4": None}
        self.teamMatesDict[name]["happiness"] = 255
        if "battlespot" in self.tier and "vgc" in self.tier:
            self.teamMatesDict[name]["level"] = 50
        else:
            self.teamMatesDict[name]["level"] = 100
        self.teamMatesDict[name]["shiny"] = None
        self.switch(name)
        self.the_menu.entryconfigure(name, state="disabled")
        self.the_menu.entryconfigure(name, label="None")

    def cut(self,text):
        textlines = []
        stop = 0
        text = text.replace("\t", "        ")
        begin = ""
        for i in range(len(text)):
            if text[i] not in ["\n", " "]:
                begin = text[0:i]
                break
        #t = ""
        #for char in begin:
        #    if char == "\n":
        #        t += "n "
        #    elif char == " ":
        #        t += "_ "
        #    else:
        #        t += "E "
        #print(t)
        isDone = False
        while not isDone:
            if stop == 0:
                if len(text) > 57:
                    if text[56] != " ":
                        if text[57] != " ":
                            for j in range(55, 0, -1):
                                if text[j] == " ":
                                    # print(text[stop:j])
                                    textlines.append(text[stop:j])
                                    stop = j + 1
                                    break
                        else:
                            textlines.append(text[:57])
                            stop = 58
                    else:
                        textlines.append(text[:57])
                        stop = 57
                else:
                    isDone = True
                    return text
            else:
                if len(text) - stop > 57 - len(begin) + 1-4:
                    if text[stop + 56 - len(begin) + 1-4] != " ":
                        if text[stop + 57 - len(begin) + 1-4] != " ":
                            for j in range(stop + 55 - len(begin) + 1-4, stop, -1):
                                if text[j] == " ":
                                    textlines.append("    "+text[stop:j])
                                    stop = j + 1
                                    break
                        else:
                            textlines.append("    "+text[stop:stop + 57 - len(begin) + 1-4])
                            stop = stop + 58 - len(begin) + 1-4
                    else:
                        textlines.append("    "+text[stop:stop + 57 - len(begin) + 1-4])
                        stop = stop + 57 - len(begin) + 1-4
                else:
                    textlines.append("    "+text[stop:])
                    isDone = True
        return begin.join(textlines)

    def __init__(self,root):
        # Team Builder Window Setup
        root.title("Team Builder")
        self.width = 1000
        self.height = 600
        root.geometry(str(self.width) + "x" + str(self.height))

        # Text Frame Setup
        textframe = Frame(root, width=int(self.width / 2), height=self.height)
        borderwidth = 10
        textframe.config(relief=RAISED, borderwidth=borderwidth)
        textframe.pack(side=RIGHT, fill=Y)

        # Input Field and Messages Setup
        input_user = StringVar()
        input_field = Entry(textframe, text=input_user)
        input_field.pack(side=BOTTOM, fill=X)
        input_user.set("")
        self.messages = Text(textframe, wrap=WORD, width=57)
        self.messages.config(state=DISABLED)
        scrollbar = Scrollbar(textframe, command=self.messages.yview)
        scrollbar.pack(side=RIGHT, fill=Y)
        self.messages.pack(side=RIGHT, fill=Y)
        self.messages["yscrollcommand"] = scrollbar.set

        def Enter_pressed(event):
            self.input_get = input_field.get()
            self.inputEvent.set()
            self.inputEvent.clear()
            self.messages.config(state=NORMAL)
            self.messages.insert(END, 'You: %s\n\n' % self.input_get)
            self.messages.see(END)
            # self.messages.edit_modified(0)
            self.messages.config(state=DISABLED)
            input_user.set("")
            # return "break"

        input_field.bind("<Return>", Enter_pressed)

        self.teamMatesDict = {}
        self.teamMateNames = []
        self.current = {}
        self.current["species"] = None
        # self.current["index"] = None
        self.current["ability"] = None
        self.current["nature"] = None
        self.current["baseStats"] = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0}
        self.current["ivs"] = {"hp": 31, "atk": 31, "def": 31, "spa": 31, "spd": 31, "spe": 31}
        self.current["evs"] = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0}
        self.current["item"] = None
        self.current["gender"] = None
        self.current["moves"] = {"move1": None, "move2": None, "move3": None, "move4": None}
        self.current["happiness"] = 255
        self.current["level"] = 100
        self.current["shiny"] = None

        # Team Frame Setup
        teamframe = Frame(root, width=int(self.width / 2), height=self.height)
        infoFrame = Frame(teamframe)
        infoFrame.columnconfigure(1, minsize=50)
        infoFrame.columnconfigure(2, minsize=150)
        infoFrame.columnconfigure(3, minsize=50)
        infoFrame.columnconfigure(4, minsize=150)
        infoFrame.pack(side=TOP, fill=X)
        teamframe.config(relief=RAISED, borderwidth=borderwidth)
        teamframe.pack(side=LEFT, fill=Y)

        # Make Images
        self.spriteCanvas = Canvas(infoFrame, width=80, height=80)
        self.spriteCanvas.config(relief=RAISED, borderwidth=1, background="white")
        self.spriteCanvas.grid(row=0, column=0, rowspan=4)

        # Individual Team Member Species Label
        Label(infoFrame, text="Species:", anchor=W).grid(row=0, column=1, sticky=E)
        self.speciesLabelText = StringVar()
        self.speciesLabelText.set(self.current["species"])
        Label(infoFrame, textvariable=self.speciesLabelText, anchor=W).grid(row=0, column=2, sticky=W)

        # Individual Team Member Type Label
        Label(infoFrame, text="Types:", anchor=W).grid(row=1, column=1, sticky=E)
        self.typeLabelText = StringVar()
        if self.current["species"] != None:
            types = Pokedex.findPokemonTypes(self.current["species"])
            if len(types) == 2:
                self.typeLabelText.set(types[0] + ", " + types[1])
            else:
                self.typeLabelText.set(types[0])
        else:
            self.typeLabelText.set("None, None")
        Label(infoFrame, textvariable=self.typeLabelText, anchor=W).grid(row=1, column=2, sticky=W)

        # Individual Team Member Ability Label
        Label(infoFrame, text="Ability:", anchor=W).grid(row=2, column=1, sticky=E)
        self.abilityLabelText = StringVar()
        self.abilityLabelText.set(self.current["ability"])
        Label(infoFrame, textvariable=self.abilityLabelText, anchor=W).grid(row=2, column=2, sticky=W)

        # Individual Team Member Item Label
        Label(infoFrame, text="Item:", anchor=W).grid(row=3, column=1, sticky=E)
        self.itemLabelText = StringVar()
        self.itemLabelText.set(self.current["item"])
        Label(infoFrame, textvariable=self.itemLabelText, anchor=W).grid(row=3, column=2, sticky=W)

        # Individual Team Member Level Label
        Label(infoFrame, text="Level:", anchor=W).grid(row=0, column=3, sticky=E)
        self.levelLabelText = StringVar()
        self.levelLabelText.set(str(self.current["level"]))
        Label(infoFrame, textvariable=self.levelLabelText, anchor=W).grid(row=0, column=4, sticky=W)

        # Individual Team Member Gender Label
        Label(infoFrame, text="Gender:", anchor=W).grid(row=1, column=3, sticky=E)
        self.genderLabelText = StringVar()
        self.genderLabelText.set(str(self.current["gender"]))
        Label(infoFrame, textvariable=self.genderLabelText, anchor=W).grid(row=1, column=4, sticky=W)

        # Individual Team Member Happiness Label
        Label(infoFrame, text="Happiness:", anchor=W).grid(row=2, column=3, sticky=E)
        self.happinessLabelText = StringVar()
        self.happinessLabelText.set(str(self.current["happiness"]))
        Label(infoFrame, textvariable=self.happinessLabelText, anchor=W).grid(row=2, column=4, sticky=W)

        # Individual Team Member Shiny Label
        Label(infoFrame, text="Shiny:", anchor=W).grid(row=3, column=3, sticky=E)
        self.shinyLabelText = StringVar()
        self.shinyLabelText.set(self.current["shiny"])
        Label(infoFrame, textvariable=self.shinyLabelText, anchor=W).grid(row=3, column=4, sticky=W)

        ttk.Separator(teamframe, orient=HORIZONTAL).pack(side=TOP, fill=X, pady=10)
        statsFrame = Frame(teamframe)
        statsFrame.columnconfigure(0, minsize=50)
        statsFrame.columnconfigure(2, minsize=70)
        statsFrame.columnconfigure(4, minsize=50)
        statsFrame.columnconfigure(6, minsize=50)
        statsFrame.columnconfigure(10, minsize=50)

        statsFrame.pack(side=TOP, fill=X)

        # Stats Titles
        Label(statsFrame, text="HP", anchor=W).grid(row=1, column=0)
        Label(statsFrame, text="Atk", anchor=W).grid(row=2, column=0)
        Label(statsFrame, text="Def", anchor=W).grid(row=3, column=0)
        Label(statsFrame, text="SpA", anchor=W).grid(row=4, column=0)
        Label(statsFrame, text="SpD", anchor=W).grid(row=5, column=0)
        Label(statsFrame, text="Spe", anchor=W).grid(row=6, column=0)

        ttk.Separator(statsFrame, orient=VERTICAL).grid(row=0, column=1, rowspan=7, sticky=NS)

        # Base Stats Label
        Label(statsFrame, text="Base Stats").grid(row=0, column=2)
        # HP Base Stat
        self.hpBS = StringVar()
        self.hpBS.set(str(self.current["baseStats"]["hp"]))
        Label(statsFrame, textvariable=self.hpBS).grid(row=1, column=2)
        # Atk Base Stat
        self.atkBS = StringVar()
        self.atkBS.set(str(self.current["baseStats"]["atk"]))
        Label(statsFrame, textvariable=self.atkBS).grid(row=2, column=2)
        # Def Base Stat
        self.defBS = StringVar()
        self.defBS.set(str(self.current["baseStats"]["def"]))
        Label(statsFrame, textvariable=self.defBS).grid(row=3, column=2)
        # SpA Base Stat
        self.spaBS = StringVar()
        self.spaBS.set(str(self.current["baseStats"]["spa"]))
        Label(statsFrame, textvariable=self.spaBS).grid(row=4, column=2)
        # SpD Base Stat
        self.spdBS = StringVar()
        self.spdBS.set(str(self.current["baseStats"]["spd"]))
        Label(statsFrame, textvariable=self.spdBS).grid(row=5, column=2)
        # Spe Base Stat
        self.speBS = StringVar()
        self.speBS.set(str(self.current["baseStats"]["spe"]))
        Label(statsFrame, textvariable=self.speBS).grid(row=6, column=2)

        ttk.Separator(statsFrame, orient=VERTICAL).grid(row=0, column=3, rowspan=7, sticky=NS)

        # IVs Label
        Label(statsFrame, text="IVs").grid(row=0, column=4)
        # HP IVs
        self.hpIV = StringVar()
        self.hpIV.set(str(self.current["ivs"]["hp"]))
        Label(statsFrame, textvariable=self.hpIV).grid(row=1, column=4)
        # Atk IVs
        self.atkIV = StringVar()
        self.atkIV.set(str(self.current["ivs"]["atk"]))
        Label(statsFrame, textvariable=self.atkIV).grid(row=2, column=4)
        # Def IVs
        self.defIV = StringVar()
        self.defIV.set(str(self.current["ivs"]["def"]))
        Label(statsFrame, textvariable=self.defIV).grid(row=3, column=4)
        # SpA IVs
        self.spaIV = StringVar()
        self.spaIV.set(str(self.current["ivs"]["spa"]))
        Label(statsFrame, textvariable=self.spaIV).grid(row=4, column=4)
        # SpD IVs
        self.spdIV = StringVar()
        self.spdIV.set(str(self.current["ivs"]["spd"]))
        Label(statsFrame, textvariable=self.spdIV).grid(row=5, column=4)
        # Spe IVs
        self.speIV = StringVar()
        self.speIV.set(str(self.current["ivs"]["spe"]))
        Label(statsFrame, textvariable=self.speIV).grid(row=6, column=4)

        ttk.Separator(statsFrame, orient=VERTICAL).grid(row=0, column=5, rowspan=7, sticky=NS)

        # EVs Label
        Label(statsFrame, text="EVs").grid(row=0, column=6)
        # HP EVs
        self.hpEV = StringVar()
        self.hpEV.set(str(self.current["evs"]["hp"]))
        Label(statsFrame, textvariable=self.hpEV).grid(row=1, column=6)
        # Atk EVs
        self.atkEV = StringVar()
        self.atkEV.set(str(self.current["evs"]["atk"]))
        Label(statsFrame, textvariable=self.atkEV).grid(row=2, column=6)
        # Def EVs
        self.defEV = StringVar()
        self.defEV.set(str(self.current["evs"]["def"]))
        Label(statsFrame, textvariable=self.defEV).grid(row=3, column=6)
        # SpA EVs
        self.spaEV = StringVar()
        self.spaEV.set(str(self.current["evs"]["spa"]))
        Label(statsFrame, textvariable=self.spaEV).grid(row=4, column=6)
        # SpD EVs
        self.spdEV = StringVar()
        self.spdEV.set(str(self.current["evs"]["spd"]))
        Label(statsFrame, textvariable=self.spdEV).grid(row=5, column=6)
        # Spe EVs
        self.speEV = StringVar()
        self.speEV.set(str(self.current["evs"]["spe"]))
        Label(statsFrame, textvariable=self.speEV).grid(row=6, column=6)

        ttk.Separator(statsFrame, orient=VERTICAL).grid(row=0, column=7, rowspan=7, sticky=NS)

        # HP Bar
        self.hpStatCanvas = Canvas(statsFrame, width=178, height=20)
        if self.current["species"] != None:
            self.hpStatBar = self.hpStatCanvas.create_rectangle(0, 5, int(
                self.hpStatCalc(self.current["baseStats"]["hp"], self.current["evs"]["hp"], self.current["ivs"]["hp"],
                                self.current["level"]) / 4), 16, fill="lawn green")
        else:
            self.hpStatBar = self.hpStatCanvas.create_rectangle(0, 5, 0, 16, fill="lawn green")
        self.hpStatCanvas.grid(row=1, column=8)

        # Atk Bar
        self.atkStatCanvas = Canvas(statsFrame, width=178, height=20)
        if self.current["species"] != None:
            self.atkStatBar = self.atkStatCanvas.create_rectangle(0, 5, int(
                self.atkStatCalc(self.current["baseStats"]["atk"], self.current["evs"]["atk"],
                                 self.current["ivs"]["atk"], self.current["level"], self.current["nature"]) / 4), 16)
            self.atkStatCanvas.itemconfig(self.atkStatBar, fill=self.atkNatureColor(self.current["nature"]))
        else:
            self.atkStatBar = self.atkStatCanvas.create_rectangle(0, 5, 0, 16, fill="lawn green")
        self.atkStatCanvas.grid(row=2, column=8)

        # Def Bar
        self.defStatCanvas = Canvas(statsFrame, width=178, height=20)
        if self.current["species"] != None:
            self.defStatBar = self.defStatCanvas.create_rectangle(0, 5, int(
                self.defStatCalc(self.current["baseStats"]["def"], self.current["evs"]["def"],
                                 self.current["ivs"]["def"], self.current["level"], self.current["nature"]) / 4), 16)
            self.defStatCanvas.itemconfig(self.defStatBar, fill=self.defNatureColor(self.current["nature"]))
        else:
            self.defStatBar = self.defStatCanvas.create_rectangle(0, 5, 0, 16, fill="lawn green")
        self.defStatCanvas.grid(row=3, column=8)

        # SpA Bar
        self.spaStatCanvas = Canvas(statsFrame, width=178, height=20)
        if self.current["species"] != None:
            self.spaStatBar = self.spaStatCanvas.create_rectangle(0, 5, int(
                self.spaStatCalc(self.current["baseStats"]["spa"], self.current["evs"]["spa"],
                                 self.current["ivs"]["spa"], self.current["level"], self.current["nature"]) / 4), 16)
            self.spaStatCanvas.itemconfig(self.spaStatBar, fill=self.spaNatureColor(self.current["nature"]))
        else:
            self.spaStatBar = self.spaStatCanvas.create_rectangle(0, 5, 0, 16, fill="lawn green")
        self.spaStatCanvas.grid(row=4, column=8)

        # SpD Bar
        self.spdStatCanvas = Canvas(statsFrame, width=178, height=20)
        if self.current["species"] != None:
            self.spdStatBar = self.spdStatCanvas.create_rectangle(0, 5, int(
                self.spdStatCalc(self.current["baseStats"]["spd"], self.current["evs"]["spd"],
                                 self.current["ivs"]["spd"], self.current["level"], self.current["nature"]) / 4), 16)
            self.spdStatCanvas.itemconfig(self.spdStatBar, fill=self.spdNatureColor(self.current["nature"]))
        else:
            self.spdStatBar = self.spdStatCanvas.create_rectangle(0, 5, 0, 16, fill="lawn green")
        self.spdStatCanvas.grid(row=5, column=8)

        # Spe Bar
        self.speStatCanvas = Canvas(statsFrame, width=178, height=20)
        if self.current["species"] != None:
            self.speStatBar = self.speStatCanvas.create_rectangle(0, 5, int(
                self.speStatCalc(self.current["baseStats"]["spe"], self.current["evs"]["spe"],
                                 self.current["ivs"]["spe"], self.current["level"], self.current["nature"]) / 4), 16)
            self.speStatCanvas.itemconfig(self.speStatBar, fill=self.speNatureColor(self.current["nature"]))
        else:
            self.speStatBar = self.speStatCanvas.create_rectangle(0, 5, 0, 16, fill="lawn green")
        self.speStatCanvas.grid(row=6, column=8)

        ttk.Separator(statsFrame, orient=VERTICAL).grid(row=0, column=9, rowspan=7, sticky=NS)

        # Total Stats Label
        Label(statsFrame, text="Total").grid(row=0, column=10)

        # HP Total
        self.hpTotal = StringVar()
        if self.current["species"]:
            self.hpTotal.set(str(
                self.hpStatCalc(self.current["baseStats"]["hp"], self.current["evs"]["hp"], self.current["ivs"]["hp"],
                                self.current["level"])))
        else:
            self.hpTotal.set(str(0))
        Label(statsFrame, textvariable=self.hpTotal).grid(row=1, column=10)

        # Atk Total
        self.atkTotal = StringVar()
        if self.current["species"]:
            self.atkTotal.set(str(self.atkStatCalc(self.current["baseStats"]["atk"], self.current["evs"]["atk"],
                                                   self.current["ivs"]["atk"], self.current["level"],
                                                   self.current["nature"])))
        else:
            self.atkTotal.set(str(0))
        Label(statsFrame, textvariable=self.atkTotal).grid(row=2, column=10)

        # Def Total
        self.defTotal = StringVar()
        if self.current["species"]:
            self.defTotal.set(str(self.defStatCalc(self.current["baseStats"]["def"], self.current["evs"]["def"],
                                                   self.current["ivs"]["def"], self.current["level"],
                                                   self.current["nature"])))
        else:
            self.defTotal.set(str(0))
        Label(statsFrame, textvariable=self.defTotal).grid(row=3, column=10)

        # SpA Total
        self.spaTotal = StringVar()
        if self.current["species"]:
            self.spaTotal.set(str(self.spaStatCalc(self.current["baseStats"]["spa"], self.current["evs"]["spa"],
                                                   self.current["ivs"]["spa"], self.current["level"],
                                                   self.current["nature"])))
        else:
            self.spaTotal.set(str(0))
        Label(statsFrame, textvariable=self.spaTotal).grid(row=4, column=10)

        # SpD Total
        self.spdTotal = StringVar()
        if self.current["species"]:
            self.spdTotal.set(str(self.spdStatCalc(self.current["baseStats"]["spd"], self.current["evs"]["spd"],
                                                   self.current["ivs"]["spd"], self.current["level"],
                                                   self.current["nature"])))
        else:
            self.spdTotal.set(str(0))
        Label(statsFrame, textvariable=self.spdTotal).grid(row=5, column=10)

        # Spe Total
        self.speTotal = StringVar()
        if self.current["species"]:
            self.speTotal.set(str(self.speStatCalc(self.current["baseStats"]["spe"], self.current["evs"]["spe"],
                                                   self.current["ivs"]["spe"], self.current["level"],
                                                   self.current["nature"])))
        else:
            self.speTotal.set(str(0))
        Label(statsFrame, textvariable=self.speTotal).grid(row=6, column=10)

        ttk.Separator(teamframe, orient=HORIZONTAL).pack(side=TOP, fill=X, pady=10)
        movesFrame = Frame(teamframe)
        movesFrame.columnconfigure(0, minsize=150)
        movesFrame.columnconfigure(2, minsize=70)
        movesFrame.columnconfigure(4, minsize=60)
        movesFrame.columnconfigure(6, minsize=70)
        movesFrame.columnconfigure(8, minsize=50)
        movesFrame.columnconfigure(10, minsize=70)
        movesFrame.pack(side=TOP, fill=X)

        # Move 1 Name
        self.move1Name = StringVar()
        self.move1Name.set(self.current["moves"]["move1"])
        move1Data = Pokedex.findMoveData(self.current["moves"]["move1"])
        Label(movesFrame, textvariable=self.move1Name).grid(row=1, column=0)
        # Move 2 Name
        self.move2Name = StringVar()
        self.move2Name.set(self.current["moves"]["move2"])
        move2Data = Pokedex.findMoveData(self.current["moves"]["move2"])
        Label(movesFrame, textvariable=self.move2Name).grid(row=2, column=0)
        # Move 3 Name
        self.move3Name = StringVar()
        self.move3Name.set(self.current["moves"]["move3"])
        move3Data = Pokedex.findMoveData(self.current["moves"]["move3"])
        Label(movesFrame, textvariable=self.move3Name).grid(row=3, column=0)
        # Move 4 Name
        self.move4Name = StringVar()
        self.move4Name.set(self.current["moves"]["move4"])
        move4Data = Pokedex.findMoveData(self.current["moves"]["move4"])
        Label(movesFrame, textvariable=self.move4Name).grid(row=4, column=0)

        ttk.Separator(movesFrame, orient=VERTICAL).grid(row=0, column=1, rowspan=5, sticky=NS)

        # Move Category Label
        Label(movesFrame, text="Category").grid(row=0, column=2)
        # Move 1 Category
        self.move1Cat = StringVar()
        if move1Data != None:
            self.move1Cat.set(move1Data["category"])
        else:
            self.move1Cat.set("N/A")
        Label(movesFrame, textvariable=self.move1Cat).grid(row=1, column=2)
        # Move 2 Category
        self.move2Cat = StringVar()
        if move2Data != None:
            self.move2Cat.set(move2Data["category"])
        else:
            self.move2Cat.set("N/A")
        Label(movesFrame, textvariable=self.move2Cat).grid(row=2, column=2)
        # Move 3 Category
        self.move3Cat = StringVar()
        if move3Data != None:
            self.move3Cat.set(move3Data["category"])
        else:
            self.move3Cat.set("N/A")
        Label(movesFrame, textvariable=self.move3Cat).grid(row=3, column=2)
        # Move 4 Category
        self.move4Cat = StringVar()
        if move4Data != None:
            self.move4Cat.set(move4Data["category"])
        else:
            self.move4Cat.set("N/A")
        Label(movesFrame, textvariable=self.move4Cat).grid(row=4, column=2)

        ttk.Separator(movesFrame, orient=VERTICAL).grid(row=0, column=3, rowspan=5, sticky=NS)

        # Move Type Label
        Label(movesFrame, text="Type").grid(row=0, column=4)
        # Move 1 Type
        self.move1Type = StringVar()
        if move1Data != None:
            self.move1Type.set(move1Data["type"])
        else:
            self.move1Type.set("N/A")
        Label(movesFrame, textvariable=self.move1Type).grid(row=1, column=4)
        # Move 2 Type
        self.move2Type = StringVar()
        if move2Data != None:
            self.move2Type.set(move2Data["type"])
        else:
            self.move2Type.set("N/A")
        Label(movesFrame, textvariable=self.move2Type).grid(row=2, column=4)
        # Move 3 Type
        self.move3Type = StringVar()
        if move3Data != None:
            self.move3Type.set(move3Data["type"])
        else:
            self.move3Type.set("N/A")
        Label(movesFrame, textvariable=self.move3Type).grid(row=3, column=4)
        # Move 4 Type
        self.move4Type = StringVar()
        if move4Data != None:
            self.move4Type.set(move4Data["type"])
        else:
            self.move4Type.set("N/A")
        Label(movesFrame, textvariable=self.move4Type).grid(row=4, column=4)

        ttk.Separator(movesFrame, orient=VERTICAL).grid(row=0, column=5, rowspan=5, sticky=NS)

        # Move Base Power Label
        Label(movesFrame, text="Base Power").grid(row=0, column=6)
        # Move 1 Base Power
        self.move1BasePower = StringVar()
        if move1Data != None:
            self.move1BasePower.set(str(move1Data["basePower"]))
        else:
            self.move1BasePower.set("N/A")
        Label(movesFrame, textvariable=self.move1BasePower).grid(row=1, column=6)
        # Move 2 Base Power
        self.move2BasePower = StringVar()
        if move2Data != None:
            self.move2BasePower.set(str(move2Data["basePower"]))
        else:
            self.move2BasePower.set("N/A")
        Label(movesFrame, textvariable=self.move2BasePower).grid(row=2, column=6)
        # Move 3 Base Power
        self.move3BasePower = StringVar()
        if move3Data != None:
            self.move3BasePower.set(str(move3Data["basePower"]))
        else:
            self.move3BasePower.set("N/A")
        Label(movesFrame, textvariable=self.move3BasePower).grid(row=3, column=6)
        # Move 4 Base Power
        self.move4BasePower = StringVar()
        if move4Data != None:
            self.move4BasePower.set(str(move4Data["basePower"]))
        else:
            self.move4BasePower.set("N/A")
        Label(movesFrame, textvariable=self.move4BasePower).grid(row=4, column=6)

        ttk.Separator(movesFrame, orient=VERTICAL).grid(row=0, column=7, rowspan=5, sticky=NS)

        # Move PP Label
        Label(movesFrame, text="PP").grid(row=0, column=8)
        # Move 1 PP
        self.move1PP = StringVar()
        if move1Data != None:
            self.move1PP.set(str(move1Data["pp"]))
        else:
            self.move1PP.set("N/A")
        Label(movesFrame, textvariable=self.move1PP).grid(row=1, column=8)
        # Move 2 PP
        self.move2PP = StringVar()
        if move2Data != None:
            self.move2PP.set(str(move2Data["pp"]))
        else:
            self.move2PP.set("N/A")
        Label(movesFrame, textvariable=self.move2PP).grid(row=2, column=8)
        # Move 3 PP
        self.move3PP = StringVar()
        if move3Data != None:
            self.move3PP.set(str(move3Data["pp"]))
        else:
            self.move3PP.set("N/A")
        Label(movesFrame, textvariable=self.move3PP).grid(row=3, column=8)
        # Move 4 PP
        self.move4PP = StringVar()
        if move4Data != None:
            self.move4PP.set(str(move4Data["pp"]))
        else:
            self.move4PP.set("N/A")
        Label(movesFrame, textvariable=self.move4PP).grid(row=4, column=8)

        ttk.Separator(movesFrame, orient=VERTICAL).grid(row=0, column=9, rowspan=5, sticky=NS)

        # Move Accuracy Label
        Label(movesFrame, text="Accuracy").grid(row=0, column=10)
        # Move 1 Accuracy
        self.move1Acc = StringVar()
        if move1Data != None:
            if move1Data["accuracy"] != True:
                self.move1Acc.set(str(move1Data["accuracy"]) + "%")
            else:
                self.move1Acc.set("100%")
        else:
            self.move1Acc.set("N/A")
        Label(movesFrame, textvariable=self.move1Acc).grid(row=1, column=10)
        # Move 2 Accuracy
        self.move2Acc = StringVar()
        if move2Data != None:
            if move2Data["accuracy"] != True:
                self.move2Acc.set(str(move2Data["accuracy"]) + "%")
            else:
                self.move2Acc.set("100%")
        else:
            self.move2Acc.set("N/A")
        Label(movesFrame, textvariable=self.move2Acc).grid(row=2, column=10)
        # Move 3 Accuracy
        self.move3Acc = StringVar()
        if move3Data != None:
            if move3Data["accuracy"] != True:
                self.move3Acc.set(str(move3Data["accuracy"]) + "%")
            else:
                self.move3Acc.set("100%")
        else:
            self.move3Acc.set("N/A")
        Label(movesFrame, textvariable=self.move3Acc).grid(row=3, column=10)
        # Move 4 Accuracy
        self.move4Acc = StringVar()
        if move4Data != None:
            if move4Data["accuracy"] != True:
                self.move4Acc.set(str(move4Data["accuracy"]) + "%")
            else:
                self.move4Acc.set("100%")
        else:
            self.move4Acc.set("N/A")
        Label(movesFrame, textvariable=self.move4Acc).grid(row=4, column=10)

        ttk.Separator(teamframe, orient=HORIZONTAL).pack(side=TOP, fill=X, pady=(10, 0))
        ttk.Separator(teamframe, orient=HORIZONTAL).pack(side=TOP, fill=X, pady=(0, 10))

        self.toplevel = Toplevel()
        self.analyzer = TeamAnalyzer.TeamAnalyzer(self.toplevel)
        self.toplevel.resizable(width=False,height=False)
        self.toplevel.withdraw()

        self.importFileName=None

        # Menu Setup
        self.the_menu = Menu(root)
        file_menu = Menu(self.the_menu, tearoff=0)
        file_menu.add_command(label="Team Analyzer", command=self.showAnalyzer)
        #file_menu.add_command(label="Import Team",command=lambda:GUIScript.analyzeImportedTeam(self))
        file_menu.add_command(label="Quit", command=root.quit)
        self.the_menu.add_cascade(label="File", menu=file_menu)

        root.config(menu=self.the_menu)

        self.inputEvent = threading.Event()
        self.aiThrd = threading.Thread(target=GUIScript.AI, args=(self,))
        self.aiThrd.setDaemon(True)
        self.aiThrd.start()

root = Tk()
root.resizable(width=False,height=False)
AL(root)
root.mainloop()
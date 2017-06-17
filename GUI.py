from tkinter import *
from tkinter import ttk
import math,Pokedex,MetaDex,TeamBuilder,threading,random,datetime,os,glob
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
            return math.floor(math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5)

    @staticmethod
    def defStatCalc(base,evs,ivs,level,nature):
        if nature in ["Bold", "Lax", "Impish", "Relaxed"]:
            return math.floor((math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5) * 1.1)
        elif nature in ["Lonely", "Mild", "Gentle", "Hasty"]:
            return math.floor((math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5) * 0.9)
        else:
            return math.floor(math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5)

    @staticmethod
    def spaStatCalc(base,evs,ivs,level,nature):
        if nature in ["Modest", "Mild", "Rash", "Quiet"]:
            return math.floor((math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5) * 1.1)
        elif nature in ["Adamant", "Impish", "Careful", "Jolly"]:
            return math.floor((math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5) * 0.9)
        else:
            return math.floor(math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5)

    @staticmethod
    def spdStatCalc(base,evs,ivs,level,nature):
        if nature in ["Calm", "Gentle", "Careful", "Sassy"]:
            return math.floor((math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5) * 1.1)
        elif nature in ["Naughty", "Lax", "Rash", "Naive"]:
            return math.floor((math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5) * 0.9)
        else:
            return math.floor(math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5)

    @staticmethod
    def speStatCalc(base,evs,ivs,level,nature):
        if nature in ["Timid", "Hasty", "Jolly", "Naive"]:
            return math.floor((math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5) * 1.1)
        elif nature in ["Brave", "Relaxed", "Quiet", "Sassy"]:
            return math.floor((math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5) * 0.9)
        else:
            return math.floor(math.floor(((2 * base + ivs + math.floor(evs / 4)) * level) / 100) + 5)

    @staticmethod
    def get_picture_name(icon, species):
        pokemonData = Pokedex.findPokemonData(species)
        num = str(pokemonData['num'])
        while len(num) < 3:
            num = '0' + num
        if 'forme' in pokemonData:
            num += '-'
            forme = TeamBuilder.compress(pokemonData['forme'])

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
        #return "break"

    def showAnalyzer(self):
        pass
    
    def switch(self,name):
        self.current = self.teamMatesDict[name]
        filename = self.get_picture_name(True,name)
        self.request_picture(filename,True)
        self.spriteCanvas.spriteFile = PhotoImage(file=os.path.dirname(os.path.realpath(__file__))+"/data/images/icons/"+filename+".png")
        self.spriteCanvas.spriteFile = self.spriteCanvas.spriteFile.zoom(80)
        self.spriteCanvas.spriteFile = self.spriteCanvas.spriteFile.subsample(int(self.spriteCanvas.spriteFile.width() / 80))
        self.spriteCanvas.create_image(2,2, anchor=NW, image=self.spriteCanvas.spriteFile)
        self.speciesLabelText.set(self.current["species"])
        types = Pokedex.findPokemonTypes(self.current["species"])
        if len(types) == 2:
            self.typeLabelText.set(types[0] + ", " + types[1])
        else:
            self.typeLabelText.set(types[0])
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

    def update(self,name,option):
        if option=="types":
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
        elif option == "shiny":
            self.shinyLabelText.set(self.current["shiny"])
        elif option == "ivs":
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
            self.atkStatCanvas.itemconfig(self.atkStatBar, fill=self.atkNatureColor(self.current["nature"]))
            self.defStatCanvas.itemconfig(self.defStatBar, fill=self.defNatureColor(self.current["nature"]))
            self.spaStatCanvas.itemconfig(self.spaStatBar, fill=self.spaNatureColor(self.current["nature"]))
            self.spdStatCanvas.itemconfig(self.spdStatBar, fill=self.spdNatureColor(self.current["nature"]))
            self.speStatCanvas.itemconfig(self.speStatBar, fill=self.speNatureColor(self.current["nature"]))
        elif option == "evs":
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
        else:
            print("whoops, you should fix "+option)

    def delete(self,name):
        self.teamMatesDict[name]["species"] = None
        self.teamMatesDict[name]["types"] = [None,None]
        self.teamMatesDict[name]["ability"] = None
        self.teamMatesDict[name]["nature"] = None
        self.teamMatesDict[name]["baseStats"] = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0}
        self.teamMatesDict[name]["ivs"] = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0}
        self.teamMatesDict[name]["evs"] = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0}
        self.teamMatesDict[name]["item"] = None
        self.teamMatesDict[name]["gender"] = None
        self.teamMatesDict[name]["moves"] = {"move1": None, "move2": None, "move3": None, "move4": None}
        self.teamMatesDict[name]["happiness"] = None
        self.teamMatesDict[name]["level"] = 100
        self.teamMatesDict[name]["shiny"] = None
        self.switch(name)
        self.the_menu.entryconfigure(name, label="None")
    
    def teamAdder(self,inputEvent):
        teamAdderGate = False
        while not teamAdderGate:
            if len(self.teamMateNames) == 0:
                self.respond("Which Pokemon would you like to start your team with?")
                inputEvent.wait()
                inputEvent.clear()
            else:
                if "anythinggoes" not in self.tier:
                    self.respond("Which Pokemon would you like to add to your team? Note that your team can not have two or more Pokemon with the same National Pokedex number!")
                    inputEvent.wait()
                    inputEvent.clear()
                else:
                    self.respond("Which Pokemon would you like to add to your team?")
                    inputEvent.wait()
                    inputEvent.clear()
            species = Pokedex.findPokemonSpecies(self.input_get)
            if species != None:
                if MetaDex.findPokemonTierData(species, self.tierfile) != None:
                    if "anythinggoes" not in self.tier:
                        numList = []
                        for s in self.teamMateNames:
                            numList.append(Pokedex.findPokemonNum(s))
                        if Pokedex.findPokemonNum(species) in numList:
                            self.respond("Oh, you can not have two or more Pokemon with the same National Pokedex number! You must select another Pokemon.")
                        else:
                            forme = Pokedex.findPokemonForme(species)
                            if forme == "Mega":
                                megaChecks = []
                                for teamMate in self.teamMateNames:
                                    if Pokedex.findPokemonForme(teamMate) == "Mega":
                                        megaChecks.append(False)
                                    else:
                                        megaChecks.append(True)
                                if all(megaChecks):
                                    self.teamMateNames.append(species)
                                    teamAdderGate = True
                                else:
                                    self.respond("Oh, I see that you're trying to add another mega to your team. I mean, this is technically allowed, but I wouldn't suggest it. You can only use one mega per battle.")
                                    multiMegaGate = False
                                    while not multiMegaGate:
                                        self.respond("Are you sure you want multiple megas in your team?")
                                        inputEvent.wait()
                                        inputEvent.clear()
                                        if self.input_get in self.yes:
                                            self.respond("Alright, I'll add another mega then!")
                                            self.teamMateNames.append(species)
                                            multiMegaGate = True
                                            teamAdderGate = True
                                        elif self.input_get in self.no:
                                            multiMegaGate = True
                                        else:
                                            self.respond("Um...I don't understand your response...")
                            else:
                                self.teamMateNames.append(species)
                                teamAdderGate = True
                    else:
                        forme = Pokedex.findPokemonForme(species)
                        if forme == "Mega":
                            megaChecks = []
                            for teamMate in self.teamMateNames:
                                if Pokedex.findPokemonForme(teamMate) == "Mega":
                                    megaChecks.append(False)
                                else:
                                    megaChecks.append(True)
                            if all(megaChecks):
                                self.teamMateNames.append(species)
                                teamAdderGate = True
                            else:
                                self.respond(
                                    "Oh, I see that you're trying to add another mega to your team. I mean, this is technically allowed, but I wouldn't suggest it. You can only use one mega per battle.")
                                multiMegaGate = False
                                while not multiMegaGate:
                                    self.respond("Are you sure you want multiple megas in your team?")
                                    inputEvent.wait()
                                    inputEvent.clear()
                                    if self.input_get in self.yes:
                                        self.respond("Alright, I'll add another mega then!")
                                        self.teamMateNames.append(species)
                                        multiMegaGate = True
                                        teamAdderGate = True
                                    elif self.input_get in self.no:
                                        multiMegaGate = True
                                    else:
                                        self.respond("Um...I don't understand your response...")
                        else:
                            self.teamMateNames.append(species)
                            teamAdderGate = True
                else:
                    self.respond("Oh, I'm sorry. There seems to be a problem.")
                    self.respond("Either Pokemon %s is not allowed in tier %s." % (species, self.tier))
                    self.respond("Or it might be that Pokemon %s is SO rare in tier %s that there isn't enough data on it" % (species, self.tier))
                    self.respond("Either way, I suggest chosing another Pokemon. That way I have the data necessary to help you")
            else:
                self.respond("Um...I don't understand your response...")

    def export(self):
        self.respond("I'm going to put your team in the same location you put this program. If you can't find it, just search for it on your computer's search bar. I promise it's there.")
        now = datetime.datetime.now()
        fileName = self.tier + "_" + str(now.day) + "-" + str(now.month) + "-" + str(now.year) + "_" + str(
            now.hour) + "-" + str(now.minute) + ".txt"
        file = open(os.path.dirname(os.path.realpath(__file__))+"/"+fileName, "w")
        for poke in self.teamMatesDict:
            if self.teamMatesDict[poke]["gender"] != None:
                if self.teamMatesDict[poke]["item"] != None:
                    file.write(self.teamMatesDict[poke]["species"] + " (" + self.teamMatesDict[poke]["gender"] + ") @ " +
                               self.teamMatesDict[poke]["item"] + "\n")
                    # self.respond(teamMatesDict[poke]["species"]+" ("+teamMatesDict[poke]["gender"]+") @ "+teamMatesDict[poke]["item"])
                else:
                    file.write(self.teamMatesDict[poke]["species"] + " (" + self.teamMatesDict[poke]["gender"] + ")\n")
                    # self.respond(teamMatesDict[poke]["species"]+" ("+teamMatesDict[poke]["gender"]+")")
            else:
                if self.teamMatesDict[poke]["item"] != None:
                    file.write(self.teamMatesDict[poke]["species"] + " @ " + self.teamMatesDict[poke]["item"] + "\n")
                    # self.respond(teamMatesDict[poke]["species"]+" @ "+teamMatesDict[poke]["item"])
                else:
                    file.write(self.teamMatesDict[poke]["species"] + "\n")
                    # self.respond(teamMatesDict[poke]["species"])

            file.write("Ability: " + self.teamMatesDict[poke]["ability"] + "\n")
            # self.respond("Ability: "+teamMatesDict[poke]["ability"])

            file.write("Level: " + str(self.teamMatesDict[poke]["level"]) + "\n")
            # self.respond("Level: "+str(teamMatesDict[poke]["level"]))

            if self.teamMatesDict[poke]["happiness"] != 255:
                file.write("Happiness: " + str(self.teamMatesDict[poke]["happiness"]) + "\n")
                # self.respond("Happiness: " + str(teamMatesDict[poke]["happiness"]))

            if self.teamMatesDict[poke]["shiny"] == "Yes":
                file.write("Shiny: Yes\n")
                # self.respond("Shiny: Yes")

            evStringNeeded = False
            evString = ""
            if self.teamMatesDict[poke]["evs"]["hp"] != 0:
                evString = evString + str(self.teamMatesDict[poke]["evs"]["hp"]) + " HP"
                evStringNeeded = True
            if self.teamMatesDict[poke]["evs"]["atk"] != 0:
                evString = evString + " / " + str(self.teamMatesDict[poke]["evs"]["atk"]) + " Atk"
                evStringNeeded = True
            if self.teamMatesDict[poke]["evs"]["def"] != 0:
                evString = evString + " / " + str(self.teamMatesDict[poke]["evs"]["def"]) + " Def"
                evStringNeeded = True
            if self.teamMatesDict[poke]["evs"]["spa"] != 0:
                evString = evString + " / " + str(self.teamMatesDict[poke]["evs"]["spa"]) + " SpA"
                evStringNeeded = True
            if self.teamMatesDict[poke]["evs"]["spd"] != 0:
                evString = evString + " / " + str(self.teamMatesDict[poke]["evs"]["spd"]) + " SpD"
                evStringNeeded = True
            if self.teamMatesDict[poke]["evs"]["spe"] != 0:
                evString = evString + " / " + str(self.teamMatesDict[poke]["evs"]["spe"]) + " Spe"
                evStringNeeded = True
            if evStringNeeded == True:
                file.write("EVs: " + evString + "\n")
                # self.respond("EVs: "+evString)

            file.write(self.teamMatesDict[poke]["nature"] + " Nature\n")
            # self.respond(teamMatesDict[poke]["nature"]+" Nature")

            ivStringNeeded = False
            ivString = ""
            if self.teamMatesDict[poke]["ivs"]["hp"] != 31:
                ivString = ivString + str(self.teamMatesDict[poke]["ivs"]["hp"]) + " HP"
                ivStringNeeded = True
            if self.teamMatesDict[poke]["ivs"]["atk"] != 31:
                ivString = ivString + " / " + str(self.teamMatesDict[poke]["ivs"]["atk"]) + " Atk"
                ivStringNeeded = True
            if self.teamMatesDict[poke]["ivs"]["def"] != 31:
                ivString = ivString + " / " + str(self.teamMatesDict[poke]["ivs"]["def"]) + " Def"
                ivStringNeeded = True
            if self.teamMatesDict[poke]["ivs"]["spa"] != 31:
                ivString = ivString + " / " + str(self.teamMatesDict[poke]["ivs"]["spa"]) + " SpA"
                ivStringNeeded = True
            if self.teamMatesDict[poke]["ivs"]["spd"] != 31:
                ivString = ivString + " / " + str(self.teamMatesDict[poke]["ivs"]["spd"]) + " SpD"
                ivStringNeeded = True
            if self.teamMatesDict[poke]["ivs"]["spe"] != 31:
                ivString = ivString + " / " + str(self.teamMatesDict[poke]["ivs"]["spe"]) + " Spe"
                ivStringNeeded = True
            if ivStringNeeded == True:
                file.write("IVs: " + ivString + "\n")
                # self.respond("IVs: " + ivString)

            for move in ["move1", "move2", "move3", "move4"]:
                if self.teamMatesDict[poke]["moves"][move] != None:
                    file.write("- " + self.teamMatesDict[poke]["moves"][move] + "\n")
                    # self.respond("- " + teamMatesDict[poke]["moves"][move])
            file.write("\n")
        file.close()
        self.respond("Ok, your team can be found in %s" % fileName)
        self.respond("So what you want to do is go to http://play.pokemonshowdown.com/")
        self.respond("Click on the 'Teambuilder' button.")
        self.respond("Click on the 'New Team' button.")
        self.respond("Click on the 'Import from text' button.")
        self.respond("Copy the entire text from the file I just sent you and paste it in the large input field.")
        self.respond("Click on the 'Import/Export' button on top.")
        self.respond("Your team will have been imported into the website!")
        self.respond("For extra measure, do you see that bar on the top left of your screen? It should read something like 'Untitled #'? This is where you can name your team!")
        self.respond("Under that, you should find the 'Format' option. Click it. A large window should appear.")
        self.respond("Select the format that most looks like %s (this is the tier/format you decided to build this team for)." % self.tier)
        self.respond("To check if everything went perfectingly in the team building process, click the 'Validate' button. A window should pop up.")
        self.respond("If your team gets validated for your chosen format/tier, your all set.")
        self.respond("If you do get an error, just follow the instructions given by the error message to correvct this. Revalidate your team and you should be ready to go!")
        self.respond("NOTE: Your imported team will be preserved on the website via cookies. Therefore, you can come back later to Pokemon Showdown, and your team will still be there!")
        self.respond("However, if you delete the cookies stored on your computer, you team will disappear. Don't worry. All you have to dude is just import your team from the file we just made today.")
        self.respond("If you want to test your team in an actual battle, click on the Home tab")
        self.respond("Before you can participate in an actual battle, you will need a Pokemon Showdown account.If you don't have one already, making one is very easy and takes two seconds: all it requires is a username and a password. If you already have an account, make sure you are signed in")
        self.respond("Now that you are signed in, click on the 'Format' option on the left of the screen. A large window will appear.")
        self.respond("Select the format that most looks like %s (this is the tier/format you decided to build this team for)." % self.tier)
        self.respond("Now that the website knows which type of battle you want to participate in, it will show you your teams (or one of them if you have multiple.)")
        self.respond("Select the team you wish to battle with.")
        self.respond("If the website doesn't show the team you wish to battle with, it means that your team hasn't been validated for that format. You must then go back to the Teambuilder, select your team, and validate it for the format/tier you wish to battle in.")
        self.respond("Alright, your all set! Just press the 'Battle!' button and have fun! Note, it may take a few moments for the servers to find you an opponent. Please be patient.")
        self.respond("glhf! Good luck and have fun!")

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

    def AI(self,inputEvent):
        self.yes = ["Y","y","Yes","yes","YES"]
        self.no = ["N","n","No","no","NO"]

        self.respond("Hello! I'm Al, here to help build your personal competitive Pokemon team!")
        self.respond("The great thing is, after we have built your team, I'll automatically export your team so you can easily import it into Pokemon Showdown, a Competitive Pokemon Battle Simulator used by hundreds of people every day!")
        self.respond("Let's get started!")
        # TODO: implement personal names and inout of user names

        # Display All Tiers Downloaded Tiers
        self.respond("First, we need to decide which tier this team will be used in.")
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
        self.respond("You have the following tiers to choose from:")
        tiersString = ""
        for t in tiers:
            tiersString+=t+"\n    "
        self.respond(tiersString[:-5])
        chooseTierGate = False
        while not chooseTierGate:
            self.respond("Which tier would you like to work in? (String)")
            inputEvent.wait()
            inputEvent.clear()
            if self.input_get in tiers:
                self.tier = self.input_get
                confirmTierGate = False
                while not confirmTierGate:
                    self.respond("You would like to build a team for %s? (Y/N)" % self.tier)
                    inputEvent.wait()
                    inputEvent.clear()
                    if self.input_get in self.yes:
                        chooseTierGate = True
                        confirmTierGate = True
                    elif self.input_get in self.no:
                        confirmTierGate = True
                    else:
                        self.respond("Um...I don't understand your response...")
            else:
                self.respond("Um...I don't understand your response...")

        # Select Level of Competitiveness
        self.respond("Ok, now how hard core do you want to make this team? You have 4 options.\n    Fun\n    Serious\n    Hard Core\n    Champion")
        tierSeverityGate = False
        while not tierSeverityGate:
            self.respond("So, what will it be? (String)")
            inputEvent.wait()
            if self.input_get in ["fun", "Fun"]:
                self.tier = self.tier + "-0"
                tierSeverityGate = True
            elif self.input_get in ["serious", "Serious"]:
                self.tier = self.tier + "-1500"
                tierSeverityGate = True
            elif self.input_get in ["hard core", "hard Core", "Hard Core", "Hard Core", "hardcore", "hardCore", "Hardcore","HardCore"]:
                if "ou" in self.tier:
                    self.tier = self.tier + "-1695"
                else:
                    self.tier = self.tier + "-1630"
                tierSeverityGate = True
            elif self.input_get in ["champion", "Champion"]:
                if "ou" in self.tier:
                    self.tier = self.tier + "-1825"
                else:
                    self.tier = self.tier + "-1760"
                tierSeverityGate = True
            else:
                self.respond("Um, I don't understand that response. You must pick one of the four options shown above.")
        self.tierfile = self.tier + ".json"
        self.respond("Excellent! Let's get started with your team then!")

        # Helping the User Start a New Team and Selecting First Team Member
        firstMemberGate = False
        while not firstMemberGate:
            self.respond("So, do you know which Pokemon you want to start your team with? (Y/N)")
            inputEvent.wait()
            inputEvent.clear()
            if self.input_get in self.yes:
                firstMemberGate = True
                self.respond("Great! Innovation makes a great team!")
            elif self.input_get in self.no:
                firstMemberGate = True
                self.respond("That's ok. There are plenty of Pokemon to choose from. Let me give you a few suggestions.")
                text=""
                for poke in TeamBuilder.rawCountTopFinds(self.tierfile, 20):
                    pokeData = Pokedex.findPokemonData(poke[0])
                    if len(pokeData["types"])==1:
                        text+=poke[0]+":\n\tTYPE: "+pokeData["types"][0]+"\n\tSTATS: "+str(pokeData["baseStats"]["hp"])+"/"+str(pokeData["baseStats"]["atk"])+"/"+str(pokeData["baseStats"]["def"])+"/"+str(pokeData["baseStats"]["spa"])+"/"+str(pokeData["baseStats"]["spd"])+"/"+str(pokeData["baseStats"]["spe"])+"\n\tPOP: "+str(poke[1])+"\n\n    "
                    elif len(pokeData["types"])==2:
                        text+=poke[0]+":\n\tTYPE: "+pokeData["types"][0]+", "+pokeData["types"][1]+"\n\tSTATS: "+str(pokeData["baseStats"]["hp"])+"/"+str(pokeData["baseStats"]["atk"])+"/"+str(pokeData["baseStats"]["def"])+"/"+str(pokeData["baseStats"]["spa"])+"/"+str(pokeData["baseStats"]["spd"])+"/"+str(pokeData["baseStats"]["spe"])+"\n\tPOP: "+str(poke[1])+"\n\n    "
                self.respond(text[:-5])
            else:
                self.respond("Um... I don't understand your response ")
        pokedex = Pokedex.loadPokedex()
        self.teamMateNames = []
        self.teamAdder(inputEvent)

        # Adding Other 5 Members
        for i in range(5):
            #TODO: include the species clause when showing new pokes
            self.respond("Ok, let me suggest some team-mates. How many suggestions would you like to see? (Int)")
            memberSelectGate = False
            while not memberSelectGate:
                try:
                    inputEvent.wait()
                    inputEvent.clear()
                    teamSuggAmount = int(self.input_get)
                    memberSelectGate = True
                except:
                    self.respond("Um...I don't understand your response...")
                    # TODO: implement ID checks for species clause
            text = ""
            for poke in TeamBuilder.findTeamMetaMatches(self.teamMateNames, self.tierfile, teamSuggAmount):
                #TODO: fix this
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

                #text+=t[0]+":\n\tPOP: "+str(t[1])+"\n\n    "
            self.respond(text[:-5])
            self.teamAdder(inputEvent)

        # Switching Team Members If Needed
        confirmTeamGate = False
        while not confirmTeamGate:
            text = ""
            text+="Here is your team!"
            for t in self.teamMateNames:
                text+="\n    "+t
            self.respond(text)
            self.respond("Are you happy with the selection? (Y/N)")
            inputEvent.wait()
            inputEvent.clear()
            if self.input_get in self.yes:
                confirmTeamGate = True
            elif self.input_get not in self.yes and self.input_get not in self.no:
                self.respond("Um...I don't understand that response...")
            else:
                # Finding Flip
                flipMemberGate = False
                while not flipMemberGate:
                    self.respond("Which Pokemon in your team would you like to swap? (String)")
                    inputEvent.wait()
                    inputEvent.clear()
                    flip = self.input_get
                    flipName = Pokedex.findPokemonSpecies(flip)
                    if flipName in self.teamMateNames:
                        flipMemberGate = True
                    else:
                        self.respond("Pokemon %s isn't part of your team" % flip)
                # Showing Team Mate Options
                self.respond("Ok, let me suggest some team-mates. How many suggestions would you like to see? (Int)")
                swapAmountGate = False
                while not swapAmountGate:
                    try:
                        inputEvent.wait()
                        inputEvent.clear()
                        swapAmount = int(self.input_get)
                        teamMateNamesprime = []
                        for i in range(len(self.teamMateNames)):
                            teamMateNamesprime.append(self.teamMateNames[i])
                        del teamMateNamesprime[teamMateNamesprime.index(flipName)]
                        swapAmountGate = True
                    except:
                        self.respond("Um...unfortunately I can't understand your request. Try again")
                text = ""
                for poke in TeamBuilder.findTeamMetaMatches(teamMateNamesprime, self.tierfile, swapAmount):
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
                    #text+=t[0]+": "+str(t[1])+"\n\n    "
                self.respond(text)
                # Finding Flop and Checking if it's another Mega
                flopMemberGate = False
                while not flopMemberGate:
                    if "anythinggoes" not in self.tier:
                        self.respond("Which Pokemon in your team would you like to swap %s with? Note that your team can not have two or more Pokemon with the same National Pokedex number!" % flipName)
                        inputEvent.wait()
                        inputEvent.clear()
                        flop = self.input_get
                    else:
                        self.respond("Which Pokemon in your team would you like to swap %s with?" % flipName)
                        inputEvent.wait()
                        inputEvent.clear()
                        flop = self.input_get
                    flopName = Pokedex.findPokemonSpecies(flop)
                    if flopName != None:
                        data = MetaDex.findPokemonTierData(flopName, self.tierfile)
                        if data != None:
                            if "anythinggoes" not in self.tier:
                                numList = []
                                for s in self.teamMateNames:
                                    numList.append(Pokedex.findPokemonNum(s))
                                if Pokedex.findPokemonNum(flopName) in numList:
                                    self.respond("Oh, you can not have two or more Pokemon with the same National Pokedex number! You must select another Pokemon.")
                                else:
                                    forme = Pokedex.findPokemonForme(flopName)
                                    if forme == "Mega":
                                        megaChecks = []
                                        for teamMate in self.teamMateNames:
                                            if Pokedex.findPokemonForme(teamMate) == "Mega":
                                                megaChecks.append(False)
                                            else:
                                                megaChecks.append(True)
                                        if all(megaChecks):
                                            self.teamMateNames[self.teamMateNames.index(flipName)] = flopName
                                            self.respond("Done! I switched %s with %s." % (flipName, flopName))
                                            flopMemberGate = True
                                        else:
                                            self.respond("Oh, I see that you're trying to add another mega to your team. I mean, this is techniaclly allowed, but I wouldn't suggest it. You can only use one mega per battle.")
                                            multiMegaGate = False
                                            while not multiMegaGate:
                                                self.respond("Are you sure you want multiple megas in your team?")
                                                inputEvent.wait()
                                                inputEvent.clear()
                                                if self.input_get in self.yes:
                                                    self.respond("Alright, I'll add another mega then!")
                                                    self.teamMateNames[self.teamMateNames.index(flipName)] = flopName
                                                    self.respond("Done! I switched %s with %s." % (flipName, flopName))
                                                    flopMemberGate = True
                                                    multiMegaGate = True
                                                elif self.input_get in self.no:
                                                    multiMegaGate = True
                                                else:
                                                    self.respond("Um...I don't understand your response...")
                                    else:
                                        self.teamMateNames[self.teamMateNames.index(flipName)] = flopName
                                        self.respond("Done! I switched %s with %s." % (flipName, flopName))
                                        flopMemberGate = True
                            else:
                                forme = Pokedex.findPokemonForme(flopName)
                                if forme == "Mega":
                                    megaChecks = []
                                    for teamMate in self.teamMateNames:
                                        if Pokedex.findPokemonForme(teamMate) == "Mega":
                                            megaChecks.append(False)
                                        else:
                                            megaChecks.append(True)
                                    if all(megaChecks):
                                        self.teamMateNames[self.teamMateNames.index(flipName)] = flopName
                                        self.respond("Done! I switched %s with %s." % (flipName, flopName))
                                        flopMemberGate = True
                                    else:
                                        self.respond(
                                            "Oh, I see that you're trying to add another mega to your team. I mean, this is techniaclly allowed, but I wouldn't suggest it. You can only use one mega per battle.")
                                        multiMegaGate = False
                                        while not multiMegaGate:
                                            self.respond("Are you sure you want multiple megas in your team?")
                                            inputEvent.wait()
                                            inputEvent.clear()
                                            if self.input_get in self.yes:
                                                self.respond("Alright, I'll add another mega then!")
                                                self.teamMateNames[self.teamMateNames.index(flipName)] = flopName
                                                self.respond("Done! I switched %s with %s." % (flipName, flopName))
                                                flopMemberGate = True
                                                multiMegaGate = True
                                            elif self.input_get in self.no:
                                                multiMegaGate = True
                                            else:
                                                self.respond("Um...I don't understand your response...")
                                else:
                                    self.teamMateNames[self.teamMateNames.index(flipName)] = flopName
                                    self.respond("Done! I switched %s with %s." % (flipName, flopName))
                                    flopMemberGate = True
                        else:
                            self.respond("Oh, I'm sorry. There seems to be a problem.")
                            self.respond("Either Pokemon %s is not allowed in tier %s." % (flop, self.tier))
                            self.respond("Or it might be that Pokemon %s is SO rare in tier %s that there isn't enough data on it" % (flop, self.tier))
                            self.respond("Either way, I suggest chosing another Pokemon. That way I have the data necessary to help you")
                    else:
                        self.respond("The inputted Pokemon is not an actual Pokemon! Try again")
        self.respond("Your team is coming along great. Let's move on to the individual team members.")

        # Make Dictionary with All Necessary Info
        for member in self.teamMateNames:
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
            self.teamMatesDict[member] = dict

        pokemon1_menu = Menu(self.the_menu,tearoff=0)
        pokemon1_menu.add_command(label="View",command=lambda:self.switch(self.teamMateNames[0]))
        pokemon1_menu.add_command(label="Delete",command=lambda:self.delete(self.teamMateNames[0]))
        self.the_menu.add_cascade(label=self.teamMateNames[0], menu=pokemon1_menu)

        pokemon2_menu = Menu(self.the_menu, tearoff=0)
        pokemon2_menu.add_command(label="View", command=lambda:self.switch(self.teamMateNames[1]))
        pokemon2_menu.add_command(label="Delete", command=lambda:self.delete(self.teamMateNames[1]))
        self.the_menu.add_cascade(label=self.teamMateNames[1], menu=pokemon2_menu)

        pokemon3_menu = Menu(self.the_menu, tearoff=0)
        pokemon3_menu.add_command(label="View", command=lambda:self.switch(self.teamMateNames[2]))
        pokemon3_menu.add_command(label="Delete", command=lambda:self.delete(self.teamMateNames[2]))
        self.the_menu.add_cascade(label=self.teamMateNames[2], menu=pokemon3_menu)

        pokemon4_menu = Menu(self.the_menu, tearoff=0)
        pokemon4_menu.add_command(label="View", command=lambda:self.switch(self.teamMateNames[3]))
        pokemon4_menu.add_command(label="Delete", command=lambda:self.delete(self.teamMateNames[3]))
        self.the_menu.add_cascade(label=self.teamMateNames[3], menu=pokemon4_menu)

        pokemon5_menu = Menu(self.the_menu, tearoff=0)
        pokemon5_menu.add_command(label="View", command=lambda:self.switch(self.teamMateNames[4]))
        pokemon5_menu.add_command(label="Delete", command=lambda:self.delete(self.teamMateNames[4]))
        self.the_menu.add_cascade(label=self.teamMateNames[4], menu=pokemon5_menu)

        pokemon6_menu = Menu(self.the_menu, tearoff=0)
        pokemon6_menu.add_command(label="View", command=lambda:self.switch(self.teamMateNames[5]))
        pokemon6_menu.add_command(label="Delete", command=lambda:self.delete(self.teamMateNames[5]))
        self.the_menu.add_cascade(label=self.teamMateNames[5], menu=pokemon6_menu)

        self.respond("I have uploaded your team members into the panel to your left. Have a look around!")

        # Iterate Over Every Team Member
        for poke in self.teamMatesDict:
            spName = self.teamMatesDict[poke]["species"]
            self.switch(spName)
            if self.teamMateNames.index(poke) == 0:
                self.respond("Let's start with %s." % spName)
            else:
                self.respond("Now let's take a look at %s." % spName)
            text = ""
            text+=spName+" has the following base stats.\n    "
            for stat in self.teamMatesDict[poke]["baseStats"]:
                if stat == "hp":
                    text+=stat+" : "+str(self.teamMatesDict[poke]["baseStats"][stat])+"\n    "
                else:
                    text+=stat+": "+str(self.teamMatesDict[poke]["baseStats"][stat])+"\n    "
            self.respond(text[:-5])

            # Choosing Ability
            abilities = Pokedex.findPokemonAbilities(spName)
            metaAbilities = MetaDex.findPokemonTierAbilities(spName, self.tierfile)
            text = ""
            text+=self.cut(spName+" can have the following abilities:")
            text+="\n\t"+abilities["0"]+":"+self.cut("\n\t    DESC: "+Pokedex.findAbilityShortDesc(abilities["0"]))+"\n\t    POP: "+str(metaAbilities[Pokedex.findAbilityID(abilities["0"])])
            if len(metaAbilities) > 1:
                if "1" in abilities:
                    text+="\n\t"+abilities["1"]+":"+self.cut("\n\t    DESC: "+Pokedex.findAbilityShortDesc(abilities["1"]))+"\n\t    POP: "+str(metaAbilities[Pokedex.findAbilityID(abilities["1"])])
                if "S" in abilities and TeamBuilder.compress(abilities["S"]) in metaAbilities:
                    text+=self.cut("\n\tAdditionally, "+spName+" also has a special ability:")
                    text+="\n\t"+abilities["S"]+":"+self.cut("\n\t    DESC: "+Pokedex.findAbilityShortDesc(abilities["S"]))+"\n\t    POP: "+str(metaAbilities[Pokedex.findAbilityID(abilities["S"])])
                    if TeamBuilder.compress(abilities["S"]) not in list(metaAbilities.keys()):
                        text+=self.cut("\n    Unfortunately, this ability is not allowed in "+self.tier)
                    else:
                        #TODO fix this
                        pass
                if "H" in abilities and TeamBuilder.compress(abilities["H"]) in metaAbilities:
                    text+=self.cut("\n    Additionally, "+spName+" also has a Hidden ability:")
                    text+="\n\t"+abilities["H"]+":"+self.cut("\n\t    DESC: "+Pokedex.findAbilityShortDesc(abilities["H"]))+"\n\t    POP: "+str(metaAbilities[Pokedex.findAbilityID(abilities["H"])])
                    if TeamBuilder.compress(abilities["H"]) not in list(metaAbilities.keys()):
                        text+=self.cut("\n    Unfortunately, this ability is not allowed in "+self.tier)
                    else:
                        #TODO fix this
                        pass
                self.respond(text)
                abilityGate = False
                while not abilityGate:
                    self.respond("What ability would you like %s to have?" % spName)
                    inputEvent.wait()
                    inputEvent.clear()
                    for s in ["0", "1", "S", "H"]:
                        abName = Pokedex.findAbilityName(self.input_get)
                        if s in abilities and abName == abilities[s]:
                            if TeamBuilder.compress(abilities[s]) in metaAbilities:
                                self.teamMatesDict[poke]["ability"] = abName
                                abilityGate = True
                    if not abilityGate:
                        self.respond("I'm sorry, but %s is not an ability that %s can have in tier %s." % (spName, self.input_get, self.tier))
            else:
                self.respond(text)
                self.respond("As you can see, %s only has one ability, so we don't have much choice here. I'll update your %s automatically, so you dont have to worry about that." % (
                    spName, spName))
                self.teamMatesDict[poke]["ability"] = abilities["0"]
            self.respond("Done! Your %s now has the ability %s" % (spName, self.teamMatesDict[poke]["ability"]))
            self.update(spName,"ability")

            self.respond("Now that we have that decided, let's move on to IV and Nature/EV spreads")

            # Choosing IVs
            self.respond("First thing's first: I propose to give your %s the following IV spread: 31/31/31/31/31/31" % spName)
            self.respond(
                "This is by far the most common IV spread for Pokemon. However, if you have something more specific in mind, you might want a different IV spread")
            ivGate = False
            while not ivGate:
                self.respond("Do you want to use this IV spread?")
                inputEvent.wait()
                inputEvent.clear()
                if self.input_get in self.yes:
                    ivGate = True
                elif self.input_get not in self.yes and self.input_get not in self.no:
                    self.respond("Um...I don't understand that response...")
                else:
                    # Selecting Hidden Power
                    hpGate = False
                    while not hpGate:
                        self.respond("Would you like to give %s the move Hidden Power (Category: Special, Power: 60, Type: Depends on user's IVs)? \nRemember that Hidden Power CAN NOT have a Fairy or Normal typing." % spName)
                        inputEvent.wait()
                        inputEvent.clear()
                        if self.input_get in self.yes:
                            ivTypeGate = False
                            while not ivTypeGate:
                                self.respond("What type would you like Hidden Power to be?")
                                inputEvent.wait()
                                inputEvent.clear()
                                typeInput = self.input_get
                                types = Pokedex.loadTypes()
                                tList = list(typeInput)
                                tList[0] = tList[0].capitalize()
                                typeInput = "".join(tList)
                                self.teamMatesDict[spName]["moves"]["move1"] = "Hidden Power " + typeInput
                                if typeInput in types and typeInput != "Normal" and typeInput != "Fairy":
                                    text = ""
                                    text+="Ok, here are a few IV spreads that result in Hidden Power having a typeInput typing."
                                    for set in types[typeInput]["hp Sets"]:
                                        text+="\n\t"+set+":"
                                        for i in range(len(types[typeInput]["hp Sets"][set])):
                                            text+="\n\t    "+types[typeInput]["hp Sets"][set][i]
                                        ivTypeGate = True
                                    self.respond(text)
                                elif typeInput == "Fairy" or typeInput == "Normal":
                                    self.respond("I told you that Hidden Power can not have a Fairy or Normal typing! Didn't you pay attention?")
                                else:
                                    self.respond("Um...I don't understand that response...")
                            hpGate = True
                        elif self.input_get in self.no:
                            hpGate = True
                        else:
                            self.respond("Um...I don't understand that response")

                    # Choosing IVs
                    self.respond("What kind of IVs should %s have?" % spName)
                    for string in ["hp", "atk", "def", "spa", "spd", "spe"]:
                        ivChoiceGate = False
                        while not ivChoiceGate:
                            self.respond(string+":")
                            inputEvent.wait()
                            inputEvent.clear()
                            iv = self.input_get
                            try:
                                iv = int(iv)
                                if 0 <= iv <= 31:
                                    self.teamMatesDict[spName]["ivs"][string] = iv
                                    ivChoiceGate = True
                                else:
                                    self.respond("Oh, I'm sorry, but I can't give %s %s %s Ivs. Try again" % (
                                    spName, iv, string.capitalize()))
                            except:
                                self.respond("Um...how can I give %s %s %s IVs? Try again" % (spName, iv, string.capitalize()))

                    self.respond("Your %s currently has the following IV spread." % spName)
                    self.respond("%s/%s/%s/%s/%s/%s" % (
                    self.teamMatesDict[spName]["ivs"]["hp"], self.teamMatesDict[spName]["ivs"]["atk"],
                    self.teamMatesDict[spName]["ivs"]["def"], self.teamMatesDict[spName]["ivs"]["spa"],
                    self.teamMatesDict[spName]["ivs"]["spd"], self.teamMatesDict[spName]["ivs"]["spe"]))
            self.respond("Great! Now your %s has the following IV spread: %s/%s/%s/%s/%s/%s." % (
            spName, self.teamMatesDict[spName]["ivs"]["hp"], self.teamMatesDict[spName]["ivs"]["atk"],
            self.teamMatesDict[spName]["ivs"]["def"], self.teamMatesDict[spName]["ivs"]["spa"],
            self.teamMatesDict[spName]["ivs"]["spd"], self.teamMatesDict[spName]["ivs"]["spe"]))
            self.update(spName,"ivs")

            # Choosing Natures
            #TODO: what nature is what? fix
            self.respond("Alright, it's time for Natures and EVs")
            self.respond("%s has a few common Nature/EV spreads. How many would you like to see? (Int)" % spName)
            gate8 = False
            while not gate8:
                try:
                    inputEvent.wait()
                    inputEvent.clear()
                    evAmount = int(self.input_get)
                    sortedSpreads = TeamBuilder.findPokemonMetaSpreads(spName, self.tierfile, evAmount)
                    gate8 = True
                except:
                    self.respond("How can I show you that many Nature/EV spreads? Try again")
            text = ""
            for s in range(len(sortedSpreads)):
                text += sortedSpreads[s][0] + ":\n\tPOP: " + str(sortedSpreads[s][1]) + "\n    "
            self.respond(text[:-5])
            natureGate = False
            while not natureGate:
                self.respond("What Nature would you like to give to %s? (String)" % spName)
                inputEvent.wait()
                inputEvent.clear()
                res = self.input_get
                rList = list(res)
                rList[0] = rList[0].capitalize()
                res = "".join(rList)
                if res in ["Hardy", "Lonely", "Adamant", "Naughty", "Brave", "Bold", "Docile", "Impish", "Lax",
                           "Relaxed", "Modest", "Mild", "Bashful", "Rash", "Quiet", "Calm", "Gentle", "Careful",
                           "Quirky", "Sassy", "Timid", "Hasty", "Jolly", "Naive", "Serious"]:
                    self.teamMatesDict[spName]["nature"] = res
                    natureGate = True
                else:
                    self.respond("Um...that's not a defined nature, so I can't assign that to %s. Try again." % spName)
            self.respond("Excellent, now your %s has a %s nature!" % (spName, self.teamMatesDict[spName]["nature"]))
            self.update(spName,"nature")

            # Choosing EVs
            self.respond("And now it's time for EVs.")
            topNatureSpread = None
            for i in range(len(sortedSpreads)):
                if sortedSpreads[i][0].split(":")[0] == self.teamMatesDict[spName]["nature"]:
                    topNatureSpread = sortedSpreads[i][0].split(":")[1]
                    self.respond("I'll start you off with the most common EV spread for your chosen Nature. In this case, that would be %s." % topNatureSpread)
                    break
            if topNatureSpread == None:
                topNatureSpread = sortedSpreads[0][0].split(":")[1]
                self.respond("I couldn't immediately find any common EV spreads for your chosen Nature, but here is the most common EV spread currently in use: %s." % topNatureSpread)
            parts2 = topNatureSpread.split("/")
            self.teamMatesDict[spName]["evs"]["hp"] = int(parts2[0])
            self.teamMatesDict[spName]["evs"]["atk"] = int(parts2[1])
            self.teamMatesDict[spName]["evs"]["def"] = int(parts2[2])
            self.teamMatesDict[spName]["evs"]["spa"] = int(parts2[3])
            self.teamMatesDict[spName]["evs"]["spd"] = int(parts2[4])
            self.teamMatesDict[spName]["evs"]["spe"] = int(parts2[5])
            evGate = False
            while not evGate:
                self.respond("Do you want to use this EV spread?")
                inputEvent.wait()
                inputEvent.clear()
                if self.input_get in self.yes:
                    evGate = True
                elif self.input_get not in self.no and self.input_get not in self.yes:
                    self.respond("Um...I don't understand that response...")
                else:
                    self.respond("What kind of EVs should %s have? \nRemember, each Stat can effectively only have a maximum of 252 EVs, and the total can not effectively be larger than 508." % spName)
                    available = 508
                    for string in ["hp", "atk", "def", "spa", "spd", "spe"]:
                        evChoiceGate = False
                        while not evChoiceGate:
                            self.respond("Number of EVs available: %s" % available)
                            self.respond(string + ":")
                            inputEvent.wait()
                            inputEvent.clear()
                            try:
                                ev = int(self.input_get)
                                if 0 <= ev <= 252:
                                    if available - ev >= 0:
                                        available = available - ev
                                        self.teamMatesDict[spName]["evs"][string] = ev
                                        evChoiceGate = True
                                    else:
                                        self.respond("You exceeded the limit on your total EVs. Hey, I didn't make the rules...")
                                else:
                                    self.respond("Oh, I'm sorry, but I can't give %s %s HP EVs. Try again" % (spName, ev))
                            except:
                                self.respond("Um...how can I give %s %s HP EVs? Try again" % (spName, ev))
                    self.respond("Your %s currently has the following IV spread." % spName)
                    self.respond("%s/%s/%s/%s/%s/%s" % (
                    self.teamMatesDict[spName]["evs"]["hp"], self.teamMatesDict[spName]["evs"]["atk"],
                    self.teamMatesDict[spName]["evs"]["def"], self.teamMatesDict[spName]["evs"]["spa"],
                    self.teamMatesDict[spName]["evs"]["spd"], self.teamMatesDict[spName]["evs"]["spe"]))
            self.respond("Great! Now your %s has the following EV spread: %s/%s/%s/%s/%s/%s." % (
            spName, self.teamMatesDict[spName]["evs"]["hp"], self.teamMatesDict[spName]["evs"]["atk"],
            self.teamMatesDict[spName]["evs"]["def"], self.teamMatesDict[spName]["evs"]["spa"],
            self.teamMatesDict[spName]["evs"]["spd"], self.teamMatesDict[spName]["evs"]["spe"]))
            self.update(spName,"evs")

            # Selecting Gender
            self.respond("Ok, now we have to change gears a little. Time to talk about your Pokemon's gender")
            if Pokedex.findPokemonGender(spName) != None:
                self.respond("Ah, this Pokemon has be a specific gender according to it's species. Don't worry, I'll take care of that")
                if Pokedex.findPokemonGender(spName) != "N":
                    self.teamMatesDict[spName]["gender"] = Pokedex.findPokemonGender(spName)
            else:
                genderGate = False
                while not genderGate:
                    self.respond("Do you have a specific gender in mind for %s? (Y/N)" % spName)
                    inputEvent.wait()
                    inputEvent.clear()
                    if self.input_get in self.no:
                        self.respond("Ok, I'll pick a gender at random for you then.")
                        genPick = random.randrange(1, 10)
                        if genPick <= 5:
                            self.teamMatesDict[spName]["gender"] = "M"
                            genderGate = True
                        else:
                            self.teamMatesDict[spName]["gender"] = "F"
                            genderGate = True
                    elif self.input_get in self.yes:
                        pickGenderGate = False
                        while not pickGenderGate:
                            self.respond("Which gender would you like to make your %s? (String)" % spName)
                            inputEvent.wait()
                            inputEvent.clear()
                            if self.input_get in ["M", "m", "Male", "male", "Man", "man"]:
                                self.teamMatesDict[spName]["gender"] = "M"
                                pickGenderGate = True
                                genderGate = True
                            elif self.input_get in ["F", "f", "Female", "female", "Woman", "woman"]:
                                self.teamMatesDict[spName]["gender"] = "F"
                                pickGenderGate = True
                                genderGate = True
                            else:
                                self.respond("Um...I don't understand that response")
                    else:
                        self.respond("Um, I don't understand that response...")
            self.respond("Done! Your %s is now has of the %s gender!" % (spName, self.teamMatesDict[spName]["gender"]))
            self.update(spName,"gender")

            # Show Popular Moves
            self.respond("Alright, now hey comes the REALLY important part: selecting moves.\tI'll show you a few of the most common moves that %s can have." % spName)
            moves = [self.teamMatesDict[spName]["moves"]["move1"], self.teamMatesDict[spName]["moves"]["move2"],self.teamMatesDict[spName]["moves"]["move3"], self.teamMatesDict[spName]["moves"]["move4"]]
            moveset = MetaDex.findPokemonTierMoves(spName, self.tierfile)
            #TODO: implement hidden powers
            if len(moveset) == 1:
                self.respond("Oh, this Pokemon species can only learn 1 move! I set whatever moves I can, k?")
                moves[0] = Pokedex.findMoveName(list(moveset.keys())[0])
                moves[1] = None
                moves[2] = None
                moves[3] = None
            elif len(moveset) == 2:
                self.respond("Oh, this Pokemon species can only learn 2 moves! I set whatever moves I can, k?")
                moves[0] = Pokedex.findMoveName(list(moveset.keys())[0])
                moves[1] = Pokedex.findMoveName(list(moveset.keys())[1])
                moves[2] = None
                moves[3] = None
            elif len(moveset) == 3:
                self.respond("Oh, this Pokemon species can only learn 3 moves! I set whatever moves I can, k?")
                moves[0] = Pokedex.findMoveName(list(moveset.keys())[0])
                moves[1] = Pokedex.findMoveName(list(moveset.keys())[1])
                moves[2] = Pokedex.findMoveName(list(moveset.keys())[2])
                moves[3] = None
            elif len(moveset) == 4:
                self.respond("Oh, this Pokemon species can only learn 4 moves! I set whatever moves I can, k?")
                moves[0] = Pokedex.findMoveName(list(moveset.keys())[0])
                moves[1] = Pokedex.findMoveName(list(moveset.keys())[1])
                moves[2] = Pokedex.findMoveName(list(moveset.keys())[2])
                moves[3] = Pokedex.findMoveName(list(moveset.keys())[3])
            else:
                self.respond("How many would you like to see? (Int)")
                showMovesGate = False
                while not showMovesGate:
                    try:
                        inputEvent.wait()
                        inputEvent.clear()
                        moveAmount = int(self.input_get)
                        sortedMoves = TeamBuilder.findPokemonMetaMoves(spName, self.tierfile, moveAmount)
                        showMovesGate = True
                    except:
                        self.respond("How can I show you that many Moves? Try again")
                text=""
                for s in range(len(sortedMoves)):
                    if sortedMoves[s][0] != "Nothing" and sortedMoves[s][0] != "":
                        moveData = Pokedex.findMoveData(sortedMoves[s][0])
                        text+=moveData["name"]+":\n\tCAT: "+moveData["category"]+",\n\tTYPE: "+moveData["type"]+",\n\tPP: "+str(moveData["pp"])+",\n\tACC: "+str(moveData["accuracy"])+",\n\tBASEPOW: "+str(moveData["basePower"])+","+self.cut("\n\tDESC: "+moveData["shortDesc"])+"\n\tPOP: "+str(sortedMoves[s][1])+"\n    "
                    else:
                        text+="Nothing:\n\tCAT: Nothing,\n\tTYPE: Nothing,\n\tPP: 0,\n\tACC: 0,\n\tBASEPOW: 0,\n\tDESC: Does nothing.\n\tPOP: 0\n    "
                self.respond(text)

            for moveIndex in [1, 2, 3, 4]:
                if moves[moveIndex - 1] == None:
                    moveGate = False
                    while not moveGate:
                        self.respond("Which move would you like %s to have in move slot #%s? (String)" % (spName, moveIndex))
                        inputEvent.wait()
                        inputEvent.clear()
                        if moveIndex != 1 and self.input_get in ["None", "none", "Null", "null"]:
                            moves[moveIndex - 1] = None
                            moveGate = True
                        else:
                            resName = Pokedex.findMoveName(self.input_get)
                            if resName != None:
                                if Pokedex.findMoveID(self.input_get) in MetaDex.findPokemonTierMoves(spName, self.tierfile):
                                    if resName not in moves:
                                        moves[moveIndex - 1] = resName
                                        moveGate = True
                                    else:
                                        self.respond("Oh, you already have %s as a move for your %s. Please select a different move." % (resName, spName))
                                else:
                                    self.respond("Oh, there seems to be a problem. Either %s can't learn this move, or it is used SO rarely that I couldn't find any useful data. In any case, try a different move." % spName)
                            else:
                                self.respond("I'm sorry, but that is not a valid move. Try again")
                    self.respond("Understood")
                else:
                    self.respond("Due to meeting various requirements, this move for your %s has already been chosen to be %s. So that's already done!" % (spName, moves[moveIndex - 1]))

            # Switching Moves Around
            movesCheckGate = False
            while not movesCheckGate:
                text = ""
                text+="Your "+spName+" will have the following moves."
                text+="\n\tMove 1: "+moves[0]
                text+="\n\tMove 2: "+moves[1]
                text+="\n\tMove 3: "+moves[2]
                text+="\n\tMove 4: "+moves[3]
                text+="\n    Do you want to keep this moveset? Y/N"
                self.respond(text)
                inputEvent.wait()
                inputEvent.clear()
                if self.input_get in self.yes:
                    movesCheckGate = True
                elif self.input_get not in self.yes and self.input_get not in self.no:
                    self.respond("Um...I don't understand that response...")
                else:
                    # Selecting Flip
                    flipMoveGate = False
                    while not flipMoveGate:
                        self.respond("Which move would you like to swap?")
                        inputEvent.wait()
                        inputEvent.clear()
                        flip = self.input_get
                        if flip in ["None", "none", "Null", "null"]:
                            flipName = None
                            flipMoveGate = True
                        else:
                            flipName = Pokedex.findMoveName(flip)
                            if flipName in moves and flipName != None:
                                flipMoveGate = True
                            else:
                                self.respond("%s isn't part of your current moveset!" % flip)

                    # Showing Move Options
                    self.respond("Ok, let me show you the most commonly-used moves again. How many suggestions would you like to see?")
                    flipAmountGate = False
                    while not flipAmountGate:
                        try:
                            inputEvent.wait()
                            inputEvent.clear()
                            swapAmount = int(self.input_get)
                            if swapAmount >= 0:
                                # TODO: Implement the inability to chose already chosen moves
                                sortedMoves = TeamBuilder.findPokemonMetaMovesExc(spName, self.tierfile, swapAmount, moves)
                                flipAmountGate = True
                            else:
                                self.respond("Well I can't suggest that many suggestions, now can I?")
                        except:
                            self.respond("Well that doesn't make any sense. Try again")
                    text = ""
                    for t in sortedMoves:
                        if t[0] != "Nothing" and t[0] != "":
                            moveData=Pokedex.findMoveData(t[0])
                            text +=moveData["name"]+":\n\tCAT: "+moveData["category"]+",\n\tTYPE: "+moveData["type"]+",\n\tPP: "+str(moveData["pp"])+",\n\tACC: "+str(moveData["accuracy"])+",\n\tBASEPOW: "+str(moveData["basePower"])+","+self.cut("\n\tDESC: "+moveData["shortDesc"])+"\n\tPOP: "+str(t[1])+"\n    "
                        else:
                            text += "Nothing:\n\tCAT: Nothing,\n\tTYPE: Nothing,\n\tPP: 0,\n\tACC: 0,\n\tBASEPOW: 0,\n\tDESC: Does nothing.\n\tPOP: 0\n    "
                    self.respond(text)

                    # Selecting Flop
                    flopMoveGate = False
                    while not flopMoveGate:
                        self.respond("Which move would you like to swap %s with?" % flipName)
                        inputEvent.wait()
                        inputEvent.clear()
                        flop = self.input_get
                        if flop in ["None", "none", "Null", "null"]:
                            placeholder = moves.index(flipName)
                            moves[placeholder] = None
                            allNone = [False, False, False, False]
                            for i in range(len(moves)):
                                if moves[i] == None:
                                    allNone[i] = True
                            if all(allNone):
                                self.respond("Oh dear, it seems that you just made a completely empty moveset! That's not allowed in Pokemon: each Pokemon must have at least ONE move")
                                moves[placeholder] = flipName
                            else:
                                flopMoveGate = True
                        else:
                            flopName = Pokedex.findMoveName(flop)
                            if flopName != None:
                                if Pokedex.findMoveID(flop) in MetaDex.findPokemonTierMoves(spName, self.tierfile):
                                    if flopName not in moves:
                                        if "Hidden Power" in flopName:
                                            self.respond("Oh, I see you want to add Hidden Power to your arsenal. That's fine, but we will then need to change your IV's then.")
                                            maxIVs = Pokedex.findTypeHPSpreads(flopName[13])["max all"][0]
                                            maxIVList = maxIVs.split("/")
                                            try:
                                                self.teamMatesDict[spName]["ivs"]["hp"] = int(maxIVList[0])
                                                self.teamMatesDict[spName]["ivs"]["atk"] = int(maxIVList[1])
                                                self.teamMatesDict[spName]["ivs"]["def"] = int(maxIVList[2])
                                                self.teamMatesDict[spName]["ivs"]["spa"] = int(maxIVList[3])
                                                self.teamMatesDict[spName]["ivs"]["spd"] = int(maxIVList[4])
                                                self.teamMatesDict[spName]["ivs"]["spe"] = int(maxIVList[5])
                                                moves[moves.index(flipName)] = flopName
                                                self.respond("I've set your IVs to be the maximum they can be and still compatible with %s.\nIf you don't like this selection, you can always change it later when you import your team into Pokemon Showdown." % flopName)
                                                flopMoveGate = True
                                            except:
                                                self.respond("An error has occurred with the data. Huh, how did that escape me? Don't worry, its not your fault, but this is unexpected and could potentially be serious.\nI'm going to exist this program. Please contact my programmer immediately.")
                                                sys.exit()
                                        else:
                                            moves[moves.index(flipName)] = flopName
                                            flopMoveGate = True
                                    else:
                                        self.respond("Oh, you already have %s as a move for your %s. Please select a different move." % (flopName, spName))
                                else:
                                    self.respond("Oh, there seems to be a problem. Either %s can't learn this move, or it is used SO rarely that I couldn't find any useful data. In any case, try a different move." % spName)
                            else:
                                self.respond("I'm sorry, but that is not a valid move. Try again")
            self.teamMatesDict[spName]["moves"]["move1"] = moves[0]
            self.teamMatesDict[spName]["moves"]["move2"] = moves[1]
            self.teamMatesDict[spName]["moves"]["move3"] = moves[2]
            self.teamMatesDict[spName]["moves"]["move4"] = moves[3]
            self.respond("Excellent! Your %s now has moves!" % spName)
            self.update(spName,"moves")

            # Selecting Items
            self.respond("Alright, it's time to look at items.")
            if len(MetaDex.findPokemonTierItems(spName, self.tierfile)) > 1:
                if "Fling" in [self.teamMatesDict[spName]["moves"]["move1"], self.teamMatesDict[spName]["moves"]["move2"],
                               self.teamMatesDict[spName]["moves"]["move3"], self.teamMatesDict[spName]["moves"]["move4"]]:
                    text=""
                    text+="Ah yes, your "+spName+" has the move Fling! Fling's power and effect depends on the user's item (the item is then used up). Here are a few interesting items and effects.\nFor the full list, check out Serebii: https://www.serebii.net/games/fling.shtml"
                    text+="\n    Iron Ball:\n\tFLING'S POWER: "+str(Pokedex.findItemFlingBasePower("iron ball"))+"\n\tFLING'S EFFECT: None"
                    text+="\n    Flame Orb:\n\tFLING'S POWER: "+str(Pokedex.findItemFlingBasePower("flame orb"))+"\n\tFLING'S EFFECT: Burns opponent"
                    text+="\n    Light Ball:\n\tFLING'S POWER: "+str(Pokedex.findItemFlingBasePower("light ball"))+"\n\tFLING'S EFFECT: Paralyses opponent"
                    text+="\n    Toxic Orb:\n\tFLING'S POWER: "+str(Pokedex.findItemFlingBasePower("toxic orb"))+"\n\tFLING'S EFFECT: Badly poisons opponent"
                    text+="\n    King's Rock:\n\tFLING'S POWER: "+str(Pokedex.findItemFlingBasePower("king's rock"))+"\n\tFLING'S EFFECT: Flinches opponent"
                    text+="\n    White Herb:\n\tFLING'S POWER: "+str(Pokedex.findItemFlingBasePower("white herb"))+self.cut("\n\tFLING'S EFFECT: Restores Stat Changes on opponent")
                    text+="\n    Lum Berry:\n\tFLING'S POWER: "+str(Pokedex.findItemFlingBasePower("lum berry"))+self.cut("\n\tFLING'S EFFECT: Opponent recovers from any status problem")
                    self.respond(text)

                if "Natural Gift" in [self.teamMatesDict[spName]["moves"]["move1"], self.teamMatesDict[spName]["moves"]["move2"],
                                      self.teamMatesDict[spName]["moves"]["move3"], self.teamMatesDict[spName]["moves"]["move4"]]:
                    text=""
                    text+="Ah yes, your "+spName+" has the move Natural Gift! Natural Gift's power and effect depends on the user's held berry (the berry is then used up). Here are a few interesting berries and effects.\nFor the full list, check out Serebii: https://www.serebii.net/games/naturalgift.shtml"
                    text+="\n    As a special note, the power that Natural Gift gets from each berry varies from generation to generation. I will be displaying data from the most recent generation."
                    text+="\n    Roseli Berry:\n\tNATURAL GIFT'S POWER: "+str(Pokedex.findItemNaturalGiftBasePower("roseliberry"))+"\n\tNATURAL GIFT'S TYPE: "+Pokedex.findItemNaturalGiftType("roseliberry")
                    text+="\n    Leppa Berry:\n\tNATURAL GIFT'S POWER: "+str(Pokedex.findItemNaturalGiftBasePower("leppaberry"))+"\n\tNATURAL GIFT'S TYPE: "+Pokedex.findItemNaturalGiftType("leppaberry")
                    text+="\n    Aguav Berry:\n\tNATURAL GIFT'S POWER: "+str(Pokedex.findItemNaturalGiftBasePower("aguavberry"))+"\n\tNATURAL GIFT'S TYPE: "+Pokedex.findItemNaturalGiftType("aguavberry")
                    text+="\n    Lum Berry:\n\tNATURAL GIFT'S POWER: "+str(Pokedex.findItemNaturalGiftBasePower("lumberry"))+"\n\tNATURAL GIFT'S Type: "+Pokedex.findItemNaturalGiftType("lumberry")
                    text+="\n    Watmel Berry:\n\tNATURAL GIFT'S POWER: "+str(Pokedex.findItemNaturalGiftBasePower("watmelberry"))+"\n\tNATURAL GIFT'S Type: "+Pokedex.findItemNaturalGiftType("watmelberry")
                    self.respond(text)

                self.respond("I'm going to show the most popular items. How many should I suggest? (Int)")
                itemAmountGate = False
                while not itemAmountGate:
                    try:
                        inputEvent.wait()
                        inputEvent.clear()
                        itemAmount = int(self.input_get)
                        itemAmountGate = True
                    except:
                        self.respond("Um...how can I show that many items? Try again")
                sortedItems = TeamBuilder.findPokemonMetaItems(spName, self.tierfile, itemAmount)
                text=""
                for s in sortedItems:
                    itemData=Pokedex.findItemData(s[0])
                    text+=itemData["name"]+":"+self.cut("\n\tDESC: "+itemData["desc"])+"\n\tPOP: "+str(s[1])+"\n    "
                self.respond(text)
                itemGate = False
                while not itemGate:
                    if "vgc" in self.tier or "battlespot" in self.tier:
                        self.respond(
                            "Which item would you like to give to %s? Note that for the team that you are building, no two Pokemon may hold the same item!" % spName)
                        inputEvent.wait()
                        inputEvent.clear()
                    else:
                        self.respond("Which item would you like to give to %s?" % spName)
                        inputEvent.wait()
                        inputEvent.clear()
                    itemName = Pokedex.findItemName(self.input_get)
                    if itemName != None:
                        if "vgc" in self.tier or "battlespot" in self.tier:
                            itemsList = []
                            for sp in self.teamMatesDict:
                                if self.teamMatesDict[sp]["item"] != None:
                                    itemsList.append(self.teamMatesDict[sp]["item"])
                            if itemName in itemsList:
                                self.respond(
                                    "Oh, it seems that one of your Pokemon already holds that item. You must therefore select another item for your %s.\nYou can change edit this later on when you import your team into Pokemon Showdown" % spName)
                            else:
                                self.teamMatesDict[spName]["item"] = itemName
                                itemGate = True
                        else:
                            self.teamMatesDict[spName]["item"] = itemName
                            itemGate = True
                    else:
                        self.respond("I'm sorry, but that's not a registered item. Did you maybe spell it wrong?")
            else:
                self.respond(
                    "Ah, I see that %s can only have one item. I'll automatically update your %s to hold that item." % (
                    spName, spName))
                self.teamMatesDict[spName]["item"] = Pokedex.findItemName(
                    list(MetaDex.findPokemonTierItems(spName, self.tierfile).keys())[0])
            self.respond("Excellent! Your %s is now holding a %s!" % (spName, self.teamMatesDict[spName]["item"]))
            self.update(spName,"item")

            self.respond("We are almost done with your %s. Just a few simple things to take care of." % spName)

            # Selecting Happiness
            self.respond("Alright, let's move on to Happiness.")
            moves = [self.teamMatesDict[spName]["moves"]["move1"], self.teamMatesDict[spName]["moves"]["move2"],
                     self.teamMatesDict[spName]["moves"]["move3"], self.teamMatesDict[spName]["moves"]["move4"]]
            if "Frustration" in moves and "Return" not in moves:
                self.respond("Ah, yes. One of your moves is Frustration. This move has it's highest power when happiness is 0. I'll do that automatically for you!")
                self.teamMatesDict[spName]["happiness"] = 0
            elif "Return" in moves and "Frustration" not in moves:
                self.respond("Ah, yes. One of your moves is Return.This move has it's highest power when happiness is maxed out. I'll do that automatically for you!")
                self.teamMatesDict[spName]["happiness"] = 255
            elif "Return" in moves and "Frustration" in moves:
                self.respond("Oh hold on, you have both Return and Frustration as moves for your %s.\nThis isn't necessary. Return and Frustration are basically the same move, except where one increases in power as happiness goes up, the other decreases in power. \nI'll set Happiness to it's max setting, as this is the default, making Return the strongest of the two.\nI can't change the moveset now, but later when you import this team into Pokemon Showdown, remove Frustration and replace it with another move, k?" % spName)
                self.teamMatesDict[spName]["happiness"] = 255
            else:
                self.respond("In your case, happiness does not affect your Pokemon at all. So I'll just set it to max, as this is it's default value.")
                self.teamMatesDict[spName]["happiness"] = 255
            self.update(spName,"happiness")

            # Selecting Level
            self.respond("Ok, almost there. Time to chose what level your %s should be at." % spName)
            if "vgc" in self.tier or "battlespot" in self.tier:
                self.respond("Remember, Pokemon in this team must be at level of 50 or under.")
                evoLevel = Pokedex.findPokemonEvoLevel(spName)
                if evoLevel != None and evoLevel < 50:
                    self.respond("Also, your %s evolves at level %s, so you must chose a level equal or greater than that" % (
                    spName, evoLevel))
                    self.respond("What level would like your Pokemon to be? (Int)")
                    levelGate = False
                    while not levelGate:
                        try:
                            inputEvent.wait()
                            inputEvent.clear()
                            if evoLevel < int(self.input_get) <= 50:
                                self.teamMatesDict[spName]["level"] = int(self.input_get)
                                levelGate = True
                            else:
                                self.respond("That's impossible to do, try again!")
                        except:
                            self.respond("Um...I don't understand that response...")
                elif evoLevel != None and evoLevel <= 50:
                    self.respond(
                        "Oh, it seems that this Pokemon can oly be level 50. Not to worry, I'll autmatically update that for you!")
                    self.teamMatesDict[spName]["level"] = 50
                    levelGate = True
                else:
                    self.respond("What level would like your Pokemon to be? (Int)")
                    levelGate = False
                    while not levelGate:
                        try:
                            inputEvent.wait()
                            inputEvent.clear()
                            if 0 < int(self.input_get) <= 50:
                                self.teamMatesDict[spName]["level"] = int(self.input_get)
                                levelGate = True
                            else:
                                self.respond("That's impossible to do, try again!")
                        except:
                            self.respond("Um...I don't understand that response...")
            else:
                evoLevel = Pokedex.findPokemonEvoLevel(spName)
                if evoLevel != None:
                    self.respond(
                        "Remember, your %s evolves at level %s, so you must chose a level equal or greater than that" % (
                        spName, evoLevel))
                    self.respond("What level would like your Pokemon to be?")
                    levelGate = False
                    while not levelGate:
                        try:
                            inputEvent.wait()
                            inputEvent.clear()
                            if evoLevel <= int(self.input_get) <= 100:
                                self.teamMatesDict[spName]["level"] = int(self.input_get)
                                levelGate = True
                            else:
                                self.respond("That's impossible to do, try again")
                        except:
                            self.respond("Um...I don't understand that response...")
                else:
                    self.respond("What level would like your Pokemon to be? (Int)")
                    levelGate = False
                    while not levelGate:
                        try:
                            inputEvent.wait()
                            inputEvent.clear()
                            if 0 <= int(self.input_get) <= 100:
                                self.teamMatesDict[spName]["level"] = int(self.input_get)
                                levelGate = True
                            else:
                                self.respond("That's impossible to do, try again")
                        except:
                            self.respond("Um...I don't understand that response...")
            self.respond("Excellent! Your %s is now at Level %s" % (spName, self.teamMatesDict[spName]["level"]))
            self.update(spName,"level")

            # Selecting Shininess
            self.respond("And last but probably the most important, shininess!")
            shinyGate = False
            while not shinyGate:
                if spName not in ["Celebi", "Victini", "Keldeo", "Meloetta", "Meloetta-Pirouette", "Zygarde", "Hoopa",
                                  "Hoopa-Unbound", "Volcanion", "Tapu Koko", "Tapu Fini", "Tapu Bulu", "Tapu Lele",
                                  "Cosmog", "Cosmoem", "Solgaleo", "Lunala", "Nihilego", "Buzzwole", "Pheromosa",
                                  "Xurkitree", "Celesteela", "Kartana", "Guzzlord", "Necrozma", "Magearna",
                                  "Marshadow"]:
                    self.respond("Do you want %s to be shiny? (Y/N)" % spName)
                    inputEvent.wait()
                    inputEvent.clear()
                    if self.input_get in self.yes:
                        self.teamMatesDict[spName]["shiny"] = "Yes"
                        shinyGate = True
                    elif self.input_get in self.no:
                        self.teamMatesDict[spName]["shiny"] = "No"
                        shinyGate = True
                    else:
                        self.respond("Um...I don't understand that response...")
                else:
                    self.respond("I see that your %s can not be legally shiny. Maybe one day..." % spName)
                    self.teamMatesDict[spName]["shiny"] = "No"
                    shinyGate = True
            self.update(spName,"shiny")

            if self.teamMateNames.index(spName)<5:
                finalGate=False
                while not finalGate:
                    self.respond("Alright, this Pokemon is done! Type 'Next' when you are ready to move on to the next member of your team.")
                    inputEvent.wait()
                    inputEvent.clear()
                    if self.input_get in ["Next","next","NEXT"]:
                        finalGate = True
            else:
                self.respond("And we are done! You have just successfulling made your very own competitive Pokemon team!")
                doneGate=False
                while not doneGate:
                    self.respond("When you are completely done, type 'Done' so I can export your team.")
                    inputEvent.wait()
                    inputEvent.clear()
                    if self.input_get in ["Done","done","DONE"]:
                        self.export()
                        doneGate=True

    def __init__(self,root):

        #Team Builder Window Setup
        root.title("Team Builder")
        self.width = 1000
        self.height = 600
        root.geometry(str(self.width)+"x"+str(self.height))

        #Text Frame Setup
        textframe = Frame(root, width=int(self.width / 2), height=self.height)
        borderwidth = 10
        textframe.config(relief=RAISED,borderwidth = borderwidth)
        textframe.pack(side=RIGHT,fill=Y)

        #Input Field and Messages Setup
        input_user = StringVar()
        input_field = Entry(textframe, text=input_user)
        input_field.place(x=0,y=textframe.winfo_reqheight()-input_field.winfo_reqheight()-2*borderwidth,width=int(self.width/2)-2*borderwidth)
        input_user.set("")
        self.messages = Text(textframe,wrap=WORD)
        self.messages.place(x=0,y=0,width=textframe.winfo_reqwidth()-2*borderwidth-17,height=self.height-2*borderwidth-input_field.winfo_reqheight())
        self.messages.config(state=DISABLED)
        scrollbar = Scrollbar(textframe,command=self.messages.yview)
        scrollbar.place(x=int(textframe.winfo_reqwidth()-2*borderwidth-17),y=0,height=560)
        self.messages["yscrollcommand"]=scrollbar.set
        def Enter_pressed(event):
            self.input_get = input_field.get()
            inputEvent.set()
            self.messages.config(state=NORMAL)
            self.messages.insert(END, 'You: %s\n\n' % self.input_get)
            self.messages.see(END)
            #self.messages.edit_modified(0)
            self.messages.config(state=DISABLED)
            input_user.set("")
            if inputEvent.is_set():
                inputEvent.clear()
            #return "break"
        input_field.bind("<Return>", Enter_pressed)

        self.teamMatesDict = {}
        self.current = {}
        self.current["species"] = None
        self.current["ability"] = None
        self.current["nature"] = None
        self.current["baseStats"] = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0}
        self.current["ivs"] = {"hp": 31, "atk": 31, "def": 31, "spa": 31, "spd": 31, "spe": 31}
        self.current["evs"] = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0}
        self.current["item"] = None
        self.current["gender"] = None
        self.current["moves"] = {"move1": None, "move2": None, "move3": None, "move4": None}
        self.current["happiness"] = None
        self.current["level"] = 100
        self.current["shiny"] = None

        #Team Frame Setup
        teamframe = Frame(root, width=int(self.width / 2), height=self.height)
        teamframe.config(relief=RAISED, borderwidth=borderwidth)
        teamframe.pack(side=LEFT, fill=Y)

        #Make Images
        self.spriteCanvas=Canvas(teamframe,width=80,height=80)
        self.spriteCanvas.config(relief=RAISED,borderwidth=1)
        self.spriteCanvas.place(x=9,y=9)

        # Individual Team Member Species Label
        speciesTitleLabel = Label(teamframe,text="Species:",anchor=W)
        speciesTitleLabel.place(x=100,y=0,width=50)
        self.speciesLabelText = StringVar()
        self.speciesLabelText.set(self.current["species"])
        speciesLabel = Label(teamframe, textvariable=self.speciesLabelText, anchor=W)
        speciesLabel.place(x=150, y=0, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2-50))
        # Individual Team Member Type Label
        typeTitleLabel = Label(teamframe, text="Types:", anchor=W)
        typeTitleLabel.place(x=100, y=25, width=50)
        self.typeLabelText = StringVar()
        if self.current["species"]!=None:
            types = Pokedex.findPokemonTypes(self.current["species"])
            if len(types)==2:
                self.typeLabelText.set(types[0]+", "+types[1])
            else:
                self.typeLabelText.set(types[0])
        else:
            self.typeLabelText.set("None, None")
        typeLabel = Label(teamframe, textvariable=self.typeLabelText, anchor=W)
        typeLabel.place(x=150, y=25, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2-50))
        #Individual Team Member Ability Label
        abilityTitleLabel = Label(teamframe, text="Ability:", anchor=W)
        abilityTitleLabel.place(x=100, y=50, width=50)
        self.abilityLabelText = StringVar()
        self.abilityLabelText.set(self.current["ability"])
        abilityLabel = Label(teamframe,textvariable=self.abilityLabelText,anchor=W)
        abilityLabel.place(x=150, y=50, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2-50))
        #Individual Team Member Item Label
        itemLabel = Label(teamframe, text="Item:", anchor=W)
        itemLabel.place(x=100, y=75, width=50)
        self.itemLabelText = StringVar()
        self.itemLabelText.set(self.current["item"])
        itemLabel = Label(teamframe, textvariable=self.itemLabelText,anchor=W)
        itemLabel.place(x=150, y=75, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2-50))
        #Individual Team Member Level Label
        levelTitleLabel = Label(teamframe, text="Level:", anchor=W)
        levelTitleLabel.place(x=100 + int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2), y=0,width=65)
        self.levelLabelText = StringVar()
        self.levelLabelText.set(str(self.current["level"]))
        levelLabel = Label(teamframe, textvariable=self.levelLabelText,anchor=W)
        levelLabel.place(x=165+int((teamframe.winfo_reqwidth()-2*borderwidth-100)/2), y=0, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2-65))
        # Individual Team Member Gender Label
        genderTitleLabel = Label(teamframe, text="Gender:", anchor=W)
        genderTitleLabel.place(x=100 + int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2), y=25, width=65)
        self.genderLabelText = StringVar()
        self.genderLabelText.set(str(self.current["gender"]))
        genderLabel = Label(teamframe, textvariable=self.genderLabelText, anchor=W)
        genderLabel.place(x=165 + int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2), y=25,width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2 - 65))
        #Individual Team Member Happiness Label
        happinessTitleLabel = Label(teamframe, text="Happiness:", anchor=W)
        happinessTitleLabel.place(x=100 + int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2), y=50,width=65)
        self.happinessLabelText = StringVar()
        self.happinessLabelText.set(str(self.current["happiness"]))
        happinessLabel = Label(teamframe, textvariable=self.happinessLabelText,anchor=W)
        happinessLabel.place(x=165+int((teamframe.winfo_reqwidth()-2*borderwidth-100)/2), y=50, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2-65))
        #Individual Team Member Shiny Label
        shinyTitleLabel = Label(teamframe, text="Shiny:",anchor=W)
        shinyTitleLabel.place(x=100+int((teamframe.winfo_reqwidth()-2*borderwidth-100)/2), y=75, width=65)
        self.shinyLabelText = StringVar()
        self.shinyLabelText.set(self.current["shiny"])
        shinyLabel = Label(teamframe, textvariable=self.shinyLabelText,anchor=W)
        shinyLabel.place(x=165+int((teamframe.winfo_reqwidth()-2*borderwidth-100)/2), y=75, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2-65))

        #Separator 1
        separator1 = ttk.Separator(teamframe,orient=HORIZONTAL)
        separator1.place(x=10,y=100,width = teamframe.winfo_reqwidth()-2*borderwidth-20)

        #Stats Titles
        hpTitleLabel = Label(teamframe,text="HP",anchor = W)
        hpTitleLabel.place(x=10,y=131,width=int((teamframe.winfo_reqwidth()-2*borderwidth-40)/10))
        atkTitleLabel = Label(teamframe, text="Atk",anchor = W)
        atkTitleLabel.place(x=10, y=157, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 40) / 10))
        defTitleLabel = Label(teamframe, text="Def",anchor = W)
        defTitleLabel.place(x=10, y=183, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 40) / 10))
        spaTitleLabel = Label(teamframe, text="SpA",anchor = W)
        spaTitleLabel.place(x=10, y=209, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 40) / 10))
        spdTitleLabel = Label(teamframe, text="SpD",anchor = W)
        spdTitleLabel.place(x=10, y=235, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 40) / 10))
        speTitleLabel = Label(teamframe, text="Spe",anchor = W)
        speTitleLabel.place(x=10, y=261, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 40) / 10))

        #Sub Separator 1_1
        subsep1_1 = ttk.Separator(teamframe,orient=VERTICAL)
        subsep1_1.place(x=42,y=110,height=172)

        #Base Stats Label
        baseStatsLabel = Label(teamframe,text="Base Stats")
        baseStatsLabel.place(x=52,y=110,width=50)
        #HP Base Stat
        self.hpBS = StringVar()
        self.hpBS.set(str(self.current["baseStats"]["hp"]))
        self.hpBSLabel = Label(teamframe, textvariable=self.hpBS)
        self.hpBSLabel.place(x=52, y=131, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 40) / 10))
        #Atk Base Stat
        self.atkBS = StringVar()
        self.atkBS.set(str(self.current["baseStats"]["atk"]))
        self.atkBSLabel = Label(teamframe, textvariable=self.atkBS)
        self.atkBSLabel.place(x=52, y=157, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 40) / 10))
        #Def Base Stat
        self.defBS = StringVar()
        self.defBS.set(str(self.current["baseStats"]["def"]))
        self.defBSLabel = Label(teamframe, textvariable=self.defBS)
        self.defBSLabel.place(x=52, y=183, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 40) / 10))
        #SpA Base Stat
        self.spaBS = StringVar()
        self.spaBS.set(str(self.current["baseStats"]["spa"]))
        self.spaBSLabel = Label(teamframe, textvariable=self.spaBS)
        self.spaBSLabel.place(x=52, y=209, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 40) / 10))
        #SpD Base Stat
        self.spdBS = StringVar()
        self.spdBS.set(str(self.current["baseStats"]["spd"]))
        self.spdBSLabel = Label(teamframe, textvariable=self.spdBS)
        self.spdBSLabel.place(x=52, y=235, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 40) / 10))
        #Spe Base Stat
        self.speBS = StringVar()
        self.speBS.set(str(self.current["baseStats"]["spe"]))
        self.speBSLabel = Label(teamframe, textvariable=self.speBS)
        self.speBSLabel.place(x=52, y=261, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 40) / 10))

        #Sub Separator 1_2
        subsep1_2 = ttk.Separator(teamframe, orient=VERTICAL)
        subsep1_2.place(x=115, y=110, height=172)

        #IVs Label
        ivsLabel = Label(teamframe, text="IVs")
        ivsLabel.place(x=125, y=110, width=25)
        #HP IVs
        self.hpIV = StringVar()
        self.hpIV.set(str(self.current["ivs"]["hp"]))
        self.hpIVLabel = Label(teamframe, textvariable=self.hpIV)
        self.hpIVLabel.place(x=125, y=131, width=25)
        #Atk IVs
        self.atkIV = StringVar()
        self.atkIV.set(str(self.current["ivs"]["atk"]))
        self.atkIVLabel = Label(teamframe, textvariable=self.atkIV)
        self.atkIVLabel.place(x=125, y=157, width=25)
        #Def IVs
        self.defIV = StringVar()
        self.defIV.set(str(self.current["ivs"]["def"]))
        self.defIVLabel = Label(teamframe, textvariable=self.defIV)
        self.defIVLabel.place(x=125, y=183, width=25)
        #SpA IVs
        self.spaIV = StringVar()
        self.spaIV.set(str(self.current["ivs"]["spa"]))
        self.spaIVLabel = Label(teamframe, textvariable=self.spaIV)
        self.spaIVLabel.place(x=125, y=209, width=25)
        #SpD IVs
        self.spdIV = StringVar()
        self.spdIV.set(str(self.current["ivs"]["spd"]))
        self.spdIVLabel = Label(teamframe, textvariable=self.spdIV)
        self.spdIVLabel.place(x=125, y=235, width=25)
        #Spe IVs
        self.speIV = StringVar()
        self.speIV.set(str(self.current["ivs"]["spe"]))
        self.speIVLabel = Label(teamframe, textvariable=self.speIV)
        self.speIVLabel.place(x=125, y=261, width=25)

        #Sub Separator 1_3
        subsep1_3 = ttk.Separator(teamframe, orient=VERTICAL)
        subsep1_3.place(x=160, y=110, height=172)

        #EVs Label
        evsLabel = Label(teamframe, text="EVs")
        evsLabel.place(x=170, y=110, width=25)
        #HP EVs
        self.hpEV = StringVar()
        self.hpEV.set(str(self.current["evs"]["hp"]))
        self.hpEVLabel = Label(teamframe, textvariable=self.hpEV)
        self.hpEVLabel.place(x=170, y=131, width=25)
        #Atk EVs
        self.atkEV = StringVar()
        self.atkEV.set(str(self.current["evs"]["atk"]))
        self.atkEVLabel = Label(teamframe, textvariable=self.atkEV)
        self.atkEVLabel.place(x=170, y=157, width=25)
        #Def EVs
        self.defEV = StringVar()
        self.defEV.set(str(self.current["evs"]["def"]))
        self.defEVLabel = Label(teamframe, textvariable=self.defEV)
        self.defEVLabel.place(x=170, y=183, width=25)
        #SpA EVs
        self.spaEV = StringVar()
        self.spaEV.set(str(self.current["evs"]["spa"]))
        self.spaEVLabel = Label(teamframe, textvariable=self.spaEV)
        self.spaEVLabel.place(x=170, y=209, width=25)
        #SpD EVs
        self.spdEV = StringVar()
        self.spdEV.set(str(self.current["evs"]["spd"]))
        self.spdEVLabel = Label(teamframe, textvariable=self.spdEV)
        self.spdEVLabel.place(x=170, y=235, width=25)
        #Spe EVs
        self.speEV = StringVar()
        self.speEV.set(str(self.current["evs"]["spe"]))
        self.speEVLabel = Label(teamframe, textvariable=self.speEV)
        self.speEVLabel.place(x=170, y=261, width=25)

        #Sub Separator 1_4
        subsep1_4 = ttk.Separator(teamframe, orient=VERTICAL)
        subsep1_4.place(x=205, y=110, height=172)

        #HP Bar
        self.hpStatCanvas = Canvas(teamframe, width = 178)
        if self.current["species"]!=None:
            self.hpStatBar=self.hpStatCanvas.create_rectangle(0,5,int(self.hpStatCalc(self.current["baseStats"]["hp"],self.current["evs"]["hp"],self.current["ivs"]["hp"],self.current["level"])/4),16,fill="lawn green")
        else:
            self.hpStatBar = self.hpStatCanvas.create_rectangle(0, 5, 0, 16, fill="lawn green")
        self.hpStatCanvas.place(x=215, y=131)
        #Atk Bar
        self.atkStatCanvas = Canvas(teamframe,width = 178)
        if self.current["species"] != None:
            self.atkStatBar=self.atkStatCanvas.create_rectangle(0, 5, int(self.atkStatCalc(self.current["baseStats"]["atk"],self.current["evs"]["atk"],self.current["ivs"]["atk"],self.current["level"],self.current["nature"])/4), 16)
            self.atkStatCanvas.itemconfig(self.atkStatBar,fill=self.atkNatureColor(self.current["nature"]))
        else:
            self.atkStatBar = self.atkStatCanvas.create_rectangle(0, 5, 0, 16, fill="lawn green")
        self.atkStatCanvas.place(x=215, y=157)
        #Def Bar
        self.defStatCanvas = Canvas(teamframe,width = 178)
        if self.current["species"] != None:
            self.defStatBar=self.defStatCanvas.create_rectangle(0, 5, int(self.defStatCalc(self.current["baseStats"]["def"],self.current["evs"]["def"],self.current["ivs"]["def"],self.current["level"],self.current["nature"])/4), 16)
            self.defStatCanvas.itemconfig(self.defStatBar, fill=self.defNatureColor(self.current["nature"]))
        else:
            self.defStatBar = self.defStatCanvas.create_rectangle(0, 5, 0, 16, fill="lawn green")
        self.defStatCanvas.place(x=215, y=183)
        #SpA Bar
        self.spaStatCanvas = Canvas(teamframe,width = 178)
        if self.current["species"] != None:
            self.spaStatBar=self.spaStatCanvas.create_rectangle(0, 5, int(self.spaStatCalc(self.current["baseStats"]["spa"],self.current["evs"]["spa"],self.current["ivs"]["spa"],self.current["level"],self.current["nature"])/4), 16)
            self.spaStatCanvas.itemconfig(self.spaStatBar, fill=self.spaNatureColor(self.current["nature"]))
        else:
            self.spaStatBar = self.spaStatCanvas.create_rectangle(0, 5, 0, 16, fill="lawn green")
        self.spaStatCanvas.place(x=215, y=209)
        #SpD Bar
        self.spdStatCanvas = Canvas(teamframe,width = 178)
        if self.current["species"] != None:
            self.spdStatBar=self.spdStatCanvas.create_rectangle(0, 5, int(self.spdStatCalc(self.current["baseStats"]["spd"],self.current["evs"]["spd"],self.current["ivs"]["spd"],self.current["level"],self.current["nature"])/4), 16)
            self.spdStatCanvas.itemconfig(self.spdStatBar, fill=self.spdNatureColor(self.current["nature"]))
        else:
            self.spdStatBar = self.spdStatCanvas.create_rectangle(0, 5, 0, 16, fill="lawn green")
        self.spdStatCanvas.place(x=215, y=235)
        #Spe Bar
        self.speStatCanvas = Canvas(teamframe,width = 178)
        if self.current["species"] != None:
            self.speStatBar=self.speStatCanvas.create_rectangle(0, 5, int(self.speStatCalc(self.current["baseStats"]["spe"],self.current["evs"]["spe"],self.current["ivs"]["spe"],self.current["level"],self.current["nature"])/4), 16)
            self.speStatCanvas.itemconfig(self.speStatBar, fill=self.speNatureColor(self.current["nature"]))
        else:
            self.speStatBar = self.speStatCanvas.create_rectangle(0, 5, 0, 16, fill="lawn green")
        self.speStatCanvas.place(x=215, y=261)

        #Sub Separator 1_5
        subsep1_5 = ttk.Separator(teamframe, orient=VERTICAL)
        subsep1_5.place(x=403, y=110, height=172)

        #Total Stats Label
        totalLabel = Label(teamframe, text="Total")
        totalLabel.place(x=413, y=110, width=25)
        #HP Total
        self.hpTotal = StringVar()
        if self.current["species"]:
            self.hpTotal.set(str(self.hpStatCalc(self.current["baseStats"]["hp"],self.current["evs"]["hp"],self.current["ivs"]["hp"],self.current["level"])))
        else:
            self.hpTotal.set(str(0))
        self.hpTotalLabel = Label(teamframe, textvariable=self.hpTotal)
        self.hpTotalLabel.place(x=413, y=131, width=25)
        #Atk Total
        self.atkTotal = StringVar()
        if self.current["species"]:
            self.atkTotal.set(str(self.atkStatCalc(self.current["baseStats"]["atk"],self.current["evs"]["atk"],self.current["ivs"]["atk"],self.current["level"],self.current["nature"])))
        else:
            self.atkTotal.set(str(0))
        self.atkTotalLabel = Label(teamframe, textvariable=self.atkTotal)
        self.atkTotalLabel.place(x=413, y=157, width=25)
        #Def Total
        self.defTotal = StringVar()
        if self.current["species"]:
            self.defTotal.set(str(self.defStatCalc(self.current["baseStats"]["def"],self.current["evs"]["def"],self.current["ivs"]["def"],self.current["level"],self.current["nature"])))
        else:
            self.defTotal.set(str(0))
        self.defTotalLabel = Label(teamframe, textvariable=self.defTotal)
        self.defTotalLabel.place(x=413, y=183, width=25)
        #SpA Total
        self.spaTotal = StringVar()
        if self.current["species"]:
            self.spaTotal.set(str(self.spaStatCalc(self.current["baseStats"]["spa"],self.current["evs"]["spa"],self.current["ivs"]["spa"],self.current["level"],self.current["nature"])))
        else:
            self.spaTotal.set(str(0))
        self.spaTotalLabel = Label(teamframe, textvariable=self.spaTotal)
        self.spaTotalLabel.place(x=413, y=209, width=25)
        #SpD Total
        self.spdTotal = StringVar()
        if self.current["species"]:
            self.spdTotal.set(str(self.spdStatCalc(self.current["baseStats"]["spd"],self.current["evs"]["spd"],self.current["ivs"]["spd"],self.current["level"],self.current["nature"])))
        else:
            self.spdTotal.set(str(0))
        self.spdTotalLabel = Label(teamframe, textvariable=self.spdTotal)
        self.spdTotalLabel.place(x=413, y=235, width=25)
        #Spe Total
        self.speTotal = StringVar()
        if self.current["species"]:
            self.speTotal.set(str(self.speStatCalc(self.current["baseStats"]["spe"],self.current["evs"]["spe"],self.current["ivs"]["spe"],self.current["level"],self.current["nature"])))
        else:
            self.speTotal.set(str(0))
        self.speTotalLabel = Label(teamframe, textvariable=self.speTotal)
        self.speTotalLabel.place(x=413, y=261, width=25)

        #Separator 2
        separator2 = ttk.Separator(teamframe, orient=HORIZONTAL)
        separator2.place(x=10, y=297, width=teamframe.winfo_reqwidth() - 2 * borderwidth - 20)

        #Move 1 Name
        self.move1Name = StringVar()
        self.move1Name.set(self.current["moves"]["move1"])
        move1Data = Pokedex.findMoveData(self.current["moves"]["move1"])
        self.move1NameLabel = Label(teamframe,textvariable=self.move1Name,anchor=W,width=21)
        self.move1NameLabel.place(x=10,y=338)
        # Move 2 Name
        self.move2Name = StringVar()
        self.move2Name.set(self.current["moves"]["move2"])
        move2Data = Pokedex.findMoveData(self.current["moves"]["move2"])
        self.move2NameLabel = Label(teamframe, textvariable=self.move2Name, anchor=W, width=21)
        self.move2NameLabel.place(x=10, y=364)
        # Move 3 Name
        self.move3Name = StringVar()
        self.move3Name.set(self.current["moves"]["move3"])
        move3Data = Pokedex.findMoveData(self.current["moves"]["move3"])
        self.move3NameLabel = Label(teamframe, textvariable=self.move3Name, anchor=W, width=21)
        self.move3NameLabel.place(x=10, y=390)
        # Move 4 Name
        self.move4Name = StringVar()
        self.move4Name.set(self.current["moves"]["move4"])
        move4Data = Pokedex.findMoveData(self.current["moves"]["move4"])
        self.move4NameLabel = Label(teamframe, textvariable=self.move4Name, anchor=W, width=21)
        self.move4NameLabel.place(x=10, y=416)

        #Sub Separator 2_1
        subsep2_1 = ttk.Separator(teamframe, orient=VERTICAL)
        subsep2_1.place(x=140, y=317, height=125)

        #Move Category Label
        moveCatLabel = Label(teamframe,text="Category")
        moveCatLabel.place(x=150,y=317,width=50)
        # Move 1 Category
        self.move1Cat = StringVar()
        if move1Data != None:
            self.move1Cat.set(move1Data["category"])
        else:
            self.move1Cat.set("N/A")
        self.move1CatLabel = Label(teamframe, textvariable=self.move1Cat)
        self.move1CatLabel.place(x=150, y=338,width=50)
        # Move 2 Category
        self.move2Cat = StringVar()
        if move2Data != None:
            self.move2Cat.set(move2Data["category"])
        else:
            self.move2Cat.set("N/A")
        self.move2CatLabel = Label(teamframe, textvariable=self.move2Cat)
        self.move2CatLabel.place(x=150, y=364,width=50)
        # Move 3 Category
        self.move3Cat = StringVar()
        if move3Data != None:
            self.move3Cat.set(move3Data["category"])
        else:
            self.move3Cat.set("N/A")
        self.move3CatLabel = Label(teamframe, textvariable=self.move3Cat)
        self.move3CatLabel.place(x=150, y=390,width=50)
        # Move 4 Category
        self.move4Cat = StringVar()
        if move4Data != None:
            self.move4Cat.set(move4Data["category"])
        else:
            self.move4Cat.set("N/A")
        self.move4CatLabel = Label(teamframe, textvariable=self.move4Cat)
        self.move4CatLabel.place(x=150, y=416, width=50)

        #Sub Separator 2_2
        subsep2_2 = ttk.Separator(teamframe, orient=VERTICAL)
        subsep2_2.place(x=210, y=317, height=125)

        #Move Type Label
        moveTypeLabel = Label(teamframe, text="Type")
        moveTypeLabel.place(x=220, y=317, width=45)
        # Move 1 Type
        self.move1Type = StringVar()
        if move1Data != None:
            self.move1Type.set(move1Data["type"])
        else:
            self.move1Type.set("N/A")
        self.move1TypeLabel = Label(teamframe, textvariable=self.move1Type)
        self.move1TypeLabel.place(x=220, y=338, width=45)
        # Move 2 Type
        self.move2Type = StringVar()
        if move2Data != None:
            self.move2Type.set(move2Data["type"])
        else:
            self.move2Type.set("N/A")
        self.move2TypeLabel = Label(teamframe, textvariable=self.move2Type)
        self.move2TypeLabel.place(x=220, y=364, width=45)
        # Move 3 Type
        self.move3Type = StringVar()
        if move3Data != None:
            self.move3Type.set(move3Data["type"])
        else:
            self.move3Type.set("N/A")
        self.move3TypeLabel = Label(teamframe, textvariable=self.move3Type)
        self.move3TypeLabel.place(x=220, y=390, width=45)
        # Move 4 Type
        self.move4Type = StringVar()
        if move4Data != None:
            self.move4Type.set(move4Data["type"])
        else:
            self.move4Type.set("N/A")
        self.move4TypeLabel = Label(teamframe, textvariable=self.move4Type)
        self.move4TypeLabel.place(x=220, y=416, width=45)

        #Sub Separator 2_3
        subsep2_3 = ttk.Separator(teamframe, orient=VERTICAL)
        subsep2_3.place(x=275, y=317, height=125)

        #Move Base Power Label
        moveBasePowerLabel = Label(teamframe, text="Base Power")
        moveBasePowerLabel.place(x=285, y=317, width=60)
        # Move 1 Base Power
        self.move1BasePower = StringVar()
        if move1Data != None:
            self.move1BasePower.set(str(move1Data["basePower"]))
        else:
            self.move1BasePower.set("N/A")
        self.move1BasePowerLabel = Label(teamframe, textvariable=self.move1BasePower)
        self.move1BasePowerLabel.place(x=285, y=338, width=60)
        # Move 2 Base Power
        self.move2BasePower = StringVar()
        if move2Data != None:
            self.move2BasePower.set(str(move2Data["basePower"]))
        else:
            self.move2BasePower.set("N/A")
        self.move2BasePowerLabel = Label(teamframe, textvariable=self.move2BasePower)
        self.move2BasePowerLabel.place(x=285, y=364, width=60)
        # Move 3 Base Power
        self.move3BasePower = StringVar()
        if move3Data != None:
            self.move3BasePower.set(str(move3Data["basePower"]))
        else:
            self.move3BasePower.set("N/A")
        self.move3BasePowerLabel = Label(teamframe, textvariable=self.move3BasePower)
        self.move3BasePowerLabel.place(x=285, y=390, width=60)
        # Move 4 Base Power
        self.move4BasePower = StringVar()
        if move4Data != None:
            self.move4BasePower.set(str(move4Data["basePower"]))
        else:
            self.move4BasePower.set("N/A")
        self.move4BasePowerLabel = Label(teamframe, textvariable=self.move4BasePower)
        self.move4BasePowerLabel.place(x=285, y=416, width=60)

        # Sub Separator 2_4
        subsep2_4 = ttk.Separator(teamframe, orient=VERTICAL)
        subsep2_4.place(x=355, y=317, height=125)

        # Move PP Label
        movePPLabel = Label(teamframe, text="PP")
        movePPLabel.place(x=365, y=317, width=25)
        # Move 1 PP
        self.move1PP = StringVar()
        if move1Data != None:
            self.move1PP.set(str(move1Data["pp"]))
        else:
            self.move1PP.set("N/A")
        self.move1PPLabel = Label(teamframe, textvariable=self.move1PP)
        self.move1PPLabel.place(x=365, y=338, width=25)
        # Move 2 PP
        self.move2PP = StringVar()
        if move2Data != None:
            self.move2PP.set(str(move2Data["pp"]))
        else:
            self.move2PP.set("N/A")
        self.move2PPLabel = Label(teamframe, textvariable=self.move2PP)
        self.move2PPLabel.place(x=365, y=364, width=25)
        # Move 3 PP
        self.move3PP = StringVar()
        if move3Data != None:
            self.move3PP.set(str(move3Data["pp"]))
        else:
            self.move3PP.set("N/A")
        self.move3PPLabel = Label(teamframe, textvariable=self.move3PP)
        self.move3PPLabel.place(x=365, y=390, width=25)
        # Move 4 PP
        self.move4PP = StringVar()
        if move4Data != None:
            self.move4PP.set(str(move4Data["pp"]))
        else:
            self.move4PP.set("N/A")
        self.move4PPLabel = Label(teamframe, textvariable=self.move4PP)
        self.move4PPLabel.place(x=365, y=416, width=25)

        # Sub Separator 2_5
        subsep2_5 = ttk.Separator(teamframe, orient=VERTICAL)
        subsep2_5.place(x=400, y=317, height=125)

        # Move Accuracy Label
        moveAccLabel = Label(teamframe, text="Accuracy")
        moveAccLabel.place(x=410, y=317, width=60)
        # Move 1 Accuracy
        self.move1Acc = StringVar()
        if move1Data != None:
            if move1Data["accuracy"]!= True:
                self.move1Acc.set(str(move1Data["accuracy"])+"%")
            else:
                self.move1Acc.set("100%")
        else:
            self.move1Acc.set("N/A")
        self.move1AccLabel = Label(teamframe, textvariable=self.move1Acc)
        self.move1AccLabel.place(x=410, y=338, width=60)
        # Move 2 Accuracy
        self.move2Acc = StringVar()
        if move2Data != None:
            if move2Data["accuracy"] != True:
                self.move2Acc.set(str(move2Data["accuracy"])+"%")
            else:
                self.move2Acc.set("100%")
        else:
            self.move2Acc.set("N/A")
        self.move2AccLabel = Label(teamframe, textvariable=self.move2Acc)
        self.move2AccLabel.place(x=410, y=364, width=60)
        # Move 3 Accuracy
        self.move3Acc = StringVar()
        if move3Data != None:
            if move3Data["accuracy"] != True:
                self.move3Acc.set(str(move3Data["accuracy"])+"%")
            else:
                self.move3Acc.set("100%")
        else:
            self.move3Acc.set("N/A")
        self.move3AccLabel = Label(teamframe, textvariable=self.move3Acc)
        self.move3AccLabel.place(x=410, y=390, width=60)
        # Move 4 Accuracy
        self.move4Acc = StringVar()
        if move4Data != None:
            if move4Data["accuracy"] != True:
                self.move4Acc.set(str(move4Data["accuracy"])+"%")
            else:
                self.move4Acc.set("100%")
        else:
            self.move4Acc.set("N/A")
        self.move4AccLabel = Label(teamframe, textvariable=self.move4Acc)
        self.move4AccLabel.place(x=410, y=416, width=60)

        #Menu Setup
        self.the_menu = Menu(root)
        file_menu = Menu(self.the_menu,tearoff=0)
        file_menu.add_command(label="Team Analyzer",command=self.showAnalyzer)
        file_menu.add_command(label="Quit",command=root.quit)
        self.the_menu.add_cascade(label="File",menu=file_menu)

        root.config(menu=self.the_menu)

        inputEvent = threading.Event()
        self.aiThrd = threading.Thread(target=self.AI, args=(inputEvent,))
        self.aiThrd.setDaemon(True)
        self.aiThrd.start()

root = Tk()
root.resizable(width=False,height=False)
AL(root)
root.mainloop()
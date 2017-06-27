from tkinter import *
from tkinter import ttk
import math,Pokedex,Tools,threading,os,glob,GUIScript, TeamAnalyzer
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
        #return "break"

    def showAnalyzer(self):
        #toplevel=Toplevel()
        #self.analyzer = TeamAnalyzer.TeamAnalyzer(self,toplevel)
        pass
    
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

    def update(self,name,option):
        if option=="types":
            self.analyzer.update(self, "species")
            #self.toplevel.deiconify()
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
            self.analyzer.update(self, "stats")
            self.analyzer.update(self, "physpec Offense")
            self.analyzer.update(self, "physpec Defense")
            self.toplevel.deiconify
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
            self.analyzer.update(self, "stats")
            self.analyzer.update(self, "physpec Offense")
            self.analyzer.update(self, "physpec Defense")
            #self.toplevel.deiconify()
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
            self.analyzer.update(self, "stats")
            self.analyzer.update(self, "physpec Offense")
            self.analyzer.update(self, "physpec Defense")
            #self.toplevel.deiconify()
            self.atkStatCanvas.itemconfig(self.atkStatBar, fill=self.atkNatureColor(self.current["nature"]))
            self.defStatCanvas.itemconfig(self.defStatBar, fill=self.defNatureColor(self.current["nature"]))
            self.spaStatCanvas.itemconfig(self.spaStatBar, fill=self.spaNatureColor(self.current["nature"]))
            self.spdStatCanvas.itemconfig(self.spdStatBar, fill=self.spdNatureColor(self.current["nature"]))
            self.speStatCanvas.itemconfig(self.speStatBar, fill=self.speNatureColor(self.current["nature"]))
        elif option == "evs":
            self.analyzer.update(self, "stats")
            self.analyzer.update(self, "physpec Offense")
            self.analyzer.update(self, "physpec Defense")
            #self.toplevel.deiconify()
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
            self.analyzer.update(self,"moves")
            self.analyzer.update(self, "physpec Offense")
            #self.toplevel.deiconify()
            #self.toplevel.iconify()
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

    def deletePopUp(self,name):
        top = Toplevel()
        top.config(width=30,height=30)
        top.title("Are you sure?")
        topMsg = Message(top, text="This command can not be undone. Do you want to proceed?")
        topMsg.pack(side=TOP, fill=X)
        topYesButton = Button(top, text="Yes", command=lambda:self.delete(name))
        #TODO: dont forget to delete top then
        topYesButton.config(width=int(top.winfo_reqwidth()/2))
        topYesButton.pack(side=LEFT)
        topNoButton = Button(top, text="No", command=top.destroy)
        topNoButton.config(width=int(top.winfo_reqwidth()/2))
        topNoButton.pack(side=RIGHT)

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
            self.inputEvent.set()
            self.inputEvent.clear()
            self.messages.config(state=NORMAL)
            self.messages.insert(END, 'You: %s\n\n' % self.input_get)
            self.messages.see(END)
            #self.messages.edit_modified(0)
            self.messages.config(state=DISABLED)
            input_user.set("")
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
        self.current["happiness"] = 255
        self.current["level"] = 100
        self.current["shiny"] = None

        #Team Frame Setup
        teamframe = Frame(root, width=int(self.width / 2), height=self.height)
        teamframe.config(relief=RAISED, borderwidth=borderwidth)
        teamframe.pack(side=LEFT, fill=Y)

        #Make Images
        self.spriteCanvas=Canvas(teamframe,width=80,height=80)
        self.spriteCanvas.config(relief=RAISED,borderwidth=1,background="white")
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

        self.toplevel = Toplevel()
        self.analyzer = TeamAnalyzer.TeamAnalyzer(self, self.toplevel)
        self.toplevel.resizable(width=False,height=False)
        self.toplevel.withdraw()

        root.config(menu=self.the_menu)

        self.inputEvent = threading.Event()
        self.aiThrd = threading.Thread(target=GUIScript.AI, args=(self,))
        self.aiThrd.setDaemon(True)
        self.aiThrd.start()

root = Tk()
root.resizable(width=False,height=False)
AL(root)
root.mainloop()
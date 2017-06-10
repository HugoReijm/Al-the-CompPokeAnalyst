from tkinter import *
from tkinter import ttk
import math,Pokedex,MetaDex,TeamBuilder,tester

class AL:

    def respond(self,text):
        # textlist = list(text)
        # for i in range(math.floor((len(text)-53)/57)+1):
        #    if textlist[53+57*i-1]!=" ":
        #        print("a "+textlist[53+57*i-1])
        #        for j in range(53+57*i-2,-1,-1):
        #            if textlist[j]==" ":
        #                print("b "+textlist[j])
        #                textlist[j]="\n"
        #                break
        # text="".join(textlist)
        self.messages.config(state=NORMAL)
        self.messages.insert(END, 'Al: %s\n\n' % text)
        self.messages.config(state=DISABLED)
        print()
        return "break"

    def showAnalyzer(self):
        pass

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
        self.messages = Text(textframe)
        self.messages.place(x=0,y=0,width=textframe.winfo_reqwidth()-2*borderwidth-17,height=self.height-2*borderwidth-input_field.winfo_reqheight())
        scrollbar = Scrollbar(textframe,command=self.messages.yview)
        scrollbar.place(x=int(textframe.winfo_reqwidth()-2*borderwidth-17),y=0,height=560)
        self.messages["yscrollcommand"]=scrollbar.set
        def Enter_pressed(event):
            input_get = input_field.get()
            self.messages.config(state=NORMAL)
            self.messages.insert(END, 'You: %s\n\n' % input_get)
            self.messages.config(state=DISABLED)
            input_user.set("")
            return "break"
        input_field.bind("<Return>", Enter_pressed)

        teamMatesDict = {}
        dict = {}
        dict["species"] = "Arcanine"
        dict["types"] = ["Fire"]
        dict["ability"] = "Intimidate"
        dict["nature"] = "Adamant"
        dict["baseStats"] = {"hp": 90, "atk": 110,"def": 80, "spa": 100,"spd": 80, "spe": 95}
        dict["ivs"] = {"hp": 31, "atk": 30, "def": 29, "spa": 28, "spd": 27, "spe": 26}
        dict["evs"] = {"hp": 252, "atk": 4, "def": 0, "spa": 0, "spd": 0, "spe": 252}
        dict["item"] = "Firium-Z"
        dict["gender"] = "M"
        dict["moves"] = {"move1": "Flare Blitz", "move2": "Close Combat", "move3": "Protect", "move4": None}
        dict["happiness"] = 255
        dict["level"] = 100
        dict["shiny"] = "No"
        teamMatesDict["Arcanine"] = dict
        dict = {}
        dict["species"] = "Garchomp"
        dict["types"] = ["Ground","Dragon"]
        dict["ability"] = "Rough Skin"
        dict["nature"] = "Jolly"
        dict["baseStats"] = {"hp": 90, "atk": 130, "def": 90, "spa": 80, "spd": 80, "spe": 102}
        dict["ivs"] = {"hp": 31, "atk": 31, "def": 31, "spa": 31, "spd": 31, "spe": 31}
        dict["evs"] = {"hp": 0, "atk": 252, "def": 0, "spa": 0, "spd": 4, "spe": 252}
        dict["item"] = "Assault Vest"
        dict["gender"] = "M"
        dict["moves"] = {"move1": "Earthquake", "move2": "Rock Slide", "move3": "Poison Jab", "move4": "Outrage"}
        dict["happiness"] = 255
        dict["level"] = 100
        dict["shiny"] = "No"
        teamMatesDict["Garchomp"] = dict
        dict = {}
        dict["species"] = "Celesteela"
        dict["types"] = ["Steel","Flying"]
        dict["ability"] = "Beast Boost"
        dict["nature"] = "Sassy"
        dict["baseStats"] = {"hp": 100, "atk": 110, "def": 100, "spa": 10, "spd":100, "spe": 50}
        dict["ivs"] = {"hp": 31, "atk": 30, "def": 29, "spa": 28, "spd": 30, "spe": 3}
        dict["evs"] = {"hp": 252, "atk": 0, "def": 4, "spa": 0, "spd": 252, "spe": 0}
        dict["item"] = "Leftovers"
        dict["gender"] = "M"
        dict["moves"] = {"move1": "Leech Seed", "move2": "Substitute", "move3": "Protect", "move4": "Heavy Slam"}
        dict["happiness"] = 255
        dict["level"] = 100
        dict["shiny"] = "No"
        teamMatesDict["Celesteela"] = dict
        dict = {}
        dict["species"] = "Tapu Koko"
        dict["types"] = ["Fire"]
        dict["ability"] = "Intimidate"
        dict["nature"] = "Adamant"
        dict["baseStats"] = {"hp": 90, "atk": 110, "def": 45, "spa": 100, "spd": 80, "spe": 130}
        dict["ivs"] = {"hp": 31, "atk": 30, "def": 29, "spa": 31, "spd": 27, "spe": 31}
        dict["evs"] = {"hp": 4, "atk": 252, "def": 0, "spa": 0, "spd": 0, "spe": 252}
        dict["item"] = "Life Orb"
        dict["gender"] = None
        dict["moves"] = {"move1": "Thunder", "move2": "Dazzling Gleam", "move3": "Protect", "move4": "U-turn"}
        dict["happiness"] = 255
        dict["level"] = 100
        dict["shiny"] = "No"
        teamMatesDict["Tapu Koko"] = dict
        dict = {}
        dict["species"] = "Porygon2"
        dict["types"] = ["Normal"]
        dict["ability"] = "Download"
        dict["nature"] = "Calm"
        dict["baseStats"] = {"hp": 100, "atk": 80, "def": 100, "spa": 80, "spd": 100, "spe": 50}
        dict["ivs"] = {"hp": 3, "atk": 0, "def": 29, "spa": 28, "spd": 27, "spe": 26}
        dict["evs"] = {"hp": 252, "atk": 0, "def": 4, "spa": 252, "spd": 0, "spe": 0}
        dict["item"] = "Eviolite"
        dict["gender"] = None
        dict["moves"] = {"move1": "Flare Blitz", "move2": "Close Combat", "move3": "Protect", "move4": None}
        dict["happiness"] = 255
        dict["level"] = 100
        dict["shiny"] = "No"
        teamMatesDict["Porygon2"] = dict
        dict = {}
        dict["species"] = "Araquanid"
        dict["types"] = ["Fire"]
        dict["ability"] = "Intimidate"
        dict["nature"] = "Adamant"
        dict["baseStats"] = {"hp": 90, "atk": 110, "def": 80, "spa": 100, "spd": 80, "spe": 95}
        dict["ivs"] = {"hp": 31, "atk": 30, "def": 29, "spa": 28, "spd": 27, "spe": 26}
        dict["evs"] = {"hp": 252, "atk": 4, "def": 0, "spa": 0, "spd": 0, "spe": 252}
        dict["item"] = "Firium-Z"
        dict["gender"] = "M"
        dict["moves"] = {"move1": "Flare Blitz", "move2": "Close Combat", "move3": "Protect", "move4": None}
        dict["happiness"] = 255
        dict["level"] = 100
        dict["shiny"] = "No"
        teamMatesDict["Araquanid"] = dict
        current = teamMatesDict["Arcanine"]

        #Team Frame Setup
        teamframe = Frame(root, width=int(self.width / 2), height=self.height)
        teamframe.config(relief=RAISED, borderwidth=borderwidth)
        teamframe.pack(side=LEFT, fill=Y)

        image=Canvas(teamframe,width=80,height=80)
        image.config(relief=RAISED,borderwidth=1)
        image.place(x=9,y=9)
        # Individual Team Member Species Label
        speciesTitleLabel = Label(teamframe,text="Species:",anchor=W)
        speciesTitleLabel.place(x=100,y=0,width=50)
        speciesLabelText = StringVar()
        speciesLabelText.set(current["species"])
        speciesLabel = Label(teamframe, textvariable=speciesLabelText, anchor=W)
        speciesLabel.place(x=150, y=0, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2-50))
        # Individual Team Member Type Label
        typeTitleLabel = Label(teamframe, text="Types:", anchor=W)
        typeTitleLabel.place(x=100, y=25, width=50)
        typeLabelText = StringVar()
        types = Pokedex.findPokemonTypes(current["species"])
        if len(types)==2:
            typeLabelText.set(types[0]+", "+types[1])
        else:
            typeLabelText.set(types[0])
        typeLabel = Label(teamframe, textvariable=typeLabelText, anchor=W)
        typeLabel.place(x=150, y=25, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2-50))
        #Individual Team Member Ability Label
        abilityTitleLabel = Label(teamframe, text="Ability:", anchor=W)
        abilityTitleLabel.place(x=100, y=50, width=50)
        abilityLabelText = StringVar()
        abilityLabelText.set(current["ability"])
        abilityLabel = Label(teamframe,textvariable=abilityLabelText,anchor=W)
        abilityLabel.place(x=150, y=50, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2-50))
        #Individual Team Member Item Label
        itemLabel = Label(teamframe, text="Item:", anchor=W)
        itemLabel.place(x=100, y=75, width=50)
        itemLabelText = StringVar()
        itemLabelText.set(current["item"])
        itemLabel = Label(teamframe, textvariable=itemLabelText,anchor=W)
        itemLabel.place(x=150, y=75, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2-50))
        #Individual Team Member Level Label
        levelTitleLabel = Label(teamframe, text="Level:", anchor=W)
        levelTitleLabel.place(x=100 + int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2), y=0,width=65)
        levelLabelText = StringVar()
        levelLabelText.set(str(current["level"]))
        levelLabel = Label(teamframe, textvariable=levelLabelText,anchor=W)
        levelLabel.place(x=165+int((teamframe.winfo_reqwidth()-2*borderwidth-100)/2), y=0, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2-65))
        # Individual Team Member Gender Label
        genderTitleLabel = Label(teamframe, text="Gender:", anchor=W)
        genderTitleLabel.place(x=100 + int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2), y=25, width=65)
        genderLabelText = StringVar()
        genderLabelText.set(str(current["gender"]))
        genderLabel = Label(teamframe, textvariable=genderLabelText, anchor=W)
        genderLabel.place(x=165 + int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2), y=25,width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2 - 65))
        #Individual Team Member Happiness Label
        happinessTitleLabel = Label(teamframe, text="Happiness:", anchor=W)
        happinessTitleLabel.place(x=100 + int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2), y=50,width=65)
        happinessLabelText = StringVar()
        happinessLabelText.set(str(current["happiness"]))
        happinessLabel = Label(teamframe, textvariable=happinessLabelText,anchor=W)
        happinessLabel.place(x=165+int((teamframe.winfo_reqwidth()-2*borderwidth-100)/2), y=50, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 100) / 2-65))
        #Individual Team Member Shiny Label
        shinyTitleLabel = Label(teamframe, text="Shiny:",anchor=W)
        shinyTitleLabel.place(x=100+int((teamframe.winfo_reqwidth()-2*borderwidth-100)/2), y=75, width=65)
        shinyLabelText = StringVar()
        shinyLabelText.set(current["shiny"])
        shinyLabel = Label(teamframe, textvariable=shinyLabelText,anchor=W)
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
        hpBS = StringVar()
        hpBS.set(str(current["baseStats"]["hp"]))
        hpBSLabel = Label(teamframe, textvariable=hpBS)
        hpBSLabel.place(x=52, y=131, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 40) / 10))
        #Atk Base Stat
        atkBS = StringVar()
        atkBS.set(str(current["baseStats"]["atk"]))
        atkBSLabel = Label(teamframe, textvariable=atkBS)
        atkBSLabel.place(x=52, y=157, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 40) / 10))
        #Def Base Stat
        defBS = StringVar()
        defBS.set(str(current["baseStats"]["def"]))
        defBSLabel = Label(teamframe, textvariable=defBS)
        defBSLabel.place(x=52, y=183, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 40) / 10))
        #SpA Base Stat
        spaBS = StringVar()
        spaBS.set(str(current["baseStats"]["spa"]))
        spaBSLabel = Label(teamframe, textvariable=spaBS)
        spaBSLabel.place(x=52, y=209, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 40) / 10))
        #SpD Base Stat
        spdBS = StringVar()
        spdBS.set(str(current["baseStats"]["spd"]))
        spdBSLabel = Label(teamframe, textvariable=spdBS)
        spdBSLabel.place(x=52, y=235, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 40) / 10))
        #Spe Base Stat
        speBS = StringVar()
        speBS.set(str(current["baseStats"]["spe"]))
        speBSLabel = Label(teamframe, textvariable=speBS)
        speBSLabel.place(x=52, y=261, width=int((teamframe.winfo_reqwidth() - 2 * borderwidth - 40) / 10))

        #Sub Separator 1_2
        subsep1_2 = ttk.Separator(teamframe, orient=VERTICAL)
        subsep1_2.place(x=115, y=110, height=172)

        #IVs Label
        ivsLabel = Label(teamframe, text="IVs")
        ivsLabel.place(x=125, y=110, width=25)
        #HP IVs
        hpIV = StringVar()
        hpIV.set(str(current["ivs"]["hp"]))
        hpIVLabel = Label(teamframe, textvariable=hpIV)
        hpIVLabel.place(x=125, y=131, width=25)
        #Atk IVs
        atkIV = StringVar()
        atkIV.set(str(current["ivs"]["atk"]))
        atkIVLabel = Label(teamframe, textvariable=atkIV)
        atkIVLabel.place(x=125, y=157, width=25)
        #Def IVs
        defIV = StringVar()
        defIV.set(str(current["ivs"]["def"]))
        defIVLabel = Label(teamframe, textvariable=defIV)
        defIVLabel.place(x=125, y=183, width=25)
        #SpA IVs
        spaIV = StringVar()
        spaIV.set(str(current["ivs"]["spa"]))
        spaIVLabel = Label(teamframe, textvariable=spaIV)
        spaIVLabel.place(x=125, y=209, width=25)
        #SpD IVs
        spdIV = StringVar()
        spdIV.set(str(current["ivs"]["spd"]))
        spdIVLabel = Label(teamframe, textvariable=spdIV)
        spdIVLabel.place(x=125, y=235, width=25)
        #Spe IVs
        speIV = StringVar()
        speIV.set(str(current["ivs"]["spe"]))
        speIVLabel = Label(teamframe, textvariable=speIV)
        speIVLabel.place(x=125, y=261, width=25)

        #Sub Separator 1_3
        subsep1_3 = ttk.Separator(teamframe, orient=VERTICAL)
        subsep1_3.place(x=160, y=110, height=172)

        #EVs Label
        evsLabel = Label(teamframe, text="EVs")
        evsLabel.place(x=170, y=110, width=25)
        #HP EVs
        hpEV = StringVar()
        hpEV.set(str(current["evs"]["hp"]))
        hpEVLabel = Label(teamframe, textvariable=hpEV)
        hpEVLabel.place(x=170, y=131, width=25)
        #Atk EVs
        atkEV = StringVar()
        atkEV.set(str(current["evs"]["atk"]))
        atkEVLabel = Label(teamframe, textvariable=atkEV)
        atkEVLabel.place(x=170, y=157, width=25)
        #Def EVs
        defEV = StringVar()
        defEV.set(str(current["evs"]["def"]))
        defEVLabel = Label(teamframe, textvariable=defEV)
        defEVLabel.place(x=170, y=183, width=25)
        #SpA EVs
        spaEV = StringVar()
        spaEV.set(str(current["evs"]["spa"]))
        spaEVLabel = Label(teamframe, textvariable=spaEV)
        spaEVLabel.place(x=170, y=209, width=25)
        #SpD EVs
        spdEV = StringVar()
        spdEV.set(str(current["evs"]["spd"]))
        spdEVLabel = Label(teamframe, textvariable=spdEV)
        spdEVLabel.place(x=170, y=235, width=25)
        #Spe EVs
        speEV = StringVar()
        speEV.set(str(current["evs"]["spe"]))
        speEVLabel = Label(teamframe, textvariable=speEV)
        speEVLabel.place(x=170, y=261, width=25)

        #Sub Separator 1_4
        subsep1_4 = ttk.Separator(teamframe, orient=VERTICAL)
        subsep1_4.place(x=205, y=110, height=172)

        #HP Bar
        hpStatCanvas = Canvas(teamframe, width = 178)
        hpStatBar=hpStatCanvas.create_rectangle(0,5,int(self.hpStatCalc(current["baseStats"]["hp"],current["evs"]["hp"],current["ivs"]["hp"],current["level"])/4),16,fill="lawn green")
        hpStatCanvas.place(x=215, y=131)
        #Atk Bar
        atkStatCanvas = Canvas(teamframe,width = 178)
        atkStatBar=atkStatCanvas.create_rectangle(0, 5, int(self.atkStatCalc(current["baseStats"]["atk"],current["evs"]["atk"],current["ivs"]["atk"],current["level"],current["nature"])/4), 16)
        atkStatCanvas.itemconfig(atkStatBar,fill=self.atkNatureColor(current["nature"]))
        atkStatCanvas.place(x=215, y=157)
        #Def Bar
        defStatCanvas = Canvas(teamframe,width = 178)
        defStatBar=defStatCanvas.create_rectangle(0, 5, int(self.defStatCalc(current["baseStats"]["def"],current["evs"]["def"],current["ivs"]["def"],current["level"],current["nature"])/4), 16)
        #defStatCanvas.itemconfig(defStatBar, fill="firebrick2")
        defStatCanvas.itemconfig(defStatBar, fill=self.defNatureColor(current["nature"]))
        defStatCanvas.place(x=215, y=183)
        #SpA Bar
        spaStatCanvas = Canvas(teamframe,width = 178)
        spaStatBar=spaStatCanvas.create_rectangle(0, 5, int(self.spaStatCalc(current["baseStats"]["spa"],current["evs"]["spa"],current["ivs"]["spa"],current["level"],current["nature"])/4), 16)
        spaStatCanvas.itemconfig(spaStatBar, fill=self.spaNatureColor(current["nature"]))
        spaStatCanvas.place(x=215, y=209)
        #SpD Bar
        spdStatCanvas = Canvas(teamframe,width = 178)
        spdStatBar=spdStatCanvas.create_rectangle(0, 5, int(self.spdStatCalc(current["baseStats"]["spd"],current["evs"]["spd"],current["ivs"]["spd"],current["level"],current["nature"])/4), 16)
        #spdStatCanvas.itemconfig(spdStatBar,fill="dodger blue")
        spdStatCanvas.itemconfig(spdStatBar, fill=self.spdNatureColor(current["nature"]))
        spdStatCanvas.place(x=215, y=235)
        #Spe Bar
        speStatCanvas = Canvas(teamframe,width = 178)
        speStatBar=speStatCanvas.create_rectangle(0, 5, int(self.speStatCalc(current["baseStats"]["spe"],current["evs"]["spe"],current["ivs"]["spe"],current["level"],current["nature"])/4), 16)
        speStatCanvas.itemconfig(speStatBar, fill=self.speNatureColor(current["nature"]))
        speStatCanvas.place(x=215, y=261)

        #Sub Separator 1_5
        subsep1_5 = ttk.Separator(teamframe, orient=VERTICAL)
        subsep1_5.place(x=403, y=110, height=172)

        #Total Stats Label
        totalLabel = Label(teamframe, text="Total")
        totalLabel.place(x=413, y=110, width=25)
        #HP Total
        hpTotal = StringVar()
        hpTotal.set(str(self.hpStatCalc(current["baseStats"]["hp"],current["evs"]["hp"],current["ivs"]["hp"],current["level"])))
        hpTotalLabel = Label(teamframe, textvariable=hpTotal)
        hpTotalLabel.place(x=413, y=131, width=25)
        #Atk Total
        atkTotal = StringVar()
        atkTotal.set(str(self.atkStatCalc(current["baseStats"]["atk"],current["evs"]["atk"],current["ivs"]["atk"],current["level"],current["nature"])))
        atkTotalLabel = Label(teamframe, textvariable=atkTotal)
        atkTotalLabel.place(x=413, y=157, width=25)
        #Def Total
        defTotal = StringVar()
        defTotal.set(str(self.defStatCalc(current["baseStats"]["def"],current["evs"]["def"],current["ivs"]["def"],current["level"],current["nature"])))
        defTotalLabel = Label(teamframe, textvariable=defTotal)
        defTotalLabel.place(x=413, y=183, width=25)
        #SpA Total
        spaTotal = StringVar()
        spaTotal.set(str(self.spaStatCalc(current["baseStats"]["spa"],current["evs"]["spa"],current["ivs"]["spa"],current["level"],current["nature"])))
        spaTotalLabel = Label(teamframe, textvariable=spaTotal)
        spaTotalLabel.place(x=413, y=209, width=25)
        #SpD Total
        spdTotal = StringVar()
        spdTotal.set(str(self.spdStatCalc(current["baseStats"]["spd"],current["evs"]["spd"],current["ivs"]["spd"],current["level"],current["nature"])))
        spdTotalLabel = Label(teamframe, textvariable=spdTotal)
        spdTotalLabel.place(x=413, y=235, width=25)
        #Spe Total
        speTotal = StringVar()
        speTotal.set(str(self.speStatCalc(current["baseStats"]["spe"],current["evs"]["spe"],current["ivs"]["spe"],current["level"],current["nature"])))
        speTotalLabel = Label(teamframe, textvariable=speTotal)
        speTotalLabel.place(x=413, y=261, width=25)

        #Separator 2
        separator2 = ttk.Separator(teamframe, orient=HORIZONTAL)
        separator2.place(x=10, y=297, width=teamframe.winfo_reqwidth() - 2 * borderwidth - 20)

        #Move 1 Name
        move1Name = StringVar()
        move1Name.set(current["moves"]["move1"])
        move1Data = Pokedex.findMoveData(current["moves"]["move1"])
        move1NameLabel = Label(teamframe,textvariable=move1Name,anchor=W,width=21)
        move1NameLabel.place(x=10,y=338)
        # Move 2 Name
        move2Name = StringVar()
        move2Name.set(current["moves"]["move2"])
        move2Data = Pokedex.findMoveData(current["moves"]["move2"])
        move2NameLabel = Label(teamframe, textvariable=move2Name, anchor=W, width=21)
        move2NameLabel.place(x=10, y=364)
        # Move 3 Name
        move3Name = StringVar()
        move3Name.set(current["moves"]["move3"])
        move3Data = Pokedex.findMoveData(current["moves"]["move3"])
        move3NameLabel = Label(teamframe, textvariable=move3Name, anchor=W, width=21)
        move3NameLabel.place(x=10, y=390)
        # Move 4 Name
        move4Name = StringVar()
        move4Name.set(current["moves"]["move4"])
        move4Data = Pokedex.findMoveData(current["moves"]["move4"])
        move4NameLabel = Label(teamframe, textvariable=move4Name, anchor=W, width=21)
        move4NameLabel.place(x=10, y=416)

        #Sub Separator 2_1
        subsep2_1 = ttk.Separator(teamframe, orient=VERTICAL)
        subsep2_1.place(x=140, y=317, height=125)

        #Move Category Label
        moveCatLabel = Label(teamframe,text="Category")
        moveCatLabel.place(x=150,y=317,width=50)
        # Move 1 Category
        move1Cat = StringVar()
        if move1Data != None:
            move1Cat.set(move1Data["category"])
        else:
            move1Cat.set("N/A")
        move1CatLabel = Label(teamframe, textvariable=move1Cat)
        move1CatLabel.place(x=150, y=338,width=50)
        # Move 2 Category
        move2Cat = StringVar()
        if move2Data != None:
            move2Cat.set(move2Data["category"])
        else:
            move2Cat.set("N/A")
        move2CatLabel = Label(teamframe, textvariable=move2Cat)
        move2CatLabel.place(x=150, y=364,width=50)
        # Move 3 Category
        move3Cat = StringVar()
        if move3Data != None:
            move3Cat.set(move3Data["category"])
        else:
            move3Cat.set("N/A")
        move3CatLabel = Label(teamframe, textvariable=move3Cat)
        move3CatLabel.place(x=150, y=390,width=50)
        # Move 4 Category
        move4Cat = StringVar()
        if move4Data != None:
            move4Cat.set(move4Data["category"])
        else:
            move4Cat.set("N/A")
        move4CatLabel = Label(teamframe, textvariable=move4Cat)
        move4CatLabel.place(x=150, y=416, width=50)

        #Sub Separator 2_2
        subsep2_2 = ttk.Separator(teamframe, orient=VERTICAL)
        subsep2_2.place(x=210, y=317, height=125)

        #Move Type Label
        moveTypeLabel = Label(teamframe, text="Type")
        moveTypeLabel.place(x=220, y=317, width=45)
        # Move 1 Type
        move1Type = StringVar()
        if move1Data != None:
            move1Type.set(move1Data["type"])
        else:
            move1Type.set("N/A")
        move1TypeLabel = Label(teamframe, textvariable=move1Type)
        move1TypeLabel.place(x=220, y=338, width=45)
        # Move 2 Type
        move2Type = StringVar()
        if move2Data != None:
            move2Type.set(move2Data["type"])
        else:
            move2Type.set("N/A")
        move2TypeLabel = Label(teamframe, textvariable=move2Type)
        move2TypeLabel.place(x=220, y=364, width=45)
        # Move 3 Type
        move3Type = StringVar()
        if move3Data != None:
            move3Type.set(move3Data["type"])
        else:
            move3Type.set("N/A")
        move3TypeLabel = Label(teamframe, textvariable=move3Type)
        move3TypeLabel.place(x=220, y=390, width=45)
        # Move 4 Type
        move4Type = StringVar()
        if move4Data != None:
            move4Type.set(move4Data["type"])
        else:
            move4Type.set("N/A")
        move4TypeLabel = Label(teamframe, textvariable=move4Type)
        move4TypeLabel.place(x=220, y=416, width=45)

        #Sub Separator 2_3
        subsep2_3 = ttk.Separator(teamframe, orient=VERTICAL)
        subsep2_3.place(x=275, y=317, height=125)

        #Move Base Power Label
        moveBasePowerLabel = Label(teamframe, text="Base Power")
        moveBasePowerLabel.place(x=285, y=317, width=60)
        # Move 1 Base Power
        move1BasePower = StringVar()
        if move1Data != None:
            move1BasePower.set(str(move1Data["basePower"]))
        else:
            move1BasePower.set("N/A")
        move1BasePowerLabel = Label(teamframe, textvariable=move1BasePower)
        move1BasePowerLabel.place(x=285, y=338, width=60)
        # Move 2 Base Power
        move2BasePower = StringVar()
        if move2Data != None:
            move2BasePower.set(str(move2Data["basePower"]))
        else:
            move2BasePower.set("N/A")
        move2BasePowerLabel = Label(teamframe, textvariable=move2BasePower)
        move2BasePowerLabel.place(x=285, y=364, width=60)
        # Move 3 Base Power
        move3BasePower = StringVar()
        if move3Data != None:
            move3BasePower.set(str(move3Data["basePower"]))
        else:
            move3BasePower.set("N/A")
        move3BasePowerLabel = Label(teamframe, textvariable=move3BasePower)
        move3BasePowerLabel.place(x=285, y=390, width=60)
        # Move 4 Base Power
        move4BasePower = StringVar()
        if move4Data != None:
            move4BasePower.set(str(move4Data["basePower"]))
        else:
            move4BasePower.set("N/A")
        move4BasePowerLabel = Label(teamframe, textvariable=move4BasePower)
        move4BasePowerLabel.place(x=285, y=416, width=60)

        # Sub Separator 2_4
        subsep2_4 = ttk.Separator(teamframe, orient=VERTICAL)
        subsep2_4.place(x=355, y=317, height=125)

        # Move PP Label
        movePPLabel = Label(teamframe, text="PP")
        movePPLabel.place(x=365, y=317, width=25)
        # Move 1 PP
        move1PP = StringVar()
        if move1Data != None:
            move1PP.set(str(move1Data["pp"]))
        else:
            move1PP.set("N/A")
        move1PPLabel = Label(teamframe, textvariable=move1PP)
        move1PPLabel.place(x=365, y=338, width=25)
        # Move 2 PP
        move2PP = StringVar()
        if move2Data != None:
            move2PP.set(str(move2Data["pp"]))
        else:
            move2PP.set("N/A")
        move2PPLabel = Label(teamframe, textvariable=move2PP)
        move2PPLabel.place(x=365, y=364, width=25)
        # Move 3 PP
        move3PP = StringVar()
        if move3Data != None:
            move3PP.set(str(move3Data["pp"]))
        else:
            move3PP.set("N/A")
        move3PPLabel = Label(teamframe, textvariable=move3PP)
        move3PPLabel.place(x=365, y=390, width=25)
        # Move 4 PP
        move4PP = StringVar()
        if move4Data != None:
            move4PP.set(str(move4Data["pp"]))
        else:
            move4PP.set("N/A")
        move4PPLabel = Label(teamframe, textvariable=move4PP)
        move4PPLabel.place(x=365, y=416, width=25)

        # Sub Separator 2_5
        subsep2_5 = ttk.Separator(teamframe, orient=VERTICAL)
        subsep2_5.place(x=400, y=317, height=125)

        # Move Accuracy Label
        moveAccLabel = Label(teamframe, text="Accuracy")
        moveAccLabel.place(x=410, y=317, width=60)
        # Move 1 Accuracy
        move1Acc = StringVar()
        if move1Data != None:
            if move1Data["accuracy"]!= True:
                move1Acc.set(str(move1Data["accuracy"])+"%")
            else:
                move1Acc.set("100%")
        else:
            move1Acc.set("N/A")
        move1AccLabel = Label(teamframe, textvariable=move1Acc)
        move1AccLabel.place(x=410, y=338, width=60)
        # Move 2 Accuracy
        move2Acc = StringVar()
        if move2Data != None:
            if move2Data["accuracy"] != True:
                move2Acc.set(str(move2Data["accuracy"])+"%")
            else:
                move2Acc.set("100%")
        else:
            move2Acc.set("N/A")
        move2AccLabel = Label(teamframe, textvariable=move2Acc)
        move2AccLabel.place(x=410, y=364, width=60)
        # Move 3 Accuracy
        move3Acc = StringVar()
        if move3Data != None:
            if move3Data["accuracy"] != True:
                move3Acc.set(str(move3Data["accuracy"])+"%")
            else:
                move3Acc.set("100%")
        else:
            move3Acc.set("N/A")
        move3AccLabel = Label(teamframe, textvariable=move3Acc)
        move3AccLabel.place(x=410, y=390, width=60)
        # Move 4 Accuracy
        move4Acc = StringVar()
        if move4Data != None:
            if move4Data["accuracy"] != True:
                move4Acc.set(str(move4Data["accuracy"])+"%")
            else:
                move4Acc.set("100%")
        else:
            move4Acc.set("N/A")
        move4AccLabel = Label(teamframe, textvariable=move4Acc)
        move4AccLabel.place(x=410, y=416, width=60)

        #Menu Setup
        the_menu = Menu(root)
        file_menu = Menu(the_menu,tearoff=0)
        file_menu.add_command(label="Team Analyzer",command=self.showAnalyzer)
        file_menu.add_command(label="Quit",command=root.quit)
        the_menu.add_cascade(label="File",menu=file_menu)

        teamList = list(teamMatesDict.keys())

        pokemon1_menu = Menu(the_menu,tearoff=0)
        pokemon1_menu.add_command(label="View",command=lambda:switch(teamList[0]))
        pokemon1_menu.add_command(label="Delete",command=lambda:delete(teamList[0]))
        the_menu.add_cascade(label=teamList[0],menu=pokemon1_menu)

        pokemon2_menu = Menu(the_menu, tearoff=0)
        pokemon2_menu.add_command(label="View", command=lambda:switch(teamList[1]))
        pokemon2_menu.add_command(label="Delete", command=lambda:delete(teamList[1]))
        the_menu.add_cascade(label=teamList[1], menu=pokemon2_menu)

        pokemon3_menu = Menu(the_menu, tearoff=0)
        pokemon3_menu.add_command(label="View", command=lambda:switch(teamList[2]))
        pokemon3_menu.add_command(label="Delete", command=lambda:delete(teamList[2]))
        the_menu.add_cascade(label=teamList[2], menu=pokemon3_menu)

        pokemon4_menu = Menu(the_menu, tearoff=0)
        pokemon4_menu.add_command(label="View", command=lambda:switch(teamList[3]))
        pokemon4_menu.add_command(label="Delete", command=lambda:delete(teamList[3]))
        the_menu.add_cascade(label=teamList[3], menu=pokemon4_menu)

        pokemon5_menu = Menu(the_menu, tearoff=0)
        pokemon5_menu.add_command(label="View", command=lambda:switch(teamList[4]))
        pokemon5_menu.add_command(label="Delete", command=lambda:delete(teamList[4]))
        the_menu.add_cascade(label=teamList[4], menu=pokemon5_menu)

        pokemon6_menu = Menu(the_menu, tearoff=0)
        pokemon6_menu.add_command(label="View", command=lambda:switch(teamList[5]))
        pokemon6_menu.add_command(label="Delete", command=lambda:delete(teamList[5]))
        the_menu.add_cascade(label=teamList[5], menu=pokemon6_menu)

        root.config(menu=the_menu)

        def switch(name):
            current = teamMatesDict[name]
            speciesLabelText.set(current["species"])
            types = Pokedex.findPokemonTypes(current["species"])
            if len(types) == 2:
                typeLabelText.set(types[0] + ", " + types[1])
            else:
                typeLabelText.set(types[0])
            abilityLabelText.set(current["ability"])
            itemLabelText.set(current["item"])
            levelLabelText.set(current["level"])
            genderLabelText.set(current["gender"])
            happinessLabelText.set(current["happiness"])
            shinyLabelText.set(current["shiny"])
            hpBS.set(str(current["baseStats"]["hp"]))
            atkBS.set(str(current["baseStats"]["atk"]))
            defBS.set(str(current["baseStats"]["def"]))
            spaBS.set(str(current["baseStats"]["spa"]))
            spdBS.set(str(current["baseStats"]["spd"]))
            speBS.set(str(current["baseStats"]["spe"]))
            hpIV.set(str(current["ivs"]["hp"]))
            atkIV.set(str(current["ivs"]["atk"]))
            defIV.set(str(current["ivs"]["def"]))
            spaIV.set(str(current["ivs"]["spa"]))
            spdIV.set(str(current["ivs"]["spd"]))
            speIV.set(str(current["ivs"]["spe"]))
            hpEV.set(str(current["evs"]["hp"]))
            atkEV.set(str(current["evs"]["atk"]))
            defEV.set(str(current["evs"]["def"]))
            spaEV.set(str(current["evs"]["spa"]))
            spdEV.set(str(current["evs"]["spd"]))
            speEV.set(str(current["evs"]["spe"]))
            hpStatCanvas.coords(hpStatBar,0,5,int(self.hpStatCalc(current["baseStats"]["hp"],current["evs"]["hp"],current["ivs"]["hp"],current["level"])/4),16)
            atkStatCanvas.coords(atkStatBar,0,5,int(self.atkStatCalc(current["baseStats"]["atk"],current["evs"]["atk"],current["ivs"]["atk"],current["level"],current["nature"])/4),16)
            atkStatCanvas.itemconfig(atkStatBar, fill=self.atkNatureColor(current["nature"]))
            defStatCanvas.coords(defStatBar, 0, 5, int(self.defStatCalc(current["baseStats"]["def"], current["evs"]["def"], current["ivs"]["def"],current["level"], current["nature"]) / 4), 16)
            defStatCanvas.itemconfig(defStatBar, fill=self.defNatureColor(current["nature"]))
            spaStatCanvas.coords(spaStatBar, 0, 5, int(self.spaStatCalc(current["baseStats"]["spa"], current["evs"]["spa"], current["ivs"]["spa"],current["level"], current["nature"]) / 4), 16)
            spaStatCanvas.itemconfig(spaStatBar, fill=self.spaNatureColor(current["nature"]))
            spdStatCanvas.coords(spdStatBar, 0, 5, int(self.spdStatCalc(current["baseStats"]["spd"], current["evs"]["spd"], current["ivs"]["spd"],current["level"], current["nature"]) / 4), 16)
            spdStatCanvas.itemconfig(spdStatBar, fill=self.spdNatureColor(current["nature"]))
            speStatCanvas.coords(speStatBar, 0, 5, int(self.speStatCalc(current["baseStats"]["spe"], current["evs"]["spe"], current["ivs"]["spe"],current["level"], current["nature"]) / 4), 16)
            speStatCanvas.itemconfig(speStatBar, fill=self.speNatureColor(current["nature"]))
            hpTotal.set(str(self.hpStatCalc(current["baseStats"]["hp"],current["evs"]["hp"],current["ivs"]["hp"],current["level"])))
            atkTotal.set(str(self.atkStatCalc(current["baseStats"]["atk"],current["evs"]["atk"],current["ivs"]["atk"],current["level"],current["nature"])))
            defTotal.set(str(self.defStatCalc(current["baseStats"]["def"], current["evs"]["def"], current["ivs"]["def"],current["level"], current["nature"])))
            spaTotal.set(str(self.spaStatCalc(current["baseStats"]["spa"], current["evs"]["spa"], current["ivs"]["spa"],current["level"], current["nature"])))
            spdTotal.set(str(self.spdStatCalc(current["baseStats"]["spd"], current["evs"]["spd"], current["ivs"]["spd"],current["level"], current["nature"])))
            speTotal.set(str(self.speStatCalc(current["baseStats"]["spe"], current["evs"]["spe"], current["ivs"]["spe"],current["level"], current["nature"])))
            move1Name.set(current["moves"]["move1"])
            move2Name.set(current["moves"]["move2"])
            move3Name.set(current["moves"]["move3"])
            move4Name.set(current["moves"]["move4"])
            move1Data = Pokedex.findMoveData(current["moves"]["move1"])
            move2Data = Pokedex.findMoveData(current["moves"]["move2"])
            move3Data = Pokedex.findMoveData(current["moves"]["move3"])
            move4Data = Pokedex.findMoveData(current["moves"]["move4"])
            if move1Data != None:
                move1Cat.set(move1Data["category"])
                move1Type.set(move1Data["type"])
                move1BasePower.set(str(move1Data["basePower"]))
                move1PP.set(str(move1Data["pp"]))
                if move1Data["accuracy"] != True:
                    move1Acc.set(str(move1Data["accuracy"]) + "%")
                else:
                    move1Acc.set("100%")
            else:
                move1Cat.set("N/A")
                move1Type.set("N/A")
                move1BasePower.set("N/A")
                move1PP.set("N/A")
                move1Acc.set("N/A")

            if move2Data != None:
                move2Cat.set(move2Data["category"])
                move2Type.set(move2Data["type"])
                move2BasePower.set(str(move2Data["basePower"]))
                move2PP.set(str(move2Data["pp"]))
                if move2Data["accuracy"] != True:
                    move2Acc.set(str(move2Data["accuracy"]) + "%")
                else:
                    move2Acc.set("100%")
            else:
                move2Cat.set("N/A")
                move2Type.set("N/A")
                move2BasePower.set("N/A")
                move2PP.set("N/A")
                move2Acc.set("N/A")

            if move3Data != None:
                move3Cat.set(move3Data["category"])
                move3Type.set(move3Data["type"])
                move3BasePower.set(str(move3Data["basePower"]))
                move3PP.set(str(move3Data["pp"]))
                if move3Data["accuracy"] != True:
                    move3Acc.set(str(move3Data["accuracy"]) + "%")
                else:
                    move3Acc.set("100%")
            else:
                move3Cat.set("N/A")
                move3Type.set("N/A")
                move3BasePower.set("N/A")
                move3PP.set("N/A")
                move3Acc.set("N/A")

            if move4Data != None:
                move4Cat.set(move4Data["category"])
                move4Type.set(move4Data["type"])
                move4BasePower.set(str(move4Data["basePower"]))
                move4PP.set(str(move4Data["pp"]))
                if move4Data["accuracy"] != True:
                    move4Acc.set(str(move4Data["accuracy"]) + "%")
                else:
                    move4Acc.set("100%")
            else:
                move4Cat.set("N/A")
                move4Type.set("N/A")
                move4BasePower.set("N/A")
                move4PP.set("N/A")
                move4Acc.set("N/A")

        def delete(name):
            teamMatesDict[name]["species"] = None
            teamMatesDict[name]["types"] = [None]
            teamMatesDict[name]["ability"] = None
            teamMatesDict[name]["nature"] = None
            teamMatesDict[name]["baseStats"] = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0}
            teamMatesDict[name]["ivs"] = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0}
            teamMatesDict[name]["evs"] = {"hp": 0, "atk": 0, "def": 0, "spa": 0, "spd": 0, "spe": 0}
            teamMatesDict[name]["item"] = None
            teamMatesDict[name]["gender"] = None
            teamMatesDict[name]["moves"] = {"move1": None, "move2": None, "move3": None, "move4": None}
            teamMatesDict[name]["happiness"] = None
            teamMatesDict[name]["level"] = 0
            teamMatesDict[name]["shiny"] = None
            current=teamMatesDict[name]
            switch(name)
            the_menu.entryconfigure(name,label="None")

root = Tk()
root.resizable(width=False,height=False)
Al = AL(root)
Al.respond("hello?")
tester.setGUI(Al)
root.mainloop()
import TeamBuilder,MetaDex,Pokedex,datetime,random,sys

class UI(object):
    mygui = None
    def __init__(self,gui):
        self.mygui = gui
        self.mygui.setUI(self)
        self.mygui.respond("connected")
        self.mygui.respond("Hello! I'm Al, here to help build your personal competitive Pokemon team!")
        self.mygui.respond("The great thing is, after we have built your team, I'll automatically export your team so you can easily import it into Pokemon Showdown, a Competitive Pokemon Battle Simulator used by hundreds of people every day!")
        self.mygui.respond("Let's get started!")
        # TODO: implement personal names and inout of user names
        self.tierDisplay()

    def tierDisplay(self):
        # Display All Tiers Downloaded Tiers
        self.mygui.respond("First, we need to decide which tier this team will be used in.")
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
        self.mygui.respond("Please input one of the following:")
        text = ""
        for t in tiers:
            text+=t+"\n    "
        self.mygui.respond(text[:len(text)-5])
        chooseTierGate = False
        while not chooseTierGate:
            self.mygui.respond("Which tier would you like to work in?")
            chooseTierGate = True
            #tier = input("Input: (String) ")
            #if tier in tiers:
            #    confirmTierGate = False
            #    while not confirmTierGate:
            #        self.mygui.respond("You would like to build a team for %s?" % tier)
            #        res = input("Input: (Y/N) ")
            #        if res == "Y":
            #            chooseTierGate = True
            #            confirmTierGate = True
            #        elif res == "N":
            #            confirmTierGate = True
            #        else:
            #            self.mygui.respond("Um...I don't understand your response...")
            # else:
            #    self.mygui.respond("Um...I don't understand your response...")

    def entry(self):
        pass

    def beep(self):
        print("BEEP")

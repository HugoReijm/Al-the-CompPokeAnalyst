from tkinter import *

class AL:

    def quit_app(event=None):
        root.quit()

    def respond(text, messages):
        messages.config(state=NORMAL)
        messages.insert(END, '%s\n' % text)
        messages.config(state=DISABLED)
        return "break"

    def __init__(self,root):
        #Team Builder Window Setup
        root.title("Team Builder")
        self.width = 800
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
        messages = Text(textframe)
        messages.place(x=0,y=0,width=textframe.winfo_reqwidth()-2*borderwidth,height=self.height-2*borderwidth-input_field.winfo_reqheight())
        def Enter_pressed(event):
            input_get = input_field.get()
            messages.config(state=NORMAL)
            messages.insert(END, 'You: %s\n' % input_get)
            messages.config(state=DISABLED)
            input_user.set("")
            return "break"
        input_field.bind("<Return>", Enter_pressed)

        #Team Fram Setup
        teamframe = Frame(root, width=int(self.width / 2), height=self.height)
        teamframe.config(relief=RAISED, borderwidth=borderwidth)
        teamframe.pack(side=LEFT, fill=Y)

        #Individual Team Member Frame Setups
        pframes = []
        for i in range(6):
            pframes.append(Frame(teamframe,width=teamframe.winfo_reqwidth()-2*borderwidth,
                            height=int((teamframe.winfo_reqheight()-2*borderwidth)/6)))
            pframes[i].config(relief=RAISED, borderwidth=1)
            pframes[i].place(x=0,y=int(i*pframes[i].winfo_reqheight()))

        #Menu Setup
        the_menu = Menu(root)
        file_menu = Menu(the_menu,tearoff=0)
        file_menu.add_command(label="Team Analyzer",command=print("hi"))
        file_menu.add_command(label="Quit",command=self.quit_app)
        the_menu.add_cascade(label="File",menu=file_menu)
        root.config(menu=the_menu)

root = Tk()
Al = AL(root)
root.mainloop()
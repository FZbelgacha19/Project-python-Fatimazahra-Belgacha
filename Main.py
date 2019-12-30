from Crypter import SetpassWord as crypter
from Decrypter import SetpassWord as decrypter
from tkinter import *


class Interface(Frame):
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=900,
                       height=900, bg="white", ** kwargs)

        self.pack(fill=BOTH)
        _bgcolor = "#d9d9d9"  # X11 color: "gray85"
        _fgcolor = "#000000"  # X11 color: "black"
        _compcolor = "#d9d9d9"  # X11 color: "gray85"
        _ana1color = "#d9d9d9"  # X11 color: "gray85"
        _ana2color = "#ececec"  # Closest X11 color: "gray92"
        font11 = "-family {@Malgun Gothic} -size 10 -weight bold "  \
            "-slant roman -underline 0 -overstrike 0"
        font12 = "-family {@Malgun Gothic} -size 11 -weight normal "  \
            "-slant roman -underline 0 -overstrike 0"
        font13 = "-family {@Malgun Gothic} -size 11 -weight bold -slant"  \
            " roman -underline 0 -overstrike 0"

        txt = "\n***************************************************************\n"
        txt += "                           Application                           \n"
        txt += "                  Encrypted / Decrypted of data                   \n"
        txt += "*******************************************************************\n"
        self.titre = Label(self, text=txt)
        self.titre.place(relx=0.020, rely=0.020, height=112, width=400)
        self.titre.configure(disabledforeground="#a3a3a3")
        self.titre.configure(font=font13)
        self.titre.configure(foreground="#083F81")
        self.titre.configure(background="white")

        self.username_txt = Label(self, text="Username:")
        self.username_txt.place(relx=0.029, rely=0.321, height=22, width=81)
        self.username_txt.configure(disabledforeground="#a3a3a3")
        self.username_txt.configure(font=font12)
        self.username_txt.configure(foreground="#000000")
        self.username_txt.configure(background="white")

        self.username = Entry(self)
        self.username.place(relx=0.314, rely=0.326, height=20, relwidth=0.669)
        self.username.configure(background="white")
        self.username.configure(disabledforeground="#a3a3a3")
        self.username.configure(font=font12)
        self.username.configure(foreground="#000000")
        self.username.configure(insertbackground="black")
        self.username.configure(background="white")

        self.Password_txt = Label(self, text="Password:")
        self.Password_txt.place(relx=0.029, rely=0.393, height=22, width=81)
        self.Password_txt.configure(activebackground="#f9f9f9")
        self.Password_txt.configure(disabledforeground="#a3a3a3")
        self.Password_txt.configure(font=font12)
        self.Password_txt.configure(foreground="#000000")
        self.Password_txt.configure(highlightbackground="#d9d9d9")
        self.Password_txt.configure(highlightcolor="black")
        self.Password_txt.configure(background="white")

        self.password = Entry(self, show="*")
        self.password.place(relx=0.314, rely=0.395, height=20, relwidth=0.669)
        self.password.configure(background="white")
        self.password.configure(disabledforeground="#a3a3a3")
        self.password.configure(font=font12)
        self.password.configure(foreground="#000000")
        self.password.configure(highlightbackground="#d9d9d9")
        self.password.configure(highlightcolor="black")
        self.password.configure(insertbackground="black")
        self.password.configure(selectbackground="#c4c4c4")
        self.password.configure(selectforeground="black")

        self.Path_txt = Label(self, text="File path : ")
        self.Path_txt.place(relx=0.029, rely=0.465, height=22, width=81)
        self.Path_txt.configure(activebackground="#f9f9f9")
        self.Path_txt.configure(activeforeground="black")
        self.Path_txt.configure(disabledforeground="#a3a3a3")
        self.Path_txt.configure(font=font12)
        self.Path_txt.configure(foreground="#000000")
        self.Path_txt.configure(highlightbackground="#d9d9d9")
        self.Path_txt.configure(highlightcolor="black")
        self.Path_txt.configure(background="white")

        self.filep = Entry(self)
        self.filep.place(relx=0.314, rely=0.465, height=20, relwidth=0.669)
        self.filep.configure(background="white")
        self.filep.configure(disabledforeground="#a3a3a3")
        self.filep.configure(foreground="#000000")
        self.filep.configure(highlightbackground="#d9d9d9")
        self.filep.configure(highlightcolor="black")
        self.filep.configure(insertbackground="black")
        self.filep.configure(selectbackground="#c4c4c4")
        self.filep.configure(selectforeground="black")

        self.Crypter = Button(
            self, text="Crypter", command=self.do_crypter)
        self.Crypter.place(relx=0.086, rely=0.558, height=26, width=82)
        self.Crypter.configure(activebackground="#ececec")
        self.Crypter.configure(activeforeground="#000000")
        self.Crypter.configure(background="#408080")
        self.Crypter.configure(disabledforeground="#a3a3a3")
        self.Crypter.configure(font=font11)
        self.Crypter.configure(foreground="#000000")
        self.Crypter.configure(highlightbackground="#d9d9d9")
        self.Crypter.configure(highlightcolor="black")
        self.Crypter.configure(pady="0")

        self.Decrypter = Button(
            self, text="Decrypter", command=self.do_decrypter)
        self.Decrypter.place(relx=0.343, rely=0.558, height=26, width=82)
        self.Decrypter.configure(activebackground="#ececec")
        self.Decrypter.configure(activeforeground="#000000")
        self.Decrypter.configure(background="#408080")
        self.Decrypter.configure(disabledforeground="#a3a3a3")
        self.Decrypter.configure(font=font11)
        self.Decrypter.configure(foreground="#000000")
        self.Decrypter.configure(highlightbackground="#d9d9d9")
        self.Decrypter.configure(highlightcolor="black")
        self.Decrypter.configure(pady="0")

        self.Quiter = Button(self, text="Quitter", command=self.quit)
        self.Quiter.place(relx=0.629, rely=0.558, height=26, width=82)
        self.Quiter.configure(activebackground="#ececec")
        self.Quiter.configure(activeforeground="#000000")
        self.Quiter.configure(background="#ff0000")
        self.Quiter.configure(disabledforeground="#a3a3a3")
        self.Quiter.configure(font=font11)
        self.Quiter.configure(foreground="#000000")
        self.Quiter.configure(highlightbackground="#d9d9d9")
        self.Quiter.configure(highlightcolor="black")
        self.Quiter.configure(pady="0")

        self.message = Label(self, text="")
        self.message.place(relx=0.020, rely=0.674, height=112, width=400)
        self.message.configure(activebackground="#f9f9f9")
        self.message.configure(background="#ffffff")
        self.message.configure(disabledforeground="#a3a3a3")
        self.message.configure(highlightbackground="#d9d9d9")
        self.message.configure(highlightcolor="black")

    def Clear(self):
        self.username.delete(0, 'end')
        self.password.delete(0, 'end')
        self.filep.delete(0, 'end')

    def do_crypter(self):
        msg1, msg = crypter(self.password.get(),
                            self.username.get(), self.filep.get())
        self.Clear()
        self.message["text"] = "{}".format(msg)
        self.message["fg"] = "{}".format(msg1)

    def do_decrypter(self):
        msg1, msg = decrypter(self.password.get(),
                              self.username.get(), self.filep.get())

        self.Clear()
        self.message["text"] = "{}".format(msg)
        self.message["fg"] = "{}".format(msg1)


fenetre = Tk()
fenetre.title("Cryptography application")
fenetre.geometry("350x430+654+95")
fenetre.minsize(400, 400)
fenetre.maxsize(400, 400)


interface = Interface(fenetre)
interface.mainloop()
interface.destroy()

from os import path
from fpdf import FPDF
import numpy as np
from PIL import Image


class Errormsg(Exception):  # Exception Errormsg : message d'erreur
    pass


password = ""
username = ""
Folder = ""
filepath = ""


def SetpassWord(pssd, user, filep):
    # fonction permet de stocker password et user name saisie par l'utilisateur
    # dans les variables globale password et username
    global password, username, filepath
    password = pssd
    username = user
    filepath = filep
    msg1, msg2 = Read_file()
    return msg1, msg2


def Read_file():  # Cette fonction permet de lire un fichier
    try:
        global Folder, filepath
        Picture_Path = filepath
        if not path.exists(Picture_Path):
            raise Errormsg(Picture_Path+" not existe")
        if path.splitext(Picture_Path)[1] != ".png":
            raise Errormsg("The Extension of \n image should be .png")
        T = Picture_Path.split("\\")
        T.pop()
        Folder = "\\".join(T)
        msg1, msg = Picture_to_array(Picture_Path)
    except Errormsg as e:
        msg1 = "red"
        msg = "\n\n_________________________________________________________________________\n"
        msg += "\nError !!! , " + repr(e)
        msg += "\n__________________________________________________________________________\n"
    return msg1, msg


def Picture_to_array(Picture_Path):
    Picture = Image.open(Picture_Path, 'r')
    Picture_array = np.array(Picture)
    Picture_array_copy = Picture_array[Picture_array != 0]  # enleve les zeros
    msg1, msg = ASCII_to_Char(Picture_array_copy)
    return msg1, msg


def ASCII_to_Char(Pic):
    T_char = []
    for i in range(len(Pic)):
        T_char.append(chr(Pic[i]))

    msg1, msg = Test_Authentification(T_char)
    return msg1, msg


def Test_Authentification(T_char):
    try:
        for i in range(len(password)):
            if T_char[i] is not password[i]:
                raise Errormsg("password is wrong")
        index = len(password)+1
        for i in range(len(username)):
            if T_char[i+index] is not username[i]:
                raise Errormsg("name of user is wrong")
# remove the password and username from image
        for x in password:
            T_char.remove(x)
        for x in username:
            T_char.remove(x)
        msg1, msg = Write_in_File(T_char)
    except Errormsg as e:
        msg1 = "red"
        msg = "\n\n_________________________________________________________________________\n"
        msg += "\nError !!! , " + str(repr(e))
        msg += "\n__________________________________________________________________________\n"
    return msg1, msg


def Write_in_File(T_char):
    global Folder
    pdf = FPDF()
    pdf.set_font("Arial", size=11)
    texte = ""
    j = 30
    space = 0
    for i in range(len(T_char)):
        if j == 30:  # nombre des lignes
            pdf.add_page()
            j = 0
        # if longeur d'un ligne ou 3 espaces de suit
        if len(texte) == 80 or space > 5:
            l = i+1  # utilisant l = i + 1 car i est commence de 0
            pdf.cell(50, 10, txt=texte, ln=l, align="L")  # nouveau ligne
            j += 1  # incrementer le nombre des lignes
            texte = ""
            space = 0
        else:
            texte += str(T_char[i])
            if str(T_char[i]) == " ":
                space += 1
            else:
                space = 0
    pdf.cell(50, 10, txt=texte, ln=(len(T_char)+1), align="L")
    pdf.output(Folder+"\\Image_decryter.pdf")
    msg1 = "green"
    msg = "\n******************************************************************"
    msg += "\nyour file is successfully decrypted\n it is saved in "+Folder+"\n"
    msg += "******************************************************************"
    return msg1, msg

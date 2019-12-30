import numpy as np
from PIL import Image
from os import mkdir, path
import docx


class Errormsg(Exception):  # Errormsg : message d'erreur
    pass


# Identifient d'utilisateur
password = "motpass"
username = "user"
filepath = ""

# fonction permet de stocker password et user name saisie par l'utilisateur


def SetpassWord(pssd, user, filep):  # dans les variables globale password et username
    global password, username, filepath
    password = pssd
    username = user
    filepath = filep
    msg1, msg2 = Read_file()
    return msg1, msg2


def Read_file():  # Cette fonction permet de lire un fichier
    global filepath
    Extension = [".txt", ".doc", ".docx"]
    tmp = False
    try:
        File_Path = filepath
        for Ex in Extension:
            if path.splitext(File_Path)[1] == Ex:
                tmp = True
                break
        if tmp == False:
            raise Errormsg(
                "the extension of the should be (.txt or .doc or .docx)")
        # test d'abord
        if len(File_Path) == 0:
            raise Errormsg(f"you didn't enter any path")

        if not path.exists(File_Path):
            raise Errormsg("this path<"+File_Path+"> doesn't existe")

        # test d'extension
        if path.splitext(File_Path)[1] == ".docx":
            doc = docx.Document(File_Path)
            Content = []
            for para in doc.paragraphs:
                Content.append(list(para.text))
        else:
            My_File = open(File_Path, 'r')
            Content = My_File.read().split(" ")
            My_File.close()

        if len(Content) == 0:
            raise Errormsg(f"your file <"+File_Path+"> is empty")
        msg1, msg2 = Text_to_array(Content)

    except Errormsg as e:
        msg1 = "red"
        msg2 = "\n____________________________________________________________________\n"
        msg2 += "Error !!! , \n" + repr(e)
        msg2 += "\n_____________________________________________________________________\n"
    return msg1, msg2


# Fonction permet de transfomer un texte à un tableau des tableaux des characteres
def Text_to_array(Texte):
    T = []  # tableau des characteres
    for Word in Texte:
        T.append([" "])
        T.append(list(Word))
    msg1, msg2 = Get_ASCII(T)
    return msg1, msg2


def Get_ASCII(T):  # Permets de transformer chaque caractère à son ASCII correspond
    T_ASCII = []
    T_ASCII.append([])
    for x in password:
        T_ASCII[0].append(ord(x))
    T_ASCII[0].append(ord(" "))

    for x in username:
        T_ASCII[0].append(ord(x))

    for i in range(len(T)):
        T_ASCII.append([])
        for j in range(len(T[i])):
            T_ASCII[i+1].append(ord(T[i][j]))
    msg1, msg2 = Create_picture(T_ASCII)
    return msg1, msg2


def Create_picture(T):
    X = []
    for i in T:
        X.append(len(i))

    # prend la longeur L de T et le plus longue liste dans ce tableau pour nombre des colonnes C
    L, C = (len(T)*10), (max(X)*10)

    # Crée une matrice des zero de L ligne et C colonnes
    T_copy = np.int64(np.zeros((L, C)))

    for i in range(len(T)):
        for j in range(len(T[i])):
            T_copy[i][j] = T[i][j]

    A = Image.fromarray(T_copy, 'RGB')

    folder = "C:\\"+username+" "
    i = 0
    while path.exists(folder+str(i)):  # test if le dossier est deja existe
        i += 1
    folder = folder+str(i)
    mkdir(folder)
    file = folder+"\\"+username+".png"
    A.save(file)
    msg1 = "green"
    msg = "\n******************************************************************"
    msg += "\nyour file is successfully encrypted\n it is saved in "+folder+"\n\n"
    msg += "******************************************************************"
    return msg1, msg

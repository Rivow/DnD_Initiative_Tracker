import random
from tkinter import *


class Character:

    # Constructor
    def __init__(self, name):
        self.name = name


class Enemies(Character):

    def __init__(self, name, initiativebonus):
        super().__init__(name)
        self.initiativebonus = initiativebonus


def pop_up(message):

    root = Tk()
    root.title('Initiative')
    w = 800  # popup window width
    h = 600  # popup window height
    sw = root.winfo_screenwidth()
    sh = root.winfo_screenheight()
    x = (sw - w) / 2
    y = (sh - h) / 2
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

    scrollbar = Scrollbar(root)
    scrollbar.pack(side=RIGHT, fill=Y)

    m = Listbox(root)
    for e in message:
        m.insert(END, e[0].name)
    m.pack(side=LEFT, fill=BOTH)
    scrollbar.config(command=m.yview())

    # w = Label(root, text=m, width=120, height=10)
    # w.config(font=('Courier', 18))
    # w.pack(expand=True)
    b = Button(root, text="OK", command=root.destroy, width=10)
    b.pack(side=BOTTOM)
    mainloop()


def enemy_types():
    noenemytyp = getinteger('Number of Enemies Types: ')
    return noenemytyp


def number_per_typ(totalentyp):
    typdict = {}

    for j in range(0, totalentyp):
        enemytyp = input('Typ of enemy: ')
        totalenemies = getinteger(f'Number of {enemytyp}: ')
        typdict[enemytyp] = int(totalenemies)

    return typdict


# adds enemys
def addenemy(totalen):
    initiativebous = getinteger('Initiative Bonus: ')
    enemy = Enemies(totalen, initiativebous)
    return enemy


# Rolls a random number between 1 and 20
def enemyini(initiativebonus):
    roll = random.randrange(19)+1
    initiative = roll + initiativebonus
    return initiative


def getinteger(message):
    integer = input(message).strip()
    try:
        integer = int(integer)
    except ValueError:
        print('Only accepts Integer')
    return integer


if __name__ == "__main__":
    # input all your character data
    jeff = Character('jeff')
    Sauf = Character('Sauf')
    Thranduil = Character('Thranduil')
    Tanneiros = Character('Tanneiros')
    Kursk = Character('Kursk')
    Ehrenmann = Character('Ehrenmann')

    listplayers = [jeff, Sauf, Thranduil, Tanneiros, Kursk, Ehrenmann]
    ends = ''

    # program loop only quit when input s q
    while True:
        phase = input('Start')
        noenemytypes = enemy_types()
        enemydic = number_per_typ(noenemytypes)
        enemieslist = []

        for EnemyTyp in enemydic:
            Typ = addenemy(EnemyTyp)
            for NoEnemy in range(1, int(enemydic[EnemyTyp])+1):
                Temp = Typ.name
                Temp += str(NoEnemy)
                new = Enemies(Temp, Typ.initiativebonus)
                enemieslist.append(new)

        # Get and make the initiative dictionary to save every enemy and there initiative
        initiativelist = {}
        for x in range(0, len(enemieslist)):
            initiativelist[enemieslist[x]] = enemyini(enemieslist[x].initiativebonus)

        # Sort and calculate every player initiative and check if roll is valid.
        for x in listplayers:
            playerroll = getinteger(f'{x.name} Roll: ')
            initiativelist[x] = playerroll

        orderddic = sorted(initiativelist.items(), key=lambda kv: (float(kv[1]), str(kv[0])))

        # list of sorted initiatives
        initiativeturn = []

        for i in orderddic:
            initiativeturn.append(i)

        # Problem with repeated initiative the sort algorithm choose alphabetacly with the key.
        initiativeturn.reverse()
        nl = '\n'

        # Go through one by one till everyones turn util combat is finisched
        pop_up(initiativeturn)
        ends = input('Do you wanna end? ').strip()
        if ends == 'y':
            break

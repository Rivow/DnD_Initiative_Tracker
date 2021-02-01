import GUI
import random


class Character:

    # Constructor
    def __init__(self, name):
        self.name = name


class Enemies(Character):

    def __init__(self, name, initiativebonus):
        super().__init__(name)
        self.initiativebonus = initiativebonus


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

# name every enemy for exaple: Goblin1, Goblin, 2 and so on
def nameenemy(NoEnemy, Typ):
    namelist = []

    for enemyname in range(1, int(NoEnemy) + 1):
        Temp = Typ.name
        Temp += str(enemyname)
        new = Enemies(Temp, Typ.initiativebonus)
        namelist.append(new)
    return namelist


def getinteger(message):
    integer = input(message).strip()
    try:
        integer = int(integer)
    except ValueError:
        print('Only accepts Integer')
    return integer


def main():
    phase = input('Start')
    noenemytypes = enemy_types()
    enemydic = number_per_typ(noenemytypes)
    enemieslist = []

    for EnemyTyp in enemydic:
        Typ = addenemy(EnemyTyp)
        newenemy = nameenemy(enemydic[EnemyTyp], Typ)
        enemieslist.extend(newenemy)

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
    GUI.pop_up(initiativeturn)




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
        main()
        ends = input('Do you wanna end? ').strip()
        if ends == 'y':
            break


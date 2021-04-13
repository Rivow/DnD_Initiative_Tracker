import random

from gui import pop_up


class Character:


    def __init__(self, name):
        self.name = name


class Enemies(Character):

    def __init__(self, name, initiativebonus):
        super().__init__(name)
        self.initiativebonus = initiativebonus


def enemy_types():
    noenemytyp = output_messege('Number of Enemies Types: ')
    return noenemytyp


def number_per_typ(totalentyp):
    typdict = {}

    for j in range(0, totalentyp):
        enemytyp = input('Typ of enemy: ')
        totalenemies = output_messege(f'Number of {enemytyp}: ')
        typdict[enemytyp] = int(totalenemies)

    return typdict


def create_enemy(totalen):
    initiativebous = output_messege('Initiative Bonus: ')
    enemy = Enemies(totalen, initiativebous)
    return enemy


# Rolls a random number between 1 and 20
def enemy_initiative(initiativebonus):
    roll = random.randrange(20)+1
    initiative = roll + initiativebonus
    return initiative


def output_messege(message):
    loop_check = False
    while loop_check is False:
        integer = input(message).strip()
        loop_check = check_if_inter(integer)

    return int(integer)


def check_if_inter(integer):
    try:
        int(integer)
        return True
    except ValueError:
        print('Only accepts Integer')
        return False




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

    # program loop only quit when input q
    while True:
        phase = input('Start')
        noenemytypes = enemy_types()
        enemydic = number_per_typ(noenemytypes)
        enemieslist = []

        for EnemyTyp in enemydic:
            Typ = create_enemy(EnemyTyp)
            for NoEnemy in range(1, int(enemydic[EnemyTyp])+1):
                Temp = Typ.name
                Temp += str(NoEnemy)
                new = Enemies(Temp, Typ.initiativebonus)
                enemieslist.append(new)

        # Get and make the initiative dictionary to save every enemy and there initiative
        initiativelist = {}
        for x in range(0, len(enemieslist)):
            initiativelist[enemieslist[x]] = enemy_initiative(enemieslist[x].initiativebonus)

        # Sort and calculate every player initiative.
        for x in listplayers:
            playerroll = output_messege(f'{x.name} Roll: ')
            initiativelist[x] = playerroll

        orderddic = sorted(initiativelist.items(), key=lambda kv: (float(kv[1]), str(kv[0])))

        # list of sorted initiatives
        initiativeorder = []

        for i in orderddic:
            initiativeorder.append(i)

        # Problem with repeated initiative the sort algorithm choose alphabetacly with the key.
        initiativeorder.reverse()
        nl = '\n'

        # Go through one by one till everyones turn util combat is finisched
        pop_up(initiativeorder)
        ends = input('Do you wanna end? ').strip()
        if ends == 'y':
            break

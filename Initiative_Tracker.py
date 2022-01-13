import random
import os.path
import pandas as pd

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


def number_per_typ(totalentyp, df):
    typdict = {}

    for j in range(0, totalentyp):
        useExistingEnemy = input('Do you want to use an existing Enemy? (y/n)')

        if useExistingEnemy == 'y':
            typdict = existing_enemy(typdict, df)

        else:
            enemytyp = input('Typ of enemy: ')
            totalenemies = output_messege(f'Number of {enemytyp}: ')
            initiativebous = output_messege('Initiative Bonus: ')
            typdict[enemytyp] = [int(totalenemies), initiativebous]

    return typdict


def existing_enemy(typdict, df):
    listOfExistingEnemies = enemydf.values.tolist()
    print(f'Enemies in Use: \n {df}')
    isIndexInter = False

    while not isIndexInter:
        index = input('Choose the index of the enemy you whant to use(number biside name): ')

        if int(index) <= len(df.index) and is_Inter(index):
            isIndexInter = True
            totalenemies = output_messege(f'Number of {listOfExistingEnemies[int(index)-1][0]}: ')
            initiativebous = listOfExistingEnemies[int(index)-1][1]
            typdict[listOfExistingEnemies[int(index)-1][0]] = [int(totalenemies), initiativebous]
            
    return typdict
    


def create_enemy(totalen, initiativebous):
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
        loop_check = is_Inter(integer)

    return int(integer)


def is_Inter(integer):
    try:
        int(integer)
        return True
    except ValueError:
        print('Only accepts Integer')
        return False

def create_file(filename, titel, initiativeBonus):
    if(os.path.exists(filename) == True):
        return 

    file = open(filename, 'a')
    if initiativeBonus == True:
        file.write(f'{titel}, Initiative Bonus \n')
        file.close()
    else:
        file.write(f'{titel} \n')
        file.close()


def add_character(df, file):
    name = input('Name of the character you whant to add: ')
    file = open(file, 'a')
    file.write(f'{name}\n')
    file.close()
    df.loc[len(df.index)+1] = [name]

def delete_character(df, file):
    index = input('Choose the index of the character you whant to delete(number biside name): ')

    if is_Inter(index) == False:
        return df 

    if int(index) <= len(df.index):
        df = df.drop([int(index)])
        df.to_csv(file, index = False)
        return df

    return df

def delete_all(df, file, titel):
    file = open(file, 'w')
    file.write(f'{titel} \n')
    file.close()


    return df


def add_enemy(df, file):
    isInteger = False
    while not isInteger: 
        name = input('Name of the enemy you whant to add: ')
        initiativeBonus = input('Initiative Bonus: ')
        if is_Inter(initiativeBonus):
            isInteger = True

    file = open(file, 'a')
    file.write(f'{name}, {initiativeBonus}\n')
    file.close()
    df.loc[len(df.index)+1] = [name, initiativeBonus]


def delete_enemy(df, file):
    index = input('Choose the index of the enemy you whant to delete(number biside name): ')

    if is_Inter(index) == False:
        return df 

    if int(index) <= len(df.index):
        df = df.drop([int(index)])
        df.to_csv(file, index = False)
        return df

    return df





if __name__ == "__main__":
    ends = ''

    charFileName = 'Characters.txt'
    enemyFileName = 'Enemies.txt'

    create_file(charFileName, 'Characters', False)
    create_file(enemyFileName, 'Enemies', True)
        
    charList = pd.read_csv(charFileName)
    enemydf = pd.read_csv(enemyFileName)

    charList.index += 1
    enemydf.index += 1

    another_char = 'y'
    another_enemy = 'y'

    # loop to add and delete more characters to the file
    while another_char == 'y':
        if charList.empty:
            add_character(charList, charFileName)

        print(f'Character in Use: \n {charList}')
        another_char = input('Do you want to add or delete a Character? (y/n)').lower()
        if another_char != 'y':
            break
        addOrDelete = input('Add, delete or delete All? (a/ d /delete all)').lower()
        if addOrDelete == 'a':
            add_character(charList, charFileName)
        elif addOrDelete == 'd':
            charList = delete_character(charList, charFileName)
        elif addOrDelete == 'delete all':
            delete_all(charList, charFileName, 'Characters')
            charList = pd.read_csv(charFileName)



    # loop to add and delete more enemies to the file
    while another_enemy == 'y':
        if enemydf.empty:
            add_enemy(enemydf, enemyFileName)

        print(f'Enemies in Use: \n {enemydf}')
        another_enemy = input('Do you want to add or delete a Enemy? (y/n)').lower()
        if another_enemy != 'y':
            break
        addOrDelete = input('Add, delete or delete All? (a/ d /delete all)').lower()
        if addOrDelete == 'a':
            add_enemy(enemydf, enemyFileName)
        elif addOrDelete == 'd':
            enemydf = delete_enemy(enemydf, enemyFileName)
        elif addOrDelete == 'delete all':
            delete_all(enemydf, enemyFileName, 'Enemies, Initiative Bonus')
            enemydf = pd.read_csv(enemyFileName)


    tempList = charList.values.tolist()
    tempList = sum(tempList, [])
    listplayers = []


    for character in tempList:
        character = Character(character)
        listplayers.append(character)
    

    # program loop only quit when input q
    while True:
        input('Start')
        noenemytypes = enemy_types() 
        enemydic = number_per_typ(noenemytypes, enemydf)
        enemieslist = [] 

        for EnemyTyp in enemydic:
            Typ = create_enemy(EnemyTyp, enemydic[EnemyTyp][1])
            
            for NoEnemy in range(1, int(enemydic[EnemyTyp][0])+1):
                Temp = Typ.name
                Temp += str(NoEnemy)
                new = Enemies(Temp, Typ.initiativebonus)
                enemieslist.append(new)
        
        # Get and make the initiative dictionary to save every enemy and there initiative
        initiativelist = {}
        for x in range(0, len(enemieslist)):
            initiativelist[enemieslist[x].name] = enemy_initiative(enemieslist[x].initiativebonus)

        # Sort and calculate every player initiative.
        for x in listplayers:
            playerroll = output_messege(f'{x.name} Roll: ')
            initiativelist[x.name] = playerroll

        orderddic = sorted(initiativelist.items(), key=lambda kv: (float(kv[1]), str(kv[0])))

        # list of sorted initiatives
        initiativeorder = []

        for i in orderddic:
            initiativeorder.append(i)

        # Problem with repeated initiative the sort algorithm choose alphabetacly with the key.
        initiativeorder.reverse()
        nl = '\n'

        # Go through one by one till everyones turn util combat is finisched
        for i in initiativeorder:
            print(i)
        ends = input('Do you wanna end? ').strip()
        if ends == 'y':
            break

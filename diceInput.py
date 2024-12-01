##import regex
import re

##define the input function
def getInput():
    strPattern = '(\d{1,2}\s*[d|D]\s*\d{1,2})'
    strDice = input('Please enter the dice to roll: ')
    if strDice.lower().strip() == 'exit':
        return False
        ##this allows the user to exit the script while it's running
    else:
        listMatches = re.findall(strPattern, strDice, re.DOTALL)
    
    ##check if list of dice is empty (regex failed), else return dice
    if len(listMatches) == 0:
        raise ValueError('Invalid input')
    else:
        print('Input valid')
        listDice = list()
        for match in listMatches:
            listDice.append(str(match).replace(' ','').lower())
        for dice in listDice:
            print(f'Rolling {dice}!')
        return listDice
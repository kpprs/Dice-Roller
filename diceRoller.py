##import input function, die object class, and regex
from diceInput import getInput
from classDice import typeOfDie
import re

##prompt user to start script, receive instructions before starting or exit the script
print('''Enter 'rules' to receive instructions, 'run' to start script or 'exit' to quit''')
strRunRulesExit = input('Enter command: ')
if strRunRulesExit.lower().strip() == 'run':
    print('Starting script')
    boolRun = True
elif strRunRulesExit.lower().strip() == 'rules':
    print('''
            ////////////////////////////////////////////////////////////////////////////////////////////
            ///                         HOW TO:                                                      ///
            /// 1: Format of desired rolls should be xdy                                             ///
            /// 2: You may enter as many dice groups as you want                                     ///
            /// 3: Dice groups should be separated by at least a whitespace, comma or dot            ///
            /// 4: The dice roller is designed to roll classic DnD dice; deviation gives a type error///
            /// 5: You can exit the script by typing 'exit' in the prompt                            ///
            ///                     STARTING SCRIPT                                                  ///
            ////////////////////////////////////////////////////////////////////////////////////////////         
        ''')
    boolRun = True
elif strRunRulesExit.lower().strip() == 'exit':
    print('Exiting script')
    boolRun = False
else:
    print('Invalid command, exiting script')
    boolRun = False

##keep rolling dice until user exits script
while boolRun:
    try:
        ##get the user input and prepare variables to handle results
        listDice = getInput()
        if listDice == False:
            boolRun = False
            continue
        listResults = list()
        intTotalResult = 0

        ##find the amount and type(s) of dice to roll
        for dice in listDice: 
            matchCount = re.search(r'(^\d{1,2})',str(dice))
            matchType = re.search(r'([d]\d{1,2}$)',str(dice))
            if matchCount and matchType:
                intDieCount = int(matchCount.group())
                ##cast strDieType as the die object with input from regex search
                strDieType = typeOfDie(str(matchType.group())) 

            ##roll the actual dice and store each roll and die type in the results list
            for _ in range(intDieCount):
                intResult = strDieType.rollDie()
                listResults.append({strDieType:intResult})

        ##print the results and sum them
        ##result of d20s are excluded due to non-damage die
        for result in listResults:
            for strDieType, intResult in result.items():
                if intResult == 20:
                    print('Natural 20!')
                elif intResult == 1 and strDieType.strDieType == 'd20':
                    print('''Uh oh, that's a fumble...''')
                else:
                    print(f'Roll result: {intResult} on a {strDieType.strDieType}')
                if strDieType.strDieType == 'd20':
                    continue
                else:
                    intTotalResult = intTotalResult + intResult

        ##print the total roll sum of non-d20s
        print(f'Total result of rolls excluding d20s: {intTotalResult}')
    except:
        print('Invalid input, try again')
        ##catch input errors
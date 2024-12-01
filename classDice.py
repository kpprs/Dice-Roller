##import random to generate roll results
import random

##define the die object
class typeOfDie:
    def __init__(self, dieType: str) -> None:
        self.strDieType = dieType

    ##define valid die types and their max results
    def rollDie(self):
        dictDieMaxValues = {
            'd4':   4,
            'd6':   6,
            'd8':   8,
            'd10':  10,
            'd12':  12,
            'd20':  20
        }

        maxRoll = dictDieMaxValues.get(self.strDieType)

        ##roll the die if valid type and return result, else raise typeerror
        if maxRoll and self.strDieType == 'd20':
            print('Rolling for initiative!')
            return random.randint(1,maxRoll)
        elif maxRoll:
            print(f'Rolling a {self.strDieType}!')
            return random.randint(1,maxRoll)
        else:
            print(f'Invalid type: {self.strDieType}')
            raise TypeError('Invalid die type')
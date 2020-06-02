import json
from C_Card import Card
from C_MonsterCard import MonsterCard
from C_SpellCard import SpellCard
from C_TrapCard import TrapCard
import C_Combo
from main import MakeNewCard



inputFileName = "../Resources/Decks/CardCollection.txt"
outputFileName = "../Resources/Decks/CardCollection.json"



def ReadList(inputFileName):

    toDict = []
    print("\nDeck loaded from: "+inputFileName)
    inputFile = open(inputFileName,'r')
    lines = inputFile.readlines()
    inputFile.close()
    for line in lines:
        line = line.strip()
        if(line[0] != '#'):
            temp = line.strip().split('|')
            toDict.append(MakeNewCard(temp))
    return toDict

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, indent=4)
    print(text)

def jwrite(obj,outputFileName):
    outputFile = open(outputFileName,'w')
    text = json.dumps(obj, indent=4)
    outputFile.write(text + "\n")

#def ListToDict():

ReadList(inputFileName)
itemsDict = {}
counter = 0
for item in ReadList(inputFileName):
    print(item.name)
    if(item.cardType == "MONSTER"):
        tempDict = {"Name":item.name,"CardType":item.cardType,"HasEffect":item.hasEffect,"Level":item.level,"MonsterType":item.monsterType,"Attribute":item.attribute,"IsTuner":item.isTuner,"IsHandtrap":item.isHandtrap}
        #itemsDict.update( {"MONSTER":{counter:tempDict} } )
    elif(item.cardType == "SPELL"):
        tempDict = {"Name":item.name,"CardType":item.cardType,"SpellType":item.spellType}
    elif(item.cardType == "TRAP"):
        tempDict = {"Name":item.name,"CardType":item.cardType,"SpellType":item.trapType,"IsHandtrap":item.isHandtrap}

    itemsDict.update( {counter:tempDict} )
    counter+=1

json.dumps(itemsDict)
jprint(itemsDict)
jwrite(itemsDict,outputFileName)

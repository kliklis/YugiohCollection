import sys
from random import shuffle
from C_Card import Card
from C_MonsterCard import MonsterCard
from C_SpellCard import SpellCard
from C_TrapCard import TrapCard
import C_Combo

LOG_ONLY_TOTAL_STATS = 0
LOG_EVERY_HAND_STATS = 1
LOG_EVERY_HAND_STATS = 2
LOG_FULL = 3

LOG_INTENSITY = LOG_FULL

EXPORT = True

def main():
    global LOG_INTENSITY, EXPORT

    
    if(len(sys.argv) > 0):
        LOG_INTENSITY = int(sys.argv[1])
        if(sys.argv[2] == 0):
            EXPORT = False
        elif(sys.argv[2] == 1):
            EXPORT = True
        deckFileName = sys.argv[3]
        combosFileName = sys.argv[4]
    

    '''
    LOG_INTENSITY = 3
    EXPORT = True
    deckFileName = "Resources/Decks/Deck.txt"
    combosFileName = "Resources/Combos/Combos.txt"
    '''
    

    outputFile = open("deckStats.txt","w")

    #uncomment to ask for verbality in runtime
    #question = '''How much do you want me to talk?\n
    #0. Show only total ratios(fastest).\n
    #1. Everything except test hands.\n
    #2. Everything except deck.\n
    #3. Everything lil'bitch! (slowest).'''
    #LOG_INTENSITY = str(input(question))


    DECK = ReadDeck(outputFile, deckFileName)
    COMBOS = ReadCombos(outputFile, combosFileName)
    combosOccurences = [0]*len(COMBOS)

    PrintDeck(outputFile, DECK)
    ExportDeck(outputFile, DECK)
    PrintCombos(outputFile, COMBOS)
    ExportCombos(outputFile, COMBOS)

    handSize = 5

    monstersRatios =  []
    spellsRatios =    []
    trapsRatios =     []
    handtrapsRatios = []
    combosDetected =  []

    totalCards =      0
    totalHandtraps =  0
    totalMonsters =   0
    totalSpells =     0
    totalTraps =      0
    totalCombos =     0

    testHandsNum = int(input("\nGive the number of testhands: "))

    #for every testHand
    for i in range(testHandsNum):
        combosNum = 0
        testHand = []
        shuffle(DECK)

        if(LOG_INTENSITY >= 2):
            print("__________________________________________________________Hand #"+str(i))
            outputFile.write("__________________________________________________________Hand #"+str(i)+"\n")

        #for every card in the current hand
        for j in range(handSize):
            currentCard = DECK[j]
            testHand.append(currentCard)
            if(LOG_INTENSITY >= 2):
                print(currentCard.name)
            totalCards += 1

            if(currentCard.cardType == "MONSTER"):
                totalMonsters += 1
                if(currentCard.isHandtrap == "HANDTRAP"):
                    totalHandtraps += 1
            elif(currentCard.cardType == "SPELL"):
                totalSpells += 1
            elif(currentCard.cardType == "TRAP"):
                totalTraps += 1
                if(currentCard.isHandtrap == "HANDTRAP"):
                    totalHandtraps += 1
        
        #combos check
        for currentCombo in COMBOS:
            tempTestHand = testHand[:]
            tempComboCards = currentCombo.cardsRequired[:]
            for j in tempTestHand:
                for i in tempComboCards:
                    if(j.name==i.name or i.name == "@MONSTER"):
                        tempComboCards.remove(i)
                        if( len(tempComboCards) == 0 ):
                            combosOccurences[ COMBOS.index(currentCombo) ] = combosOccurences[ COMBOS.index(currentCombo) ] + 1
                            combosDetected.append( currentCombo )
                            combosNum += 1
                            totalCombos += 1
                            break

        monstersRatio = totalMonsters*100 / totalCards
        spellsRatio =totalSpells*100 / totalCards
        trapsRatio = totalTraps*100 / totalCards
        handtrapsRatio = totalHandtraps*100 / totalCards
        
        monstersRatios.append(monstersRatio)
        spellsRatios.append(spellsRatio)
        trapsRatios.append(trapsRatio)
        handtrapsRatios.append(handtrapsRatio)

        avgMonstersRatio = sum(monstersRatios) / len(monstersRatios)
        avgSpellsRatio = sum(spellsRatios) / len(spellsRatios)
        avgTrapsRatio = sum(trapsRatios) / len(trapsRatios)
        avgHandtrapsTatio = sum(handtrapsRatios) / len(handtrapsRatios)
        avgCombosRatio = totalCombos / testHandsNum
        
        PrintHandStats(monstersRatio, spellsRatio, trapsRatio, handtrapsRatio, combosNum)
        ExportHandStats(outputFile,monstersRatio, spellsRatio, trapsRatio, handtrapsRatio, combosNum)

        
    PrintTotalStats(testHandsNum, COMBOS, combosOccurences, avgMonstersRatio, avgSpellsRatio, avgTrapsRatio, avgHandtrapsTatio, avgCombosRatio, totalCombos)
    ExportTotalStats(outputFile, testHandsNum, COMBOS, combosOccurences, avgMonstersRatio, avgSpellsRatio, avgTrapsRatio, avgHandtrapsTatio, avgCombosRatio, totalCombos)

    outputFile.close()
    input("\n\nPRESS ENTER TO EXIT.")

def PrintDeck(outputFile, deck):
    if(LOG_INTENSITY >= 3):
        print("________DECK:")
        for i in range(len(deck)):
            print(str(i+1)+". "+deck[i].name)
        print()

def ExportDeck(outputFile, deck):
    if(LOG_INTENSITY >= 3):
        outputFile.write("________DECK:\n")
        for i in range(len(deck)):
            outputFile.write(str(i+1)+". "+deck[i].name+"\n")
        outputFile.write("\n")

def PrintCombos(outputFile, combos):
    if(LOG_INTENSITY >= 3):
        print("________COMBOS:")
        for i in range(len(combos)):
            print(str(i+1)+". "+combos[i].comboName)
        print()

def ExportCombos(outputFile, combos):
    if(LOG_INTENSITY >= 3):
        outputFile.write("________COMBOS:\n")
        for i in range(len(combos)):
            outputFile.write(str(i+1)+". "+combos[i].comboName+"\n")
        outputFile.write("\n")

def PrintHandStats(monstersRatio, spellsRatio, trapsRatio, handtrapsRatio, combosNum):
    global LOG_INTENSITY
    if(LOG_INTENSITY >= 1):
            print()
            print("  -->  |  Monsters ratio:    "+str(round(monstersRatio, 2))+"%") 
            print("  -->  |  Spells ratio:      "+str(round(spellsRatio, 2))+"%")
            print("  -->  |  Traps ratio:       "+str(round(trapsRatio, 2))+"%")
            print("  -->  |  Handtraps ratio:   "+str(round(handtrapsRatio, 2))+"%")
            print("  -->  |  Number of combos:  "+str(combosNum))

def PrintTotalStats(testHandsNum, combos, combosOccurences, avgMonstersRatio, avgSpellsRatio, avgTrapsRatio, avgHandtrapsTatio, avgCombosRatio, totalCombos):
    print("\n\n\n")
    print("__________________________________________________________Testhands completed.")
    print("  ---->  |  Average monsters per hand ratio:      "+str(round(avgMonstersRatio, 2))+"%") 
    print("  ---->  |  Average spells per hand ratio:        "+str(round(avgSpellsRatio, 2))+"%")
    print("  ---->  |  Average traps per hand ratio:         "+str(round(avgTrapsRatio, 2))+"%")
    print("  ---->  |  Average handtraps per hand ratio:     "+str(round(avgHandtrapsTatio, 2))+"%")
    print("  ---->  |  Average combos per hand ratio:        "+str(round(avgCombosRatio, 2))+"%")
    print("  ---->  |  Total number of combos in all hands:  "+str(totalCombos))

    print("\n")
    print("__________________________________________________________Achieved Combos:")
    if(LOG_INTENSITY >= 0):
        for combo in combos:
            print( "{0:30}: achieved in {1:1} out of {2:1} testhands. ({3:1}%)".format(combo.comboName,combosOccurences[ combos.index(combo) ],str(testHandsNum), round( (combosOccurences[ combos.index(combo) ] / testHandsNum) * 100 ), 2) )

def ExportHandStats(outputFile,monstersRatio, spellsRatio, trapsRatio, handtrapsRatio, combosNum):
    global LOG_INTENSITY
    if(LOG_INTENSITY >= 1):
            outputFile.write("\n  -->  |  Monsters ratio:    "+str(round(monstersRatio, 2))+"%\n") 
            outputFile.write("  -->  |  Spells ratio:      "+str(round(spellsRatio, 2))+"%\n")
            outputFile.write("  -->  |  Traps ratio:       "+str(round(trapsRatio, 2))+"%\n")
            outputFile.write("  -->  |  Handtraps ratio:   "+str(round(handtrapsRatio, 2))+"%\n")
            outputFile.write("  -->  |  Number of combos:  "+str(combosNum)+"\n")

def ExportTotalStats(outputFile, testHandsNum, combos, combosOccurences, avgMonstersRatio, avgSpellsRatio, avgTrapsRatio, avgHandtrapsTatio, avgCombosRatio, totalCombos):
    outputFile.write("\n\n\n")
    outputFile.write("__________________________________________________________Testhands completed.\n")
    outputFile.write("  ---->  |  Average monsters per hand ratio:      "+str(round(avgMonstersRatio, 2))+"%\n") 
    outputFile.write("  ---->  |  Average spells per hand ratio:        "+str(round(avgSpellsRatio, 2))+"%\n")
    outputFile.write("  ---->  |  Average traps per hand ratio:         "+str(round(avgTrapsRatio, 2))+"%\n")
    outputFile.write("  ---->  |  Average handtraps per hand ratio:     "+str(round(avgHandtrapsTatio, 2))+"%\n")
    outputFile.write("  ---->  |  Average combos per hand ratio:        "+str(round(avgCombosRatio, 2))+"%\n")
    outputFile.write("  ---->  |  Total number of combos in all hands:  "+str(totalCombos)+"\n")

    outputFile.write("\n")
    outputFile.write("__________________________________________________________Achieved Combos:\n")
    if(LOG_INTENSITY >= 0):
        for combo in combos:
            outputFile.write( "{0:30}: achieved in {1:1} out of {2:1} testhands. ({3:1}%)\n".format(combo.comboName,combosOccurences[ combos.index(combo) ],str(testHandsNum), round( (combosOccurences[ combos.index(combo) ] / testHandsNum) * 100 ), 2) )


def ReadDeck(outputFile, deckFileName):
    global LOG_INTENSITY

    deck = []
    if(LOG_INTENSITY >= 2):
            print("\nDeck loaded from: "+deckFileName)
            outputFile.write("Deck loaded from: "+deckFileName+"\n")
    inputFile = open(deckFileName,'r')
    lines = inputFile.readlines()
    inputFile.close()

    for line in lines:
        line = line.strip()
        if(line[0] != '#'):
            temp = line.strip().split('|')
            deck.append(MakeNewCard(temp))
    return deck



def ReadCombos(outputFile, combosFileName):
    global LOG_INTENSITY
    combos = []

    if(LOG_INTENSITY >= 2):
            print("Combos loaded from: " + combosFileName+"\n")
            outputFile.write("Combos loaded from: "+combosFileName+"\n\n")
    inputFile = open(combosFileName,'r')
    lines = inputFile.readlines()
    inputFile.close()

    combosInput = "\n".join(lines).split("_")
    #print(composInput)
    for combo in combosInput:
        #print(combo+" - end")
        tempComboName = ""
        tempComboRequiredCards = []
        tempComboDescription = "Random Descr..."
        combo = combo.split("\n")
        for c in combo:
            if(c==""):
                combo.remove(c)
        for line in combo:
            #print()
            #print(line)
            if( len(line) > 0 ):
                if(line[0] == "#"):
                    tempComboName = line[1:]
                elif(line[0] == "@"):
                    if(line[1:] == "MONSTER"):
                        tempComboRequiredCards.append( MakeNewCard( ("@MONSTER", "-", "-", "-", "-", "-", "-", "-")) )
                else:
                    tempComboRequiredCards.append( MakeNewCard( line.strip().split('|') ) )
        newCombo = MakeNewCombo( (tempComboName, tempComboRequiredCards, tempComboDescription) )
        if( newCombo not in combos ):
            combos.append( newCombo )
    return combos

def MakeNewCard(temp):
    newCard = None
    if(temp[1] == "MONSTER" or temp[0] == "@MONSTER"):
        name, cardType, hasEffect, level, attribute, theType, isTuner, isHandtraprap = temp
        newCard = MonsterCard( name, cardType, hasEffect, level, attribute, theType, isTuner, isHandtraprap )
    elif(temp[1] == "SPELL"):
        name, cardType, theType = temp
        newCard = SpellCard( name, cardType, theType )
    elif(temp[1] == "TRAP"):
        name, cardType, theType, isHandtraprap = temp
        newCard = TrapCard( name, cardType, theType, isHandtraprap )
    return newCard

def MakeNewCombo(comboArgs):
    comboName, cardsRequired, description = comboArgs
    return C_Combo.Combo(comboName, cardsRequired, description)


if __name__ == "__main__":
    main()

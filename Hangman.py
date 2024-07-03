
import os
import random

words_list = []

# Hangman.txt - Text Datei mit einer Liste von 100 zufälligen Wörtern

path = "C:/Users/051500/Desktop/Bondar/Hangman.txt"
# path = "C:/Users/bondr/PycharmProjects/Learning/Hangman.txt"
# path = "C:/Users/051500/PycharmProjects/Bondar"

def isLetterUsed(letter, usedLetters):
    for x in usedLetters:
        if x == letter:
            return True
    return False


# -------------------  Spiel-Engine -------------------------------
def gameHangman(wordAnswer):
    attempt = 10
    listAnswer = list(wordAnswer.lower())
    word = []
    usedLetters = []

    for i in range(len(listAnswer)):
        word.append("_")


    while True:
        for i in range(10):
            print("")

        isletter = False

        print("Erraten Sie das Wort(ein Produkt oder ein Artikel ):")
        print(word)
        print(f"Sie haben noch {attempt} Versuche")
        print(f"Sie haben schon diese Buchstaben eingegeben{usedLetters}")
        letter = input("Buchstabe eingeben: ")

        if not letter.isalpha():
            print("Nur Buchstaben eingeben!")
        else:
            letter = letter.lower()
            if isLetterUsed(letter, usedLetters):
                print(f"Sie haben schon diese Buchstabe eingegeben")
                continue
            else:
                usedLetters.append(letter)
                for i in range(len(wordAnswer)):
                    if listAnswer[i] == letter:
                        word[i] = letter
                        isletter = True

                if isletter == False:
                    attempt = attempt - 1

                if attempt == 0:
                    print("Du hast verloren!")
                    print(f"Das Wort, das erraten werden musste: {word}")
                    return

                if word.count("_") == 0:
                    print("Du hast gewonnen!")
                    print(f"Das gewinnende Wort: {word}")
                    return



# -------------------------- main program ----------------------------------------------

if os.path.exists(path):
    f = open(path)
    words_list = f.read().rsplit("\n")
    stringFromFile = f.read()
    f.close

    while True:
        print("1. Neues Spiel")
        print("2. Beenden das Programm")
        userSelect = input("Wählen Sie eine Option:")

        if not userSelect.isdigit():
            print("Drücken Sie nur 1 oder 2")
            continue
        else:
            userSelect = int(userSelect)
            if userSelect < 1 or userSelect > 2:
                print("Drücken Sie nur 1 oder 2")
                continue
            else:
                randomNumber = random.randint(0, (len(words_list)-1))
                wordAnswer = words_list[randomNumber]
                gameHangman(wordAnswer)
                words_list.pop(randomNumber)
            if userSelect == 2:
                    break

else:
    print("Es sind keine Wörter mehr zur Auswahl. Es kann nicht mehr gespielt werden.")


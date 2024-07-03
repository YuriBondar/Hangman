
import os

# I have a now comment
# I have a now comment 2


words_list = []
path = '"C:/Users/051500/Desktop/Bondar/Hangman.txt"'


def gameHangman(word):

    attempt = 10    
    gameWord = "---------------------------------------------------------------------"
    gameWord = gameWord[:word.length()+1]

    while True: 
        print("Find out this word:")
        print(gameWord)
        print(f"Attempt: {attempt}")
        gameLetter = input("Input letter: ")

        for i in range:
            if i == gameLetter 





# -------------------------- main programe ----------------------------------------------

if os.path.exists(path):
        f = open(path)
        words_list = f.read().rsplit("\n") 
        stringFromFile = f.read()
        f.close
else:
    print("Something wrong. There is not database with words. Call support servise: 900-77-88")


while True:

    print("Wählen Sie eine Option:")
    print("1. New game")
    print("2. Out")

    if not userChoise.isdigit():
        print("Drucken Sie Zahlen von 1 bis 2")
        continue
    else:
        userChoise = int(userChoise)
        if  userChoise < 1 or userChoise > 2:
            print("Drucken Sie Zahlen von 1 bis 2")
            continue
        else:
            randomNumber = int(round((words_list.count() * random.random() + 1), 0)) 
            gameHangman(words_list[randomNumber])
            words_list.pop(randomNumber)
        if userChoise == 2:
                break


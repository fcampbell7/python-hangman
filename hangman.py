'''
A simple hangman game
'''

import random

def main():
    difficulty = startGame()
    easy = ['cafe','soar','hill','foot','turn','toll','sand','will','hole','gear']
    medium = ['danger','volume','listen','Europe','ladder','morsel','effort','relate','lounge','outfit']
    hard = ['bathroom','consumer','positive','discover','interest','ceremony','ancestor','diplomat','activity','folklore']

    word = ""
    
    if difficulty == "easy":
        word = easy[random.randrange(len(easy)+1)]

    if difficulty == "medium":
        word = medium[random.randrange(len(medium)+1)]

    if difficulty == "hard":
        word = hard[random.randrange(len(hard)+1)]
    
    playGame(word)
    

def startGame():
    sentence = "H A N G M A N"
    version = "v0.1"
    stars = len(sentence) * "*"
    spaces = ((len(sentence) - len(version))//2) * " "

    print(stars)
    print(sentence)
    print(spaces + version + spaces)
    print(stars)
    print("")
    print("")

    sentence = "Welcome to hangman. Please select a difficulty or type 'help'."
    mode = "Easy    Medium     Hard"
    spaces = ((len(sentence) - len(mode))//2) * " "
    print(sentence)
    print(spaces + mode + spaces)

    difficulty = str(input("> ")).lower()

    while difficulty != "easy" and difficulty != "medium" and difficulty != "hard":
        if difficulty == "help":
            print("Type 'easy', 'medium' or 'hard' to choose your difficulty")
        else:
            print("Invalid option. Please try again.")
        difficulty = str(input("> ")).lower()
    print("")
    print(len(sentence)*"=")
    print("Starting game on", difficulty, "mode.")
    print(len(sentence)*"=")

    return difficulty


def playGame(word):
    clueOutput = list(len(word) * "_")
    letterCount = len(word)
    lives = 6

    while lives > 0 and letterCount > 0:
        print("You have",lives,"lives left.")
        print(' '.join(clueOutput))
        guess = str(input("> ")).lower()

        while len(guess)>1:
            print("Guess is longer than one letter. Please try again.")
            guess = str(input("> ")).lower()
            
        outcome = False
        for i in range(len(word)):
            if word[i] == guess:
                outcome = True
                letterCount -= 1
                clueOutput[i] = guess
                
        if outcome == True:
            print("Correct!")
                
        if outcome == False:
            lives -= 1
            print("Incorrect!")

    if letterCount == 0:
        sentence = "Congratulations, you won! The word was " + word
        print("*"*len(sentence))
        print(sentence)
        print("*"*len(sentence))

    if lives == 0:
        sentence = "Game over! The word was " + word
        print("*"*len(sentence))
        print(sentence)
        print("*"*len(sentence))

    print("\n Play again? Type yes or no")
    response = str(input("> ")).lower()

    while response != "yes" and response != "no":
        print("Invalid option. Please try again.")
        response = str(input("> ")).lower()

    if response == "yes":
        print("\n\n")
        main()
    else:
        print("Goodbye.")
        
        

main()
    

import random


def main():
    randomNumber = random.randint(1,100)
    found = False
    counter = 5
    print( 'Welcome to the number Guessing game\n'
           '-------------------------------------\n'
           'Rules are simple, Guess the number between 1 and 100 which Genie has in his mind\n'
           '-------------------------------------\n'
           'Catch is, you have only 5 chances to guess\n'
           '-------------------------------------\n'
           )


    while counter > 0:

        randomNumber = random.randint( 1, 100 )
        print(randomNumber)
        found = False
        while not found:
            userGuess = int( input( 'your guess: ' ) )
            if userGuess == randomNumber :
                print( "You got it!" )
                found = True
            elif userGuess > randomNumber and counter >0:
                print( "Guess lower!" )
            else:
                print( "Guess higher!" )
                # Print contratulations and goodbye
        print( "Thanks for playing our game." )
        counter = counter-1

main()


import random


running = True
playing = True

while running:
    numMax = 100
    numMin = 1
    Num = random.randint(numMin,numMax)   #set up the game
    tries = 0

    while playing:    #start the round
        print ('Guess the number between ' + str(numMin) + ' and ' + str(numMax))
        guess = int(input())
        tries += 1   #count tries

        if guess == Num:
            print ('Correct!')
            playing = False  #end round if correct
        elif guess > Num:
            print ('Try guessing Lower')
        else:
            print ('Try Guessing Higher')
        print ()

    print('Thanks for playing!, you took ', tries, ' tries.')
    print("Press 'r' to replay or 'q' to quit.")
    ans =  input()

    if ans == 'r':
        playing = True
    elif ans == 'q':
        break
    else:
        print('oops what you entered is invalid.')
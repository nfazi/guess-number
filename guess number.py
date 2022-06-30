import random
number = random.randint(1, 10)

def papar(guess, number_of_guesses): #procedure memaparkan tekaan nombor
    if guess == number:
        print('\nYou guessed the number in ' + str(number_of_guesses) + ' tries!')
    else:
        print('\nYou did not guess the number, The number was ' + str(number) +'.')

#main menu
aktif = 1
#number_of_guesses = 0
print('\n\n*****Guessing the number*****\n')
player_name = input('Hello, What is your name? ')

while aktif == 1: #loop games
    print('\nOk! '+ player_name+ '.I am Guessing a number between 1 and 10.')
    print('Do you want to play this game? Type 1 for Yes/ 2 for No')
    play = int(input('\nEnter your choice: '))
    if play == 2: #input 2 untuk berhenti
        aktif = 0
    elif play == 1: #input 1 untuk main games
        number_of_guesses = 0
        while number_of_guesses < 5:
            guess = int(input('Enter your number: '))
            number_of_guesses += 1
            if guess < number:
                print('Your guess is too low')
            elif guess > number:
                print('Your guess is too high')
            else : 
                break
        papar(guess, number_of_guesses)
    else: #input salah
        print('\nWrong input!')
            
print('Thank you.')


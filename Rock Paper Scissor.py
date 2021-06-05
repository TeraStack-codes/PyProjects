import random

#variable

computer = 0
user = 0



while True:
    #Get input from the user

    choice = input("Choose R, P or S: ")
    choice = choice.lower()

    #Generate a Random Computer Choice

    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = 'r'

    elif comp_choice == 2:
        comp_choice = 'p'

    elif comp_choice == 3:
        comp_choice = 's'


    #Compare the Choices

    if comp_choice == choice:
        print(f'It was a Tie\nComputer Choice = {comp_choice}\nYour Choice = {choice}')

    #cases of user losing
    elif comp_choice == 'r' and choice == 's':
        print(f'Computer wins\nComputer Choice = {comp_choice}\nYour Choice = {choice}')
        computer = computer + 1

    elif comp_choice == 's' and choice == 'p':
        print(f'Computer wins\nComputer Choice = {comp_choice}\nYour Choice = {choice}')
        computer = computer + 1

    elif comp_choice == 'p' and choice == 'r':
        print(f'Computer wins\nComputer Choice = {comp_choice}\nYour Choice = {choice}')
        computer =computer + 1

    #User wins

    elif comp_choice == 's' and choice == 'r':
        print(f'You win\nComputer Choice = {comp_choice}\nYour Choice = {choice}')
        user = user + 1

    elif comp_choice == 'p' and choice == 's':
        print(f'You win\nComputer Choice = {comp_choice}\nYour Choice = {choice}')
        user = user + 1

    elif comp_choice == 'r' and choice == 'p':
        print(f'You win\nComputer Choice = {comp_choice}\nYour Choice = {choice}')
        user = user + 1

    #Get and show result

    print(f'Your Score: {user}\nComputer Score: {computer}')

    #Ask if the user wants to play again

    ask = input('Do you want to play again??\ny for yes and n for no: ')
    ask = ask.lower()
    if ask == 'n':
        break



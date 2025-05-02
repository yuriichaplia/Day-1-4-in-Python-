import random
import symbols

user_number = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
list_of_symbols = [symbols.rock, symbols.paper, symbols.scissors]

if 0 <= user_number <= 2:
    print(list_of_symbols[user_number])
    computer_number = random.randint(0, 2)

    print("Computer chose: ")
    print(list_of_symbols[computer_number])

    if user_number == computer_number:
        print("It's a draw")
    elif computer_number == user_number + 1 and user_number < 2:
        print("You lose")
    elif user_number == 2 and computer_number == 0:
        print("You lose")
    else:
        print("You win!")
else:
    print("You typed an invalid number, you lose!")




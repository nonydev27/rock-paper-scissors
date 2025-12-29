# import random

# user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
# comp_random = random.choice(user_choice) 

# if user_choice  not in ['r', 'p', 's']:
#      print('Please your choice is invalid!')

# emojis = {'r': '🪨', 's': '✂️', 'p': '📄'}
# choices = ('r', 'p', 's')

# # op1 = 'rock '
# # op2 = 'scissors '
# # op3 = 'paper '

# while True:
#     if user_choice == 'r':
#         print(f'You chose {emojis[user_choice]}')
#         print(f'Computer chose {emojis[comp_random]}')
#         break
#     elif user_choice == 'p':
#         print(f'You chose {emojis[user_choice]}')
#         print(f'Computer chose {emojis[comp_random]}')
#         break
#     elif user_choice == 's':
#         print(f'You chose {emojis[user_choice]}')
#         print(f'Computer chose {emojis[comp_random]}')
#         break

#     user_continue = input('Continue? (y/n): ').lower()




import random

emojis = {'r': '🪨', 's': '✂️', 'p': '📄'}
choices = ('r', 'p', 's')

def get_user_choice():
    while True:


        user_choice = input('Rock, paper, or scissors? (r/p/s): ').lower()
        if user_choice not in choices:
            print('Invalid choice!')
        computer_choice = random.choice(choices)
        print(f'You chose {emojis[user_choice]}')
        print(f'Computer chose {emojis[computer_choice]}')

        if user_choice ==  computer_choice:
            print('Tie!')
        elif user_choice == 'r' and computer_choice == 'p':
            print('You win!') 
        elif user_choice == 's' and computer_choice == 'p':
            print('You win!') 
        elif user_choice == 'p' and computer_choice == 'r':
            print('You win!') 
        else:
            print(' You lose!') 

        should_continue = input('Contniue? (y/n): ').lower()
        if should_continue == 'n':
            break
user_choice = input('Rock, paper, or scissors? (r/p/s): ')

op1 = 'rock 🪨'
op2 = 'scissors ✂️'
op3 = 'paper 📄'

while True:
    if user_choice == 'r':
        print(f'You chose {op1}')
        break
    elif user_choice == 'p':
        print(f'You chose {op3}')
        break
    elif user_choice == 's':
        print(f'You chose {op2}')
        break

    user_continue = input('Continue? (y/n): ').lower()
    


if user_choice  not in ['r', 'p', 's']:
     print('Please your choice is invalid!')

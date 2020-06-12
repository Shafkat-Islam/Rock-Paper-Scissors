def rps():
    import random
    gg = input('Enter: ')
    str = gg.lower()
    if str == 'rock' or str == 'paper' or str == 'scissors':
        hh = random.randrange(1, 4)
        if hh == 1:
            comp = 'rock'
        elif hh == 2:
            comp = 'paper'
        else:
            comp = 'scissors'
        if str == 'rock' and comp == 'rock':
            print(f'You played: {gg} and computer played: {comp}')
            print('Draw! Try again!')
        elif str == 'rock' and comp == 'paper':
            print(f'You played: {gg} and computer played: {comp}')
            print('You Lose!')
        elif str == 'rock' and comp == 'scissors':
            print(f'You played: {gg} and computer played: {comp}')
            print('You Win!')
        elif str == 'paper' and comp == 'paper':
            print(f'You played: {gg} and computer played: {comp}')
            print('Draw! Try again!')
        elif str == 'paper' and comp == 'rock':
            print(f'You played: {gg} and computer played: {comp}')
            print('You Win!')
        elif str == 'paper' and comp == 'scissors':
            print(f'You played: {gg} and computer played: {comp}')
            print('You Lose!')
        elif str == 'scissors' and comp == 'paper':
            print(f'You played: {gg} and computer played: {comp}')
            print('You Win!')
        elif str == 'scissors' and comp == 'rock':
            print(f'You played: {gg} and computer played: {comp}')
            print('You Lose!')
        elif str == 'scissors' and comp == 'scissors':
            print(f'You played: {gg} and computer played: {comp}')
            print('Draw! Try again!')
    else:
        print('Input either Rock or Paper or Scissors')

rps()
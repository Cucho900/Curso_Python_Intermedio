import os
import random

def word():
    with open('./archivos/data.txt', 'r') as f:
        list = [i for i in f]
        words = [i.replace('\n','') for i in list]
        
        words_dict = {c: value for c, value in enumerate(words)}
        word = words_dict.get(random.randint(0, len(words) - 1))
    return word


def main():
    word_to_guess = word().upper()
    underscores = ['_']*len(word_to_guess)

    count = 9
    
    while True:
        clue = "".join(underscores)

        if word_to_guess == clue:
            os.system('clear')
            print(f'Ganaste!\nLa palabra era {word_to_guess}')
            break
        
        if count == 0:
            os.system('clear')
            print(f'Perdiste!\nLa palabra era {word_to_guess}')
            break
        
        os.system('clear')
        print('Juego del ahorcado')
        print(f'Tienes {count} intentos')
        print(clue)
        letter = input('Inserte una letra: ').upper()
        
        for c, value in enumerate(word_to_guess):
            if letter == value:
                underscores[c] = letter
        
        if letter in list(word_to_guess):
            pass
        else:
            count -= 1



if __name__ == '__main__':
    main()
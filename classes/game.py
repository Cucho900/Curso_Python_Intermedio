
import os
import random
import time


class Game:

    def __init__(self) -> None:
        self.menu_state = None

    def set_menu_state(self):
        self._print_menu()
        option = input('Elija una opcion ')
        if option == '1':
            return 'new_game'

        elif option == '2':
            return 'score'

        else:
            return None

    def start(self):
        os.system('clear')
        name = input('Nombre de Usuario: ')
        word = self._set_word()
        player = Player(name)
        self._start_view(word, player)

    def _start_view(self, word, player):
        print_message = '_ '
        attempt = [print_message for i in word]
        while True:

            os.system('clear')
            print(f"Jugador: {player.name}")
            print("\n\n")
            print(*attempt)
            print("\n\n")
            char = input('Ingrese una letra: ')
            if len(char) != 1 or type(char) != str:
                print('No ingrese mas de una letra')
                time.sleep(1)
                char = ""
            else:
                count = 0
                for value in word:
                    if char == value:
                        attempt[count] = char
                    count += 1

                if word == ''.join(attempt):
                    self._win(True, player)
                    break

    def _win(self, state, player):
        os.system('clear')
        if (state):
            print(""" 
                        Felicidades Ganaste
                         
                         """)
            _ = input('Presiona enter para continuar')

    def exit(self):
        pass

    def save_player_score(self):
        pass

    def _print_menu(self):
        os.system('clear')
        print(""" 
                    1) Iniciar Juego
                    2) Score
                    3) salir

                     """)

    def _set_word(self):
        with open('./data/data.txt', 'r') as f:
            words = [i.replace('\n', '') for i in f]
            random_number = random.randint(0, len(words) - 1)

        return words[random_number]


class Player:
    def __init__(self, name) -> None:
        self.__score = 0
        self.__attempts = 0
        self.__winner = False
        self.name = name

    def set_score(self):
        pass

    def set_attempts(self):
        pass

    def has_won(self):
        pass

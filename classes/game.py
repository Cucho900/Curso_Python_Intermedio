
import os
import random
import time
import csv


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
        trys = 10
        print_message = '_ '
        attempt = [print_message for i in word]
        while True:

            os.system('clear')
            print(f"Jugador: {player.name}")
            print(f'Te quedan {trys} intentos')
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

                if char in list(word):
                    pass
                else:
                    trys -= 1

                if word == ''.join(attempt):
                    self._win(True, player, word, trys)
                    break

                if trys == 0:
                    self._win(False, player, word, trys)
                    break

    def _win(self, state, player, word, trys):
        os.system('clear')
        if (state):
            self.save_player_score(player,trys)
            print(""" 
                        Felicidades Ganaste
                      La palabra era:""", word)
            _ = input('\nPresiona enter para continuar')
        else:
            print(""" 
                            Perdiste :c
                      La palabra era:""", word)
            _ = input('\nPresiona enter para continuar')

    def exit(self):
        pass

    def show_score(self):
        os.system('clear')
        player_scores = self.old_scores()
        for key, val in player_scores.items():
            print(key, '', val)
        _ = input('\nPresiona enter para volver al menu')

    def old_scores(self):
        with open('./data/players_scores.csv', 'r') as f:
            reader = csv.DictReader(f)
            for i in reader:
                player_scores = i
        return player_scores

    def write_new_scores(self, player_scores, fieldnames):
        with open('./data/players_scores.csv', 'w') as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)

            writer.writeheader()
            writer.writerow(player_scores)

    def save_player_score(self, player, trys):
        name = player.name
        score = trys * 10
        fieldnames = []
        count = 0

        player_scores = self.old_scores()

        for key, val in player_scores.items():
            if key == name:
                player_scores[key] = str(int(val) + score)
            else:
                count += 1

        if count == len(player_scores.keys()):
            player_scores = player_scores | {name: str(score)}

        for key, val in player_scores.items():
            fieldnames.append(key)
    
        self.write_new_scores(player_scores, fieldnames)


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

from classes.game import Game


def main():
    new_game = Game()

    while True:
        state = new_game.set_menu_state()
        if state == 'new_game':
            new_game.start()
        elif state == 'score':
            new_game.show_score()
        else:
            new_game.exit()
            break


if __name__ == '__main__':
    main()

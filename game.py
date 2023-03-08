"""
This module starts the game process.
"""
import game_exceptions
import models
import menu_class
import settings


def play():
    """
    The function of creating gameplay, player and enemy objects,
    as well as switching the game mode.
    :return:
    """
    lvl = 1
    first_lvl = 1
    game_mode = ''
    game_mode_start = False
    while game_mode_start is False:
        game_mode = input(f'Select game mode {settings.GAME_MODE[0]} or {settings.GAME_MODE[1]}: ')
        if game_mode in settings.GAME_MODE:
            game_mode_start = True
            if game_mode == 'hard':
                first_lvl *= settings.N
                settings.SUCCESS_ATTACK *= settings.N
                settings.ENEMY_DEAD *= settings.N

    player = models.Player(name=input('Write your mane: '), game_mode=game_mode)
    enemy = models.Enemy(lvl=first_lvl)
    while True:
        try:
            player.attack(enemy_obj=enemy)
            player.defence(enemy_obj=enemy)
        except game_exceptions.EnemyDown:
            if game_mode == 'hard':
                lvl += 1
                lvl *= settings.N
                player.score += 5 * settings.N
            else:
                lvl += 1
                player.score += 5
            enemy = models.Enemy(lvl=lvl)
            print(f'Enemy lvl up - {enemy.lvl}')


if __name__ == '__main__':
    try:
        START = False
        while START is not True:
            command = input('Write command: ')
            menu = menu_class.MainMenu()
            START = menu.menu(command)

        play()
    except game_exceptions.GameOver as ex_:
        name, scores, game_mode_ = tuple(ex_.args)
        ex_.write_scores(name, scores, game_mode_)
        settings.SUCCESS_ATTACK = 1
        settings.ENEMY_DEAD = 5
        print('Game over')
    except KeyboardInterrupt:
        pass
    finally:
        print('Good bye!')

import settings
import game_exceptions
import models
import menu_class


def play():
    player = models.Player(name=input('Write your mane: '))
    lvl = 1
    enemy = models.Enemy(lvl=lvl)
    while True:
        try:
            player.attack(enemy_obj=enemy)
            player.defence(enemy_obj=enemy)
        except game_exceptions.EnemyDown:
            player.score += 5
            lvl += 1
            enemy = models.Enemy(lvl=lvl)
            print(f'Enemy lvl up - {enemy.lvl}')


if __name__ == '__main__':
    try:
        start = False
        while start is not True:
            command = input('Write command: ')
            menu = menu_class.MainMenu()
            start = menu.menu(command)

        play()
    except game_exceptions.GameOver as ex_:
        ex_.write_scores(*ex_.args)
        print('Game over')
    except KeyboardInterrupt:
        pass
    finally:
        print('Good bye!')

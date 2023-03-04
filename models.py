from random import randint
import game_exceptions
import settings
import menu_class


class Enemy:
    def __init__(self, lvl):
        self.lvl = lvl
        self.hp = self.lvl

    @staticmethod
    def select_attack():
        return randint(1, 3)

    def decrease_lives(self):
        self.hp -= 1
        if self.hp == 0:
            raise game_exceptions.EnemyDown


class Player:
    def __init__(self, name):
        self.name = name
        self.hp = settings.HP
        self.score = 0
        self.allowed_attacks = ['1', '2', '3']

    @staticmethod
    def fight(attack, defence):
        if (attack == 1 and defence == 2) or \
                (attack == 2 and defence == 3) or \
                (attack == 3 and defence == 1):
            return 1
        elif attack == defence:
            return 0
        else:
            return -1

    def decrease_lives(self):
        self.hp -= 1
        if self.hp == 0:
            raise game_exceptions.GameOver(self.name, self.score)

    def __validate_attack(self, attack):
        if attack in settings.MENU:
            menu = menu_class.MenuInValidate()
            menu.menu(attack)
            return False
        elif attack not in self.allowed_attacks:
            print("Your attack isn't in permitted attack!!!")
            return False
        return True

    def attack(self, enemy_obj):
        print('\n---ATTACK---')
        valid = False
        my_attack = 0
        while valid is not True:
            my_attack = input('Choose your attack: (1) Mage, (2) Warrior, (3) Robber: ')
            valid = self.__validate_attack(my_attack)

        type_of_attack = enemy_obj.select_attack()
        print(f'Enemy defence - {type_of_attack}')
        result_attack = self.fight(attack=int(my_attack), defence=type_of_attack)
        if result_attack == 0:
            print("It's a draw!")
        elif result_attack == 1:
            print('You attacked successfully!!!')
            self.score += 1
            print(f'Your score: {self.score}')
            enemy_obj.decrease_lives()
        elif result_attack == -1:
            self.decrease_lives()
            print(f'You missed!!! Your lives - 1. Lives: {self.hp}')

    def defence(self, enemy_obj):
        print('\n---DEFENCE---')
        valid = False
        my_attack = 0
        while valid is not True:
            my_attack = input('Choose your attack: (1) Mage, (2) Warrior, (3) Robber: ')
            valid = self.__validate_attack(my_attack)

        type_of_attack = enemy_obj.select_attack()
        print(f'Enemy attack - {type_of_attack}')
        result_attack = self.fight(attack=type_of_attack, defence=int(my_attack))
        if result_attack == 0:
            print("It's a draw!")
        elif result_attack == 1:
            print('You defence successfully!!! Enemy lives -1')
            enemy_obj.decrease_lives()
        elif result_attack == -1:
            self.decrease_lives()
            print(f'Your defense has been destroyed!!! Your lives - 1. Lives: {self.hp}')

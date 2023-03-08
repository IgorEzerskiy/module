"""
This module contains the player and enemy classes.
"""
from random import randint

import game_exceptions
import menu_class
import settings


class Enemy:
    """
    The enemy class contains attack selection and life reduction methods.
    """
    def __init__(self, lvl):
        self.lvl = lvl
        self.lives = self.lvl

    @staticmethod
    def select_attack():
        """
        Selection attack.
        :return:
        """
        return randint(1, 3)

    def decrease_lives(self):
        """
        Life reduction methods
        :return:
        """
        self.lives -= 1
        if self.lives == 0:
            raise game_exceptions.EnemyDown


class Player:
    """
    The player class contains a method for determining the result of a battle,
    a method for lowering the level of lives,
    a method for validating user input,
    an attack method, and a defense method.
    """
    def __init__(self, name, game_mode):
        self.name = name
        self.lives = settings.HP
        self.score = 0
        self.allowed_attacks = ['1', '2', '3']
        self.game_mode = game_mode

    @staticmethod
    def fight(attack, defence):
        """
        Determining the result of a battle
        :param attack:
        :param defence:
        :return:
        """
        if (attack == 1 and defence == 2) or \
                (attack == 2 and defence == 3) or \
                (attack == 3 and defence == 1):
            return 1
        if attack == defence:
            return 0
        return -1

    def decrease_lives(self):
        """
        Method for lowering the level of lives
        :return:
        """
        self.lives -= 1
        if self.lives == 0:
            raise game_exceptions.GameOver(self.name, self.score, self.game_mode)

    def __validate_attack(self, attack):
        """
        Method for validating user input
        :param attack:
        :return:
        """
        if attack in settings.MENU:
            menu = menu_class.MenuInValidate()
            menu.menu(attack)
            return False
        if attack not in self.allowed_attacks:
            print("Your attack isn't in permitted attack!!!")
            return False
        return True

    def attack(self, enemy_obj):
        """
        -receives input (1, 2, 3) from the user;
        -selects the enemy's attack from the enemy_obj object;
        -calls the method fight();
        -If the result is 0 - output "It's a draw!"
        -If 1 = "You attacked successfully!" and reduces the number of enemy lives by 1;
        -If -1 = "You missed!"
        :param enemy_obj:
        :return:
        """
        print('\n---ATTACK---')
        print(f'Enemy HP: {enemy_obj.lives}')
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
            self.score += settings.SUCCESS_ATTACK
            print(f'Your score: {self.score}')
            enemy_obj.decrease_lives()
        elif result_attack == -1:
            print(f'You missed!!!')

    def defence(self, enemy_obj):
        """
        The same as the attack() method, only the enemy attack is first passed to the fight method,
        and the player's decrease_lives method is called upon a successful enemy attack.
        :param enemy_obj:
        :return:
        """
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
            print('You defence successfully!!!')
        elif result_attack == -1:
            self.decrease_lives()
            print(f'Your defense has been destroyed!!! Your lives - 1. Lives: {self.lives}')

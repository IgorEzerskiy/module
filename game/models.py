from random import randint
import game_exceptions
import settings


class Enemy:
    def __init__(self, lvl):
        self.lvl = lvl
        self.hp = self.lvl

    @staticmethod
    def select_attack():
        return randint(1, 3)

    def decrease_lives(self):
        if self.hp == 0:
            raise game_exceptions.EnemyDown
        self.hp -= 1


class Player:
    def __init__(self, name):
        self.name = name
        self.hp = settings.HP
        self.score = 0
        self.allowed_attacks = True

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
        if self.hp == 0:
            raise game_exceptions.GameOver
        self.hp -= 1

    @staticmethod
    def __validate_attack(attack):
        check_list = [1, 2, 3]
        if attack not in check_list:
            print("Your attack isn't in permitted attack!!!")
            return False
        return True

    def attack(self, enemy_obj):
        valid = False
        my_attack = 0
        while valid != True:
            my_attack = int(input('Your attack: '))
            valid = self.__validate_attack(my_attack)

        type_of_attack = enemy_obj.select_attack()
        result_attack = self.fight(attack=my_attack, defence=type_of_attack)
        if result_attack == 0:
            print("It's a draw!")
        elif result_attack == 1:
            print('You attacked successfully!!!')
            enemy_obj.decrease_lives()
        elif result_attack == -1:
            print('You missed!!!')

    def defence(self, enemy_obj):
        valid = False
        my_attack = 0
        while valid != True:
            my_attack = int(input('Your attack: '))
            valid = self.__validate_attack(my_attack)

        type_of_attack = enemy_obj.select_attack()
        result_attack = self.fight(attack=type_of_attack, defence=my_attack)
        if result_attack == 0:
            print("It's a draw!")
        elif result_attack == 1:
            print('You defence successfully!!!')
            enemy_obj.decrease_lives()
        elif result_attack == -1:
            self.decrease_lives()
            print('Your defense has been destroyed!!!')

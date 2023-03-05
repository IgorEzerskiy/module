"""
This module contains menu options.
One to call at the beginning of the game, the other to call during the game.
"""
from abc import abstractmethod

import settings


class MenuInterface:
    """
    Abstract menu class.
    """
    @staticmethod
    @abstractmethod
    def menu(menu_command):
        """
        Menu interface.
        :param menu_command:
        :return:
        """


class MainMenu(MenuInterface):
    """
    Main menu class.
    """
    @staticmethod
    def menu(menu_command):
        """
        Main menu.
        :param menu_command:
        :return:
        """
        if menu_command == 'show scores':
            with open(f'{settings.SCORE_PATH}', encoding='utf-8') as score:
                scores = score.readlines()
                for line in scores:
                    print(line)
        elif menu_command == 'exit':
            raise SystemExit
        elif menu_command == 'help':
            command = "".join(item + ", " if item != settings.MENU[-1] else item
                              for item in settings.MENU)
            print(f'Menu: {command}')
        elif menu_command == 'start':
            return True
        return None


class MenuInValidate(MainMenu):
    """
    The menu class that is called from the game process.
    """
    @staticmethod
    def menu(menu_command):
        """
        The menu that is called from the game process
        :param menu_command:
        :return:
        """
        if menu_command == 'show scores':
            with open(f'{settings.SCORE_PATH}', encoding='utf-8') as score:
                scores = score.readlines()
                for line in scores:
                    print(line)
        elif menu_command == 'exit':
            raise SystemExit
        elif menu_command == 'help':
            command = "".join(item + ", " if item != settings.MENU[-1] else item
                              for item in settings.MENU[1::])
            print(f'Menu: {command}')

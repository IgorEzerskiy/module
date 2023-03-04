import settings
from abc import abstractmethod


class MenuInterface:
    @staticmethod
    @abstractmethod
    def menu(menu_command):
        pass


class MainMenu(MenuInterface):
    @staticmethod
    def menu(menu_command):
        if menu_command == 'show scores':
            with open(f'{settings.SCORE_PATH}') as score:
                scores = score.readlines()
                for line in scores:
                    print(line)
        elif menu_command == 'exit':
            raise SystemExit
        elif menu_command == 'help':
            print(f'Menu: {"".join(item + ", " if item != settings.MENU[-1] else item for item in settings.MENU)}')
        elif menu_command == 'start':
            return True


class MenuInValidate(MainMenu):
    @staticmethod
    def menu(menu_command):
        if menu_command == 'show scores':
            with open(f'{settings.SCORE_PATH}') as score:
                scores = score.readlines()
                for line in scores:
                    print(line)
        elif menu_command == 'exit':
            raise SystemExit
        elif menu_command == 'help':
            print(f'Menu: {"".join(item + ", " if item != settings.MENU[-1] else item for item in settings.MENU[1::])}')

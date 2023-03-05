"""
This module contains custom exceptions for handling game events.
"""
import settings


class GameOver(Exception):
    """
    This exception is thrown when the player has lost
    and it writes the result of the game to a file.
    """
    @staticmethod
    def write_scores(name, scores, game_mode):
        """
        The method writes the result of the game to a file.
        :param name:
        :param scores:
        :param game_mode:
        :return:
        """
        exit_ = f'Name: {name} | Score: {scores} | Game Mode: {game_mode}\n'
        print(f'\n{exit_}')
        with open(f'{settings.SCORE_PATH}', 'a+', encoding='utf-8') as score:
            score.write(str(exit_))


class EnemyDown(Exception):
    """
    This exception is thrown when an enemy is destroyed.
    """

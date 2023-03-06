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
        with open(f'{settings.SCORE_PATH}', 'a+', encoding='utf-8') as score:
            exit_ = f'Name: {name} | Score: {scores} | Game Mode: {game_mode}\n'
            print(f'\n{exit_}')
            score.write(exit_)

        with open(f'{settings.SCORE_PATH}', encoding='utf-8') as score:
            scores = score.readlines()
            scores_kv = [list(x.rstrip('\n').split(' | ')) for x in scores]
            unsort_dict = {}
            for list_ in scores_kv:
                unsort_dict[int(list_[1].split(': ')[1])] = {'Name': list_[0].split(': ')[1],
                                                             'Game mode': list_[2].split(': ')[1]}

        my_keys = list(unsort_dict.keys())
        my_keys.sort()
        my_keys.reverse()
        sorted_dict = {i: unsort_dict[i] for i in my_keys[:10]}

        with open(f'{settings.SCORE_PATH}', 'w+', encoding='utf-8') as score:
            for k, v in sorted_dict.items():
                str_for_write = f'Name: {v["Name"]} | Score: {k} | Game mode: {v["Game mode"]}\n'
                score.write(str_for_write)


class EnemyDown(Exception):
    """
    This exception is thrown when an enemy is destroyed.
    """

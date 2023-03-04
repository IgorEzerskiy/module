import settings


class GameOver(Exception):
    @staticmethod
    def write_scores(name, scores):
        exit_ = f'Name: {name} | Score: {scores}\n'
        with open(f'{settings.SCORE_PATH}', 'a+') as score:
            score.write(str(exit_))


class EnemyDown(Exception):
    pass

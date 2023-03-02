import settings


class GameOver(Exception):
    @staticmethod
    def gema_over(player_obj):
        result = {f'{player_obj.name}|{player_obj.score}\n'}
        with open(rf'{settings.SCORE_PATH}', 'w') as score:
            score.write(str(result))


class EnemyDown(Exception):
    pass

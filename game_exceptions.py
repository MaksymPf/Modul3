'''
Custom exeptions
'''


class GameOver(Exception):
    '''will raise in the end of game'''
    # def __init__(self, txt):
    #     self.txt = txt

    def __str__(self):
        return 'Game Over'

    # def write_result(self):
    #     '''will write user scores in scores.txt '''
    #     return None


class EnemyDown(Exception):
    '''will raise when enemy down'''
    # def __init__(self, txt):
    #     self.txt = txt

    def __str__(self):
        return 'Enemy Down'

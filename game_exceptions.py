'''
Custom exeptions
'''

from datetime import datetime


class GameOver(Exception):
    '''will raise in the end of game'''
    def __init__(self, name, score):
        self.name = name
        self.score = score
        self.date = datetime.date

    def __str__(self):
        return 'Game Over!'

    def write_result(self):
        '''write user scores in scores.txt '''
        with open('scores.txt', 'a+') as fp:
            fp.write(self.name, self.score, self.date)


class EnemyDown(Exception):
    '''will raise when enemy down'''

    def __str__(self):
        return 'Enemy Down'

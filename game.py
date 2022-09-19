'''
Starting game
'''
from datetime import datetime

import game_exceptions
import models

def play():
    '''Starting game'''
    player_name = input('Input your name: ').capitalize
    user_obj = models.Player(player_name)
    level = 1
    enemy_obj = models.Enemy(level)
    
    while True:
        try:
            user_obj.attack(enemy_obj)
            print('Your lives:', user_obj.lives)
            print('Enemy lives:', enemy_obj.lives, '\n')
            user_obj.defence(enemy_obj)
            print('Your lives:', user_obj.lives)
            print('Enemy lives:', enemy_obj.lives, '\n')
        except game_exceptions.EnemyDown:
            print('Enemy Down')
            level += 1
            user_obj.score += 1
            enemy_obj = models.Enemy(level)
        # except game_exceptions.GameOver(user_obj.name, user_obj.score):
        #     print('err')


if __name__ == '__main__':
    try:
        play()
    except game_exceptions.GameOver as err:
        print(err)
    except KeyboardInterrupt:
        pass
    finally:
        print('Good Bye!')

input()

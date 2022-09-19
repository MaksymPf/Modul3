'''
Starting game
'''
import game_exceptions
import models

def play():
    '''Starting game'''
    player_name = input('Input your name: ').capitalize
    user_obj = models.Player(player_name)
    level = 1
    enemy_obj = models.Enemy(level)
    
    try:
        while 2:
            user_obj.attack(enemy_obj)
            user_obj.defence(enemy_obj)
            print('Your lives:', user_obj.lives)
            print('Enemy lives:', enemy_obj.lives)
    except game_exceptions.EnemyDown:
        level += 1


if __name__ == '__main__':

    try:
        play()
    # except game_exceptions.EnemyDown as err1:
    #     print(err1)
    except game_exceptions.GameOver as err:
        print(err)
    except KeyboardInterrupt:
        pass
    finally:
        print('Good Bye!')

input()

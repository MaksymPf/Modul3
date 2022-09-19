'''
Models of player and computer
'''

from random import randrange

import game_exceptions
import settings

class Enemy():
    '''the class defines the characteristics of ENEMY'''
    def __init__(self, level: int) -> None:
        self.level = level
        self.lives = level

    @staticmethod
    def select_attack():
        attack = randrange(1, 4)
        return attack

    def decrease_lives(self):
        self.lives -= 1
        if self.lives <= 0:
            raise game_exceptions.EnemyDown()


class Player:
    '''the class defines the characteristics of PLAYER'''
    lives = settings.PLAYER_LIVES
    score = 0
    allowed_attacks = [1, 2, 3]

    def __init__(self, name):
        self.name = name
        
    @staticmethod
    def fight(attack, defense):
        '''return result of attack or defense'''
        if attack == defense:
            return 0
        if attack == 1 and defense == 2:
            return 1
        if attack == 1 and defense == 3:
            return -1
        if attack == 2 and defense == 3:
            return 1
        if attack == 2 and defense == 1:
            return -1
        if attack == 3 and defense == 1:
            return 1
        if attack == 3 and defense == 2:
            return -1

    def decrease_lives(self):
        self.lives -= 1
        if self.lives == 0:
            raise game_exceptions.GameOver('Game Over')
    
    def attack(self, enemy_obj):
        attack = int(input('Input number 1, 2, 3: '))
        # enemy_obj = Enemy(self)                                           ###
        enemy_attack = enemy_obj.select_attack()                          ###
        res_fight = Player.fight(attack, enemy_attack)                    ###
        print('\nYou attak with:', attack, 'enemy defence with:', enemy_obj)
        print('Result of fight:', res_fight)

        if res_fight == 0:
            print('It\'s a draw!')
        elif res_fight == 1:
            enemy_obj.decrease_lives()
            print('You attacked successfully!')
        elif res_fight == -1:
            print('You missed!')

    def defence(self, enemy_obj):
        enemy_obj = Enemy.select_attack()
        defence = int(input('Input number 1, 2, 3: '))
        res_fight = Player.fight(enemy_obj, defence)
        print('\nEnemy attack with', enemy_obj, 'you defence with:', defence)
        print('Result of fight:', res_fight)

        if res_fight == 0:
            print('It\'s a draw!')
        if res_fight == 1:
            self.decrease_lives()
            print('You missed!')
        if res_fight == -1:
            print('You defended successfully!')


if __name__ == '__main__':

    # first_enemy = Enemy(int(input('input numb: ')))
    # print('\nEnemy lives:', first_enemy.lives)
    # print('Enemy level:', first_enemy.level)
    # input()
    # first_enemy.decrease_lives()
    # print('\nEnemy lives:', first_enemy.lives)
    # print('Enemy level:', first_enemy.level)
    # input()

    while True:
        try:
            first_enemy = Enemy(int(input('input numb: ')))
            print('\nEnemy lives:', first_enemy.lives)
            print('Enemy level:', first_enemy.level)
            input()
            first_enemy.decrease_lives()
        except game_exceptions.EnemyDown as error:
            print(error)
        else:
            print('\nEnemy lives:', first_enemy.lives)
            print('Enemy level:', first_enemy.level)
            input()
        finally:
            print('__________________')
            input()

import random
import os
import time
from gameClasses import *
from gameMonsters import *

player = Character()


def main():
    os.system('cls')
    while True:
        new_name = (
            input('\nWhat would you like you player name to be? (<30 characters): ')).strip()
        if len(new_name) <= 30 and new_name:
            player.name = new_name
            break
    menu_game()


def menu_game():
    os.system('cls')
    # player.print_stats()
    # print('\n')
    print(
        f'Hello {player.name}. This is a monster fighting game. Player Damage Resistance = {player.dmg_res} percent, to get this stat up you must play and win.\n')
    while True:
        play = input('Would you like to fight a monster? [y/n] ').lower()
        if play == 'y':
            print('\n')
            break
        elif play == 'n':
            exit()
        else:
            print('\nPlease try again. We will only accept y for yes and n for no.\n')
    game()


def game():
    enemy = Monster(*monsters[random.choice([m[0]
                    for m in monsters.values() if m[5] <= player.lvl])])
    print(f'You are fighting a {enemy.name}!\n{enemy.description}\n\n')
    while player.health >= 1 and enemy.health >= 1:
        while True:
            atkType = input(
                '\nPlease enter if you would like to stab [st], slash [sl] or cast a spell [sp]: [st/sl/sp] ').lower()
            if atkType in ['st', 'sl', 'sp']:
                print('\n')
                break
            else:
                print('Please enter a valid input.')

        player_dmg = player.Attack(atkType, enemy.dmg_res)
        enemy.health -= player_dmg
        print(f'You did {player_dmg} damage to the {enemy.name}!')
        print(enemy.health_check())
        print('\n\n')

        enemy_dmg = enemy.Attack(player.dmg_res)
        player.health -= enemy_dmg
        print(f'{enemy.name} did {enemy_dmg} damage to the {player.name}!')
        print(player.health_check())
        print('\n\n')

    if player.health <= 0:
        print('Sorry but you died!  -Wait 10 sec.\n')
        time.sleep(6)
        player.reset_all()
        main()
    else:
        print('Wow, You won! I am totally impressed! I have given you 5 percent damage resistance if you want to play again.  -Wait 10 sec.\n')
        player.Lvl_up()
        time.sleep(6)
        menu_game()


if __name__ == "__main__":
    main()

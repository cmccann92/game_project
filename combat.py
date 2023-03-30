from gamestory import slow_print
from playable_chars import *
from enemy import Zombie
from time import sleep


def combat(player, zombie):
    while player.health > 0 and zombie.health > 0:
        print("What do you want to do?")
        print("[1] Shoot      [2] Hit")
        print("[3] Inventory  [4] Run")
        choice = input()
        
        if choice == "1" and player.check_range() == True:
            if player.health > 0:
                player.calc_damage()
                sleep(1)
                zombie.defend(player)
                sleep(1)
            if zombie.health > 0:
                zombie.attack(player)
                sleep(1)
                player.take_damage(zombie.damage)
                sleep(1)
                if player.health <= 0:
                    print(f"You died. Game over")
                    exit()
                elif zombie.health <= 0:
                    print(f"You defeated {zombie.name}!")
                    break
                else:
                    continue
        elif choice == "2" and player.check_melee() == True:
            if player.health > 0:
                player.calc_damage()
                sleep(1)
                zombie.defend(player)
                sleep(1)
            if zombie.health > 0:
                zombie.attack(player)
                sleep(1)
                player.take_damage(zombie.damage)
                sleep(1)
                if zombie.health <= 0:
                    print(f"You defeated {zombie.name}! ")
                    zombie.health = 75
                elif player.health <= 0:
                    print(f"You died. Game over")
                    exit()
                else:
                    continue
        elif choice == "3":
                player.check_inventory()
        elif choice == "4":
             print(run())
             break
        else:
            continue

def run():
    return f"You ran away from the fight... Coward!"
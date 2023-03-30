
from playable_chars import CharacterFactory
from enemy import Zombie
from time import sleep


def combat(player, zombie):
    while player.health > 0 and zombie.health > 0:
        print("What do you want to do? [1] Shoot  [2] Hit\n [3] Inventory  [4] Run")
        choice = input()
        if choice == "1" and player.shoot(zombie.name) == True:
            if player.health > 0:
                player.shoot(zombie.name)
                zombie.health - player.damage
                sleep(1)
                zombie.defend(player)
                sleep(1)
            if zombie.health > 0:
                zombie.attack(player)
                sleep(1)
                player.take_damage(zombie.damage)
                sleep(1)
        elif choice == "2" and player.hit(zombie.name) == True:
            if player.health > 0:
                player.hit(zombie.name)
                zombie.health - player.damage
                sleep(1)
                zombie.defend(player)
                sleep(1)
            if zombie.health > 0:
                zombie.attack(player)
                sleep(1)
                player.take_damage(zombie.damage)
                sleep(1)
        elif choice == "3":
                player.check_inventory()
        elif choice == "4":
             print(run())
             break
        else:
            continue

def run():
    return f"You ran away from the fight... Coward!"
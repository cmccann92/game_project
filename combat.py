
from playable_chars import CharacterFactory
from enemy import Zombie
from time import sleep

zombie = Zombie("Zombie",100,10,10)
player = CharacterFactory.create_char("medic","Hans")

def combat():
    while player.health > 0 and zombie.health > 0:
        player.calc_damage(5)
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
combat()
def run():
    return f"You ran away from the fight... Coward!"
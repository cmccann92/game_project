from time import sleep
import random


class Enemy:
    def __init__(self, name, health: int, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        print(f'{self.name} attacks {target.name}')
        target.defend(self)

    def defend(self, attacker):
        print(f'{self.name} defends against {attacker.name}')
        self.take_damage(25)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f'{self.name} has been defeated!')
        else:
            print(
                f'{self.name} takes {damage} damage and has {self.health} health remaining')


class Zombie(Enemy):
    def __init__(self):
        super().__init__("Zombie", 75, 8)
    #    self.bite = bite
        damage = 10

    def attack(self, target):
        print(f'{self.name} bites the {target.name}')
        return 

    def defend(self, attacker):
        p_choices = [1, 2, 3]
        x = random.choice(p_choices)
        limps = ['arm', 'leg', 'foot', 'knee', 'hand', 'shoulder']
        y = random.choice(limps)
        if x == 1:
            print(
                f"{self.name} dodges {attacker.name}'s attack, but attack hits the {y}.")
            self.take_damage(attacker.damage)
        elif x == 2:
            print(
                f'{self.name}  cannot dodge the {attacker.name} and get hit in body!')
            self.take_damage(attacker.damage * 2)
        else:
            print(
                f"{attacker.name} attack hit {self.name}'s head. Critical strike!!!")
            self.take_damage(attacker.damage * 5)


class ZombieDog(Enemy):
    def __init__(self):
        super().__init__("Zombie Dog", 90, 13)
        

    def attack(self, target):
        print(f'{self.name} bites the  {target.name}')
        target.defend(self)

    def defend(self, attacker):
        p_choices = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4]
        x = random.choice(p_choices)
        limps = ['arm', 'leg', 'foot', 'knee', 'hand', 'shoulder']
        y = random.choice(limps)
        if x == 1:
            print(f"{attacker.name}'s attack missed, {self.name} got no damage.")
        elif x == 2:
            print(
                f"{self.name} dodges {attacker.name}'s attack, but attack hits his {y}.")
            self.take_damage(10)
        elif x == 3:
            print(
                f'{self.name}  cannot dodge the {attacker.name} and get hit in body!')
            self.take_damage(20)
        else:
            print(
                f"{attacker.name} attack hit {self.name}'s head. Critical strike!!!")
            self.take_damage(self.health)


class MutantZombie(Enemy):
    def __init__(self):
        super().__init__("Mutant Zombie", 100, 15)
        

    def attack(self, target):
        print(f'{self.name} bites the survivor{target.name}')
        #target.defend(self)

    def defend(self, attacker):
        p_choices = [1, 2, 3, 4, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4]
        x = random.choice(p_choices)
        limps = ['arm', 'leg', 'foot', 'knee', 'hand', 'shoulder']
        y = random.choice(limps)
        if x == 1:
            print(
                f"{attacker.name} hits the armor body part. {self.name} gets no damage.")
            self.take_damage(0)
        elif x == 2:
            print(
                f"{self.name} dodges {attacker.name}'s attack, but attack hits his {y}.")
            self.take_damage(10)
        elif x == 2:
            print(
                f'{self.name}  cannot dodge the {attacker.name} and get hit in body!')
            self.take_damage(20)
        else:
            print(
                f"{attacker.name} attack hit {self.name}'s head. Critical strike!!!")
            self.take_damage(self.health)


#zombie = Zombie('Zombie', 100, 10)
#dog_z = ZombieDog('ZombieDog', 120, 10)

"""while zombie.health > 0 and dog_z.health > 0:
    if zombie.health > 0:
        sleep(0.5)
        zombie.attack(dog_z)
    if dog_z.health > 0:
        sleep(0.5)
        dog_z.attack(zombie)"""

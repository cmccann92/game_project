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
        print(f'{self.name} bites you!')
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
                f'{self.name}  cannot dodge your attack and gets hit in body! [Damage x2!]')
            self.take_damage(attacker.damage * 2)
        else:
            print(
                f'Your attack hits {self.name}s head. Critical strike!!! [Damage x3!!]')
            self.take_damage(attacker.damage * 3)


class ZombieDog(Enemy):
    def __init__(self):
        super().__init__("Zombie Dog", 90, 13)
        

    def attack(self, target):
        print(f'{self.name} bites the you!')

    def defend(self, attacker):
        p_choices = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4]
        x = random.choice(p_choices)
        limps = ['arm', 'leg', 'foot', 'knee', 'hand', 'shoulder']
        y = random.choice(limps)
        if x == 1:
            print(f"Your attack missed, {self.name} got no damage.")
        elif x == 2:
            print(
                f"{self.name} dodges your attack, but attack hits his {y}.")
            self.take_damage(attacker.damage)
        elif x == 3:
            print(
                f'{self.name}  cannot dodge the your attack and gets hit in the body! [Damage x2!]')
            self.take_damage(attacker.damage * 2)
        else:
            print(
                f"Your attack hits {self.name}'s head. Critical strike!!! [Damage x3!!]")
            self.take_damage(attacker.damage * 3)


class MutantZombie(Enemy):
    def __init__(self):
        super().__init__("Mutant Zombie", 100, 15)
        

    def attack(self, target):
        print(f'{self.name} bites you!')

    def defend(self, attacker):
        p_choices = [1, 2, 3, 4, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4]
        x = random.choice(p_choices)
        limps = ['arm', 'leg', 'foot', 'knee', 'hand', 'shoulder']
        y = random.choice(limps)
        if x == 1:
            print(
                f"Your attack hits the armor body part. {self.name} gets no damage.")
            self.take_damage(0)
        elif x == 2:
            print(
                f"{self.name} dodges your attack, but attack hits his {y}.")
            self.take_damage(attacker.damage)
        elif x == 2:
            print(
                f'{self.name}  cannot dodge your attack and gets hit in body! [Damage x2!]')
            self.take_damage(attacker.damage * 2)
        else:
            print(
                f"Your attack hits {self.name}'s head. Critical strike!!! [Damage x3!!]")
            self.take_damage(attacker.damage * 3)

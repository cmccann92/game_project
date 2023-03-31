from time import sleep
import random
from weapon import *

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print()

class Enemy:
    def __init__(self, name, health: int, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def attack(self, target):
        slow_print(f'{self.name} attacks you!{style.RESET}')
        target.defend(self)

    def defend(self, attacker):
        slow_print(f'{self.name} defends against {attacker.name}')
        self.take_damage(25)

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            slow_print(f'{style.BLUE}{self.name} has been defeated!{style.RESET}')
        else:
            slow_print(
                f'{style.BLUE}{self.name} takes {damage} damage and has {self.health} health remaining{style.RESET}')


class Zombie(Enemy):
    def __init__(self):
        super().__init__("Zombie", 75, 8)

    def attack(self, target):
        slow_print(f'{style.RED}{self.name} bites you!{style.RESET}')
        return 

    def defend(self, attacker):
        p_choices = [1, 2, 3]
        x = random.choice(p_choices)
        limps = ['arm', 'leg', 'foot', 'knee', 'hand', 'shoulder']
        y = random.choice(limps)
        if x == 1:
            slow_print(
                f"{style.BLUE}{self.name} dodges your attack, but attack hits the {y}.{style.RESET}")
            self.take_damage(attacker.damage)
        elif x == 2:
            slow_print(
                f'{style.BLUE}{self.name} cannot dodge your attack and gets hit in body! [Damage x2!]{style.RESET}')
            self.take_damage(attacker.damage * 2)
        else:
            slow_print(
                f'{style.BLUE}Your attack hits {self.name}s head. Critical strike!!! [Damage x3!!]{style.RESET}')
            self.take_damage(attacker.damage * 3)


class ZombieDog(Enemy):
    def __init__(self):
        super().__init__("Zombie Dog", 90, 13)
        

    def attack(self, target):
        slow_print(f'{style.RED}{self.name} bites you!{style.RESET}')

    def defend(self, attacker):
        p_choices = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4]
        x = random.choice(p_choices)
        limps = ['arm', 'leg', 'foot', 'knee', 'hand', 'shoulder']
        y = random.choice(limps)
        if x == 1:
            slow_print(f"{style.BLUE}Your attack missed, {self.name} got no damage.{style.RESET}")
        elif x == 2:
            slow_print(
                f"{style.BLUE}{self.name} dodges your attack, but attack hits his {y}.{style.RESET}")
            self.take_damage(attacker.damage)
        elif x == 3:
            slow_print(
                f'{style.BLUE}{self.name}  cannot dodge your attack and gets hit in the body! [Damage x2!]{style.RESET}')
            self.take_damage(attacker.damage * 2)
        else:
            slow_print(
                f"{style.BLUE}Your attack hits {self.name}'s head. Critical strike!!! [Damage x3!!]{style.RESET}")
            self.take_damage(attacker.damage * 3)


class MutantZombie(Enemy):
    def __init__(self):
        super().__init__("Mutant Zombie", 100, 15)
        

    def attack(self, target):
        slow_print(f'{style.RED}{self.name} bites you!{style.RESET}')

    def defend(self, attacker):
        p_choices = [1, 2, 3, 4, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4]
        x = random.choice(p_choices)
        limps = ['arm', 'leg', 'foot', 'knee', 'hand', 'shoulder']
        y = random.choice(limps)
        if x == 1:
            slow_print(
                f"{style.BLUE}Your attack hits the armor body part. {self.name} gets no damage.{style.RESET}")
            self.take_damage(0)
        elif x == 2:
            slow_print(
                f"{style.BLUE}{self.name} dodges your attack, but attack hits his {y}.{style.RESET}")
            self.take_damage(attacker.damage)
        elif x == 2:
            slow_print(
                f'{style.BLUE}{self.name}  cannot dodge your attack and gets hit in body! [Damage x2!]{style.RESET}')
            self.take_damage(attacker.damage * 2)
        else:
            slow_print(
                f"{style.BLUE}Your attack hits {self.name}'s head. Critical strike!!! [Damage x3!!]{style.RESET}")
            self.take_damage(attacker.damage * 3)

class Character:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        self.level = 1
        self.inventory = []
        self.weapon = []

    def get_info(self):
        return f"Your character {self.name}'s current stats:\n current Level: {self.level} Health: {self.health}\n Damage: {self.damage}\n Armor: {self.armor}\n Accuracy: {self.accuracy}\n Dodge: {self.dodge}"
        

    def shoot(self,target):
        weapon_dmg = 5
        total = self.damage + weapon_dmg
        return f"You shoot {target} with your weapon. You do {total} damage"
    
    def take_damage(self,damage):
        total =  damage - self.armor
        self.health -= total
        return f"You took {total} damage. Remaining health: {self.health}"

    def run(self):
        return f"You run away from the fight."
        
    def calc_damage(self, weapon_dmg):
        total = self.damage + weapon_dmg
        self.damage = total

    def hit(self,weapon):
        if weapon.ammo == 0:
            total = self.damage + weapon_dmg
        return f"You hit the enemy. You did {total} damage."
        

class Soldier(Character):
    def __init__(self, name):
        super().__init__(name, 90, 10, 5)
        self.ammo_box = 2

    def get_info(self):
        super().get_info()
        return f"Your character {self.name}'s current stats:\n current Level: {self.level} Health: {self.health}\n Damage: {self.damage}\n Armor: {self.armor}\n Accuracy: {self.accuracy}\n Dodge: {self.dodge}"

    def calc_damage(self, weapon_dmg):
        total = self.damage + weapon_dmg
        self.damage = total
    
    def take_damage(self,damage):
        total =  damage - self.armor
        self.health -= total
        print(f"You took {total} damage. Remaining health: {self.health}")
    
    def hit(self):
        super().hit()

    def run(self):
        super().run()
    
    def ammo(self, weapon):
        self.ammo_box -= 1
        return f"Ammo box used. All weapons reloaded" 

class Medic(Character):
    def __init__(self, name):
        super().__init__(name, 100, 6, 4)

    def shoot(self,target):
        weapon_dmg = 5
        total = self.damage + weapon_dmg
        print(f"You shoot {target} with your weapon. You do {total} damage")
    
    def take_damage(self,damage):
        super().take_damage(damage)
        total =  damage - self.armor
        self.health -= total
        self.health += 3
        print(f"You took {total} damage. You healed yourself for 3 with your self heal ability. Remaining health: {self.health}")
    
    def calc_damage(self, weapon_dmg):
        total = self.damage + weapon_dmg
        self.damage = total

    def hit(self):
        super().hit()

    def run(self):
        super().run()
    
    
class Demolition(Character):
    def __init__(self, name):
        super().__init__(name, 70, 12, 7)
        self.pipe_bomb = 2
    
    def shoot(self):
        super().shoot()

    def hit(self):
        super().hit()

    def run(self):
        super().run()

    def kaboom(self):
        self.pipe_bomb -= 1
        return f"Thrown pipe bomb! Damaged all enemies for {self.damage * 10} "
    
class Sniper(Character):
    def __init__(self, name):
        super().__init__(name, 60, 15, 3)

    def shoot(self):
        super().shoot()

    def hit(self):
        super().hit()

    def run(self):
        super().run()
    
    def sharpshooter(self):
        
        return f"Sharpshooter ability active. You will only deal headshots for the next 10 seconds"

class CharacterFactory:
    def create_char(char_class, name):
        if char_class.lower() == "soldier":
            return Soldier(name)
        elif char_class.lower() == "medic":
            return Medic(name)
        elif char_class.lower() == "demolition":
            return Demolition(name)
        elif char_class.lower() == "sniper":
            return Sniper(name)
        else:
            raise ValueError(f"Invalid character class")



player = CharacterFactory.create_char("Sniper","Hans")

class Character:
    def __init__(self, name, health, damage, armor, accuracy, dodge, energy=100, xp=0):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        self.level = 1
        self.accuracy = accuracy
        self.dodge = dodge
        self.energy = energy
        self.xp = xp

    def get_info(self):
        pass

    def shoot():
        pass
    
    def take_damage(self,damage):
        self.health -= damage

    def run():
        pass
    
    def hit():
        pass

class Soldier(Character):
    def __init__(self, name):
        super().__init__(name, 90, 10, 5, 70, 20)
        self.ammo_box = 2

    def get_info(self):
        super().get_info()
        return f"Your character {self.name}'s current stats:\n current Level: {self.level} Health: {self.health}\n Damage: {self.damage}\n Armor: {self.armor}\n Accuracy: {self.accuracy}\n Dodge: {self.dodge}"

    def shoot(self):
        super().shoot()

    def hit(self):
        super().hit()

    def run(self):
        super().run()
    
    def ammo(self, weapon):
        self.ammo_box -= 1
        return f"Ammo box used. All weapons reloaded" 

class Medic(Character):
    def __init__(self, name):
        super().__init__(name, 110, 6, 4, 60, 30)

    def shoot(self):
        super().shoot()

    def hit(self):
        super().hit()

    def run(self):
        super().run()
    
    def self_heal(self):
        self.energy -= 10
        self.health += 5
        return f"Healing kit used. Current health: {self.health}"
    
class Demolition(Character):
    def __init__(self, name):
        super().__init__(name, 70, 12, 7, 40, 15)
        self.pipe_bomb = 2
    
    def shoot(self):
        super().shoot()

    def hit(self):
        super().hit()

    def run(self):
        super().run()

    def kaboom(self):
        self.pipe_bomb -= 1
        return f"Thrown pipe bomb! Damaged all enemies for  "
    
class Sniper(Character):
    def __init__(self, name):
        super().__init__(name, 60, 15, 3, 80, 10)

    def shoot(self):
        super().shoot()

    def hit(self):
        super().hit()

    def run(self):
        super().run()
    
    def sharpshooter(self):
        self.energy -= 50
        self.accuracy = 100
        return f"Sharpshooter ability active. You will only deal headshots for the next 2 rounds"

class CharacterFactory:
    def create_char(self, char_class, name):
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



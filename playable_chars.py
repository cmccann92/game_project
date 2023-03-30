from time import sleep

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print()


class Character:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        self.level = 1
        self.inventory = []
        self.weapon = []

    def check_melee(self):
        for item in self.weapon:
            if 'range' in item.weptype:
                slow_print(f"No melee weapon equipped")
                return False
            else:
                return True
            
    def check_range(self):
        for item in self.weapon:
            if 'melee' in item.weptype:
                slow_print(f"No range weapon equipped")
                return False
            else:
                return True

    def get_info(self):
       slow_print(f"Your character {self.name}'s current stats:\n current Level: {self.level} Health: {self.health}\n Damage: {self.damage}\n Armor: {self.armor}")
    
    def check_inventory(self):
        for item in self.inventory:
            slow_print(item)
    
    def take_damage(self,damage):
        total =  damage - self.armor
        self.health -= total
        return  slow_print(f"You took {total} damage. Remaining health: {self.health}")

    def run(self):
       slow_print(f"You run away from the fight.")
        
    def calc_damage(self):
        self.damage = 10
        total = self.damage + self.weapon[0].damage
        self.damage = total
                       

class Soldier(Character):
    def __init__(self, name):
        super().__init__(name, 90, 10, 5)
        self.ammo_box = 2

    def get_info(self):
        super().get_info()

    def calc_damage(self):
        super().calc_damage()
    
    def take_damage(self,damage):  
        super().take_damage(damage)

    def ammo(self):
        self.ammo_box -= 1
        print(f"Ammo box used. All weapons reloaded")

class Medic(Character):
    def __init__(self, name):
        super().__init__(name, 100, 6, 4)
    
    def take_damage(self,damage):
        super().take_damage(damage)
        total =  damage - self.armor
        self.health += 3
        slow_print(f"You healed yourself for 3 with your self heal ability. Remaining health: {self.health}")
    
    def calc_damage(self):
        super().calc_damage()
        
class Demolition(Character):
    def __init__(self, name):
        super().__init__(name, 70, 12, 4)
        self.pipe_bomb = 2
    
    def get_info(self):
        super().get_info()

    def calc_damage(self):
        super().calc_damage()
    
    def take_damage(self,damage):  
        super().take_damage(damage)

    def kaboom(self):
        self.pipe_bomb -= 1
        return f"Thrown pipe bomb! Damaged all enemies for {self.damage * 10} "
    
class Sniper(Character):
    def __init__(self, name):
        super().__init__(name, 60, 16, 7)

    def get_info(self):
        super().get_info()

    def calc_damage(self):
        super().calc_damage()
    
    def take_damage(self,damage):  
        super().take_damage(damage)

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





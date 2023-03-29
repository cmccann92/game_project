
class Weapons:
    def __init__(self,type, damage, distance):
        self.type = type
        self.damage = damage
        self.distance = distance
       
class Lancer(Weapons):
    def __init__(self, type,max_capacity, distance,damage, fire_mode, ammo_type, fire_rate ):
         super().__init__(type, max_capacity ,distance)
         self.fire_mode = fire_mode
         self.ammo_type = ammo_type
         self.fire_rate = fire_rate

    def attack(self):
        
        print('This weapon is surely the best of world.')
        print(f'Type of weapon: {self.type}\nRate of fire: {self.fire_rate}\nAmmunition Type: {self.ammo_type}\nMaximum Ammunition: {self.damage}\nFire Mode: {self.fire_mode}')

class Headhunter(Weapons):  

    def __init__(self,type,damage,distance):
         super().__init__(type,damage,distance)          
    def attack(self):
        print('Coming already equipped with explosive ammo is reason enough,but the fact that you control the flight of the bullet too allowed for limitless possibilities. No wasted shot,and multiple kills per shot means as long as you keep some distance, the Head Hunter will treat you well.')
        print(f'Type: {self.type}\nDamage: {self.damage}\nDistance: {self.distance}')

class Baseball(Weapons):

    def __init__(self,type,damage,distance):
         super().__init__(type,damage,distance)
    def attack(self):
        print('This will do the job for you all day, every day.Durable, easy to wield, it will break skulls and never run out of ammo.')
        print(f'Type:   {self.type}\nDamage: {self.damage}\nDistance: {self.distance}')

class Sword(Weapons):  

    def __init__(self,type,damage,distance):
         super().__init__(type,damage,distance)
    def attack(self):
        print('the Energy Sword is made entirely of focused plasma energy.t can melt through Spartan armor though then it should do just fine against rotten flesh.')
        print(f'Type: {self.type}\nDamage: {self.damage}\nDistance: {self.distance}')

class Axe(Weapons):

    def __init__(self,type,damage,distance):
         super().__init__(type,damage,distance)
    def attack(self):
        print('Axe is easier balanced, more powerful. It is a classic apocalyptic weapon used for more than killing zombies,in ways ranging from hacking down doors to amputation. ')
        print(f'Type: {self.type}\nDamage: {self.damage}\nDistance: {self.distance}')

class Bomb(Weapons):
     
     def __init__(self,type,damage,distance):
         super().__init__(type,damage,distance)
     def attack(self):
        print(f'Type: {self.type}\nDamage: {self.damage}\nDistance: {self.distance}')
     
print("\t\tWELCOME TO WEAPONS STORE \n")
print("""CHOOSE WHAT YOU WANT:-\n1. Lancer Gun(Gears of war)\n2. Head Hunter - Bulletstorm\n3. Spiked baseball Bat\n4. Energy sword\n5. AXE \n6. Bombs\n7. Leave store\n""")

while (True):

    usr_response = int(input("Enter your choice: "))

    if usr_response == 1:  
        gun = Lancer('Gun',660,'High','Far','Automatic','Cartridge','90/m')
        gun.attack()
        print()

    elif usr_response == 2:
        gun1 = Headhunter('Gun','High','Far')
        gun1.attack()
        print()

    elif usr_response == 3:
        ball = Baseball('Spiked bat','Medium-high','Near')
        ball.attack()
        print()
    
    elif usr_response == 4:
        sword = Sword('Energy Sword','Medium-high','Near') 
        sword.attack()
        print()

    elif usr_response == 5:
        axe = Axe('Axe','Medium','Near')
        axe.attack()
        print()

    elif usr_response == 6:
        bomb = Bomb('Bomb','High','Far')
        bomb.attack()
        print()

    elif usr_response == 7:
        print("THANK YOU ! \n")
        exit()
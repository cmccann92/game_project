class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

class Weapons:
    def __init__(self,type, damage):
        self.type = style.GREEN +type
        self.damage = damage
       
class Lancer(Weapons):
    def __init__(self, type, damage):
         super().__init__(type,damage)

    def attack(self):
        
        print('This weapon is surely the best of world.')
        print(f'Type of weapon: {self.type}\n{self.damage}\n')

class Headhunter(Weapons):  

    def __init__(self,type,damage):
         super().__init__(type,damage)          
    def attack(self):
        print('Coming already equipped with explosive ammo is reason enough,but the fact that you control the flight of the bullet too allowed for limitless possibilities. No wasted shot,and multiple kills per shot means as long as you keep some distance, the Head Hunter will treat you well.')
        print(f'Type: {self.type}\nDamage: {self.damage}')

class Baseball(Weapons):

    def __init__(self,type,damage):
         super().__init__(type,damage)
    def attack(self):
        print('This will do the job for you all day, every day.Durable, easy to wield, it will break skulls and never run out of ammo.')
        print(f'Type:   {self.type}\nDamage: {self.damage}')

class Sword(Weapons):  

    def __init__(self,type,damage):
         super().__init__(type,damage)
    def attack(self):
        print('the Energy Sword is made entirely of focused plasma energy.t can melt through Spartan armor though then it should do just fine against rotten flesh.')
        print(f'Type: {self.type}\nDamage: {self.damage}')

class Axe(Weapons):

    def __init__(self,type,damage):
         super().__init__(type,damage)
    def attack(self):
        print('Axe is easier balanced, more powerful. It is a classic apocalyptic weapon used for more than killing zombies,in ways ranging from hacking down doors to amputation. ')
        print(f'Type: {self.type}\nDamage: {self.damage}')

class Bomb(Weapons):
     
     def __init__(self,type,damage):
         super().__init__(type,damage)
     def attack(self):
        print(f'Type: {self.type}\nDamage: {self.damage}')
     
#print("\t\tCHOOSE YOUR START WEAPON\n")
#print("""CHOOSE WHAT YOU WANT:-\n1. Lancer Gun(Gears of war)\n2. Head Hunter - Bulletstorm\n3. Spiked baseball Bat\n4. Energy sword\n5. AXE \n6. Bombs\n7.\n""")
def weapon_choice(player):
    while (True):
        print("\t\tCHOOSE YOUR START WEAPON\n")
        print("""CHOOSE WHAT YOU WANT:-\n1. Lancer Gun(Gears of war)\n2. Head Hunter - Bulletstorm\n3. Spiked baseball Bat\n4. Energy sword\n5. AXE \n6. Bombs\n""")

        usr_response = int(input("Enter your choice: "))

        if usr_response == 1:  
            gun = Lancer('range',10)
            gun.attack()
            ans = input("Choose this weapon? (Y/N) ")
            if ans.lower() == "y":
                print(f"{style.RED}Nice choice {style.RESET}")
                player.weapon.append(gun)
                break
            elif ans.lower() == "n":
                continue
            
            

        elif usr_response == 2:
            gun1 = Headhunter('range',8)
            gun1.attack()
            ans = input("Choose this weapon? (Y/N) ")
            if ans.lower() == "y":
                print(style.GREEN +"Nice choice")
                player.weapon.append(gun1)
                break
            elif ans.lower() == "n":
                continue

        elif usr_response == 3:
            ball = Baseball('melee',6)
            ball.attack()
            ans = input("Choose this weapon? (Y/N) ")
            if ans.lower() == "y":
                print(style.GREEN +"Nice choice")
                player.weapon.append(ball)
                break
            elif ans.lower() == "n":
                continue
        
        elif usr_response == 4:
            sword = Sword('melee',7) 
            sword.attack()
            ans = input("Choose this weapon? (Y/N) ")
            if ans.lower() == "y":
                print(style.GREEN +"Nice choice")
                player.weapon.append(sword)
                break
            elif ans.lower() == "n":
                continue

        elif usr_response == 5:
            axe = Axe('melee',5)
            axe.attack()
            ans = input("Choose this weapon? (Y/N) ")
            if ans.lower() == "y":
                print(style.GREEN +"Nice choice")
                player.weapon.append(axe)
                break
            elif ans.lower() == "n":
                continue

        elif usr_response == 6:
            bomb = Bomb('range',10)
            bomb.attack()
            ans = input("Choose this weapon? (Y/N) ")
            if ans.lower() == "y":
                print(style.GREEN +"Nice choice")
                player.weapon.append(bomb)
                break
            elif ans.lower() == "n":
                continue

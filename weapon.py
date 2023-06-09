from time import sleep

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

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print()


class Weapons:
    def __init__(self,name,weptype, damage):
        self.name = name
        self.weptype = weptype
        self.damage = damage
       
class Lancer(Weapons):
    def __init__(self, name, weptype, damage):
         super().__init__(name, weptype, damage)

    def attack(self):
        
        slow_print('This weapon is surely the best in the world.')
        slow_print(f'Type of weapon: {self.weptype}\n{self.damage}\n')

class Headhunter(Weapons):  

    def __init__(self,name,weptype,damage):
         super().__init__(name,weptype,damage)          
    def attack(self):
        slow_print('Coming already equipped with explosive ammo is reason enough,but the fact that you control the flight of the bullet too allowed for limitless possibilities. No wasted shot,and multiple kills per shot means as long as you keep some distance, the Head Hunter will treat you well.')
        slow_print(f'Type: {self.weptype}\nDamage: {self.damage}')

class Baseball(Weapons):

    def __init__(self,name,weptype,damage):
         super().__init__(name,weptype,damage)
    def attack(self):
        slow_print('This will do the job for you all day, every day.Durable, easy to wield, it will break skulls and never run out of ammo.')
        slow_print(f'Type:   {self.weptype}\nDamage: {self.damage}')

class Sword(Weapons):  

    def __init__(self,name,weptype,damage):
         super().__init__(name,weptype,damage)
    def attack(self):
        slow_print('the Energy Sword is made entirely of focused plasma energy. It can melt through Spartan armor though then it should do just fine against rotten flesh.')
        slow_print(f'Type: {self.weptype}\nDamage: {self.damage}')

class Axe(Weapons):

    def __init__(self,name,weptype,damage):
         super().__init__(name,weptype,damage)
    def attack(self):
        slow_print('Axe is easier balanced, more powerful. It is a classic apocalyptic weapon used for more than killing zombies,in ways ranging from hacking down doors to amputation. ')
        slow_print(f'Type: {self.weptype}\nDamage: {self.damage}')

class Bomb(Weapons):
     
     def __init__(self,name,weptype,damage):
         super().__init__(name,weptype,damage)
     def attack(self):
        slow_print(f'Type: {self.weptype}\nDamage: {self.damage}')
     
#print("\t\tCHOOSE YOUR START WEAPON\n")
#print("""CHOOSE WHAT YOU WANT:-\n1. Lancer Gun(Gears of war)\n2. Head Hunter - Bulletstorm\n3. Spiked baseball Bat\n4. Energy sword\n5. AXE \n6. Bombs\n7.\n""")
def weapon_choice(player):
    while (True):
        slow_print(f"\t\t{style.CYAN}CHOOSE YOUR START WEAPON{style.RESET}\n")
        slow_print(f"""CHOOSE WHAT YOU WANT:\n1. Lancer Gun(Rifle) {style.BLUE}Damage: 10{style.RESET}\n2. Head Hunter(Sniper Rifle) {style.BLUE}Damage: 8{style.RESET}\n3. Spiked baseball Bat {style.BLUE}Damage: 6{style.RESET}\n4. Energy sword {style.BLUE}Damage: 7{style.RESET}\n5. AXE {style.BLUE}Damage: 5{style.RESET}\n6. Bombs {style.BLUE}Damage: 10{style.RESET}\n""")

        usr_response = int(input("Enter your choice: "))

        if usr_response == 1:  
            gun = Lancer('Lancer','range',10)
            gun.attack()
            ans = input("Choose this weapon? (Y/N) ")
            if ans.lower() == "y":
                slow_print("Nice choice")
                player.weapon.append(gun)
                break
            elif ans.lower() == "n":
                continue
            
        elif usr_response == 2:
            gun1 = Headhunter('Headhunter','range',8)
            gun1.attack()
            ans = input("Choose this weapon? (Y/N) ")
            if ans.lower() == "y":
                slow_print("Nice choice")
                player.weapon.append(gun1)
                break
            elif ans.lower() == "n":
                continue

        elif usr_response == 3:
            ball = Baseball('Baseball Bat','melee',6)
            ball.attack()
            ans = input("Choose this weapon? (Y/N) ")
            if ans.lower() == "y":
                slow_print("Nice choice")
                player.weapon.append(ball)
                break
            elif ans.lower() == "n":
                continue
        
        elif usr_response == 4:
            sword = Sword('Energy Sword','melee',7) 
            sword.attack()
            ans = input("Choose this weapon? (Y/N) ")
            if ans.lower() == "y":
                slow_print("Nice choice")
                player.weapon.append(sword)
                break
            elif ans.lower() == "n":
                continue

        elif usr_response == 5:
            axe = Axe('Axe','melee',5)
            axe.attack()
            ans = input("Choose this weapon? (Y/N) ")
            if ans.lower() == "y":
                slow_print("Nice choice")
                player.weapon.append(axe)
                break
            elif ans.lower() == "n":
                continue

        elif usr_response == 6:
            bomb = Bomb('Bombs','range',10)
            bomb.attack()
            ans = input("Choose this weapon? (Y/N) ")
            if ans.lower() == "y":
                slow_print("Nice choice")
                player.weapon.append(bomb)
                break
            elif ans.lower() == "n":
                continue

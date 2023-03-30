from os import system
from playable_chars import *
from enemy import *
from weapon import *
from gamestory import *
from time import sleep
from combat import *

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print()



zombie = Zombie()
zom_dog = ZombieDog()
zom_mut = MutantZombie()

# Game Story of Zombie 
slow_print("Welcome to the Zombie game!")
sleep(1)
slow_print("What is your name?")
name = input()
slow_print("Hello, " + name + "! The world has been overrun by zombies and you're one of the few survivors.\nYour military background will surely give you an advantage.")
sleep(1)
slow_print("Tell me, what was your specialization again? ")
slow_print(f" [1] Soldier:\t{style.RED}HP: 90 {style.BLUE}Damage: 10 {style.YELLOW}Armor: 5{style.RESET}\n [2] Medic:\t{style.RED}HP 100 {style.BLUE}Damage:  6 {style.YELLOW}Armor: 4{style.RESET}\n [3] Demolition:{style.RED}HP: 70 {style.BLUE}Damage: 12 {style.YELLOW}Armor: 4 {style.RESET}\n [4] Sniper:\t{style.RED}HP: 60 {style.BLUE}Damage: 16 {style.YELLOW}Armor: 6{style.RESET} ")
answer = int(input())
if answer == 1:
    slow_print("You are now a Soldier ")
    player_class = "soldier"
elif answer == 2:
    slow_print("You are now a Medic ")
    player_class = "medic"
elif answer == 3:
    slow_print("You are now a Demolition ")
    player_class = "demolition"
elif answer == 4:
    slow_print("You are now a Sniper")
    player_class = "sniper"
player = CharacterFactory.create_char(player_class, name)

sleep(1)
system("clear")
weapon_choice(player)
sleep(2)
system("clear")
# Searching for supplies
slow_print("You are wandering through a small town and need to reach a safe spot.")
slow_print("You look around. On your left is a grocery store. Probably looted already, but maybe worth a look.\nOn your right is a weapon store. If you continue down the road there is a hospital ahead")
slow_print("[1] Grocery\n[2] Weapon store\n[3] Hospital")
choice = input()
if choice == "1":
    system("clear")
    slow_print("You search the Grocery store and find some food and water.")
    slow_print("You also find a first aid kit")
    player.inventory.append("First_aid_kit")
    slow_print("First aid kit added to inventory!")
    slow_print("You also see a dead body, mauled by zombies. The lifeless body clings to a rare Energy sword.")
    for weapon in player.weapon:
        slow_print(f"You already have a weapon. Replace {player.weapon[0].name} with Sword?  (Y/N)")
        ans = input()
        if ans.lower() == "y":
            slow_print(f"Replaced {player.weapon[0].name} with Sword")
            sword = Sword("melee",7)
            player.weapon[0] = sword
            break
        else:
            slow_print(f"You leave the weapon. Surely didn't gift it's last owner with luck")
            break
    slow_print("You suddenly hear noises in a backroom of the Grocery Store. You check it out. It is a Zombie! ")
    combat(player, zombie)
    sleep(2)
    system("clear")
    slow_print(f"After fighting the Zombie you decide to leave the Grocery store.")

elif choice == "Weapon store":
    system("clear")
    print("You search the weapon store and find some weapons and tools.")
    print("You find an Axe")
    print("You also find some twinkies and energy drinks")
    for weapon in player.weapon:
        print(f"You already have a weapon. Replace {player.weapon[0].type} with Axe?  (Y/N)")
        ans = input()
        if ans.lower() == "y":
            print(f"replaced {player.weapon[0].type} with Axe")
            axe = Axe("melee",5)
            player.weapon[0] = axe  

elif choice == "medical care":
    system("clear")
    print("You search the hospital and find some medical supplies.")
    player.inventory.append("first_aid_kit")
    print("Added First aid kit to inventory")
    print("You also find a Baseball bat")
    for weapon in player.weapon:
        print(f"You already have a weapon. Replace {player.weapon[0].type} with Baseball bat?  (Y/N)")
        ans = input()
        if ans.lower() == "y":
            print(f"replaced {player.weapon[0].type} with Baseball bat")
            bball = Baseball("melee",6)
            player.weapon[0] = bball

# Finding a safe place
system("clear")
print("You need to find a safe place to hide from the zombies.")
print("You can either head to the top floor of a building, call for a helicopter rescue, or the police station.")
choice = input("Enter 'top floor','helicopter', or 'police station': ")
if choice == "Top floor":
    system("clear")
    print("You head to the top floor of a building and block yourself inside.")
    print("You find some other survivors and work together to secure the building.")
    print("You're able to hold off the zombies for a while, but they eventually break through.")
    print("You and the other survivors are forced to flee.")
elif choice == "helicopter":
    system("clear")
    print("You head to the military base and find it relatively secure.")
    print("You find some other survivors and work together to defend the military base.")
    print("You're able to hold off the zombies for a while, but they eventually break through.")
    print("You and the other survivors are forced to flee.")
elif choice == "police station":
    system("clear")
    print("You head to the police station and find it abandoned.")
    print("You're able to find some weapons and ammunition.")
    print("You also find a radio and call for help.")

# Fighting the zombies
print("You and the other survivors are on the run from the zombies.")
print("You can either fight your way through, try to sneak past them.")
choice = input("Enter 'fight', 'sneak': ")
if choice == "fight":
    system("clear")
    print("You and the other survivors fight your way through the zombies.")
    print("You use your weapons and skills to take out as many zombies as you can.")
    print("Congratulations, " + name + "! You're able to make it to a safe zone and join a group of survivors.")
elif choice == "sneak":
    system("clear")
    print("You and the other survivors try to sneak past the zombies.")
    print("You move slowly and quietly, trying not to attract attention.")
    print("You're able to make it to a safe zone, but some of them")
    print("Congratulations, " + name + "! You survived the zombie .")





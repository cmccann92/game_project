from os import system
from playable_chars import *
from enemy import *
from weapon import *
from gamestory import *
from time import sleep
from combat import *

# Game Story of Zombie 
print("Welcome to the Zombie game!")
name = input("What's your name? ")
print("What class do you choose?\n [1] Soldier: HP: 90. Damage: 10. Armor: 5\n [2] Medic: HP 100. Damage: 6. Armor: 4\n [3] Demolition: HP: 70. Damage: 12. Armor: 7\n [4] Sniper: HP: 60. Damage: 15. Armor: 3 ")
answer = int(input())
if answer == 1:
    print("You are now a Soldier ")
    player_class = "soldier"
elif answer == 2:
    print("You are now a Medic ")
    player_class = "medic"
elif answer == 3:
    print("You are now a Demolition ")
    player_class = "demolition"
elif answer == 4:
    print("You are now a Sniper")
    player_class = "sniper"
player = CharacterFactory.create_char(player_class, name)
print("Hello, " + name + "! The world has been overrun by zombies and you're one of the few survivors.")

zombie = Zombie("Zombie",80,9)
weapon_choice(player)
system("clear")
combat(player,zombie)
sleep(2)
system("clear")
# Searching for supplies
print("You're in a small town and need to find supplies to survive.")
print("You can either search the grocery store, the weapon store, or Medical Care.")
choice = input("Enter 'grocery', 'weapon store', or 'Medical Care': ")
if choice == "grocery":
    system("clear")
    print("You search the grocery store and find some food and water.")
    print("You also find a first aid kit and a Sword.")
    player.inventory.append("First_aid_kit")
    print(player.inventory[0])
    for weapon in player.weapon:
        print(f"You already have a weapon. Replace {player.weapon[0].type} with Sword?  (Y/N)")
        ans = input()
        if ans.lower() == "y":
            print(f"replaced {player.weapon[0].type} with Sword")
            sword = Sword("melee",7)
            player.weapon[0] = sword
    

elif choice == "weapon store":
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

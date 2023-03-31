from os import system
from playable_chars import *
from enemy import *
from weapon import *
from gamestory import *
from time import sleep
from combat import *
import pygame
import time

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
    print()



zombie = Zombie()
zom_dog = ZombieDog()
zom_dog2 = ZombieDog()
zom_mut = MutantZombie()

# Game Story of Zombie 
slow_print("Welcome to Death Calling I")
sleep(1)
slow_print("What is your name?")
name = input()
system("clear")
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
slow_print("Where do you want to go?\n[1] Grocery\n[2] Weapon store\n[3] Hospital")
choice = input()
if choice == "1":
    system("clear")
    slow_print("You search the Grocery store and find some food and water.")
    slow_print("You also find a first aid kit")
    player.inventory.append("First_aid_kit")
    slow_print(f"{style.GREEN}First aid kit added to inventory!{style.RESET}")
    slow_print("You also see a dead body, mauled by zombies. The lifeless body clings to a rare Energy sword.")
    for weapon in player.weapon:
        slow_print(f"You already have a weapon. Replace {player.weapon[0].name} with Sword?  (Y/N)")
        ans = input()
        if ans.lower() == "y":
            slow_print(f"Replaced {player.weapon[0].name} with Sword")
            sword = Sword("Energy Sword","melee",7)
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

elif choice == "2":
    system("clear")
    slow_print("You search the weapon store. You find a backpack with some Energy Drinks and twinkies inside.")
    slow_print("You also find some ammo. And an Axe")
    for weapon in player.weapon:
        slow_print(f"You already have a weapon. Replace {player.weapon[0].name} with Axe?  (Y/N)")
        ans = input()
        if ans.lower() == "y":
            slow_print(f"replaced {player.weapon[0].name} with Axe")
            axe = Axe("melee",5)
            player.weapon[0] = axe  
        else:
            slow_print(f"You keep your weapon and leave the Axe lying on the ground")
    slow_print("When grabbing some Ammo off a shelf, an arm suddenly appears from behind the shelf and holds your arm. A Zombie! ")
    combat(player,zombie)
    sleep(2)

elif choice == "3":
    system("clear")
    slow_print("You slowly stroll through the hospital. The sight is really terrifying. There are dead people everywhere.")
    slow_print("The search for supplies is tough, there is almost nothing left. On a higher floor you discover an unopened first aid kit")
    slow_print(f"{style.GREEN}First aid kit added to inventory!{style.RESET}")
    player.inventory.append("first_aid_kit")
    slow_print("You also find a spiked Baseball bat")
    for weapon in player.weapon:
        print(f"You already have a weapon. Replace {player.weapon[0].name} with Baseball bat?  (Y/N)")
        ans = input()
        if ans.lower() == "y":
            print(f"replaced {player.weapon[0].name} with Baseball bat")
            bball = Baseball("Baseball Bat","melee",6)
            player.weapon[0] = bball
    else:
        slow_print(f"You keep your weapon and leave the Baseball bat")
    
    slow_print("On your way back to the ground floor you encounter a Zombie in the stairway!")
    combat(player,zombie)

# Finding a safe place
sleep(2)
system("clear")
slow_print("You exit the building and need to find a safe place to hide from the zombies or you will be overrun.")
slow_print("You can either head to the top floor of a building, go to the military base, or the police station.")
slow_print("[1] Top floor\n[2] Military Base\n[3] Police station")
choice = input()
if choice == "1":
    system("clear")
    slow_print("You head to the top floor of a building.")
    slow_print("You find some other survivors. They are all heavily wounded and cannot fight any longer. You have to help them get out of here.")
    slow_print("You hear some Zombies breaking through the self made barricade. Damn it, those are Zombie Dogs. These Beasts are very tough!")
    combat(player,zom_dog)
    sleep(2)
    system("clear")
    slow_print("You survive the fight. But another Zombie dog charges in!")
    combat(player,zom_dog2)
    sleep(2)
    system("clear")
    slow_print("You think that was the last one for now. Better get out of here before more appear. You lead the way for the survivors")

elif choice == "2":
    system("clear")
    slow_print("You head to the military base and find it relatively secure.")
    slow_print("You find some other survivors and work together to defend the military base.")
    slow_print("Suddenly a pack of zombie dogs charges in the base and takes out a handful of soldiers!")
    combat(player,zom_dog)
    sleep(2)
    system("clear")
    slow_print("You're able to hold off the zombie dogs for a while, but they eventually break through. Another one charges directly towards you!")
    combat(player, zom_dog2)
    sleep(2)
    system("clear")
    slow_print("You and the other survivors are forced to flee.")
elif choice == "3":
    system("clear")
    slow_print("You head to the police station and find it abandoned. But then you discover some survivors who have locked themselves in the cells to be safe from the zombies")
    slow_print("You offer to help them and open the cell from the outside.")
    slow_print("Suddenly an alarm goes off. This will certainly attract some zombies!")
    slow_print("Some dangerous Zombie Dogs charge inside the police station!")
    combat(player,zom_dog)
    sleep(2)
    system("clear")
    slow_print("Another Zombie Dog charges for the survivors, but you can interfere! ")
    combat(player,zom_dog2)
    sleep(2)
    system("clear")
    slow_print("Phew... that was close. Time to get out of here!")

# Fighting the zombies
slow_print("You and the other survivors are on the run from the zombies.")
slow_print("One of the survivors tells you that the military is preparing a train to get survivors out of this city")
slow_print("You decide to head towards the train station")
slow_print("The train station is in sight. But something blocks the path.")
slow_print("It is a zombie like you have never seen before. He is big and bulky and is wearing armor. Whats up with that guy, he looks like you will need a rocket to bring him down")
slow_print("Your priority is to get these survivors to the train station. You could fight the Mutant Zombie, or you could distract him away from the survivors.")
slow_print("What will you do?: [1] Fight! [2] Run and distract!")
choice = input()
if choice == "1":
    system("clear")
    slow_print("You choose to fight this beast!")
    combat(player,zom_mut)
    sleep(2)
    system("clear")
    slow_print("What a tough fight... but you defeated that disgusting creature")
    slow_print("You get up and lead the survivors to the train station.")
    slow_print("The military welcomes you and you are safe and sound")
    slow_print("The train departs shortly after and you leave this god forsaken city")
    slow_print("Finally some peace. You try and realize what is going on with the world at the moment")
    slow_print("However this calm doesn't last long. You hear screams from an other train cart")
    slow_print("Seems like some infected humans have made it onboard and are now turning into Zombies...")
    slow_print("The fight continues")
    slow_print("...")
    slow_print("The End? ...")

elif choice == "2":
    slow_print("You decide to distract the Mutant Zombie and lure him away from the survivors.")
    slow_print("You shoot against his armor. That got his attention! But it also made him angry. Better run fast!")
    slow_print("You run towards a bridge. He is still following you closely")
    slow_print("You are now on the middle of the bridge and realize that you have ran into a dead end.")
    slow_print("A barricade of cars has been built on the other side and there is no way through")
    slow_print("You turn around and face the Mutant Zombie!")
    combat(player,zom_mut)
    sleep(2)
    system("clear")
    slow_print("You barely survived that fight... ")
    slow_print("The big Mutant Zombie falls to the ground. His fall makes the earth shake.")
    slow_print("It keeps on shaking... You realize that the bridge is collapsing")
    slow_print("You try to get up and run off but it's too late!")
    slow_print("Together with the rubble you get dragged down, and fall into the river...")
    slow_print("...")
    slow_print("The End? ...")


pygame.init()
screen = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Rolling Credits")

font = pygame.font.Font(None, 36)
text = font.render("Program Credits:", True, (255, 255, 255))
text_rect = text.get_rect(center=(320, 50))

credits = [
    "Developers: Ammara, Connor, Florin, Swarna, ChatGPT",
    "Designer: Ammara, Connor, Florin, Swarna",
    "Tester: Ammara, Connor, Florin, Swarna",
    "Special Thanks: Ammara, Connor, Florin, Swarna"
]

import time
import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Rolling Credits")

font = pygame.font.Font(None, 36)
text = font.render("Program Credits:", True, (255, 255, 255))
text_rect = text.get_rect(center=(320, 50))
font_color = (255, 255, 255) 
clock = pygame.time.Clock()
clock.tick(60)
credits = [
    "Developers: Ammara, Connor, Florin, Swarna, ChatGPT",
    "Designer: Ammara, Connor, Florin, Swarna",
    "Tester: Ammara, Connor, Florin, Swarna",
    "Special Thanks: Ammara, Connor, Florin, Swarna"
]

y_pos = [200, 240, 280, 320]
scroll_speed = 2

def draw_credit(credit_text, y_pos):
    # render the text surface
    text_surface = font.render(credit_text, True, font_color)

    # get the text surface rectangle and center it horizontally
    text_rect = text_surface.get_rect()
    text_rect.centerx = screen.get_rect().centerx

    # set the text surface's y coordinate
    text_rect.top = y_pos

    # blit the text surface onto the display surface
    screen.blit(text_surface, text_rect)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill((0, 0, 0))
    screen.blit(text, text_rect)

    for i in range(len(credits)):
        draw_credit(credits[i], y_pos[i])
        y_pos[i] -= scroll_speed
        if y_pos[i] < -40:
            y_pos[i] = 600

    pygame.display.update()
    time.sleep(0.02)




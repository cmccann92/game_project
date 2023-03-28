# Game Story of Zombie 

print("Welcome to the Zombie  game!")
name = input("What's your name? ")
print("Hello, " + name + "! The world has been overrun by zombies and you're one of the few survivors.")

# Searching for supplies
print("You're in a small town and need to find supplies to survive.")
print("You can either search the grocery store or Weapon store.")
choice = input("Enter 'grocery' or 'Weapon store': ")
if choice == "grocery":
    print("You search the grocery store and find some food and water.")
    print("You also find a first aid kit and a knife.")
elif choice == "Weapon store":
    print("You search the  store and find some weapons and tools.")
    print("You find a shotgun and some ammunition.")
    print("You also find a hammer and some nails.")

# Finding a safe place
print("You need to find a safe place to hide from the zombies.")
print("You can either head to the top floor of mall or the Military Base.")
choice = input("Enter 'top Roof of  Building' or 'Military Base ': ")
if choice == "Building":
    print("You head to the mall and barricade yourself inside.")
    print("You find some other survivors and work together to secure the Building.")
    print("You're able to hold off the zombies for a while, but they eventually break through.")
    print("You and the other survivors are forced to flee.")
elif choice == "Military Base":
    print("You head to the military base and find it relatively secure.")
    print("You find some other survivors and work together to defend the military base.")
    print("You're able to hold off the zombies for a while, but they eventually break through.")
    print("You and the other survivors are forced to flee.")

#  Fighting the zombies
print("You and the other survivors are on the run from the zombies.")
print("You can either fight your way through or try to sneak past them.")
choice = input("Enter 'fight' or 'Runaway': ")
if choice == "fight":
    print("You and the other survivors fight your way through the zombies.")
    print("You use your weapons and skills to take out as many zombies as you can.")
    print("You're able to make it to a safe zone and join a group of survivors.")
elif choice == "Runaway":
    print("You and the other survivors try to runaway from zombies.")
    print("You move slowly and quietly, trying not to attract attention.")
    print("Unfortunately, one of the survivors makes a noise and alerts the zombies.")
    print("You're forced to fight your way through and many of the survivors are killed.")
    print("You're able to make it to a safe zone, but you're the only survivor.")
    print("Congratulations, " + name + "! You survived the zombie .")
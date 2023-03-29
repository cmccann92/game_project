# Game Story of Zombie 
print("Welcome to the Zombie game!")
name = input("What's your name? ")
print("Hello, " + name + "! The world has been overrun by zombies and you're one of the few survivors.")

# Searching for supplies
print("You're in a small town and need to find supplies to survive.")
print("You can either search the grocery store, the weapon store, or the hospital.")
choice = input("Enter 'grocery', 'weapon store', or 'Medical Care': ")
if choice == "grocery":
    print("You search the grocery store and find some food and water.")
    print("You also find a first aid kit and a knife.")
elif choice == "weapon store":
    print("You search the weapon store and find some weapons and tools.")
    print("You find a shotgun and some ammunition.")
    print("You also find a hammer and some nails.")
elif choice == "medical care":
    print("You search the hospital and find some medical supplies.")
    print("You find some bandages and painkillers.")
    print("You also find a defibrillator.")

# Finding a safe place
print("You need to find a safe place to hide from the zombies.")
print("You can either head to the top floor of a building, call for a helicopter rescue, or the police station.")
choice = input("Enter 'top floor','helicopter':, or 'police station': ")
if choice == "Top floor":
    print("You head to the top floor of a tall building and barricade yourself inside.")
    print("You find some other survivors and work together to secure the building.")
    print("You're able to hold off the zombies for a while, but they eventually break through.")
    print("You and the other survivors are forced to flee.")
elif choice == "helicopter":
    print("You head to the military base and find it relatively secure.")
    print("You find some other survivors and work together to defend the military base.")
    print("You're able to hold off the zombies for a while, but they eventually break through.")
    print("You and the other survivors are forced to flee.")
elif choice == "police station":
    print("You head to the police station and find it abandoned.")
    print("You're able to find some weapons and ammunition.")
    print("You also find a radio and call for help.")

# Fighting the zombies
print("You and the other survivors are on the run from the zombies.")
print("You can either fight your way through, try to sneak past them.")
choice = input("Enter 'fight', 'sneak': ")
if choice == "fight":
    print("You and the other survivors fight your way through the zombies.")
    print("You use your weapons and skills to take out as many zombies as you can.")
    print("You're able to make it to a safe zone and join a group of survivors.")
elif choice == "sneak":
    print("You and the other survivors try to sneak past the zombies.")
    print("You move slowly and quietly, trying not to attract attention.")
    print("You're able to make it to a safe zone, but some of the")
    print("Congratulations, " + name + "! You survived the zombie .")

import random
import pygame
import os
# initialize game variables
inventory = [""]
shield = False
str_path = "C:\\Users\\Markus\\Downloads\\"
health = 10
#"G:\Meine Ablage\TGM FÄCHEr\code\Text_Aventure_Game\Bilder\zelda.map.jfif"
# define story blocks
def platzh():
    print("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
# define functions
def print_inventory():
    if len(inventory)==0:
        print("Du hast nichts in deinem Inventar")
    print("Inventory: " + ", ".join(inventory))


def zelda_map():
    # Initialize the Pygame library 
    pygame.init()
    
    # Load image as a surface object from the file path "Bilder\zelda_mapresize.png"
    image = pygame.image.load("Bilder\zelda_mapresize.png")
    
    # Get the width and height of the loaded image and store it in width and height variables
    width, height = image.get_size()
    
    # Set the display surface for the window with given dimensions
    screen = pygame.display.set_mode((width, height))
    
    # Draw the loaded image on the screen starting from the top left corner at the position (0, 0)
    screen.blit(image, (0, 0))
    
    # Update the full display Surface to the screen
    pygame.display.update()
    
    # Start the game loop that runs until the player exits the game or closes the window
    while True:
        
        # Waiting for events such as keyboard and mouse input
        for event in pygame.event.get():
            
            # If X button is clicked, quit the game and exit the window
            if event.type == pygame.QUIT:
                pygame.quit()
                return 


# Define function to print the current health of the player 
def print_health():
    print("Health:" + str(health))

# Define function to print whether the shield is equipped or not
def print_shield():
    if shield:
        print("Shield: Equipped")
    else:
        print("Shield: Not equipped")

# Define function to print the inventory, current health and shield status.
def print_status(): 
    print_inventory()
    print_health()
    print_shield()

# Define function to reduce the player's health by an amount of damage inflicted.
def damage(amount):
    global health  # Use the global variable "health".
    if shield:                      # If the player has a shield, display that they have blocked the attack.
        print("You blocked the attack with your shield!")
    else:                            # If the player doesn't have a shield in their inventory,                             # reduce their health by the amount of damage inflicted.                            # If their health reaches zero or below, the game ends.
        health -= amount             # reduce their health by the amount of damage inflicted.
        if health <= 0:              # If their health reaches zero or below, the game ends.
            print("Game over!")
            quit()


# zelda portrait
print("             _______")
print("        ..-'`       ````---.")
print("       .'          ___ .'````.'SS'.")
print("      /        ..-SS####'.  /SSHH##'.")
print("     |       .'SSSHHHH##|/#/#HH#H####'. ")
print("    /      .'SSHHHHH####/||#/: \SHH#####\ ")
print("   /      /SSHHHHH#####/!||;`___|SSHH###\ ")
print("-..__    /SSSHHH######.         \SSSHH###\ ")
print("`.'-.''--._SHHH#####.'           '.SH####/ ")
print("  '. ``'-  '/SH####`/_             `|H##/ ")
print("  | '.     /SSHH###|`'==.       .=='/\H| ")
print("  |   `'-.|SHHHH##/\__\/        /\//|~|/ ")
print("  |    |S#|/HHH##/             |``  |")
print("  |    \H' |H#.'`              \    |")
print("  |        ''`|               -     /")
print("  |          /H\          .----    /")
print("  |         |H#/'.           `    /")
print("  |          \| | '..            /")
print("  |    ^~DLF   /|    ''..______.'")
print("   \          //\__    _..-. | ")
print("    \         ||   ````     \ |_")
print("     \    _.-|               \| |_")
print("     _\_.-'   `'''''-.        |   `--.")
print(" ''``    \            `''-;    \ /")
print("          \      .-'|     ````.' -")
print("          |    .'  `--'''''-.. |/")
print("          |  .'               \|")
print("          |.'")         
print()


# main game loop

def Copyrigtname():
    name = "Markus Ernst Kattner"
    copyright = u"\u00A9" # Erstellt das Copyright-Zeichen
    print(copyright + " " + name)# Gibt das Ergebnis aus

# Welcome message
def StartMessage():
    print("Welcome to The Legend of Zelda: Breath of the Wild text adventure")
    print("You are Link, a hero in the kingdom of Hyrule.")
    print("You wake up in a mysterious Cave with some kind of an old Table standing in the midle of it")
Copyrigtname()
QandA = {
    "Kap1":  {"Text": "You look around the room and see an exit. What do you do?", 
              "Q1": "[1]Go through the exit", 
              "Q2": "[2]Inspect the mysterious table in the middle of the room", 
              "Q3": "[3]Check your status", 
              "Q4": "[4]You are going to sleep because you're some lazy MF"},
    "Kap2": {"Text": "You see an old hag outside the cave and she wants to talk to you", 
             "Q1": "[1]Talk with her", 
              "Q2": "[2]Steal her food", 
              "Q3": "[3]Ask for a map of Hyrule",
              "Q4": "[4]You kill her to obtain all her belongings",
              "Q5": "[5]Check your status"},
    "Kap3": {"Text": "You now go into the forest and see a couple of goblins molesting a woman. What do you do?",
             "Q1": "[1]Help her and try to kill the goblins",
             "Q2": "[2]Try distracting the goblins with setting their base camp on fire.",
             "Q3": "[3]Ignoring it and try to loot the goblins' base",
             "Q4": "[4]Check your status",
             "Q5": "[5]Check the map"},
    "Kap4": {"Text": "You now understand the uncomfortable position the woman is in and need to make a decision.",
             "Q1": "[1]Try to rescue her village and defeat one of the 4 great titans Vah Ruta",
             "Q2": "[2]Requesting some items or coins as an equal exchange for saving her village",
             "Q3": "[3]Don't help her and go off into the wild to find other adventures waiting for you",
             "Q4": "[4]Check your status",
             "Q5": "[5]Check the map"},
    "Kap5": {"Text": "You defeated the Titan Vah Ruta and now realized the consequences of Ganon and his evil doing. The village leader also told you about the fire Titan Vah Rudania. ",
             "Q1": "[1]Going to help the people that suffer like the Zora villagers from the Fire Titan Vah Rudania",
             "Q2": "[2]Go on your own adventure to obtain materials and sell them to buy food/equipment with the coins you obtained",
             "Q3": "[3]Check your status",
             "Q4": "[4]Check the map"},
    "Kap6": {"Text": "You defeated the Titan Vah Rudania and"},
}


ChoiceA = {
    "Kap1": {"Q1A": "You follow the light and go through the exit.",
             "Q2A": "You research the mysterious magic table and touch it. A holograph of Zelda appears and explains that you've slept for 100 years and that Hyrule needs your help.",
             "Q3A": "You check your status and see that you have nothing in your inventory, and that you have 10 health points."},
    "Kap2": {"Q1A": "You talk with the old hag, and she tells you that she is the last of her kind and that she is looking for a way to get back to her home. She also tells you that she has a map of Hyrule and wants to give it to you. She gives you some starter equipment and food for your long adventure.",
             "Q2A": "You steal the old hag's food, and she gets angry and attacks you. You fail to defend yourself and are defeated.",
             "Q3A": "The old hag gives you a map of Hyrule and explains that the world is in chaos.", 
             "Q4A": "You try to attack the old hag but she overwhelms you, and you are defeated."},
    "Kap3": {"Q1A": "You helped the woman and killed the goblins. She thanks you and tells you that she is a woman from the Zora Village. She also tells you that her village is in danger because of a flood, which is caused by the Titan Vah Ruta, and tries to persuade you into helping her.",
             "Q2A": "You craft a Molotov cocktail but are too incompetent to throw it and accidentally harm yourself.",
             "Q3A": "You try to loot the goblin's base but they overpower you, and you are defeated."},
    "Kap4": {"Q1A": "You go to the woman's village and fight the Titan Vah Ruhta.",
             "Q2A": "She gives you her sword, which is a holy sword from her village. Then you go to her village and try to defeat the Titan.",
             "Q3A": "You ignore her and venture off to find other adventures waiting for you."},
    "Kap5": {"Q1A": "You travel to the Goronen Village and c",
             "Q2A": "You go and hunt down a rare monster that can only be found near the Zora Village, but then you come across some children who fled from the Goronen Village due to the Chaos caused by the Fire Titan. You decide to assist them and head towards the Goronen Village."},
    "Kap6": {"Q1A": ""}
} 


   
   

         



StartMessage()
platzh()
def Kapitel1():
    while True:
        print(QandA["Kap1"]['Text'])
        print(QandA["Kap1"]['Q1'])
        print(QandA["Kap1"]['Q2'])
        print(QandA["Kap1"]['Q3'])
        print(QandA["Kap1"]['Q4'])
        choice = input("Enter your choice (1, 2, 3, 4): ")

        if choice == "1":
            print(ChoiceA["Kap1"]["Q1A"])
            platzh()
            Kapitel2()
        elif choice == "2":
            print(ChoiceA["Kap1"]["Q2A"])
            platzh
            Kapitel1()
        elif choice == "3":
            print_status()
            platzh()
            Kapitel1()
        elif choice == "4":
            print ("You are going to sleep for another 100 years")
            platzh()
            Kapitel1()
        else:
            print("Invalid choice. Please try again.")

def Kapitel2():
    while True:
        print(QandA["Kap2"]['Text'])
        print(QandA["Kap2"]['Q1'])
        print(QandA["Kap2"]['Q2'])
        print(QandA["Kap2"]['Q3'])
        print(QandA["Kap2"]['Q4'])
        print(QandA["Kap2"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4, 5): ")

        if choice == "1":
            print(ChoiceA["Kap2"]["Q1A"])
            inventory.append("Map","Sword","Shield","Apple","Grilled Fish")
            platzh()
            Kapitel3
        elif choice == "2":
            print(ChoiceA["Kap2"]["Q2A"])
            platzh()
            Kapitel1()
        elif choice == "3":
            print(ChoiceA["Kap2"]["Q3A"])
            inventory.append("Map")
            platzh()
            Kapitel2()
        elif choice == "4":
            print(ChoiceA["Kap2"]["Q4A"])
            platzh()
            Kapitel1()
        elif choice == "5":
            print_status()
            platzh()
            Kapitel2()
        else:
            print("Invalid choice. Please try again.")

def Kapitel3():
    while True:
        print(QandA["Kap3"]['Text'])
        print(QandA["Kap3"]['Q1'])
        print(QandA["Kap3"]['Q2'])
        print(QandA["Kap3"]['Q3'])
        print(QandA["Kap3"]['Q4'])
        print(QandA["Kap3"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            print(ChoiceA["Kap3"]["Q1A"]) 
            platzh()
            Kapitel4()
        elif choice == "2":
            print(ChoiceA["Kap3"]["Q2A"])
            platzh()
            Kapitel1()
        elif choice == "3":
            print(ChoiceA["Kap3"]["Q2A"])
            platzh()
            Kapitel1()
        elif choice == "4":
            print(ChoiceA["Kap3"]["Q2A"])
            print_status()
            platzh()
        elif choice == "5":
            zelda_map()
            platzh()
            Kapitel2()
        else:
            print("Invalid choice. Please try again.")

Kapitel1()



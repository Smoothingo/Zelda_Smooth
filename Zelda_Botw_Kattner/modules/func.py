from modules.Game import *
import pygame
health = 10
defense = 10
import os

# define functions
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
# define functions

def sep_line():
    print("="*100)

def ssep_line():
    print("-"*100)

def bsep_line():
    print("═"*100)

inventory = {
    "weapons": {"sword": {"qty": 2, "atk": 10}, "axe": {"qty": 1, "atk": 12}, "mace": {"qty": 1, "atk": 15}},
    "food": {"potion": {"qty": 5, "health_bonus": 50}, "fish": {"qty": 2, "health_bonus": 20}},
    "defense": {"shield": {"qty": 1, "def": 5}, "armor": {"qty": 1, "def": 10}},
    "items": {"Map": {"qty": 1}, "Apple": {"qty": 5, "health_bonus": 10}, "Grilled Fish": {"qty": 2, "health_bonus": 30}, "Goblin Shield": {"qty": 1, "def": 8}},

}

Purse = 100


prices = {
    "sword": 20,
    "axe": 25,
    "mace": 30,
    "potion": 10,
    "fish": 5,
    "shield": 15,
    "armor": 30,
    "Map": 5,
    "Apple": 2,
    "Grilled Fish": 10,
    "Goblin Shield": 20
} # prices of items in the shop

def shop():
    print("Willkommen im Shop!")
    while True:
        print("Was möchten Sie tun?")
        print("1. Kaufen")
        print("2. Verkaufen")
        print("3. Verlassen")
        choice = input(">> ")
        if choice == "1":
            print("Was möchten Sie kaufen?")
            for item in prices:
                print(f"{item}: {prices[item]}")
            item_choice = input(">> ")
            if item_choice in prices:
                if inventory[item_choice]["qty"] > 0:
                    if Purse["Gold"] >= prices[item_choice]:
                        inventory[item_choice]["qty"] -= 1
                        Purse["Gold"] -= prices[item_choice]
                        print(f"Sie haben {item_choice} gekauft.")
                        print(f"Ihr neuer Kontostand beträgt {Purse['Gold']} Gold.")
                    else:
                        print("Sie haben nicht genug Gold.")
                else:
                    print(f"{item_choice} ist ausverkauft.")
            else:
                print("Das ist kein gültiger Artikel.")
        elif choice == "2":
            print("Was möchten Sie verkaufen?")
            for item in inventory:
                if inventory[item]["qty"] > 0:
                    print(f"{item}: {inventory[item]['qty']}")
            item_choice = input(">> ")
            if item_choice in inventory:
                qty = int(input(f"Wie viele {item_choice} möchten Sie verkaufen? "))
                if qty <= inventory[item_choice]["qty"]:
                    inventory[item_choice]["qty"] -= qty
                    Purse["Gold"] += prices[item_choice] * qty
                    print(f"Sie haben {qty} {item_choice} verkauft.")
                    print(f"Ihr neuer Kontostand beträgt {Purse['Gold']} Gold.")
                else:
                    print(f"Sie haben nicht genug {item_choice}.")
            else:
                print("Das ist kein gültiger Artikel.")
        elif choice == "3":
            break
        else:
            print("Das ist keine gültige Option.")



shop()

# This function takes an inventory dictionary as its input and prints the contents of the inventory in a formatted manner.
def print_inventory(inventory):
    # print the header for the inventory
    print("          Inventory:")
    print("================================")
    # print the weapons section of the inventory
    print("🗡 Weapons:")
    # iterate through each weapon and its attributes (quantity and attack power)
    for k, v in inventory["weapons"].items():
        # print the name of the weapon, its quantity, and its attack power
        print(f"\t• {k}: {v['qty']} ({v['atk']} attack)")
    # print the food section of the inventory
    print("\n🍔 Food:")
    # iterate through each food item and its attributes (quantity and health bonus)
    for k, v in inventory["food"].items():
        # print the name of the food item, its quantity, and its health bonus
        print(f"\t• {k}: {v['qty']} ({v['health_bonus']} health bonus)")
    # print the defense section of the inventory
    print("\n🛡 Defense:")
    # iterate through each defense item and its attributes (quantity and defense power)
    for k, v in inventory["defense"].items():
        # print the name of the defense item, its quantity, and its defense power
        print(f"\t• {k}: {v['qty']} ({v['def']} defense)")
    # print the items section of the inventory
    print("\n🧰 Items:")
    # iterate through each item and its attributes (quantity, health bonus, or defense power)
    for k, v in inventory["items"].items():
        # check if the item has a health bonus attribute
        if 'health_bonus' in v:
            # print the name of the item, its quantity, and its health bonus
            print(f"\t• {k}: {v['qty']} ({v['health_bonus']} health bonus)")
        # check if the item has a defense power attribute
        elif 'def' in v:
            # print the name of the item, its quantity, and its defense power
            print(f"\t• {k}: {v['qty']} ({v['def']} defense)")
        # if the item has neither health bonus nor defense power, it is a regular item
        else:
            # print the name of the item and its quantity
            print(f"\t• {k}: {v['qty']}")

if __name__ == "__main__":
    print_inventory(inventory)


def zelda_themesound(start_time=0):
    pygame.init()
    pygame.mixer.init()
    sound_file = "Zelda_Botw_Kattner\Sounds\zeldatheme.mp3"
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1, start_time)
    while pygame.mixer.music.get_busy():
        continue


def zeldamap():
    # initialize Pygame and set window size
    pygame.init()
    screen_height = 640
    screen_width = 960
    screen = pygame.display.set_mode((screen_width, screen_height))

    # load the image and scale it to fit the window
    zelda_map = pygame.image.load("Zelda_Botw_Kattner/Bilder\zelda_map.png")
    zelda_map = pygame.transform.scale(zelda_map, (screen_width, screen_height))

    # display the map and wait for user to close the window
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        screen.blit(zelda_map, (0, 0))
        pygame.display.update()

    pygame.quit()


# test the function

    

# Define function to print the current health of the player 
def print_health():
    print("Health: " + str(health), "\u2764\uFE0F "*health)
    # print("\u2764\uFE0F "*3)

# Define function to print whether the shield is equipped or not
def print_defense():
    print("Defense: " + str(defense), "🛡️ "*defense)

# Define function to print the inventory, current health and shield status.
def print_status(): 
    print_inventory(inventory)
    print("================================")
    print_health()
    print_defense()
    input("Press Enter to continue your Story...")
    bsep_line()
 
    

# Define function to reduce the player's health by an amount of damage inflicted.



# zelda portrait
def zelda_portrait():
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

#www
def Copyrigtname():
    name = "Markus Ernst Kattner"
    copyright = u"\u00A9" # Erstellt das Copyright-Zeichen
    print(copyright + " " + name)# Gibt das Ergebnis aus




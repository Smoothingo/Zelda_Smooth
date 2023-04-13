from modules.Game import *
import pygame
import os
import sys

health = 10
defense = 10


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

def beta_version_sorry():
    print("Sorry, this feature is not available in the beta version. 🚫")
    print("Im sorry to disappoint you, but use the time that you initially wanted to play in learning the German language.")
    print("I wish you a nice day and a good time.")
    print("This is my Github account for the repository of this project: https://github.com/Smoothingo/Zelda_Smooth")
    sys.exit()
personal_inventory = {
    "weapons": {
    },
    "food": {
    
    },
    "defense": {
        
    },
    "items": {
    },
}
shop_inventory = {
    "weapons": {
        "sword": {"qty": 2, "atk": 10, "price": 15},
        "axe": {"qty": 1, "atk": 12, "price": 15},
        "mace": {"qty": 1, "atk": 15, "price": 15},
    },
    "food": {
        "potion": {"qty": 5, "health_bonus": 50, "price": 15},
        "fish": {"qty": 2, "health_bonus": 20, "price": 15},
    },
    "defense": {
        "shield": {"qty": 1, "def": 5, "price": 10},
        "armor": {"qty": 1, "def": 10, "price": 11},
    },
    "items": {
        "map": {"qty": 1, "price": 0},
        "apple": {"qty": 5, "health_bonus": 10, "price": 5},
        "grilled_fish": {"qty": 2, "health_bonus": 30, "price": 15},
        "goblin_shield": {"qty": 1, "def": 8, "price": 15},
    },
}

purse = {"💰 Rupees": 30}

def show_balance(purse):
    print(f"You're total Rupees are {purse['💰 Rupees']}")

def buy_item(item, shop_personal_inventory, purse):
    excluded_items = ["map"]
    if item in excluded_items:
        print("You can't buy this item! 🚫")
        return False
    item_data = None
    for category, items in shop_personal_inventory.items():
        if item in items:
            item_data = items[item]
            break
    if not item_data:
        print(f"{item} is not available in this shop. 🚫")
        return False
    if purse['💰 Rupees'] < item_data['price']:
        print("You dont have enough Rupees! 💔")
        return False
    qty_available = item_data['qty']
    qty_to_buy = 1
    if qty_available > 1:
        qty_to_buy = int(input(f"How many {item} do you want to buy? "))
        if qty_to_buy > qty_available:
            print(f"Sorry, only {qty_available} {item}(s) are available.")
            return False
    total_price = item_data['price'] * qty_to_buy
    purse['💰 Rupees'] -= total_price
    item_data['qty'] -= qty_to_buy
    if item_data['qty'] == 0:
        del shop_personal_inventory[category][item]
        if not shop_personal_inventory[category]:
            del shop_personal_inventory[category]
    print(f"You bought {qty_to_buy} {item}(s)! 🛍️")
    return True

def sell_item(item, shop_personal_inventory, purse):
    excluded_items = ["map"]
    if item in excluded_items:
        print("You can't sell this item! 🚫")
        return False
    item_data = None
    for category, items in shop_personal_inventory.items():
        if item in items:
            item_data = items[item]
            break
    if not item_data:
        print(f"{item} is not available in this shop. 🚫")
        return False
    qty_available = item_data['qty']
    qty_to_sell = 1
    if qty_available > 1:
        qty_to_sell = int(input(f"How many {item} do you want to sell? "))
        if qty_to_sell > qty_available:
            print(f"Sorry, you only have {qty_available} {item}(s).")
            return False
    total_price = item_data['price'] * qty_to_sell
    purse['💰 Rupees'] += total_price
    item_data['qty'] += qty_to_sell
    print(f"You sold {qty_to_sell} {item}(s)! 💰")
    return True



def dis_personal_inventory(shop_personal_inventory, category):
    print(f"{category.capitalize()}:")
    for item in shop_personal_inventory[category]:
        qty = shop_personal_inventory[category][item]['qty']
        price = shop_personal_inventory[category][item]['price']
        stats = ""
        if 'atk' in shop_personal_inventory[category][item]:
            stats += f" ATK: {shop_personal_inventory[category][item]['atk']}"
        if 'def' in shop_personal_inventory[category][item]:
            stats += f" DEF: {shop_personal_inventory[category][item]['def']}"
        if 'health_bonus' in shop_personal_inventory[category][item]:
            stats += f" HP: {shop_personal_inventory[category][item]['health_bonus']}"
        print(f"{item.capitalize()}: {qty} available for {price} 💰 per unit.{stats}")
        

def shop_interact(shop_personal_inventory, purse):
    while True:
        print("Welcome to the Shop! What do you want to do?")
        print("[B] - Buy something")
        print("[S] - Sell something")
        print("[Q] - Quit shopping")

        action = input("Choose an option:").lower()

        if action == "b":
            show_balance(purse)
            print_shop_personal_inventory(shop_personal_inventory)
            item = input("What do you want to buy: ").lower()
            if buy_item(item, shop_personal_inventory, purse):
                print(f"You have {purse['💰 Rupees']} Rupees.")
                a = input("Would you like to continue shopping or safe Hyrule before its to late? (shop/safe) ").lower()
                if a == "shop":
                    continue
                elif a == "safe":
                    break
                else:
                    print("Sorry, that not an valid option.")
            else:
                print(f"Im sorry, {item} could not be bought.")
        elif action == "s":
            show_balance(purse)
            print_shop_personal_inventory(shop_personal_inventory)
            item = input("What do you want to sell: ").lower()
            if sell_item(item, shop_personal_inventory, purse):
                print(f"You have {purse['💰 Rupees']} Rupees.")
                a = input("Would you like to continue shopping or safe Hyrule before its to late? (shop/safe) ").lower()
                if a == "shop":
                    continue
                elif a == "safe":
                    break
                else:
                    print("Sorry, that not an valid option.")
            else:
                print(f"Im sorry, {item} could not be selled.")
        elif action == "q":
            print("Good bye! Enjoy your life young Adventurer!")


   # show_personal_inventory(shop_personal_inventory)
def print_shop_personal_inventory(shop_personal_inventory):
    # print the header for the personal_inventory
    print("          Shop Items:")
    print("================================")
    # print the weapons section of the personal_inventory
    print("🗡 Weapons:")
    # iterate through each weapon and its attributes (quantity and attack power)
    for k, v in shop_personal_inventory["weapons"].items():
        # print the name of the weapon, its quantity, and its attack power
        print(f"\t• {k}: {v['qty']} ({v['atk']} attack) ({v['price']} 💰 Rupees each)")
    # print the food section of the personal_inventory
    print("\n🍔 Food:")
    # iterate through each food item and its attributes (quantity and health bonus)
    for k, v in shop_personal_inventory["food"].items():
        # print the name of the food item, its quantity, and its health bonus
        print(f"\t• {k}: {v['qty']} ({v['health_bonus']} health bonus) ({v['price']} 💰 Rupees each)")
    # print the defense section of the personal_inventory
    print("\n🛡 Defense:")
    # iterate through each defense item and its attributes (quantity and defense power)
    for k, v in shop_personal_inventory["defense"].items():
        # print the name of the defense item, its quantity, and its defense power
        print(f"\t• {k}: {v['qty']} ({v['def']} defense) ({v['price']} 💰 Rupees each)")
    # print the items section of the personal_inventory
    print("\n🧰 Items:")
    # iterate through each item and its attributes (quantity, health bonus, or defense power)
    for k, v in shop_personal_inventory["items"].items():
        # check if the item has a health bonus attribute
        if 'health_bonus' in v:
            # print the name of the item, its quantity, and its health bonus
            print(f"\t• {k}: {v['qty']} ({v['health_bonus']} health bonus) ({v['price']} 💰 Rupees each)")
        # check if the item has a defense power attribute
        elif 'def' in v:
            # print the name of the item, its quantity, and its defense power
            print(f"\t• {k}: {v['qty']} ({v['def']} defense) ({v['price']} 💰 Rupees each)")
        # if the item has neither health bonus nor defense power, it is a regular item
        else:
            # print the name of the item and its quantity
            print(f"\t• {k}: {v['qty']}")



# This function takes an personal_inventory dictionary as its input and prints the contents of the personal_inventory in a formatted manner.
def print_personal_inventory(personal_inventory):
    # print the header for the personal_inventory
    print("          Personal personal_inventory:")
    print("================================")
    # print the weapons section of the personal_inventory
    print("🗡 Weapons:")
    # iterate through each weapon and its attributes (quantity and attack power)
    for k, v in personal_inventory["weapons"].items():
        # print the name of the weapon, its quantity, and its attack power
        print(f"\t• {k}: {v['qty']} ({v['atk']} attack) ({v['price']} 💰 Rupees each)")
    # print the food section of the personal_inventory
    print("\n🍔 Food:")
    # iterate through each food item and its attributes (quantity and health bonus)
    for k, v in personal_inventory["food"].items():
        # print the name of the food item, its quantity, and its health bonus
        print(f"\t• {k}: {v['qty']} ({v['health_bonus']} health bonus) ({v['price']} 💰 Rupees each)")
    # print the defense section of the personal_inventory
    print("\n🛡 Defense:")
    # iterate through each defense item and its attributes (quantity and defense power)
    for k, v in personal_inventory["defense"].items():
        # print the name of the defense item, its quantity, and its defense power
        print(f"\t• {k}: {v['qty']} ({v['def']} defense) ({v['price']} 💰 Rupees each)")
    # print the items section of the personal_inventory
    print("\n🧰 Items:")
    # iterate through each item and its attributes (quantity, health bonus, or defense power)
    for k, v in personal_inventory["items"].items():
        # check if the item has a health bonus attribute
        if 'health_bonus' in v:
            # print the name of the item, its quantity, and its health bonus
            print(f"\t• {k}: {v['qty']} ({v['health_bonus']} health bonus) ({v['price']} 💰 Rupees each)")
        # check if the item has a defense power attribute
        elif 'def' in v:
            # print the name of the item, its quantity, and its defense power
            print(f"\t• {k}: {v['qty']} ({v['def']} defense) ({v['price']} 💰 Rupees each)")
        # if the item has neither health bonus nor defense power, it is a regular item
        else:
            # print the name of the item and its quantity
            print(f"\t• {k}: {v['qty']}")

if __name__ == "__main__":
    print_personal_inventory(personal_inventory)

relativ = 'Sounds\\zeldatheme.mp3'
absolut = os.path.abspath(os.path.join(sys.path[0], relativ))                            ##Credit Dragoljub Mitrovic

def zelda_themesound():
    pygame.init()
    pygame.mixer.music.load("C:\\Users\\Markus\\Desktop\\Zelda_BOTW\\Zelda_Botw_Kattner\\Sounds\\zeldatheme.mp3")
    pygame.mixer.music.play()


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

# Define function to print the personal_inventory, current health and shield status.
def print_status(): 
    print_personal_inventory(personal_inventory)
    print("================================")
    print_health()
    print_defense()
    input("Press Enter to continue your Story...")
    bsep_line()
 
    

# Define function to reduce the player's health by an amount of damage inflicted.
def death():
        print("You have died. Game Over.")
        sys.exit()


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




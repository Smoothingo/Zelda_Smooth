import pygame
import os
import sys
import threading
import time
health = 10
defense = 10
#https://www.pygame.org/docs/
def play_music(file_name):
            dir_path = os.path.dirname(os.path.abspath(__file__))    
            file_path = os.path.join(dir_path, file_name)
            pygame.mixer.init()
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play(-1)
#help from here:https://stackoverflow.com/questions/53246933/python-execute-playsound-in-separate-thread
def start_music_thread(file_name):
    music_thread = threading.Thread(target=play_music, args=(file_name,))
    music_thread.start()

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
    print("YOU WON THE BETA VERSION be hyped for the full version")
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
        "apple": {"qty": 5, "health_bonus": 10, "price": 5},
        "grilled_fish": {"qty": 2, "health_bonus": 30, "price": 15},
        "goblin_shield": {"qty": 1, "def": 8, "price": 15},
    },
}

purse = {"💰 Rupees": 30}
# looked a bit there: https://stackoverflow.com/questions/73286001/beating-textbased-game-with-a-full-inventory-of-items
def show_balance(purse):
    print(f"You're total Rupees are {purse['💰 Rupees']}")

def buy_item(item, shop_personal_inventory, purse):
    excluded_items = ["map"]
    if item in excluded_items:
        print("You can't buy this item! 🚫")
        return False
    item_data = None
    for category, items in shop_personal_inventory.items():       #https://stackoverflow.com/questions/66453344/dict-items-function
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
        del shop_personal_inventory[category][item]                 # https://stackoverflow.com/questions/6146963/when-is-del-useful-in-python
        if not shop_personal_inventory[category]:                   
            del shop_personal_inventory[category]
    print(f"You bought {qty_to_buy} {item}(s)! 🛍️")
    return True

def sell_item(item, shop_personal_inventory, purse):
    excluded_items = ["map"]
    if item in excluded_items:
        print("You can't sell this item! 🚫")
        return False                          # ('w', 2 [])
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
    print("          Personal inventory:")
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

def fightsystem(health, defense, enemy_health, enemy_defense, enemy_attack, enemy_name):

    while True:

 
    

# Define function to reduce the player's health by an amount of damage inflicted.
def death():
        pygame.mixer.stop()
        time.sleep(1)
        bsep_line()
        start_music_thread("zeldadeath.mp3")        #https://www.asciiart.eu/mythology/skeletons
        print(''' 	

                              ,,..
                            ,@$$$$$.
                          .,$$$$$$$$i
                    .,z$""')$$$$$$$$C`^#`-..
                 ,zF'        `""#*"'       "*o.
              ,zXe>        u:..        ..      "c
            ,' zP'    ,:`"          .            "N.
          ,d",d$   ,'"   ,uB" .,uee..,?R.  ,  .    ^$.
        ,@P d$"     .:$$$$$$$$$$$$$@$CJN.,"    `     #b
       z$" d$P    :SM$$$$$$$$$$$$$$$$$$$Nf.           ^$.
      J$" J$P  , ,@$$$$$$$$$$$$$$$$$$$$$$$$$k.         "$r
     z$   $$.   ,$$$$$$$$$$$$$$$$$$$$$$$$$$f'   .    .   $b
    ,$"  $$u,-.x'^""$$$$$$$$$$$$$$$$$$$$$$$$$.        `.  $k
    $"  :$$$$> 8.   `#$$$$$$$$$$$$$$$$$$$$$"\  d  .    F   $.
   $P  .$$$$$N `$b.  $$$$$$$$$$$$$$$$$$$$$k.$  $"  :   '   `$
  {$'  4$$k $$c `*$.,Q$$$$$$$$$$$$$$$$$$$$$$$ ..            $L
  $P   4$$$$$F:   `"$$$$$$$$$$$$$$$$$$$$$$'`$"     .   ,    `$
 ,$'  ,$$$$$d$$    '##$$c3$$$$$$$$$$$$$$$$. '      :   L.    $.
 J$  u$$$$$$$$$.,oed$*$$$$N "#$$$$$$$$$$***$@$N. , $  ,B$$N.,9L
 $F,$$$$$$$$$$,@*"'  `J$$$$$#h$$$$$$P"`     `"*$$. $4W$' "$$uJF
 4$$$$$$$$$$$$F'      $*'`$$RR@$$$$$R        ,' "$d$4"    '$$$R
,$$$$$$$$$$$$$F     ,'    @$.3$$$$ R>            `$F$  dN.4$$$$.
$$$$$$$$$$$$*$"          J$'$$$$$& $.             $'   $$$$$$$$$o
^$$$$$$$$$$B@$$          $P $$$"?N/$k             $r   $$P"*$$$$'
  $$i  .$$$$"$'         $$ ~R$P '$k^$$,'          $   "'  ,d$$'
  $$$$ J$$$$ `,'    .,z$P'd.$P   #$. #$$u.       .$  eu. ,d$$$
  $^$$$$$$$$. `"=+=N#'.,d$M$$'   `$$@s.#$$$u.   ,$C  $$$@$$$"$
  "  `*$$$$$$bx..        ,M$"     `*$$$b/""$R"*"'d$ ,$$$$P"  '
  4     "$$k3$9$$B.e.  ,ud$F       `3$$$$b.      ,$,@R$*'    4
  {       *$$$$$$$b$$@$$$$$L   ,.  ,J$$.'**$$k$NX$"M"'       .
  $         "$#"  `" {$$$$$$c,z$N.,o$$$$   ,NW$*"'           $
  $.         ',    `$$$$$$$$$d$$$$$$$$$f ,$e*'               $
 ,$c         d.     `^$$$$$$$$$$$$$$$$$.u '"                :$.
 $$$         $\   .,  `"#$$$*$$$$$$$$$$$$ '                 4$F
 $$"         $ `  k.`.     ``"#`"""'      ,' ,'             `$$
 `"          $>,  `b.,ce(b:o uz CCLd$4$*F?\,o                "' 
             $&    $$k'*"$$$$$$#$$$$s$$$$$$ d'
             $$.,$$$$$$$$,e,$#$.*$`""""'e4 $
             `$$$$  ^$$\$"$$$$$$$$$$$$$$$.eL
              $$$"  $$$$$$$e$.$.$$.$e$d$$$$k
              R`$$  '$$$$$$$$$$$$$$$$$$$$$$P
              `  $Nc'"$$N3$$$$$$$$$$$$$$$$$'
                  *$  9$.`@$$$$$$$$$$R$$$#'
                   `$.  `"*$$$$$$$$$$P'' #
                     "$u.    `""""''   ,'
                       `"$Nu..  .,z{p"'
                           `"####""''')
        time.sleep(3)
        deathmessage = "You have died. Game Over."
        for char in deathmessage:
            print(char, end='', flush=True)
            time.sleep(0.03)
        sys.exit()


# zelda portrait ( https://www.asciiart.eu/video-games/zelda )
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




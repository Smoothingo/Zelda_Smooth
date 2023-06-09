inventory = {
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
    print(f"You have {purse['💰 Rupees']} left.")

def buy_item(item, shop_inventory, purse):
    excluded_items = ["map"]
    if item in excluded_items:
        print("You can't buy this item! 🚫")
        return False
    item_data = None
    for category, items in shop_inventory.items():
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
        del shop_inventory[category][item]
        if not shop_inventory[category]:
            del shop_inventory[category]
    print(f"You bought {qty_to_buy} {item}(s)! 🛍️")
    return True

def sell_item(item, shop_inventory, purse):
    excluded_items = ["map"]
    if item in excluded_items:
        print("You can't sell this item! 🚫")
        return False
    item_data = None
    for category, items in shop_inventory.items():
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



def dis_inventory(shop_inventory, category):
    print(f"{category.capitalize()}:")
    for item in shop_inventory[category]:
        qty = shop_inventory[category][item]['qty']
        price = shop_inventory[category][item]['price']
        stats = ""
        if 'atk' in shop_inventory[category][item]:
            stats += f" ATK: {shop_inventory[category][item]['atk']}"
        if 'def' in shop_inventory[category][item]:
            stats += f" DEF: {shop_inventory[category][item]['def']}"
        if 'health_bonus' in shop_inventory[category][item]:
            stats += f" HP: {shop_inventory[category][item]['health_bonus']}"
        print(f"{item.capitalize()}: {qty} available for {price} 💰 per unit.{stats}")
        

def shop_interact(shop_inventory, purse):
    while True:
        print("Welcome to the Shop! What do you want to do?")
        print("[B] - Buy something")
        print("[S] - Sell something")
        print("[Q] - Quit shopping")

        action = input("Choose an option:").lower()

        if action == "b":
            show_balance(purse)
            print_shop_inventory(shop_inventory)
            item = input("What do you want to buy: ").lower()
            if buy_item(item, shop_inventory, purse):
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
            print_shop_inventory(shop_inventory)
            item = input("What do you want to sell: ").lower()
            if sell_item(item, shop_inventory, purse):
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


   # show_inventory(shop_inventory)
def print_shop_inventory(shop_inventory):
    # print the header for the inventory
    print("          Inventory:")
    print("================================")
    # print the weapons section of the inventory
    print("🗡 Weapons:")
    # iterate through each weapon and its attributes (quantity and attack power)
    for k, v in shop_inventory["weapons"].items():
        # print the name of the weapon, its quantity, and its attack power
        print(f"\t• {k}: {v['qty']} ({v['atk']} attack)")
    # print the food section of the inventory
    print("\n🍔 Food:")
    # iterate through each food item and its attributes (quantity and health bonus)
    for k, v in shop_inventory["food"].items():
        # print the name of the food item, its quantity, and its health bonus
        print(f"\t• {k}: {v['qty']} ({v['health_bonus']} health bonus)")
    # print the defense section of the inventory
    print("\n🛡 Defense:")
    # iterate through each defense item and its attributes (quantity and defense power)
    for k, v in shop_inventory["defense"].items():
        # print the name of the defense item, its quantity, and its defense power
        print(f"\t• {k}: {v['qty']} ({v['def']} defense)")
    # print the items section of the inventory
    print("\n🧰 Items:")
    # iterate through each item and its attributes (quantity, health bonus, or defense power)
    for k, v in shop_inventory["items"].items():
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

shop_interact(shop_inventory, purse)
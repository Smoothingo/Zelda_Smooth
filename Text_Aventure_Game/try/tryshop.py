# Define initial variables
inventory = {
    "weapons": {"sword": {"qty": 2, "atk": 10}, "axe": {"qty": 1, "atk": 12}, "mace": {"qty": 1, "atk": 15}},
    "food": {"potion": {"qty": 5, "health_bonus": 50}, "fish": {"qty": 2, "health_bonus": 20}},
    "defense": {"shield": {"qty": 1, "def": 5}, "armor": {"qty": 1, "def": 10}},
    "items": {"Map": {"qty": 1}, "Apple": {"qty": 5, "health_bonus": 10}, "Grilled Fish": {"qty": 2, "health_bonus": 30}, "Goblin Shield": {"qty": 1, "def": 8}}
}

rupees = 100

def print_rupees(rupees):
   print("You have {} rupees".format(rupees))


shop = {
    "sword": {"price": 50, "atk": 10},
    "axe": {"price": 75, "atk": 12},
    "mace": {"price": 100, "atk": 15},
    "potion": {"price": 20, "health_bonus": 50},
    "fish": {"price": 10, "health_bonus": 20},
    "shield": {"price": 30, "def": 5},
    "armor": {"price": 100, "def": 10},
    "map": {"price": 50},
    "apple": {"price": 5, "health_bonus": 10},
    "grilled fish": {"price": 15, "health_bonus": 30},
    "goblin shield": {"price": 40, "def": 8}
}

# Define helper functions
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


def print_shop():
    print("Shop inventory:")
    for item, details in shop.items():
        if item not in inventory[details.get("category", "")]:
            print(f"{item.capitalize()} ({details.get('category', 'item').capitalize()}): {details['price']} rupees")
    print()

# Define main loop
def print_Trader(rupees):
    while True:
        print(f"You have {rupees} rupees")
        print_inventory(inventory)
        print_shop()

        action = input("What would you like to do? (buy/sell/exit) ")
        if action == "buy":
            item = input("What would you like to buy? ").lower()
            if item not in shop:
                print("Sorry, we don't have that item")
            elif shop[item]["price"] > rupees:
                print("Sorry, you don't have enough rupees")
            else:
                category = shop[item].get("category", "items")
                if category not in inventory:
                    inventory[category] = {}
                if item not in inventory[category]:
                    inventory[category][item] = {"qty": 0}
                inventory[category][item]["qty"] += 1
                rupees -= shop[item]["price"]
                print(f"You bought {item.capitalize()} for {shop[item]['price']} rupees")
        elif action == "sell":
            item = input("What would you like to sell? ").lower()
            category = None
            for cat, items in inventory.items():
                if item in items:
                    category = cat
                    break
            if not category:
                print("Sorry, you don't have that item")
            elif item not in shop:
                print("Sorry, we don't accept that item")
            else:
                qty = inventory[category][item]["qty"]
                inventory[category][item]["qty"] -= 1
                if inventory[category][item]["qty"] == 0:
                    del inventory[category][item]
                rupees += shop[item]["price"] * qty
                print(f"You sold {qty}x {item.capitalize()} for {shop[item]['price']*qty} rupees")
        elif action == "exit":
            print("Thanks for playing!")
            break
        else:
            print("Sorry, I didn't understand that")
print_Trader(rupees)
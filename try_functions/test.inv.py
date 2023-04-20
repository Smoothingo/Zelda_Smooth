inventory = {
    "weapons": {"sword": {"qty": 2, "atk": 10}, "axe": {"qty": 1, "atk": 12}, "mace": {"qty": 1, "atk": 15}},
    "food": {"potion": {"qty": 5, "health_bonus": 50}, "fish": {"qty": 2, "health_bonus": 20}},
    "defense": {"shield": {"qty": 1, "def": 5}, "armor": {"qty": 1, "def": 10}},
    "items": {"Map": {"qty": 1}, "Apple": {"qty": 5, "health_bonus": 10}, "Grilled Fish": {"qty": 2, "health_bonus": 30}, "Goblin Shield": {"qty": 1, "def": 8}}
}

# This function takes an inventory dictionary as its input and prints the contents of the inventory in a formatted manner.
def display_inventory(inventory):
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

# example usage
# display the contents of the inventory dictionary
display_inventory(inventory)



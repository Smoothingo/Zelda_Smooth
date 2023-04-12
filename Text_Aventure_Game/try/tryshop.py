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

def show_balance(purse):
    print(f"You have {purse['💰 Rupees']} left.")

def buy_item(item, shop_inventory, purse):
    item_data = shop_inventory.get(item.lower())
    if not item_data:
        print(f"{item} is not available in this shop. 🚫")
        return False
    if purse['💰 Rupees'] < item_data['price']:
        print("You dont have enough Rupees! 💔")
        return False
    purse['💰 Rupees'] -= item_data['price']
    item_data['qty'] -= 1
    if item_data['qty'] == 0:
        shop_inventory.pop(item.lower())
    print(f"You bought {item} ! 🛍️")
    return True

def sell_item(item, shop_inventory, purse):
    if item in shop_inventory:
        purse['💰 Rupees'] += shop_inventory[item]['price']
        shop_inventory[item]['qty'] += 1
        print(f"You sold {item} ! 💰")
        return True
    else:
        print(f"{item} is not available in this shop. 🚫")
        return False

def show_inventory(shop_inventory):
    for item in shop_inventory:
        print(f"{item}: {shop_inventory[item]['qty']} available for {shop_inventory[item]['price']} 💰 per Unit.")

def shop_interact():
    purse = {"💰 Rupees": 10}
    shop_inventory = {
        "apple": {"qty": 10, "health_bonus": 10, "price": 1},
        "banana": {"qty": 5, "health_bonus": 10, "price": 2},
        "orange": {"qty": 3, "health_bonus": 10, "price": 3},
        "sword": {"qty": 1, "atk": 10, "price": 10},
        "shield": {"qty": 1, "def": 5, "price": 5},
    }

    while True:
        print("Welcome to the Shop! What do you want to do?")
        print("[K] - Buy something")
        print("[V] - Sell something")
        print("[B] - Show balance")
        print("[Q] - Shop verlassen")

        action = input("Choose an option:").lower()

        if action == "k":
            show_inventory(shop_inventory)
            item = input("What do you want to buy").lower()
            if buy_item(item, shop_inventory, purse):
                print(f"You have {purse['💰 Rupees']} Rupees.")
            else:
                print(f"Im sorry, {item} could not be bought.")
        elif action == "v":
            show_inventory(inventory)
            item = input("What do you want to sell ").lower()
            if sell_item(item, shop_inventory, purse):
                print(f"You have {purse['💰 Rupees']} Rupees.")
            else:
                print(f"Im sorry, {item} could not be selled.")
        elif action == "b":
            show_balance(purse)
        elif action == "q":
            print("Good bye! Enjoy your life young Adventurer!")

shop_interact()

   # show_inventory(shop_inventory)
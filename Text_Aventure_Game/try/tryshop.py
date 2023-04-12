inventory = {'gold': 50, 'sword': 1, 'armor': 0, 'potion': 2} # player's inventory
prices = {'sword': 10, 'armor': 20, 'potion': 5} # prices of items in the shop

def shop_system():
    print("You meet a merchant in the town square.")
    print("Merchant: Welcome adventurer, do you need any supplies for your journey?")
    while True:
        print("What would you like to do?")
        print("1. Buy items")
        print("2. Sell items")
        print("3. Leave")
        choice = input("> ")
        if choice == '1':
            buy_items()
        elif choice == '2':
            sell_items()
        elif choice == '3':
            print("Merchant: Goodbye.")
            break
        else:
            print("Merchant: I'm sorry, I didn't understand your choice.")

def buy_items():
    print("Items for sale:")
    for item, price in prices.items():
        print(f"- {item.capitalize()} ({price} gold)")
    print("What would you like to buy? (Enter 'done' to exit.)")
    cart = {}
    while True:
        item = input("> ").lower()
        if item == 'done':
            break
        elif item not in prices:
            print("Merchant: I'm sorry, I don't have that item.")
        elif inventory['gold'] < prices[item]:
            print("Merchant: I'm sorry, you don't have enough gold for that item.")
        else:
            cart[item] = cart.get(item, 0) + 1
            inventory['gold'] -= prices[item]
            inventory[item] += 1
            print(f"Merchant: You bought a {item.capitalize()} for {prices[item]} gold.")
            print(f"You have {inventory['gold']} Gold left")

    if cart:
        print("Shopping Cart:")
        for item, quantity in cart.items():
            print(f"- {item.capitalize()}: {quantity}")
        total_cost = calculate_total(cart)
        print(f"Total cost: {total_cost} gold")
        print("Would you like to buy these items? (yes or no)")
        choice = input("> ")
        if choice.lower() == 'yes':
            print("Merchant: Thank you for your purchase.")
        else:
            for item, quantity in cart.items():
                inventory['gold'] += prices[item] * quantity
                inventory[item] -= quantity
            print("Merchant: Your items have been returned to your inventory.")
    else:
        print("Merchant: Goodbye.")

def sell_items():
    print("Items to sell:")
    for item, quantity in inventory.items():
        if item != 'gold' and quantity > 0:
            print(f"- {item.capitalize()} ({prices[item]} gold each, {quantity} in inventory)")
    print("What would you like to sell? (Enter 'done' to exit.)")
    sold_items = {}
    while True:
        item = input("> ").lower()
        if item == 'done':
            break
        elif item not in prices:
            print("Merchant: I'm sorry, I can't buy that item.")
        elif inventory[item] == 0:
            print("Merchant: You don't have any of those items to sell.")
        else:
            sold_items[item] = sold_items.get(item, 0) + 1
            inventory['gold'] += prices[item]
            inventory[item] -= 1
            print(f"Merchant: I bought your {item.capitalize()} for {prices[item]} gold.")
            print(f"You're total Gold is {inventory['gold']}")
    if sold_items:
        print("Sold Items:")
        for item, quantity in sold_items.items():
            print(f"- {item.capitalize()}: {quantity}")
        print(f"Earned: {calculate_total(sold_items)} gold")
    else:
        print("Merchant: Goodbye.")



def calculate_total(items):
    total = 0
    for item in items:
        total += prices[item] * items[item]
        return total
    
shop_system()
print("Final Inventory:")
print(inventory)
    



# inventory = {
#     "weapons": {"sword": {"qty": 2, "atk": 10}, "axe": {"qty": 1, "atk": 12}, "mace": {"qty": 1, "atk": 15}},
#     "food": {"potion": {"qty": 5, "health_bonus": 50}, "fish": {"qty": 2, "health_bonus": 20}},
#     "defense": {"shield": {"qty": 1, "def": 5}, "armor": {"qty": 1, "def": 10}},
#     "items": {"Map": {"qty": 1}, "Apple": {"qty": 5, "health_bonus": 10}, "Grilled Fish": {"qty": 2, "health_bonus": 30}, "Goblin Shield": {"qty": 1, "def": 8}}
# }















# import random

# # Set up the player and enemy stats
# player_hp = 100
# player_atk = 10
# player_def = 5

# enemy_hp = 80
# enemy_atk = 15
# enemy_def = 8

# # Print out the enemy stats
# print("You have encountered an enemy!")
# print(f"Enemy HP: {enemy_hp}")
# print(f"Enemy ATK: {enemy_atk}")
# print(f"Enemy DEF: {enemy_def}")

# # Define the available weapons
# weapons = inventory["weapons"]
# weapon_names = list(weapons.keys())
# print("Available weapons:")
# for i, weapon_name in enumerate(weapon_names):
#     weapon_stats = weapons[weapon_name]
#     print(f"{i + 1}. {weapon_name} (ATK: {weapon_stats['atk']})")
# print("")

# # Choose a weapon
# while True:
#     weapon_choice = input("Choose your weapon: ")
#     if weapon_choice.isdigit() and int(weapon_choice) in range(1, len(weapon_names) + 1):
#         weapon_choice = int(weapon_choice) - 1
#         weapon_name = weapon_names[weapon_choice]
#         weapon_stats = weapons[weapon_name]
#         break
#     else:
#         print("Invalid choice.")

# # Calculate the damage based on the weapon
# weapon_damage = weapon_stats["atk"] + random.randint(-2, 2)
# print(f"You attack with your {weapon_name} for {weapon_damage} damage.")

# # Apply the damage to the enemy
# enemy_damage = max(0, weapon_damage - enemy_def)
# enemy_hp -= enemy_damage
# print(f"The enemy takes {enemy_damage} damage.")
# print(f"Enemy HP: {enemy_hp}")

# # Check if the enemy is still alive
# if enemy_hp <= 0:
#     print("You have defeated the enemy!")
#     # You could add code here to reward the player with loot or XP.
# else:
#     # Calculate the enemy's attack damage
#     enemy_attack_damage = max(0, enemy_atk - player_def)
#     player_hp -= enemy_attack_damage
#     print(f"The enemy attacks you for {enemy_attack_damage} damage.")
#     print(f"Your HP: {player_hp}")

#     # Check if the player is still alive
#     if player_hp <= 0:
#         print("You have been defeated. Game over.")
#     else:
#         print("You continue the fight...")
#         # The fight would continue until either the player or the enemy is defeated.
goblin_hp = 50

import random

inventory = {
    "weapons": {"sword": {"qty": 2, "atk": 10}, "axe": {"qty": 1, "atk": 12}, "mace": {"qty": 1, "atk": 15}},
    "food": {"potion": {"qty": 5, "health_bonus": 50}, "fish": {"qty": 2, "health_bonus": 20}},
    "defense": {"shield": {"qty": 1, "def": 5}, "armor": {"qty": 1, "def": 10}},
    "items": {"Map": {"qty": 1}, "Apple": {"qty": 5, "health_bonus": 10}, "Grilled Fish": {"qty": 2, "health_bonus": 30}, "Goblin Shield": {"qty": 1, "def": 8}}
}

def fight(goblin_hp):
    print("You are fighting a goblin!")
    
    weapon_choice = input("Choose your weapon (sword/axe/mace): ")
    if weapon_choice not in inventory["weapons"]:
        print("Invalid weapon!")
        return
    
    defense_choice = input("Choose your defense (shield/armor): ")
    if defense_choice not in inventory["defense"]:
        print("Invalid defense!")
        return
    
    food_choice = input("Choose your food (potion/fish): ")
    if food_choice not in inventory["food"]:
        print("Invalid food!")
        return
    
    weapon_atk = inventory["weapons"][weapon_choice]["atk"]
    defense_def = inventory["defense"][defense_choice]["def"]
    
    while goblin_hp > 0:
        goblin_atk = random.randint(1,5)
        goblin_def = random.randint(1,5)
        
        print(f"Goblin HP: {goblin_hp}")
        print(f"Your HP: {100}")
        
        attack_choice = input("Do you want to attack? (y/n): ")
        
        if attack_choice == 'y':
            damage = weapon_atk - goblin_def
            if damage < 0:
                damage = 0
            goblin_hp -= damage
            print(f"You dealt {damage} damage to the goblin!")
            
            food_use_choice = input("Do you want to use your food? (y/n): ")
            if food_use_choice == 'y':
                health_bonus = inventory["food"][food_choice]["health_bonus"]
                print(f"You gained {health_bonus} health points!")
                
                if food_choice == 'potion':
                    inventory["food"][food_choice]["qty"] -= 1
                    if inventory["food"][food_choice]["qty"] == 0:
                        del inventory["food"][food_choice]
                else:
                    inventory["food"][food_choice]["qty"] -= 1
                    if inventory["food"][food_choice]["qty"] == 0:
                        del inventory["food"][food_choice]
                        
            else:
                print("You didn't use your food.")
                
        else:
            print("You didn't attack.")
            
        if goblin_hp <= 0:
            print("You won!")
            break
        
        damage = goblin_atk - defense_def
        if damage < 0:
            damage = 0
        print(f"The goblin dealt {damage} damage to you!")
        
        if 'shield' in defense_choice and random.random() < .3:
            print('Your shield broke!')
            del inventory['defense']['shield']
            
        elif 'armor' in defense_choice and random.random() < .3:
            print('Your armor broke!')
            del inventory['defense']['armor']
            
        elif random.random() < .3:
            print('Your weapon broke!')
            del inventory['weapons'][weapon_choice]


fight(goblin_hp)
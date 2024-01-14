from modules.story import QandA, ChoiceA
from modules.func import  start_music_thread, Copyrigtname, clear, sep_line, zelda_portrait, ssep_line, bsep_line, print_status, death, zeldamap, beta_version_sorry, shop_interact, personal_inventory, purse, shop_inventory
import sys
import webbrowser
import time


def Kapitel1():
    while True:
        print(QandA["Kap1"]['Text'])
        ssep_line()
        print(QandA["Kap1"]['Q1'])
        print(QandA["Kap1"]['Q2'])
        print(QandA["Kap1"]['Q3'])
        print(QandA["Kap1"]['Q4'])
        choice = input("Enter your choice (1, 2, 3, 4): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap1"]["Q1A"])
            Kapitel2()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap1"]["Q2A"])
            Kapitel1()
        elif choice == "3":
            bsep_line()
            print_status()
            Kapitel1()
        elif choice == "4":
            bsep_line()
            print ("You are going to sleep for another 100 years")
            Kapitel1()
        else:
            print("Invalid choice. Please try again.")

def Kapitel2():
    while True:
        print(QandA["Kap2"]['Text'])
        ssep_line()
        print(QandA["Kap2"]['Q1'])
        print(QandA["Kap2"]['Q2'])
        print(QandA["Kap2"]['Q3'])
        print(QandA["Kap2"]['Q4'])
        print(QandA["Kap2"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4, 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap2"]["Q1A"])
            #inventory.extend(["Map","Apple","Grilled Fish","Goblin Sword","Goblin Shield"])
            personal_inventory["weapons"].update({"Goblin Sword": {"qty": 1, "atk": 10, "price": 7}})
            personal_inventory["food"].update({"Apple": {"qty": 5, "health_bonus": 10, "price": 1}})
            personal_inventory["defense"].update({"Goblin Shield": {"qty": 1, "def": 10, "price": 10}})
            personal_inventory["items"].update({"map": {"qty": 1, "health_bonus": 0, "price": 0}})
            Kapitel3()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap2"]["Q2A"])
            death()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap2"]["Q3A"])
            personal_inventory["items"].update({"map": {"qty": 1, "health_bonus": 0, "price": 0}})
            Kapitel2()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap2"]["Q4A"])
            death()
        elif choice == "5":
            bsep_line()
            print_status()
            Kapitel2()
        else:
            print("Invalid choice. Please try again.")

def Kapitel3():
    while True:
        print(QandA["Kap3"]['Text'])
        ssep_line()
        print(QandA["Kap3"]['Q1'])
        print(QandA["Kap3"]['Q2'])
        print(QandA["Kap3"]['Q3'])
        print(QandA["Kap3"]['Q4'])
        print(QandA["Kap3"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap3"]["Q1A"]) 
            Kapitel4()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap3"]["Q2A"])
            Kapitel1()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap3"]["Q2A"])
            Kapitel1()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap3"]["Q2A"])
            print_status()
        elif choice == "5":
            bsep_line()
            zeldamap()
            Kapitel3()
        else:
            print("Invalid choice. Please try again.")

def Kapitel4():
    while True:
        print(QandA["Kap4"]['Text'])
        ssep_line()
        print(QandA["Kap4"]['Q1'])
        print(QandA["Kap4"]['Q2'])
        print(QandA["Kap4"]['Q3'])
        print(QandA["Kap4"]['Q4'])
        print(QandA["Kap4"]['Q5'])
        print(QandA["Kap4"]['Q6'])
        choice = input("Enter your choice (1, 2, 3, 4, 5 or 6): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap4"]["Q1A"]) 
            beta_version_sorry()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap4"]["Q2A"])
            beta_version_sorry()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap4"]["Q2A"])
            death()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap4"]["Q2A"])
            print_status()
        elif choice == "5":
            bsep_line()
            zeldamap()
            Kapitel4()
        elif choice == "6":
            bsep_line()
            print("You go find a shop nearby")
            shop_interact(shop_inventory , purse)
            Kapitel4()
        else:
            print("Invalid choice. Please try again.")


def Start():
        clear()
        zelda_portrait()    

        start_music_thread("zeldatheme.mp3")

        Copyrigtname()  
        input("Press Enter to start your legendary Adventure....")
        first_message = "Welcome to The Legend of Zelda: Breath of the Wild text adventure"
        sec_message = "You are Link, a hero in the kingdom of Hyrule."
        third_message = "You wake up in a mysterious Cave with some kind of an odd Table standing in the middle of it"
        for char in first_message:
            print(char, end='', flush=True)
            time.sleep(0.05)
        print() # print a new line at the end
        sep_line()
        for char in sec_message:
            print(char, end='', flush=True)
            time.sleep(0.05)
        print() # print a new line at the end
        for char in third_message:
            print(char, end='', flush=True)
            time.sleep(0.05)
        print()  # print a new line at the end
        sep_line()

        Kapitel1()



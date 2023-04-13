from modules.story import *
from modules.func import *
import sys
import threading
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
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap4"]["Q1A"]) 
            Kapitel4()
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
            Kapitel2()
        elif choice == "6":
            bsep_line()
            print("You go find a shop nearby")
            shop_interact()
            Kapitel4()
        else:
            print("Invalid choice. Please try again.")

def Kapitel5():
    while True:
        print(QandA["Kap5"]['Text'])
        ssep_line()
        print(QandA["Kap5"]['Q1'])
        print(QandA["Kap5"]['Q2'])
        print(QandA["Kap5"]['Q3'])
        print(QandA["Kap5"]['Q4'])
        print(QandA["Kap5"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap5"]["Q1A"]) 
            Kapitel4()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap5"]["Q2A"])
            Kapitel1()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap5"]["Q2A"])
            Kapitel1()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap5"]["Q2A"])
            print_status()
        elif choice == "5":
            bsep_line()
            zeldamap()
            Kapitel2()
        else:
            print("Invalid choice. Please try again.")

def Kapitel6():
    while True:
        print(QandA["Kap6"]['Text'])
        ssep_line()
        print(QandA["Kap6"]['Q1'])
        print(QandA["Kap6"]['Q2'])
        print(QandA["Kap6"]['Q3'])
        print(QandA["Kap6"]['Q4'])
        print(QandA["Kap6"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap6"]["Q1A"]) 
            Kapitel4()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap6"]["Q2A"])
            Kapitel1()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap6"]["Q2A"])
            Kapitel1()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap6"]["Q2A"])
            print_status()
        elif choice == "5":
            bsep_line()
            zeldamap()
            Kapitel2()
        else:
            print("Invalid choice. Please try again.")

def Kapitel7():
    while True:
        print(QandA["Kap7"]['Text'])
        ssep_line()
        print(QandA["Kap7"]['Q1'])
        print(QandA["Kap7"]['Q2'])
        print(QandA["Kap7"]['Q3'])
        print(QandA["Kap7"]['Q4'])
        print(QandA["Kap7"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap7"]["Q1A"]) 
            Kapitel4()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap7"]["Q2A"])
            Kapitel1()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap7"]["Q2A"])
            Kapitel1()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap7"]["Q2A"])
            print_status()
        elif choice == "5":
            bsep_line()
            zeldamap()
            Kapitel3()
        else:
            print("Invalid choice. Please try again.")

def Kapitel8():
    while True:
        print(QandA["Kap8"]['Text'])
        ssep_line()
        print(QandA["Kap8"]['Q1'])
        print(QandA["Kap8"]['Q2'])
        print(QandA["Kap8"]['Q3'])
        print(QandA["Kap8"]['Q4'])
        print(QandA["Kap8"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap8"]["Q1A"]) 
            Kapitel4()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap8"]["Q2A"])
            Kapitel1()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap8"]["Q2A"])
            Kapitel1()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap8"]["Q2A"])
            print_status()
        elif choice == "5":
            bsep_line()
            zeldamap()
            Kapitel3()
        else:
            print("Invalid choice. Please try again.")

def Kapitel9():
    while True:
        print(QandA["Kap9"]['Text'])
        ssep_line()
        print(QandA["Kap9"]['Q1'])
        print(QandA["Kap9"]['Q2'])
        print(QandA["Kap9"]['Q3'])
        print(QandA["Kap9"]['Q4'])
        print(QandA["Kap9"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap9"]["Q1A"]) 
            Kapitel4()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap9"]["Q2A"])
            Kapitel1()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap9"]["Q2A"])
            Kapitel1()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap9"]["Q2A"])
            print_status()
        elif choice == "5":
            bsep_line()
            zeldamap()
            Kapitel3()
        else:
            print("Invalid choice. Please try again.")

def Kapitel10():
    while True:
        print(QandA["Kap10"]['Text'])
        ssep_line()
        print(QandA["Kap10"]['Q1'])
        print(QandA["Kap10"]['Q2'])
        print(QandA["Kap10"]['Q3'])
        print(QandA["Kap10"]['Q4'])
        print(QandA["Kap10"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap10"]["Q1A"]) 
            Kapitel4()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap10"]["Q2A"])
            Kapitel1()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap10"]["Q2A"])
            Kapitel1()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap10"]["Q2A"])
            print_status()
        elif choice == "5":
            bsep_line()
            zeldamap()
            Kapitel3()
        else:
            print("Invalid choice. Please try again.")

def Kapitel9():
    while True:
        print(QandA["Kap8"]['Text'])
        ssep_line()
        print(QandA["Kap8"]['Q1'])
        print(QandA["Kap8"]['Q2'])
        print(QandA["Kap8"]['Q3'])
        print(QandA["Kap8"]['Q4'])
        print(QandA["Kap8"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap8"]["Q1A"]) 
            Kapitel4()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap8"]["Q2A"])
            Kapitel1()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap8"]["Q2A"])
            Kapitel1()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap8"]["Q2A"])
            print_status()
        elif choice == "5":
            bsep_line()
            zeldamap()
            Kapitel3()
        else:
            print("Invalid choice. Please try again.")

def Kapitel10():
    while True:
        print(QandA["Kap9"]['Text'])
        ssep_line()
        print(QandA["Kap9"]['Q1'])
        print(QandA["Kap9"]['Q2'])
        print(QandA["Kap9"]['Q3'])
        print(QandA["Kap9"]['Q4'])
        print(QandA["Kap9"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap9"]["Q1A"]) 
            Kapitel4()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap9"]["Q2A"])
            Kapitel1()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap9"]["Q2A"])
            Kapitel1()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap9"]["Q2A"])
            print_status()
        elif choice == "5":
            bsep_line()
            zeldamap()
            Kapitel3()
        else:
            print("Invalid choice. Please try again.")

def Kapitel11():
    while True:
        print(QandA["Kap11"]['Text'])
        ssep_line()
        print(QandA["Kap11"]['Q1'])
        print(QandA["Kap11"]['Q2'])
        print(QandA["Kap11"]['Q3'])
        print(QandA["Kap11"]['Q4'])
        print(QandA["Kap11"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap11"]["Q1A"]) 
            Kapitel4()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap11"]["Q2A"])
            Kapitel1()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap11"]["Q2A"])
            Kapitel1()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap11"]["Q2A"])
            print_status()
        elif choice == "5":
            bsep_line()
            zeldamap()
            Kapitel3()
        else:
            print("Invalid choice. Please try again.")

def Kapitel12():
    while True:
        print(QandA["Kap12"]['Text'])
        ssep_line()
        print(QandA["Kap12"]['Q1'])
        print(QandA["Kap12"]['Q2'])
        print(QandA["Kap12"]['Q3'])
        print(QandA["Kap12"]['Q4'])
        print(QandA["Kap12"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap12"]["Q1A"]) 
            Kapitel4()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap12"]["Q2A"])
            Kapitel1()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap12"]["Q2A"])
            Kapitel1()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap12"]["Q2A"])
            print_status()
        elif choice == "5":
            bsep_line()
            zeldamap()
            Kapitel3()
        else:
            print("Invalid choice. Please try again.")

def Kapitel13():
    while True:
        print(QandA["Kap13"]['Text'])
        ssep_line()
        print(QandA["Kap13"]['Q1'])
        print(QandA["Kap13"]['Q2'])
        print(QandA["Kap13"]['Q3'])
        print(QandA["Kap13"]['Q4'])
        print(QandA["Kap13"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap13"]["Q1A"]) 
            Kapitel4()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap13"]["Q2A"])
            Kapitel1()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap13"]["Q2A"])
            Kapitel1()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap13"]["Q2A"])
            print_status()
        elif choice == "5":
            bsep_line()
            zeldamap()
            Kapitel3()
        else:
            print("Invalid choice. Please try again.")

def Kapitel14():
    while True:
        print(QandA["Kap14"]['Text'])
        ssep_line()
        print(QandA["Kap14"]['Q1'])
        print(QandA["Kap14"]['Q2'])
        print(QandA["Kap14"]['Q3'])
        print(QandA["Kap14"]['Q4'])
        print(QandA["Kap14"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap14"]["Q1A"]) 
            Kapitel4()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap14"]["Q2A"])
            Kapitel1()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap14"]["Q2A"])
            Kapitel1()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap14"]["Q2A"])
            print_status()
        elif choice == "5":
            bsep_line()
            zeldamap()
            Kapitel3()
        else:
            print("Invalid choice. Please try again.")

def Kapitel15():
    while True:
        print(QandA["Kap15"]['Text'])
        ssep_line()
        print(QandA["Kap15"]['Q1'])
        print(QandA["Kap15"]['Q2'])
        print(QandA["Kap15"]['Q3'])
        print(QandA["Kap15"]['Q4'])
        print(QandA["Kap15"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap15"]["Q1A"]) 
            Kapitel4()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap15"]["Q2A"])
            Kapitel1()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap15"]["Q2A"])
            Kapitel1()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap15"]["Q2A"])
            print_status()
        elif choice == "5":
            bsep_line()
            zeldamap()
            Kapitel3()
        else:
            print("Invalid choice. Please try again.")

def Kapitel16():
    while True:
        print(QandA["Kap16"]['Text'])
        ssep_line()
        print(QandA["Kap16"]['Q1'])
        print(QandA["Kap16"]['Q2'])
        print(QandA["Kap16"]['Q3'])
        print(QandA["Kap16"]['Q4'])
        print(QandA["Kap16"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap16"]["Q1A"]) 
            Kapitel4()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap16"]["Q2A"])
            Kapitel1()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap16"]["Q2A"])
            Kapitel1()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap16"]["Q2A"])
            print_status()
        elif choice == "5":
            bsep_line()
            zeldamap()
            Kapitel3()
        else:
            print("Invalid choice. Please try again.")

def Kapitel17():
    while True:
        print(QandA["Kap17"]['Text'])
        ssep_line()
        print(QandA["Kap17"]['Q1'])
        print(QandA["Kap17"]['Q2'])
        print(QandA["Kap17"]['Q3'])
        print(QandA["Kap17"]['Q4'])
        print(QandA["Kap17"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap17"]["Q1A"]) 
            Kapitel4()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap17"]["Q2A"])
            Kapitel1()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap17"]["Q2A"])
            Kapitel1()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap17"]["Q2A"])
            print_status()
        elif choice == "5":
            bsep_line()
            zeldamap()
            Kapitel3()
        else:
            print("Invalid choice. Please try again.")

def Kapitel18():
    while True:
        print(QandA["Kap18"]['Text'])
        ssep_line()
        print(QandA["Kap18"]['Q1'])
        print(QandA["Kap18"]['Q2'])
        print(QandA["Kap18"]['Q3'])
        print(QandA["Kap18"]['Q4'])
        print(QandA["Kap18"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap18"]["Q1A"]) 
            Kapitel4()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap18"]["Q2A"])
            Kapitel1()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap18"]["Q2A"])
            Kapitel1()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap18"]["Q2A"])
            print_status()
        elif choice == "5":
            bsep_line()
            zeldamap()
            Kapitel3()
        else:
            print("Invalid choice. Please try again.")

def Kapitel19():
    while True:
        print(QandA["Kap19"]['Text'])
        ssep_line()
        print(QandA["Kap19"]['Q1'])
        print(QandA["Kap19"]['Q2'])
        print(QandA["Kap19"]['Q3'])
        print(QandA["Kap19"]['Q4'])
        print(QandA["Kap19"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap19"]["Q1A"]) 
            Kapitel4()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap19"]["Q2A"])
            Kapitel1()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap19"]["Q2A"])
            Kapitel1()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap19"]["Q2A"])
            print_status()
        elif choice == "5":
            bsep_line()
            zeldamap()
            Kapitel3()
        else:
            print("Invalid choice. Please try again.")

def Kapitel20():
    while True:
        print(QandA["Kap20"]['Text'])
        ssep_line()
        print(QandA["Kap20"]['Q1'])
        print(QandA["Kap20"]['Q2'])
        print(QandA["Kap20"]['Q3'])
        print(QandA["Kap20"]['Q4'])
        print(QandA["Kap20"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap20"]["Q1A"]) 
            Kapitel4()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap20"]["Q2A"])
            Kapitel1()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap20"]["Q2A"])
            Kapitel1()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap20"]["Q2A"])
            print_status()
        elif choice == "5":
            bsep_line()
            zeldamap()
            Kapitel3()
        else:
            print("Invalid choice. Please try again.")

def Kapitel21():
    while True:
        print(QandA["Kap21"]['Text'])
        ssep_line()
        print(QandA["Kap21"]['Q1'])
        print(QandA["Kap21"]['Q2'])
        print(QandA["Kap21"]['Q3'])
        print(QandA["Kap21"]['Q4'])
        print(QandA["Kap21"]['Q5'])
        choice = input("Enter your choice (1, 2, 3, 4 or 5): ")

        if choice == "1":
            bsep_line()
            print(ChoiceA["Kap21"]["Q1A"]) 
            Kapitel1()
        elif choice == "2":
            bsep_line()
            print(ChoiceA["Kap21"]["Q2A"])
            Kapitel1()
        elif choice == "3":
            bsep_line()
            print(ChoiceA["Kap21"]["Q2A"])
            Kapitel1()
        elif choice == "4":
            bsep_line()
            print(ChoiceA["Kap21"]["Q2A"])
            print_status()
        elif choice == "5":
            bsep_line()
            zeldamap()
            Kapitel3()
        else:
            print("Invalid choice. Please try again.")



def Start():
    sep_line()
    print("Im sorry but you got to excited. You cant play my Game without Brain")
    ssep_line()
    while True:
        print("[1]Solve the answer of the Test to play the Game.")
        print("[2]Be a Failier your whole Life")
        choice = input("Enter your Choice (1, 2): ")
        if choice == "1":
            break
        elif choice == "2":
            print("You are a Failier and you will never be able to play this Game")
            print("Good Bye")
            sys.exit()
        else:
            print("Invalid Choice. Try Again")

    # Intermediate physics question
    question = "A car of mass 1000 kg is traveling at a velocity of 20 m/s. It applies a force of 500 N in the opposite direction of its velocity for 10 seconds. What is the final velocity of the car? (Assume no external forces acting on the car.)"

    # Define the correct answer
    correct_answer = -30

    # Prompt the user for an answer to the physics question
    while True:
        answer = input(question + "\n\nEnter your answer: ")
        try:
            answer = int(answer)
            break
        except ValueError:
            print("Invalid answer. Please enter an integer.")

    # Check if the answer is correct
    if answer == correct_answer:
        print("You may play the game now. Im proud that we have a Teacher who knows what they are doing at this school.")
        time.sleep(8)
        clear()
        time.sleep(5)
        zelda_portrait()
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
    else:
        print("Sorry, that's incorrect.")
        # Redirect the user to a Rick Astley video on YouTube
        webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
        sys.exit()


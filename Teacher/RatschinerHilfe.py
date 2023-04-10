def hello_world(arg):
    print("Hello World", arg)

def super_loop(j):
    for i in range(j):
        print(i)

kattner_list = ['o', 'i', 'd', 'a']

# Wird nur aufgerufen wenn script_1.py direkt ausgeführt wird. Wenn script_1.py als Modul importiert wurde, dann nicht.
if __name__ == "__main__":
    super_loop(100)

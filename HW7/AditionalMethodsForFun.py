import os
import platform
import random
import time



def display_loading_bar():
    total_slots = 10
    load = ""
    for i in range(total_slots):
        wait_time = random.random()
        load += "█"
        empty_slots = ' ' * (total_slots - len(load))
        print(f"Loading [{load}{empty_slots}]")
        time.sleep(wait_time)
        clear_terminal()

def clear_terminal():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
from enum import Enum
import os
import ast


class Actions(Enum):
    EXIT = 0
    DISPLAY = 1
    ADD = 2
    FIND = 3
    DELETE = 4

def menu(): 
    load_to_cars_display()
    for act in Actions: print(f"{act.value} - {act.name}" )
    return input("choose desired action:")


def clear_terminal():
    os.system('clear') 


def add_cars():
    cars.append({"brand" :input("Brand:"), "model": input("Model:"), "color": input("color:")})
    write_cars_to_file ()
    return

def display_cars ():
    load_to_cars_display ()
    global cars
    for index, car in enumerate(cars):
        print(str(f"Brand: {car['brand']} , Model: {car['model']}, Color: {car['color']}"))

def write_cars_to_file ():
    global cars
    FILE_NAME = 'myCars.txt'
    with open(FILE_NAME, 'w+') as f:      
            f.write(str(cars))
 
# close the file
    f.close() 

def load_to_cars_display ():
    global cars
    try:
        FILE_NAME = 'myCars.txt'
        with open(FILE_NAME, 'r') as f:
            cars = ast.literal_eval(f.read())
    except: 
        print("ERROR")
# close the file
    f.close() 

def delete_car_from_file():
    global cars
    display_cars()
    delete_selection = input("Choose Brand to delete:")
    deleted = False
    for car in cars[:]:
        if delete_selection == car['brand']:
            cars.remove(car)
            deleted = True
            break
    if deleted:
        print(f" car:{car['brand']}-deleted")
        write_cars_to_file()
        load_to_cars_display ()  
    else:  
        print("Delete Error") 


def find_car_from_file ():
    global cars
    find_brand = input("look for desired brand:")
    exist = False
    FILE_NAME = 'myCars.txt'
    with open(FILE_NAME, 'r') as f:
            for car in cars:
               if find_brand == car['brand']:
                   exist=True
                   break
    if exist:print(str(f"Brand: {car['brand']} , Model: {car['model']}, Color: {car['color']}"))
    else: print("we dont have it")
    return
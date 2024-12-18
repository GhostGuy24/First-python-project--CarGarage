from car_operations import *

cars = []


  



if __name__ == "__main__":
    user_selection = ""
    while True: 
        user_selection = Actions(int(menu()))
        clear_terminal()
        if user_selection == Actions.EXIT : exit()
        elif user_selection == Actions.DISPLAY: display_cars()
        elif user_selection == Actions.ADD:add_cars()
        elif user_selection == Actions.FIND: find_car_from_file()
        elif user_selection == Actions.DELETE: delete_car_from_file()
        
        else: print("Please choose from given actions")
            

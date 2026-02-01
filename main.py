from typing import Callable, Dict
from colorama import init
from logo import show_logo


init(autoreset=True)

def main() -> None:
    """Program main function"""
    
    show_logo()    
        
        
    # --- Menu functions ---
    def menu()-> None:
        """Show program menu"""
        show_logo()  
        print("This is menu: ")
    
        
    def program_exit() -> None:
        """Exit the program"""
        print("Program will now exit. Have a nice day!")
        exit()
    
    # --- Program options---
    options:Dict[int, Callable[[], None]] = {
        1:menu,
        5:program_exit,
    }
    
    #--- Main menu loop ---
    while True:
        #Possible options
        print("\nChoose options:")
        print("1 - Menu")
        print("2 - Extract Data")
        print("3 - Transform Data")
        print("4 - Load Data ")
        print("5 - Exit")

        
        #User input
        try:
            user_choice: int = int(input("Chose your option: "))
        except ValueError:
            print("Pls give men the proper number:")
            continue
        
        #Options execution
        if user_choice in options:
            options[user_choice]()
        else:
            print("Incorrect number")
    
        
if __name__ == "__main__":
    main()


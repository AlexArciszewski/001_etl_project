import pandas as pd
from typing import Callable, Dict
from colorama import init
from logo import show_logo
from extract import data_extractor, choose_loader

init(autoreset=True)


def main() -> None:
    """Program main function"""
    
    show_logo()
    
    etl_status: Dict[str, bool] = {
        "extract": False,
        "transform": False,
        "load": False
    }    
        
        
    # --- Menu functions ---
    def menu_loader()-> None:
        """Show program menu"""
        show_logo()  
        print("This is menu: ")
    
    
    # --- Loading data ---
    def load_raw_data() -> None:
        """Extracting raw data from the file"""
        loader: str | None = choose_loader()
        # data_extractor(loader)
        df: pd.DataFrame | None = data_extractor(loader)
        
        if df is not None:
            etl_status["extract"] = True
            print("Data extraction completed")
        else:
            print("Error during extraction of a data")
            
    
    
    # ---Transforming data ---
    def data_transformer() -> None:
        """Tranforming loaded data"""
        pass
    
    
    # --- Loading data ---
    def data_saver() -> None:
        """Loading tranformer data and saves it"""
        pass        
    
  
    # ---Exiting the program ---      
    def program_exit() -> None:
        """Exit the program"""
        print("Program will now exit. Have a nice day!")
        exit()
    
    # --- Checking programs tatus ---
    def check_status() -> None:
        """Show ETL operation status"""
        print("\n---ETL STATUS check--- ")
        print(f"Extraction: {'Done' if etl_status["extract"] else "Waiting" }")
        print(f"Transforming: {'Done' if etl_status["transform"] else "Waiting" }")
        print(f"Loading: {'Done' if etl_status["load"] else "Waiting" }")
        print("\n")
        
    
    # --- Program options---
    options: Dict[int, Callable[[], None]] = {
        1: menu_loader,
        2: load_raw_data,
        3: data_transformer,
        4: data_saver,
        5: check_status,
        6: program_exit,
    }
    
    
    #--- Main menu loop ---
    while True:
        #Possible options
        print("\nChoose options:")
        print("1 - Menu")
        print("2 - Extract Data")
        print("3 - Transform Data")
        print("4 - Load Data ")
        print("5 - Check Data status")
        print("6 - Exit")

        
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


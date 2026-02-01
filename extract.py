import pandas as pd




def data_extractor() -> None:
    """Extracting data from the file"""
    while True: 
        
        print("Choose a type of a file you want load the data: ")
        print("Press 1 for .csv file")
        print("Press 2 for .xls file")
        print("Press 3 for exit to main menu")
        
        user_choice:str = input("Your choice: ") 
        file_path:str = input("Enter the path of a file to open: ")
        if not file_path.strip():
            print("No file path  given, try again")
            continue
        
        print(f"Chosen data type is {user_choice}")
        print(f"chosen path is {file_path}")
        
        if user_choice == '1':
            try:
                df = pd.read_csv(file_path)
                if df is not None:
                    print(f"File loaded with {len(df)} rows and {len(df.columns)} columns.")
                    print(f"The head is {df.head()}")
            except FileNotFoundError:
                print(f"File not found:{file_path}.")
            except pd.errors.EmptyDataError:
                print(f"File {file_path} is empty.")
            except Exception as e:
                print(f"Error loading file from {file_path}")
            break
                 
        elif user_choice == '2':
            try:
                df = pd.read_excel(file_path)
            except FileNotFoundError:
                print(f"File not found:{file_path}")
            except pd.errors.EmptyDataError:
                print(f"File {file_path} is empty.") 
            except Exception as e:
                print(f"Error loading file from {file_path}")    
        elif user_choice == '3':
            break
        else:
            print("Invalid choice, try again and choose 1,2 or 3")
    return df
            
        
            
            
    
    







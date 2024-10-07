def read_file(file_path):
    try:
        with open(file_path, 'r') as file: # Open the file in read mode
            content = file.read() # Read the content of the file
            print(content)
    except FileNotFoundError: # Handle the FileNotFoundError exception
        print("File not found. Please check the file path.")
    except IsADirectoryError: # Handle the IsADirectoryError exception
        print("The provided path is a directory, not a file.")
    except PermissionError: # Handle the PermissionError exception
        print("You do not have permission to read this file.")
    except Exception as e: # Handle any other exceptions
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Enter the path to the text file: ") # Ask the user to enter the file path
    read_file(file_path) # Call the function to read the file
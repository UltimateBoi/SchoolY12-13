from datetime import datetime

def get_user_age():
    while True:
        try:
            age = int(input("Please enter your age: "))
            if age < 0:
                print("Age cannot be negative. Please try again.")
            else:
                return age
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def calculate_birth_year(age):
    current_year = datetime.now().year
    birth_year = current_year - age
    return birth_year

def main():
    age = get_user_age()
    birth_year = calculate_birth_year(age)
    print(f"You were born in the year {birth_year}.")

if __name__ == "__main__":
    main()
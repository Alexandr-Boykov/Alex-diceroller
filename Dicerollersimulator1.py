import random

def roll_die():
    return random.randint(1, 6)

def main():
    while True:
        try:
            num_rolls = int(input("Enter the number of dice rolls (or 0 to exit): "))
            if num_rolls == 0:
                print("Exit the program.")
                break
            elif num_rolls < 0:
                print("Please enter a positive number ")
            else:
                results = [roll_die() for _ in range(num_rolls)]
                print(f"Throw results : {results}")
        except ValueError:
            print("Please enter a valid number ")

if __name__ == "__main__":
    main()

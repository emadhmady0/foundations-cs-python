

def displayMenu():
    print("1. Count Digits\n" +
          "2. Find Max\n" +
          "3. Count Tags\n" +
          "4. Exit\n" +
          "- - - - - - - - - - - - - - -")


def main():
    displayMenu()
    user_input_menu = int(input("Enter a choice: "))
    while (user_input_menu > 4 or user_input_menu < 1):
        print("\nOnly numbers between 1 and 4 are allowed \n")
        displayMenu()
        user_input_menu = int(input("Enter a choice: "))


main()

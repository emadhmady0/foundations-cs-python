

def displayMenu():
    print("1. Count Digits\n" +
          "2. Find Max\n" +
          "3. Count Tags\n" +
          "4. Exit\n" +
          "- - - - - - - - - - - - - - -")

def countDigits(num, counter):
    if ((num//10) == 0):
        counter += 1
        return counter
    else:
        counter += 1
        return countDigits(num//10, counter)


def main():
    displayMenu()
    user_input_menu = int(input("Enter a choice: "))
    while (user_input_menu > 4 or user_input_menu < 1):
        print("\nOnly numbers between 1 and 4 are allowed \n")
        displayMenu()
        user_input_menu = int(input("Enter a choice: "))
    match user_input_menu:
        case 1:
            count_digits_user_input = int(input("Enter a number: "))
            print(countDigits(count_digits_user_input, 0))

main()

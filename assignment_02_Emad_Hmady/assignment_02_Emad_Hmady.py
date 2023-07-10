

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

def findMax(lst):
    if (len(lst) == 0):
        return 0
    elif (len(lst) == 1):
        return str(lst[0])
    else:
        if (lst[0] >= lst[1]):
            lst.pop(1)
        else:
            lst.pop(0)
        return findMax(lst)

def countTags(strng, tag, counter, index):
    if (len(strng) == 0 or len(strng) <= len(tag)):
        return counter
    else:
        if (strng[index] == "<" and strng[index+1:index+1+len(tag)] == tag and strng[index+1+len(tag)] == ">"):
            counter += 1
        return countTags(strng[index+1:], tag, counter, index)

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
        case 2:
            user_list = []
            number_of_items_in_list_user_input = int(input(
                "How many numbers do you want to add to your list: "))
            while (number_of_items_in_list_user_input < 0):
                print("\nOnly numbers greater than or equal to zero are allowed \n")
                number_of_items_in_list_user_input = int(input(
                    "How many numbers do you want to add to your list: "))
            if (number_of_items_in_list_user_input == 0):
                print(findMax(user_list))
            else:
                for i in range(number_of_items_in_list_user_input):
                    numbers_user_input = int(input("Enter a number: "))
                    user_list.append(numbers_user_input)
                print(findMax(user_list))
        case 3:
            tag_user_input = input("Enter a tag to find it's count: ")
            f = open("assignment_02_Emad_Hmady\html-text.txt","r") 
            html_text = f.read()
            print(countTags(html_text, tag_user_input, 0, 0))
main()

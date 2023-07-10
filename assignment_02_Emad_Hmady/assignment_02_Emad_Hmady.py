
#Display Menu
def displayMenu():
    print("1. Count Digits\n" +
          "2. Find Max\n" +
          "3. Count Tags\n" +
          "4. Exit\n" +
          "- - - - - - - - - - - - - - -")

#function that takes a number from the user and return the count of digits of that number
#if number is negative we multiply it by -1
#this function takes a counter that is always zero
#we use the integer division to remove one digit at a time and increase the counter by 1
def countDigits(num, counter):
    if(num<0):
        num = num*(-1)
    if ((num//10) == 0):
        counter += 1
        return counter
    else:
        counter += 1
        return countDigits(num//10, counter)

#function that takes a list of numbers from the user and returns the max number between them
#if the list is empty we return 0
#we compare the first two numbers and remove the smaller one from them
#the program stops when the list length is 1 and returns the number at index 0
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

#function that reads a text from a text file
#Takes a tag from the user input
#searches the file, if the user input is surronded by < and > signs then the counter increases by 1
#we use string slicing to remove one letter from the string each time the function is called
#the program stops when the string length is zero or less than or equal the length of the tag
#this function returns a count of the occurences of the tag in the text file
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
        case 4:
            print("Thank you for using my program!, you exited.")
main()

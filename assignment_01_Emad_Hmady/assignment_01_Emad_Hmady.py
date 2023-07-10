##################
# Exercise   1   #
##################

# user_input = int(input("Please Enter a positive Integer: "))
# while (user_input < 1):
#     user_input = int(input("Invalid input, kindly enter a positive integer: "))


# def doFactorial(input):
#     x = 1
#     for i in range(1, input+1):
#         x *= i
#     return x

# print(doFactorial(user_input))

#######################################################################################

##################
# Exercise   2   #
##################

# user_input = int(input("Please enter a positive integer: "))
# while (user_input < 1):
#     user_input = int(input("Invalid input, kindly enter a positive integer: "))
# def findDivisors(input):
#     divisors_list = []
#     for i in range(1, input+1):
#         if (input % i == 0):
#             divisors_list.append(i)
#     return divisors_list
# print(findDivisors(user_input))

#########################################################################################

##################
# Exercise   3   #
##################

# Solution 1 #

# user_input = input("Enter a string that you want to reverse: ")
# def reverseString(input):
#     reverse_string = ""
#     for i in range(len(input)-1, -1, -1):
#         reverse_string += input[i]
#     return reverse_string
# print(reverseString(user_input))


# Solution 2 #


# user_input = input("Enter a string that you want to reverse: ")
# def reverseString(input):
#     reverse_string = ""
#     for i in range(len(input)):
#         reverse_string = input[i] + reverse_string
#     return reverse_string
# print(reverseString(user_input))


##################
# Exercise   4   #
##################

# number_of_items_in_list = int(
#     input("please input the number of integers you want to work with: "))
# while number_of_items_in_list < 1:
#     number_of_items_in_list = int(
#         input("Invalid input, please enter an integer greater than zero: "))
# list_of_integers = []
# list_of_even_integers = []
# for i in range(number_of_items_in_list):
#     item = int(input("Enter an integer: "))
#     list_of_integers.append(item)
# def createEvenList(list):
#     for i in range(len(list)):
#         if (list[i] % 2 == 0):
#             list_of_even_integers.append(list[i])
#     return list_of_even_integers


# print(createEvenList(list_of_integers))

##################
# Exercise   5   #
##################

# user_password = input("Please enter the password you want to check: ")
# list_of_special_characters = ["#", "?", "!", "$"]
# eight_characters_at_least = False
# one_uppercase_letter_at_least = False
# one_lowercase_letter_at_least = False
# one_digit_at_least = False
# one_special_character_at_least = False


# def checkPassword(input):
#     if (len(input) >= 8):
#         eight_characters_at_least = True

#     for i in range(len(input)):
#         if (input[i].isalpha() == True and input[i].isupper() == True):
#             one_uppercase_letter_at_least = True
#             break
#         else:
#             one_uppercase_letter_at_least = False
#     for i in range(len(input)):
#         if (input[i].isalpha() == True and input[i].islower() == True):
#             one_lowercase_letter_at_least = True
#             break
#         else:
#             one_lowercase_letter_at_least = False
#     for i in range(len(input)):
#         if (input[i].isnumeric() == True):
#             one_digit_at_least = True
#             break
#         else:
#             one_digit_at_least = False
#     for i in range(len(input)):
#         if (input[i] in list_of_special_characters):
#             one_special_character_at_least = True
#             break
#         else:
#             one_special_character_at_least = False

#     if (eight_characters_at_least == True and one_digit_at_least == True and one_lowercase_letter_at_least == True and one_uppercase_letter_at_least == True and one_special_character_at_least == True):
#         return "Strong Password"
#     else:
#         return "Weak Password"


# print(checkPassword(user_password))


##################
# Exercise   6   #
##################

# Solution 1 : Detailed Solution #

# user_input = input("Enter IPv4 to be checked: ")
# def checkIpv4(input):
#     for i in range(len(input)-1):
#         if (input[i] == "." and input[i+1] == "."):
#             return "Invalid IPv4, Consecutive periods"
#     periods_counter = 0
#     for i in range(len(input)):
#         if (input[i] == "."):
#             periods_counter += 1
#     if (periods_counter < 3):
#         return "Invalid IPv4, missing octet"
#     elif (periods_counter > 3):
#         return " Invalid IPv4, extra period"
#     else:
#         octet_list = input.split(".")
#         for i in range(len(octet_list)):
#             if (int(octet_list[i]) > 0 and len(octet_list[i]) > 1 and int(octet_list[i][0]) == 0):
#                 return "Invalid IPv4, leading zero"
#             if (int(octet_list[i]) > 255):
#                 return "Invalid IPv4, octet too large"
#             if (int(octet_list[i]) < 0):
#                 return "Invalid IPv4, negative number"
#     return ("Valid IPv4")
# print(checkIpv4(user_input))


# Solution 2 : Shorter code #


# user_input = input("Enter IPv4 to be checked: ")
# def checkIpv4(input):
#     for i in range(len(input)-1):
#         if (input[i] == "." and input[i+1] == "."):
#             return "Invalid IPv4"
#     periods_counter = 0
#     for i in range(len(input)):
#         if (input[i] == "."):
#             periods_counter += 1
#     if (periods_counter != 3):
#         return "Invalid IPv4"
#     else:
#         octet_list = input.split(".")
#         for i in range(len(octet_list)):
#             if ((len(octet_list[i]) > 1 and int(octet_list[i][0]) == 0) or int(octet_list[i]) > 255 or int(octet_list[i]) < 0):
#                 return " Invalid IPv4"
#     return " Valid IPv4 "
# print(checkIpv4(user_input))

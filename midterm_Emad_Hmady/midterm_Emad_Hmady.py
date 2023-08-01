# https://www.w3schools.com/python/python_datetime.asp
import datetime


def printAdminMenu():
    print("1. Display Statistics\n" +
          "2. Book a Ticket\n" +
          "3. Display all Tickets\n" +
          "4. Change Ticket’s Priority\n" +
          "5. Disable Ticket\n" +
          "6. Run Events\n" +
          "7. Exit")


def printUserMenu():
    print("1. Book a ticket\n" +
          "2. Exit")


def readFile(file):
    # https://www.w3schools.com/python/ref_file_read.asp
    f = open(file, "r")
    return f.read()


def transformFromStringToDictionary(string):
    # split the whole string by "\n" into a list of strings
    lst = string.split("\n")
    dict = {}
    # using a for loop split each string in the first list into list1 by ", "
    # and create a key value pair where the key is the ticket name and value is the rest of list1 items
    for i in range(len(lst)):
        lst1 = lst[i].split(", ")
        dict[lst1[0]] = lst1[1:len(lst1)]
    return dict


def displayStatistics(dict):
    dictionar = {}
    # iterates over each key/value pairs in the dictionary
    # creates a new dictionary where key is the event Id and value is an integer (initiate it as 0)
    # this helps us remove duplicate event ids
    for key, value in dict.items():
        dictionar[value[0]] = 0
    # iterate over the main dictionary again and increment the value of the key in the second dictionary
    # that matches the correct event Id by 1
    for i in dict:
        dictionar[dict[i][0]] += 1
    # create a variable to detect the highest value between all the keys in the second dictionary
    highest = 0
    # iterate over the second dictionary and check the highest value and make highest variable equal to it
    for i in dictionar:
        if (dictionar[i] > highest):
            highest = dictionar[i]
    # check if there is multiple event ids in the dictionary that matches the highest variable and print it
    for key, value in dictionar.items():
        if (value == highest):
            print(key)


def BookTicket(dic, list1):
    ticket_ids = list(dic.keys())
    ticket_ids.sort()
    # detect the last ticket id in the dictionary
    last_ticket_id = ticket_ids[-1]
    # take the integer part from the last ticket id
    last_ticket_id_number = int(last_ticket_id[4:])
    # form the new ticket id by concatinating the "tick" word with the last ticket id incremented by 1
    new_ticket_id = "tick" + str(last_ticket_id_number+1)
    # create a new key/value pair from the new ticket id and the list
    dic[new_ticket_id] = list1


def transformFromDictionaryToList(dic):
    list1 = list(dic.items())
    return list1


def getTickets(dic):
    # https://www.w3schools.com/python/ref_dictionary_copy.asp
    # makes an exact copy of the dictionary
    dic_copy = dic.copy()
    for i in dic:
        # https://www.geeksforgeeks.org/python-time-strptime-function/
        # transform the time stamp string in the dictionary to actual date
        t = datetime.datetime.strptime(dic[i][2], '%Y%m%d')
        # https://www.freecodecamp.org/news/strftime-in-python/#:~:text=strftime()%20is%20a%20Python,dates%20in%20a%20readable%20way.
        # format the date in the form(Y-M-D)
        td = datetime.datetime.strftime(t, '%Y-%m-%d')
        # https://www.freecodecamp.org/news/python-datetime-now-how-to-get-todays-date-and-time/
        # get today's date formated (Y-M-D)
        date_now = datetime.datetime.now().strftime('%Y-%m-%d')
        # check if the ticket date is older than today's date and remove it from dic_copy
        if td < date_now:
            dic_copy.pop(i)
        # transform the dic_copy to a list of tuples so that we can sort
    return transformFromDictionaryToList(dic_copy)


# https://www.youtube.com/watch?v=cVZMah9kEjI
# using merge sort, sort the list of tuples by date
def mergeSortByDate(lst):
    if (len(lst) > 1):
        middle = len(lst)//2
        left_list = lst[:middle]
        right_list = lst[middle:]
    # recursive slicing
        mergeSortByDate(left_list)
        mergeSortByDate(right_list)
        i = 0  # left list index
        j = 0  # right list index
        k = 0  # main lst index

        while i < len(left_list) and j < len(right_list):
            if (int(left_list[i][1][2]) < int(right_list[j][1][2])):
                lst[k] = left_list[i]
                i += 1
                k += 1
            else:
                lst[k] = right_list[j]
                j += 1
                k += 1

        while i < len(left_list):
            lst[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            lst[k] = right_list[j]
            j += 1
            k += 1

# after sorting the list of tuples by date, sort the items that have the same date by event id using bubble sort


def bubbleSortByEventId(lst):
    for i in range(len(lst)):
        for j in range(len(lst)-1):
            if (int(lst[j][1][2]) == int(lst[j+1][1][2])):
                if (int(lst[j][1][0][2:]) > int(lst[j+1][1][0][2:])):
                    temp = lst[j]
                    lst[j] = lst[j+1]
                    lst[j+1] = temp


def changeTicketPriority(dic, ticket_id, priority):
    if ticket_id in dic:
        dic[ticket_id][3] = priority
    else:
        print("Ticket doesn't exist.")


def disableTicket(dic, tick_id):
    if tick_id in dic:
        dic.pop(tick_id)
    else:
        print("Ticket doesn't exist")


def getTodayEvents(dic):
    dicti = {}
    date_now = datetime.datetime.now().strftime('%Y-%m-%d')
    for i in dic:
        t = datetime.datetime.strptime(dic[i][2], '%Y%m%d')
        td = datetime.datetime.strftime(t, '%Y-%m-%d')
        if (td == date_now):
            dicti[i] = dic[i]
    return dicti


def mergeSortByPriority(lst):
    if (len(lst) > 1):
        middle = len(lst)//2
        left_list = lst[:middle]
        right_list = lst[middle:]
    # recursive slicing
        mergeSortByPriority(left_list)
        mergeSortByPriority(right_list)
        i = 0  # left list index
        j = 0  # right list index
        k = 0  # main lst index

        while i < len(left_list) and j < len(right_list):

            if (left_list[i][1][3] > right_list[j][1][3]):
                lst[k] = left_list[i]
                i += 1
                k += 1
            else:
                lst[k] = right_list[j]
                j += 1
                k += 1

        while i < len(left_list):
            lst[k] = left_list[i]
            i += 1
            k += 1

        while j < len(right_list):
            lst[k] = right_list[j]
            j += 1
            k += 1


def runEvents(dic, list1):
    for i in range(len(list1)):
        dic.pop(list1[i][0])
    print(list1)


def tranformDictionaryToString(dic):
    strng = ""
    ticket_ids = list(dic.keys())
    ticket_ids.sort()
    for i in ticket_ids:
        str1 = i + ", " + dic[i][0] + ", " + dic[i][1] + \
            ", " + dic[i][2] + ", " + dic[i][3] + "\n"
        strng += str1
    return strng[:len(strng)-1]


def saveChanges(strng, file):
    # https://www.w3schools.com/python/python_file_write.asp
    f = open(file, "w")
    f.write(strng)
    f.close()


def Main():
    dict = transformFromStringToDictionary(
        readFile("midterm_Emad_Hmady/tickets.txt"))
    print("Hello!\n")
    username_user_input = input("Enter Username: ")
    print()
    password_user_input = input("Enter Password: ")
    login_counter = 0
    while ((username_user_input == "admin" and password_user_input != "admin123123") or (username_user_input != "admin" and password_user_input != "")):
        if (login_counter < 4):
            print("\nIncorrect Username and/or Password\n")
            username_user_input = input("Enter Username: ")
            print()
            password_user_input = input("Enter Password: ")
            login_counter += 1
        else:
            print("\nYou Exceeded the allowed number of login attempt\n")
            return

    stop_program = False
    while (stop_program == False):
        if ((username_user_input == "admin" and password_user_input == "admin123123")):
            # https://www.w3schools.com/python/python_try_except.asp
            while True:
                try:
                    print()
                    printAdminMenu()
                    print()
                    option_admin_input = int(
                        input("Choose an option from the menu above: "))
                    # https://www.w3schools.com/python/ref_keyword_assert.asp
                    assert 0 < option_admin_input < 8
                    break
                except ValueError:
                    print("\nPlease enter an integer.\n")
                except AssertionError:
                    print("\nPlease Enter an integer between 1 and 7.\n")
            # https://www.geeksforgeeks.org/python-match-case-statement/
            match (option_admin_input):
                case 1:
                    displayStatistics(dict)
                case 2:
                    username1_user_input = input("Add Username: ")
                    event_id_user_input = input("Add event id: ")
                    while True:
                        try:
                            date_of_the_event_user_input = input(
                                "Add event Date: ")
                            t = datetime.datetime.strptime(
                                date_of_the_event_user_input, '%Y%m%d')
                            td = datetime.datetime.strftime(t, '%Y-%m-%d')
                            break
                        except ValueError:
                            print("Enter date in the format(YYYYMMDD)")
                    priority_user_input = input("Add priority: ")
                    ticket_details_list = [
                        event_id_user_input, username1_user_input, date_of_the_event_user_input, priority_user_input]
                    BookTicket(dict, ticket_details_list)
                case 3:
                    list_tickets = getTickets(dict)
                    mergeSortByDate(list_tickets)
                    bubbleSortByEventId(list_tickets)
                    print(list_tickets)
                case 4:
                    ticket_id_admin_input = input("Enter the ticket Id: ")
                    priority_admin_input = input("Enter the new priority: ")
                    changeTicketPriority(
                        dict, ticket_id_admin_input, priority_admin_input)
                case 5:
                    tick_id_admin_input = input("Enter the ticket Id: ")
                    disableTicket(dict, tick_id_admin_input)
                case 6:
                    today_events = getTodayEvents(dict)
                    if (len(today_events) > 0):
                        list_today_events = transformFromDictionaryToList(
                            today_events)
                        mergeSortByPriority(list_today_events)
                        runEvents(dict, list_today_events)
                    else:
                        print("No events today!")
                case 7:
                    while True:
                        try:
                            print(
                                "Would you like to save your changes?\n" + "1. yes\n" + "2. no")
                            exit_user_input = int(input())
                            assert 0 < exit_user_input < 3
                            break
                        except ValueError:
                            print("\nOnly integers are allowed!\n")
                        except AssertionError:
                            print("\nOnly 1 or 2 are the available options!\n")

                    match (exit_user_input):
                        case 1:
                            str1 = tranformDictionaryToString(dict)
                            saveChanges(str1, "midterm_Emad_Hmady/tickets.txt")
                            stop_program = True
                        case 2:
                            stop_program = True

        elif (username_user_input != "admin" and password_user_input == ""):
            while True:
                try:
                    print()
                    printUserMenu()
                    print()
                    option_user_input = int(
                        input("Choose an option from the menu above: "))
                    assert 0 < option_user_input < 3
                    break
                except ValueError:
                    print("\nPlease enter an integer.\n")
                except AssertionError:
                    print("\nPlease enter 1 or 2.\n")

            match (option_user_input):
                case 1:
                    user_event_id_input = input("Enter event Id: ")
                    while True:
                        try:
                            user_date_input = input(
                                "Add event Date (YYYYMMDD): ")
                            t = datetime.datetime.strptime(
                                user_date_input, '%Y%m%d')
                            td = datetime.datetime.strftime(t, '%Y-%m-%d')
                            break
                        except ValueError:
                            print("Enter date in the format(YYYYMMDD)")
                    user_info_list = [user_event_id_input,
                                      username_user_input, user_date_input, str(0)]
                    BookTicket(dict, user_info_list)
                    print("\nTicket Registered Successfully!\n")
                case 2:
                    str2 = tranformDictionaryToString(dict)
                    saveChanges(str2, "midterm_Emad_Hmady/tickets.txt")
                    stop_program = True


Main()

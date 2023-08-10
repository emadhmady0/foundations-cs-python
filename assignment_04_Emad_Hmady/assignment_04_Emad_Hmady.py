def printMenu():
    while True:
        print("1. Add a user to the platform.\n" +
              "2. Remove a user from the platform.\n" +
              "3. Send a friend request to another user.\n" +
              "4. Remove a friend from your list.\n" +
              "5. View your list of friends.\n" +
              "6. View the list of users on the platform.\n" +
              "7. Exit\n" +
              "- - - - - - - - - - - - - - -")
        try:
            choice_from_menu_user_input = int(input("Enter a choice: "))
            assert 1 <= choice_from_menu_user_input <= 7
            return choice_from_menu_user_input
        except ValueError:
            print("Enter an integer")
        except AssertionError:
            print("Make a choice between 1 and 7")

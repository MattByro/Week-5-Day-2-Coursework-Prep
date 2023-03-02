from team_dict import *
from View_table import *
from Top_Scorers import *
from Club_Manager import *
from Update_results import *
from Relegate_and_promote import *
from Save_and_view import *
number = 0
while number != 6:
    print("Please select one of the following:")
    print("1. View the EPL table")
    print("2. See/change the top scorers")
    print("3. See/change club manager")
    print("4. Input team results")
    print("5. Save results or view past seasons")
    print("6. Exit the menu")
    number = int(input("Enter your selection (1-6): "))

    if number == 1:
        view_table(t)
    elif number == 2:
        top_scorer(t)
    elif number == 3:
        club_manager(t)
    elif number == 4:
        update_results(t)
    elif number == 5:
        save_and_view(t)
    elif number == 6:
        print("Goodbye!")
        break
    else:
        print("Invalid input, Please try again")

    another_operation = input("Do you want to perform another operation? (yes/no): ")
    if another_operation == 'no':
        print("Goodbye!")
        break

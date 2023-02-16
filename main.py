#import team

number = 0
while number != 6:
    print("Please select one of the following:")
    print("1. View a table in a specific league")
    print("2. See/change the top scorers")
    print("3. See/change club manager")
    print("4. Input team results")
    print("5. See end of season results")
    print("6. Quit")
    number = int(input("Enter your selection (1-6): "))

    if number == 1:
        selection = str()
        data_filename = 'epl.txt'
        headers = 'Team Name', 'Stadium', 'City',
        with open(data_filename) as file:
            datatable = [line.split() for line in file.read().splitlines()]
        widths = [max(len(value) for value in col)
                  for col in zip(*(datatable + [headers]))]
        format_spec = '{:{widths[0]}}  {:>{widths[1]}}  {:>{widths[2]}}'
        print(format_spec.format(*headers, widths=widths))
        for fields in datatable:
            print(format_spec.format(*fields, widths=widths))
    elif number == 2:
        topScorer = str(input("please enter the name of the top scorer"))
        playerAssignment = str(input("please enter the team this player plays for"))
        numberOfGoals = int(input("please enter the amount of goals this player has scored"))
        print(topScorer, "has scored", numberOfGoals, "goals for", playerAssignment)
    elif number == 3:
        clubManager = str(input("please enter the name of the manager"))
        managerAssignment = str(input("please enter the name of the team the manager manages"))
        print(clubManager, "manages", managerAssignment)
    elif number == 4:
        footballTeam = str(input("please enter the name of the team you are updating results for"))
        results = int(input("please enter the points for the team you have entered"))
        print(footballTeam, "have accumulated", results, "points \nThis has been updated to the table")
    elif number == 5:
        print("please code end of season results")
    elif number == 6:
        print("Goodbye!")
        break
    else:
        print("Invalid input, Please try again")

    another_operation = input("Do you want to perform another operation? (yes/no): ")
    if another_operation == 'no':
        print("Goodbye!")
        break
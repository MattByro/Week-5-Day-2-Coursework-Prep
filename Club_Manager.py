from team_dict import *
from Save_and_view import *
from Relegate_and_promote import *
from Update_results import *
from Top_Scorers import *
from View_table import *
def club_manager(t):
    view_or_change = str(input("Please enter 'view' or 'change' to view or change the team manager: "))
    if view_or_change == "view":
        team_name = str(input("Please enter the team name to view their manager: "))
        for team in t:
            if team.club.lower() == team_name.lower():
                if team.manager == None:
                    print(f"No manager found for {team_name}")
                else:
                    print(f"The manager of {team_name} is {team.manager}.")
    elif view_or_change == "change":
        manager_name = str(input("Please enter the name of the new manager: "))
        team_name = str(input("Please enter the team name to change their manager: "))
        for team in t:
            if team.club.lower() == team_name.lower():
                team.manager = manager_name
                print(f"{team_name} now has {manager_name} as their manager.")
                break
        else:
            print(f"Error: Team {team_name} not found.")
    else:
        print("Invalid input.")
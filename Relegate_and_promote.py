from team_dict import *
from Save_and_view import *
from Update_results import *
from Club_Manager import *
from Top_Scorers import *


def relegate_and_promote(t):
    # Sort the teams in descending order by points
    sorted_teams = sorted(t, key=lambda x: (-x.points, -x.goal_difference, -x.goals_scored, x.club))

    removed_teams = []
    for i in range(3):
        removed_team = sorted_teams.pop(-1)
        removed_teams.append(removed_team)
        print(f"Removing {removed_team.club} from the league table...")

    # Remove the relegated teams from the original list
    for team in removed_teams:
        t.remove(team)

    # Ask the user to input the names, stadium, and city of three new teams
    new_teams = []
    for i in range(3):
        new_team_name = input(f"Enter the name of new team {i+1}: ")
        new_team_stadium = input(f"Enter the stadium for {new_team_name}: ")
        new_team_city = input(f"Enter the city for {new_team_name}: ")
        new_team = Team(new_team_name, new_team_stadium, new_team_city)
        new_teams.append(new_team)

    # Add the new teams to the table
    t.extend(new_teams)

    return sorted_teams

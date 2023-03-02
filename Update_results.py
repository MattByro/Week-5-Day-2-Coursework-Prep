from team_dict import *
from Save_and_view import *
from Relegate_and_promote import *
from Club_Manager import *
from Top_Scorers import *
from View_table import *
def update_results(t):
    footballTeam = str(input("Please enter the name of the team you are updating results for: "))
    played_matches = int(input("Please enter the number of games played by the team: "))
    wins = int(input("Please enter the number of wins for the team: "))
    draws = int(input("Please enter the number of draws for the team: "))
    losses = int(input("Please enter the number of losses for the team: "))

    # Check if the sum of wins, draws and losses equals the number of games played
    while wins + draws + losses != played_matches:
        print("The sum of wins, draws and losses must equal the number of games played.")
        wins = int(input("Please enter the number of wins for the team: "))
        draws = int(input("Please enter the number of draws for the team: "))
        losses = int(input("Please enter the number of losses for the team: "))

    goals_scored = int(input("Please enter the number of goals scored by the team: "))
    goals_conceded = int(input("Please enter the number of goals conceded by the team: "))

    # Calculate the goal difference and points
    if wins + draws + losses != 0:
        goal_difference = goals_scored - goals_conceded
        points = (wins * 3) + (draws * 1)
    else:
        goal_difference = 0
        points = 0

    for team in t:
        if team.club.lower() == footballTeam.lower():
            team.played_matches = played_matches
            team.wins = wins
            team.draws = draws
            team.losses = losses
            team.goals_scored = goals_scored
            team.goals_conceded = goals_conceded
            team.goal_difference = goal_difference
            team.points = points

    print(f"The results for {footballTeam} have been updated.")
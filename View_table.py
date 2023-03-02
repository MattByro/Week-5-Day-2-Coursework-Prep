from team_dict import *
from Save_and_view import *
from Relegate_and_promote import *
from Update_results import *
from Club_Manager import *
from Top_Scorers import *


def view_table(t):
    sorted_teams = sorted(t, key=lambda x: (-x.points, -x.goal_difference, -x.goals_scored, x.club))
    print("\nCurrent League Table:")
    print("{:<4} {:<25} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
        'Pos', 'Club', 'Played', 'Won', 'Drawn', 'Lost', 'GF', 'GA', 'GD', 'Points'))
    for i, team in enumerate(sorted_teams):
        print("{:<4} {:<25} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
            i + 1, team.club, team.played_matches, team.wins, team.draws, team.losses,
            team.goals_scored, team.goals_conceded, team.goal_difference, team.points
        ))

    # Check if the league table needs to be updated
    while True:
        update_table = input("Do you want to relegate the bottom 3 teams and promote 3 new teams? (yes/no): ").lower()
        if update_table not in ['yes', 'no']:
            print("Invalid input. Please enter 'yes' or 'no'.")
        else:
            break

    if update_table == 'yes':
        updated_table = relegate_and_promote(t)
        sorted_teams = sorted(updated_table, key=lambda x: (-x.points, -x.goal_difference, -x.goals_scored, x.club))
        print("\nUpdated League Table:")
        print("{:<4} {:<25} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
            'Pos', 'Club', 'Played', 'Won', 'Drawn', 'Lost', 'GF', 'GA', 'GD', 'Points'))
        for i, team in enumerate(sorted_teams):
            print("{:<4} {:<25} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format(
                i + 1, team.club, team.played_matches, team.wins, team.draws, team.losses,
                team.goals_scored, team.goals_conceded, team.goal_difference, team.points
            ))


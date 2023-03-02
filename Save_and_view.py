from team_dict import *
from Relegate_and_promote import *
from Update_results import *
from Club_Manager import *
from Top_Scorers import *
from View_table import *
def save_and_view(t):
    save_or_view = str(input("Please enter 'save' or 'view' to save results or view past results: "))
    if save_or_view == 'save':
        filename = input("Please enter the name of the file to save the data to: ")
        with open(filename, 'w') as f:
            for team in t:
                f.write(
                    team.club + ',' + team.homeground + ',' + team.city + ',' + str(team.played_matches) + ','
                    + str(team.wins) + ',' + str(team.draws) + ',' + str(team.losses) + ',' + str(
                        team.goals_scored)
                    + ',' + str(team.goals_conceded) + ',' + str(team.goal_difference) + ',' + str(
                        team.points) + '\n')
        print("Data saved to file ", filename)
    elif save_or_view == 'view':
        filename = input("Please enter the name of the file to view the data from: ")
        try:
            with open(filename, 'r') as f:
                print("{:<25} {:<30} {:<12} {:<12} {:<12} {:<12} {:<20} {:<20}".format(
                    "Club", "Stadium", "Played", "Won", "Drawn", "Lost", "GF-GA", "Points"))
                for line in f:
                    team_data = line.strip().split(',')
                    print("{:<25} {:<30} {:<12} {:<12} {:<12} {:<12} {:<20} {:<20}".format(
                        team_data[0], team_data[1], team_data[3], team_data[4], team_data[5], team_data[6],
                        team_data[7] + '-' + team_data[8], team_data[9]
                    ))
        except FileNotFoundError:
            print("File not found.")
    else:
        print("Invalid input.")
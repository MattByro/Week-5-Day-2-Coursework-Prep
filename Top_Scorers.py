from team_dict import *
from Save_and_view import *
from Relegate_and_promote import *
from Update_results import *
from Club_Manager import *
from View_table import *
def top_scorer(t):
   view_or_change = str(input("Please enter 'view' or 'change' to view or change the top scorer: "))
   if view_or_change == "view":
       team_name = str(input("Please enter the team name to view their top scorer: "))
       for team in t:
           if team.club.lower() == team_name.lower():
               if team.top_scorer is None:
                   print(f"No top scorer found for {team_name}.")
               else:
                   number_of_goals = team.top_scorer_goals
                   print(f"The top scorer for {team_name} is {team.top_scorer} with {number_of_goals} goals.")
               break
       else:
           print(f"Error: Team {team_name} not found.")
   elif view_or_change == "change":
       top_scorer = str(input("Please enter the name of the top scorer: "))
       team_name = str(input("Please enter the team this player plays for: "))
       number_of_goals = int(input("Please enter the amount of goals this player has scored: "))
       for team in t:
           if team.club.lower() == team_name.lower():
               team.top_scorer = top_scorer
               team.top_scorer_goals = number_of_goals
               print(f"{team_name}'s top scorer is now {team.top_scorer} with {number_of_goals} goals.")
               break
       else:
           print(f"Error: Team {team_name} not found.")
   else:
       print("Invalid input. Please enter 'view' or 'change'.")
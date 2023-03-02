
try:
    f = open("epl.txt", "r")

    content = f.read()
    teams_list = content.split("\n")  # creating a list by splitting each line
finally:
    f.close()


# Team class
class Team:
    def __init__(self, clubname, stadium, city, played_matches=0, wins_set = 0, draws_set = 0, losses_set = 0, goals_scored=0, goals_conceded=0, goal_difference=0, points=0, manager=None, top_scorer=None):
        self.club = clubname
        self.homeground = stadium
        self.city = city
        self.played_matches = played_matches
        self.wins = wins_set
        self.draws = draws_set
        self.losses = losses_set
        self.goals_scored = goals_scored
        self.goals_conceded = goals_conceded
        self.goal_difference = goal_difference
        self.points = points
        self.manager = manager
        self.top_scorer = top_scorer


teams_list_final = []

for team in teams_list:
    team_name_ls = team.split(":")
    team_name = team_name_ls[0]

    team_stadium_ls = team_name_ls[1].split("-")
    team_stadium = team_stadium_ls[0]

    team_area = team_stadium_ls[1]

    teams_dict = {"Club": team_name, "Stadium": team_stadium, "City": team_area}
    teams_list_final.append(teams_dict)

t = []
for team in teams_list_final:
    t.append(Team(team["Club"], team["Stadium"], team["City"]))


class Team:
    def __init__(self, name, stadium, city, ):
        self.name = name
        self.stadium = stadium
        self.city = city

    def __repr__(self):
        return f"{self.name},{self.stadium},{self.city}"


def parseTeamData(data):
    data1 = data.split(":")
    club = data1[0]
    data2 = data1[1].split("-")
    stadium = data2[0]
    area = data2[1]
    return Team(club, stadium, area)


def load_teams_fr_file():
    try:
        teams = []
        my_file = open("epl.txt", "r")
        for line in my_file:
            teams.append(parseTeamData(line))
    except FileNotFoundError:
        print("Please save the file in the project folder!")
    finally:
        my_file.close()
        return teams


ts = load_teams_fr_file()
print(ts)
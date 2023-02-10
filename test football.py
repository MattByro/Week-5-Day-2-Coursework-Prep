#here we have the code for loading the file
try:
 my_file = open ("epl.txt", "r")
 teams = []
 stadiums = []
 areas = []
 for line in my_file:
     data1 = line.split(":")
     club = data1[0]
     data2 = data1[1].split("-")
     stadium = data2[0]
     area = data2[1]
     teams.append(club)
     stadiums.append(stadium)
     areas.append(area)




finally:
  my_file.close()
print(teams)
print(stadiums)
print(areas)
#this is the code for the start menu
selection = 0
while selection != 6:
    print("Please select one of the following:")
    print("1. View the table")
    print("2. See/change the top scorers")
    print("3. See/change club manager")
    print("4. Input team results")
    print("5. Declare relegation and promotion with champion results")
    print("6. Quit")
    selection = int(input("Enter your selection (1-6): "))


#here we have the code for loading the file
try:
 my_file = open ("C:\\Users\\N1163880\\PycharmProjects\\day 2\\epl.txt", "r")
 for line in epl.txt:
     data = line.split()
     print(data)

finally:
  my_file.close()
#this is the code for the start menu
while True:
    print("Please select one of the following:")
    print("1. View the table")
    print("2. See/change the top scorers")
    print("3. See/change club manager")
    print("4. Input team results")
    print("5. Declare relegation and promotion with champion results")
    print("7. Quit")
    selection = input("Enter your selection (1-7): ")
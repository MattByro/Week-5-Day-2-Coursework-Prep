# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 15:26:01 2023

@author: N1163880
"""

try:
    my_file = open("C:\\Users\\G01311903\\PycharmProjects\\pythonProject\\epl.txt", "r+")
    for line in my_file.readlines():
        print(line)

finally:
  my_file.close()

  while True:
      print("Please select one of the following:")
      print("1. View the table")
      print("2. Save/Change the top scorers")
      print("3. See/Change the manager")
      print("4. Input team results")
      print("5. Declare relegation and promotion and champion")

#put loop everytime (aka if) team wins, gain 3 points, if my team draws get 1 point, if my team loses
#0 points. Total wins is 0 to begin with


class teams:
    def __init__(self, name, stadium, city, manager, points, top_scorer):
        self.name=name
        self.stadium=stadium
        self.city=city
        self.manager=manager
        self.points=points
        self.top_scorer=top_scorer


    #methods
    #def #method
    def initial_point(self):
        self.points=0
    def points_win(self):
        self.points+=3
    def points_draw(self):
        self.points+=1
    def points_loss(self):
        self.points+=0



tLiv=team()
tBr=team()
tFul=team()
tLee=team()
tBr=team()
tEver=team()
tLi=team()
tWe=team()
tWol=team()
tMU = teams()
tCr=team()
tNew=team()
tSou=team()
tChe=team()
tNott=team()
tArs=team()
tMCI=team()
tTott=team()
tAst=team()
tBou=team()
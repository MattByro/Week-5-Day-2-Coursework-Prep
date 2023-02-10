# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# "20/12/2022"
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        
    def __repr__(self):
        return f"{self.day}/{self.month}/{self.year}"

def parseDate(s : str):
    data = s.split("/")
    return Date(data[0], data[1], data[2])

d = parseDate( "20/12/2022")
print(d)
print(d.day)
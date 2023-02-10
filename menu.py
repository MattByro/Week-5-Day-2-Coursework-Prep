# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 16:31:21 2023

@author: N1163880
"""

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
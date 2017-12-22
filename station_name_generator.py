# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 12:16:34 2017

@author: mikkopos
"""

""" Program connect text and numbers"""
# Create variable "basename" 
basename = "station"

# empty list for filenames
filenames = []

# iterate over numbers and add items to list

for number in range(21):
    #create a ' station' variable and generate the station name
    station = basename + "_" + str(number) + ".text"
    
    # add the content to list
    filenames.append(station)
    # print the list
    #print(filenames)
  #  print (station)
    
# count values
    list_count = len(filenames)
    print(filenames)
    
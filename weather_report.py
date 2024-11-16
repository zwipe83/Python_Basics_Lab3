"""
File Name: weather_report.py
Author: Samuel Jeffman
Date: 2024-11-16
Description: Programming in Python: Basic and Preparatory Course, Assignment 3. Weather data app.
"""

from pathlib import Path
#import file_reader
from file_reader import read_from_file
# import weather_functions as wf
from weather_functions import calculate_avg_temp
from weather_functions import when_is_it_spring as springtime
from weather_functions import when_is_it_spring2 as springtime_v2
from weather_functions import get_min_max
from user_interaction import print_to_screen as message
from user_interaction import read_input_as_int as read_int

# The file name is actually 'temperature_data.csv' but added some extra path-stuff here
# to make sure that it will be found by everyone
file_path = Path(__file__).parent / 'temperature_data.csv'

#read month 2 temperatures from data.csv
temp_list = read_from_file(file_path, 0)

avg_temp = sum(temp_list)/len(temp_list)
print(f"Avg temp 1: {avg_temp:.2f}")
print(f"Avg temp 2: {calculate_avg_temp(temp_list):.2f}")

spring = springtime(temp_list)

print(f"Spring starts on day: {spring}") # 0 == Jan. 1, 11 == Jan. 10

message("\nWhat do you want to do?")
while True:
    message("Enter\n1 for average temperature,\n2 for the arrival of spring or\n3 to get min/max temperatures for a specific month")
    choice = read_int(input())
    if choice > 0 and choice < 4: # Number must be within valid range
        break;
if choice == 1:
    message("Which month do you want to calculate the average temperature for?")
    while True:
        message("Enter month number:")
        month = read_int(input())
        if month > 0 and month < 13: # Check for valid input, if no valid input ask again
            break;
    temp_list = read_from_file(file_path, month)
    avg_temp = calculate_avg_temp(temp_list)
    message(f"The average temperature for month {month} was: {avg_temp:.2f}")
elif choice == 2:
    message("Looking for spring...")
    temp_list = read_from_file(file_path, return_dates=True, day=45)
    #Optional task (a bit harder):
    spring = springtime_v2(temp_list)
    message(f"Spring arrived on index {spring}")
#Optional task (simple):
elif choice == 3:
    message("Which month do you want to get min/max temperature for?")
    while True:
        message("Enter month number:")
        month = read_int(input())
        if month > 0 and month < 13: # Check for valid input, if no valid input ask again
            break;
    temp_list = read_from_file(file_path, month)
    minmax = get_min_max(temp_list)
    message(f"Min temperature for month {month} was {minmax.min:.2f} and Max temperature was {minmax.max:.2f}")
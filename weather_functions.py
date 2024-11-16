"""
File Name: weather_functions.py
Author: Samuel Jeffman
Date: 2024-11-16
Description: Programming in Python: Basic and Preparatory Course, Assignment 3. Helper functions for weather data app.
"""

from collections import namedtuple

# calculates average of data provided in the list
def calculate_avg_temp(list):
    sum = 0;
    count = 0;
    for temperature in list:
        sum += temperature
        count += 1
    return sum/count

# Calculate when spring starts
def when_is_it_spring(list):
    streak = 0
    first_day = -1
    day_count = 0
    for i in list:
        if i > 0.0:
            streak += 1
        elif i <= 0.0:
            streak = 0
        if streak == 1:
            first_day = day_count
        if streak >= 7:
            return first_day
        day_count += 1
    return -1

#Optional task (a bit harder):
# Calculate when spring starts
def when_is_it_spring2(list):
    streak = 0
    first_day = -1
    day_count = 0
    for i in list:
        if i[1] > 0.0:
            streak += 1
        elif i[1] <= 0.0:
            streak = 0
        if streak == 1:
            first_day = day_count
        if streak >= 7:
            return list[first_day][0]
        day_count += 1
    return -1

#Optional task (simple):
def get_min(list):
    return min(list)

def get_max(list):
    return max(list)

#Init named tuple
MinMax = namedtuple('MinMax', ['min', 'max'])
def get_min_max(list):
    return MinMax(min=min(list), max=max(list))
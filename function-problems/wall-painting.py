#To calculate how many cans of paint required to paint the wall
#one can of paint covers a 5 Square meters of area
#number_of_cans_needed = (wall_height * wall_width)/ coverage_per_can


import math #to round up result we used math module
wall_height = float(input("Enter Height of Wall "))
wall_width = float(input("Enter Width of a Wall "))

coverage_per_can = 5

def cans_required (height = wall_height , width = wall_width , cover = coverage_per_can ):

    numbers_of_cans_needed = (height * width) / cover

    print(f"You need {math.ceil(numbers_of_cans_needed)} cans to Paint the wall ")

cans_required()

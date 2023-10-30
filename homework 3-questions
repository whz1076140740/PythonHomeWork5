from functools import reduce
import pandas as pd
from datetime import date
from geopy.distance import geodesic

##### Try to use map and reduce in the next 3 exercises
# 1)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#

def count_simba(string_list: list, target_str: str) -> int: 
    # The below counts the number of times the target string appears in each string in the list
    count_per_string = list(map(lambda x: x.count(target_str), string_list))
    
    # The reduce function accumulates the counts from count_per_string
    count = reduce(lambda x, y: x + y, count_per_string)

    return count

string_list = ["Simba and Nala are lions.", "I laugh in the face of danger.",
"Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."]

target_str = "Simba"

count = count_simba(string_list, target_str)

print(f"The string {target_str} appears {count} times in the list")


# 2)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 


# We haven't used the reduce in the below function as you can achieve the result just using map

def get_day_month_year(date_list: list) -> pd.DataFrame:
    # Map function applies the lambda function to each entry in date_list
    date_info_list = list(map(lambda x: (x.day, x.month, x.year),date_list))
    # List with date info is then converted into a dataframe
    df = pd.DataFrame(date_info_list, columns=['day', 'month', 'year'])
    return df

date_list = [date(2023, 2, 9), date(2022, 12, 2), date(1997, 1, 7)]

df = get_day_month_year(date_list)

print(df)


# 3) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#

def compute_distance(coordinates: list) -> float:
    distances = list(map(lambda pair: geodesic(pair[0], pair[1]).kilometers, coordinates)) #map function applies the geodesic function to each pair of coordinates into a list of distances 
    total_distance = round(reduce(lambda x, y: x + y, distances),3) #sums up the list via x+y
    return (total_distance) 

coordinates = [((41.23,23.5), (41.5, 23.4)),((52.38, 20.1), (52.3, 17.8))]

total_distance = compute_distance(coordinates) #call function over the coordinates

print(f"Total Distance: {total_distance} kilometers")


#################################################
# 4)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13
#


def sum_general_int_list(lst: list) -> int:
    total = 0 #initliase total
    for item in lst: 
        if isinstance(item, int): #isinstance function checks type of each element
            total += item #add to total if integer
        elif isinstance(item, list):
            total += sum_general_int_list(item) #recursively call function if element is a list, handles nested list
    return total

# Example usage:
list_1 = [[2], 3, [[1, 2], 5]]
result = sum_general_int_list(list_1)
print(f"Result: {result}")  # Output: 13

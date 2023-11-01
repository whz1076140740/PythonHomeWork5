
import pandas as pd
from datetime import date
from geopy.distance import geodesic


# 1)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#
def count_simba(string_list) -> int: #HW3 function to count the number of times that Simba appears in a list of strings
    count = 0
    for text in string_list:
        text_lower = text.lower()
        count += text_lower.count("simba")
    return count


# 2)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 

def get_day_month_year(date_list)-> pd.DataFrame: #HW3 function to return a pandas dataframe with 3 columns (day, month, year) 
    date_info_list = list(map(lambda x: (x.day, x.month, x.year), date_list))
    df = pd.DataFrame(date_info_list, columns=['day', 'month', 'year'])
    return df



# 3) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#

def compute_distance(coordinates):
    distances = list(map(lambda pair: round(geodesic(pair[0], pair[1]).kilometers, 3), coordinates)) #HW3 function to compute the distance between two pairs of coordinates
    return distances



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
def sum_general_int_list(lst: list) -> int: #HW3 function to sum all the integers within the lists
    total = 0
    for item in lst:
        if isinstance(item, int):
            total += item
        elif isinstance(item, list):
            total += sum_general_int_list(item)
    return total


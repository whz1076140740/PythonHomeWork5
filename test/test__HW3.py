from functools import reduce
import pandas as pd
from datetime import date
from geopy.distance import geodesic
import unittest
import datetime 
import pytest
import pytest_cov

import HW3

# 1)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#

class TestCountSimba(unittest.TestCase): #test class for count_simba function
    def test__count_simba_case_insensitive(self): #test that tests for case insensitivity
        string_list = [
            "Simba and Nala are lions.",
            "simba and nala are lions.",
            "sIMba and Nala are lions."
        ]
        count = HW3.count_simba(string_list)
        self.assertEqual(count, 3)  # "Simba" occurs 3 times in list in different cases so it passes the test

    def test__count_simba_no_occurrence(self): #test for no occurrence
        string_list = [
            "Hakuna matata",
            "I laugh in the face of danger."
        ]
        count = HW3.count_simba(string_list)
        self.assertEqual(count, 0)  # "Simba" does not occur in list so it passes the test

    def test__count_simba_multiple_occurrences(self): #test for multiple occurrences
        string_list = [
            "SimbaSimbaSimbaSimba",
            "Simba Simba Simba"
        ]
        count = HW3.count_simba(string_list)
        self.assertEqual(count, 7)  # "Simba" occurs 7 times in list so it passes the test

    def test__count_simba_mixed_strings(self):
        # Test with a mix of strings containing "Simba"
        string_list = [
            "Simba and Nala are lions.",
            "I laugh in the face of danger.",
            "Hakuna matata",
            "Timon, Pumba and Simba are friends, but Simba could eat the other two."
        ]
        count = HW3.count_simba(string_list)
        self.assertEqual(count, 3)  # "Simba" occurs 3 times

if __name__ == '__main__': #ensures that the test class is only run when the file is run directly
    unittest.main()


# 2)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 


class TestGetDayMonthYear(unittest.TestCase): #Test class on the the get_day_month_year function
    def test__get_day_month_year_single_date(self):
        date_list = [date(2023, 2, 9)]
        expected_df = pd.DataFrame({'day': [9], 'month': [2], 'year': [2023]})
        result_df = HW3.get_day_month_year(date_list)
        self.assertTrue(expected_df.equals(result_df)) #only a single date so it passes the test 

    def test__get_day_month_year_multiple_dates(self): #test for multiple dates
        date_list = [date(2023, 2, 9), date(2022, 12, 2), date(1997, 1, 7)]
        expected_df = pd.DataFrame({
            'day': [9, 2, 7],
            'month': [2, 12, 1],
            'year': [2023, 2022, 1997]
        })
        result_df = HW3.get_day_month_year(date_list)
        self.assertTrue(expected_df.equals(result_df)) #multiple dates so it passes the test
    
if __name__ == '__main__':
    unittest.main()


# 3) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#


class TestComputeDistance(unittest.TestCase): #test class for compute_distance function
    def test__compute_distance_single_pair(self): #test for a single pair
        coordinates = [((41.23, 23.5), (41.5, 23.4))]
        expected_distances = [31.132]  # Expected distance for the single pair
        result_distances = HW3.compute_distance(coordinates)
        self.assertEqual(result_distances, expected_distances) #only a single pair so it passes the test

    def test__compute_distance_multiple_pairs(self): #test for multiple pairs
        coordinates = [((41.23, 23.5), (41.5, 23.4)), ((52.38, 20.1), (52.3, 17.8))]
        expected_distances = [31.132, 157.006]  # Expected distances for the two pairs
        result_distances = HW3.compute_distance(coordinates)
        self.assertEqual(result_distances, expected_distances) #multiple pairs so it passes the test

if __name__ == '__main__':
    unittest.main()

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
class TestSumGeneralIntList(unittest.TestCase): #test class for sum_general_int_list function
    def test__sum_general_int_list_single_list(self): #test for a single list
        lst = [1, 2, 3, 4]
        expected_result = 10
        result = HW3.sum_general_int_list(lst)
        self.assertEqual(result, expected_result) #only a single list so it passes the test

    def test__sum_general_int_list_nested_lists(self): #test for nested lists
        lst = [1, [2, [3, 4]], 5]
        expected_result = 15
        result = HW3.sum_general_int_list(lst)
        self.assertEqual(result, expected_result) #nested lists so it passes the test

    def test__sum_general_int_list_empty_list(self): #test for empty list
        lst = []
        expected_result = 0
        result = HW3.sum_general_int_list(lst)
        self.assertEqual(result, expected_result) #empty list so it passes the test

    def test__sum_general_int_list_no_integers(self): #test for no integers
        lst = ["a", [1.5, "b"], {"key": 2}]
        expected_result = 0
        result = HW3.sum_general_int_list(lst)
        self.assertEqual(result, expected_result) #no integers so it passes the test

if __name__ == '__main__':
    unittest.main()
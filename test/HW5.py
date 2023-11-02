########################################## HW3  ######################################
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



###################################### HW4 ########################################
###########################################

#
# 1. In this exercise we will make a "Patient" class
#
# The Patient class should store the state of
# a patient in our hospital system.
#
#
# 1.1)
# Create a class called "Patient".
# The constructor should have two parameters
# (in addition to self, of course):
#
# 1. name (str)
# 2. symptoms (list of str)
#
# the parameters should be stored as attributes
# called "name" and "symptoms" respectively


class Patient:
    def __init__(self, name, symptoms):
        self.name = name

        self._symptoms = []
        if symptoms != None:
            if type(symptoms) == str:
                self._symptoms.append(symptoms)
            elif type(symptoms) == list:
                self._symptoms.extend(symptoms)
        
        self._test = []
        self._result = []

#
# 1.2)
# Create a method called "add_test"
# which takes two paramters:
# 1. the name of the test (str)
# 2. the results of the test (bool)
#
# This information should be stored somehow.

    def add_test(self, test, result):
        self._test.append(test)
        self._result.append(result)
        #it's sort by add sequence, 
        #if add "covid" with true at beginning and add "covid" with false at later time
        #probability is taken by later added time
        

#
# 1.3)
# Create a method called has_covid()
# which takes no parameters.
#
# "has_covid" returns a float, between 0.0
# and 1.0, which represents the probability
# of the patient to have Covid-19
#
# The probability should work as follows:
#
# 1. If the user has had the test "covid"
#    then it should return .99 if the test
#    is True and 0.01 if the test is False
# 2. Otherwise, probability starts at 0.05
#    and increases by 0.1 for each of the
#    following symptoms:
#    ['fever', 'cough', 'anosmia']
    def has_covid(self):
        #create initial probaility
        covidProbability = 0.05;

        #each count add each symptom possibility by 0.1
        feverCount = 0.1;
        coughCount = 0.1;
        anosmiaCount = 0.1;

        length_of_tests = len(self._test)
        for t,covid_Index in zip(self._test,range(length_of_tests)):
            if t == 'covid':
                if self._result[covid_Index]==True:
                    covidProbability = .99
                    return covidProbability
                elif self._result[covid_Index]== False:
                    covidProbability = 0.01
        if covidProbability == 0.01:
            return covidProbability

        #check not-tested patient possibility
        #for each symptom, add possibility by 0.1
        #and only count once
        for s in self._symptoms:
            if s == 'fever':
                covidProbability += feverCount
                feverCount = 0
            elif s == 'cough':
                covidProbability += coughCount
                coughCount = 0
            elif s == 'anosmia':
                covidProbability += anosmiaCount
                anosmiaCount = 0
        return covidProbability


######################

# 2. In this exercise you will make an English Deck class made of Card classes
# 
# the Card class should represent each of the cards
#
# the Deck class should represent the collection of cards and actions on them

# 2.1) Create a Card class called "Card".
# The constructor (__init__ ) should have two parameters the "suit" and the "value" and the suit of the card.
# The class should store both as attributes.


# 2.2) Create a Deck class called "Deck".
# The constructor will create an English Deck (suits: Hearts, Diamonds, Clubs, Spades 
# and values: A, 2, 3, 4, 5, 6, 7, 8, 9, 10, J, Q, K). 
# It will create a list of cards that contain each of the existing cards in an English Deck.
# Create a method called "shuffle" that shuffles the cards randomly. 
# Create a method called "draw" that will draw a single card and print the suit and value. When a card is drawn, the card should be removed from the deck.


import random

#seed will create each compile, random choose in exact same sequences
#even after recompile
#random.seed(42)

class Card:
    def __init__(self, suit, value):
        self._suit = suit
        self._value = value

    def accessSuit(self):
        suit = str(self._suit)
        return suit
    def accessValue(self):
        value = str(self._value)
        return value
        
class EnglishDeck():

    def __init__(self):
        #cards: 4 suits* 13 values
        self._cards = []
        #create card and append by 13 times loops.
        #each append 4 suits
        for i in range(1,14):
            #after we append Card, A,J,Q,K, we append card by numeric value
            if i == 1:
                self._appendCards("A")
            elif i == 11:
                self._appendCards("J")
            elif i == 12:
                self._appendCards("Q")
            elif i == 13:
                self._appendCards("K")
            else:
                #in Card class, we can access card Value by public function
                #and it only return string of value
                self._appendCards(i)

    #append four suits type of cards by input Value
    def _appendCards(self, suitValue):
        HeartsCard = Card("Hearts",suitValue)
        DiamondsCard = Card("Diamonds",suitValue)
        ClubsCard = Card("Clubs",suitValue)
        SpadesCard = Card("Spades",suitValue)

        self._cards.append(HeartsCard)
        self._cards.append(DiamondsCard)
        self._cards.append(ClubsCard)
        self._cards.append(SpadesCard)

    def shuffle(self):
        random.shuffle(self._cards)

    def draw(self):
        if self._cards.__len__() != 0:
            self._cards.pop(0)
        else:
            print("No Card to Draw.")




###################

# 3. In this exercise you will create an interface that will serve as template 
# for different figures to compute their perimeter and surface. 

# 3.1Create an abstract class (interface) called "PlaneFigure" with two abstract methods:
# compute_perimeter() that will implement the formula to compute the perimiter of the plane figure.
# compute_surface() that will implement the formula to compute the surface of the plane figure.

# 3.2 Create a child class called "Triangle" that inherits from "PlaneFigure" and has as parameters in the constructor "base", "c1", "c2", "h". ("base" being the base, "c1" and "c2" the other two sides of the triangle and "h" the height). Implement the abstract methods with the formula of the triangle.

# 3.3 Create a child class called "Rectangle" that inherits from "PlaneFigure" and has as parameters in the constructor "a", "b" (sides of the rectangle). Implement the abstract methods with the formula of the rectangle.

# 3.3 Create a child class called "Circle" that inherits from "PlaneFigure" and has as parameters in the constructor "radius" (radius of the circle). Implement the abstract methods with the formula of the circle.

from math import pi
from abc import ABCMeta, abstractmethod
#abstract class
class PlaneFigure(metaclass = ABCMeta):
    def __init__(self):
        return

    
    #compute total length
    @abstractmethod
    def compute_perimeter(self):
        return NotImplementedError

    @abstractmethod
    def compute_surface(self):
        return NotImplementedError
    
class Rectangle(PlaneFigure):
    def __init__(self,a,b):
        self.a = int(a)
        self.b = int(b)

    def compute_perimeter(self):
        return (self.a+self.b)*2
    
    def compute_surface(self):
        return self.a*self.b


class Triangle(PlaneFigure):
    def __init__(self,base,c1,c2,h):
        self.base = int(base)
        self.c1 = int(c1)
        self.c2 = int(c2)
        self.h = h

    def compute_perimeter(self):
        return self.base + self.c1 + self.c2
    
    def compute_surface(self):
        return self.base*self.h/2
    


class Circle(PlaneFigure):
    def __init__(self,radius):
        self.radius = int(radius)

    def compute_perimeter(self):
        return 2*pi*self.radius
    
    def compute_surface(self):
        return pi*self.radius*self.radius

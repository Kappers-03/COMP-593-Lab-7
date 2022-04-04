#   LAB 7 PYTHON 
#   -----------------------------------------------------------------
#   -----------------------------------------------------------------
#   PROGRAM DESCRIPTION: This lab is designed to send a introduction
#   message from data about their name, student number, favourite 
#   pizza toppings, and as well as their favourite movies! 
#   -----------------------------------------------------------------
#   -----------------------------------------------------------------
#   USAGE: python A7L-NolanKapshey.py
#
#   -----------------------------------------------------------------
#   -----------------------------------------------------------------
#
#   DUE DATE: MONDAY APRIL 4TH, 2022
#
#   -----------------------------------------------------------------
#   -----------------------------------------------------------------
#   HISTORY:
#       DATE        AUTHOR      Description
#       2022-04-02  N.KAPSHEY   Initial Creation
#
#   _________________________________________________________________
#   

from urllib3 import Retry


def main():
    
    # Create data info 
    personal_info = { 
                     'name': 'Nolan Kapshey',
                     'student_id': 10260252,
                     'toppings': [
                         'Cheese',
                         'Peperoni',
                         'Pineapple'
                     ],
                     'favourite_movie': [
                         {'movie': 'Happy Gilmore',
                          'genre': 'Sports Comedy'
                          },
                         {'movie': 'Step Brothers',
                          'genre': 'Comedy'
                          },
                        ]
                     }
    # Create a new movie and append it to favourite_movie
    new_movie = {'movie': 'Star Wars: The Rise of Skywalker', 'genre': 'Action'}
    personal_info['favourite_movie'].append(new_movie)  
    
    # Initialize new toppings 
    new_toppings = ('Ham', 'Kale', 'Bacon')
    new_pizza_top(personal_info, new_toppings)
    
    # Print out the sentence(s)
    sentence_structure_one(personal_info)
    sentence_structure_two(personal_info)
    sentence_structure_three(personal_info)
    sentence_structure_four(personal_info)
    
    # Create a function that accepts pizza topings to the data structure in alhabetical order 
def new_pizza_top(personal_info, toppings):
    for t in toppings:
        personal_info['toppings'].append(t)
    personal_info['toppings'].sort()
    pass

def sentence_structure_one(personal_info):
    output_one = "Hey, my name is " + str(personal_info['name']) + ", and my Student ID is " + str(personal_info['student_id'])
    print(output_one, end = ". \n")
    return


def sentence_structure_two(personal_info):
    output_two = "My ideal pizza contains  "
    
    for i in enumerate(personal_info):
        if i < len(personal_info['toppings']) -1:
            output_two += personal_info['toppings'] + ', '
        else:
            output_two +="and " + personal_info['toppings'] + '.'
    print(output_two)

def sentence_structure_three(personal_info):
    output_three = "My favourite movie genres are: "
    
    for i,g in enumerate(personal_info['favourite_movie']):
        
        if i < len(personal_info['favourite_movie']) - 1:
            output_three += g['genre'] + ', '
        else: 
            output_three += "and " + g['genre'] + '.'
    print(output_three, end = '\n')

def sentence_structure_four(personal_info):
    output_four = "My favourite movies of all time are: "
    
    for i,m in enumerate(personal_info['favourite_movie']):
        
        if i < len(personal_info['favourite_movie']) - 1:
                output_four += m['movie'] + ", "
        else: 
            output_four += "and " +  m['movie'] + "."
    print(output_four, end = '\n')


main()   
"""
We need to write a program to find the position of a given number in a list of
numbers arranged in decreasing order. We also need to minimize the number of times
we access elements from the list.

Input: A list of numbers sorted in decreasing order:. E.g. [13,11,10,7,4,3,1,0]
Query: A number, whose position in the array is to be determined.E.g. 7
Output: The position o query in the list cards. E.g 3 in the above case (counting from 0)
"""


tests = []

#query occurs in the middle
tests.append ( {
    'input' : {
        'cards' : [13,11,10,7,4,3,1,0],
        'query' : 7
    },
    'output': 3
} )

#query occurs in the first element
tests.append ( {
    'input' : {
        'cards' : [4,2,1,-1],
        'query' : 4
    },
    'output':0
})
#query occurs in the last eleent

tests.append ( {
    'input' : {
        'cards' : [3,-1,-9,-127],
        'query' : -127
    },
    'output':3
})

#cards contains just one element, query in the last eleent

tests.append ( {
    'input' : {
        'cards' : [6],
        'query' : 6
    },
    'output':0
})

#cards does not contain query
tests.append({
    'input': {
        'cards': [9,7,5,2,-9],
        'query': 4
    },
    'output': -1
})

#cards is empty
tests.append({
    'input': {
        'cards': [],
        'query': 4
    },
    'output': -1
})

#numbers can repeat in cards
tests.append({
    'input': {
        'cards': [8,8,6,6,6,6,6,3,2,2,2,0,0,0],
        'query': 3
    },
    'output': 7
})

#query occurs multiple times
tests.append({
    'input': {
        'cards': [8,8,6,6,6,6,6,3,2,2,2,0,0,0],
        'query': 3
    },
    'output': 2
})

# locate_cards(**tests['input']) == tests['output']

def locate_cards(cards, query):
    # create a variable position with the value 0
    position = 0
    
    #set up a loop for repetion
    while True:
        
        #check if the element at the current position matche the query
        if cards[position] == query:
            return position
        
        # increment the position
        position += 1

        # check if we have reached the end of the array
        if position == len(cards):

            #number not found, return -1
            return -1
        
print(locate_cards(tests[0]['input']['cards'],tests[0]['input']['query']) == tests[0]['output'])
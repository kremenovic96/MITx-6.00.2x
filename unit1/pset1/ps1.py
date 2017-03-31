###########################
# 6.00.2x Problem Set 1: Space Cows 

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """

    cow_dict = dict()

    f = open(filename, 'r')
    
    for line in f:
        line_data = line.split(',')
        cow_dict[line_data[0]] = int(line_data[1])
    return cow_dict


# Problem 1
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    inner = []
    sol = []
    cowsCopy = list(cows.keys())
    weight = 0
    while len(cowsCopy) != 0:
        heaviest = None
        for cow in cowsCopy:
            if cows[cow] + weight <= limit:
                if heaviest == None:
                    heaviest = cow
                if cows[cow] > cows[heaviest]:
                    heaviest = cow
        if heaviest == None:
            sol.append(inner)
            weight = 0
            inner = []
            
        else:    
            
            inner.append(heaviest)
            weight += cows[heaviest]
            cowsCopy.remove(heaviest) 
    sol.append(inner)        
    return sol        
            
                
        

 


# Problem 2
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    def addWeight(cows):
        sum = 0
        for cow in cows:
            sum += cows[cow]
        return sum
    for i in get_partitions():
        
    

        
# Problem 3
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    pass


"""
Here is some test data for you to see the results of your algorithms with. 
Do not submit this along with any of your answers. Uncomment the last two
lines to print the result of your problem.
"""

#cows = load_cows("ps1_cow_data.txt")
limit=100
#print(cows)

#print(greedy_cow_transport(cows, limit))
#print(brute_force_cow_transport(cows, limit))
############################## below is added by me ############################
print()
someCows = {"Jesse": 6, "Maybel": 3, "Callie": 2, "Maggie": 5}
print(greedy_cow_transport(someCows, 10))
print()
print(greedy_cow_transport({'MooMoo': 85, 'Muscles': 65, 'Patches': 60, 'Horns': 50, 'Clover': 5, 'Lotus': 10, 'Louis': 45, 'Milkshake': 75, 'Polaris': 20, 'Miss Bella': 15}, 100))
print("CORRECT OUTPUT: ")
print([['MooMoo', 'Miss Bella'], ['Milkshake', 'Polaris', 'Clover'], ['Muscles', 'Lotus'], ['Patches'], ['Horns', 'Louis']])

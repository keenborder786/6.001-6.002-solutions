###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time
import operator

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
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
    dic_cow={}
    with open(filename,"r") as f:
        for line in f:
            new_line=line.rstrip('\n')
            cow_list=new_line.split(",")
            if len(cow_list) > 1:
               dic_cow[cow_list[0]]=cow_list[1]
            cow_list=[]
        print(dic_cow)
        return dic_cow
# Problem 2
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
    # TODO: Your code here
    cow_copy=cows.copy()
    sorted_cow = sorted(cow_copy.items(), key=operator.itemgetter(1),reverse=True)
    sorted_cow_dic=dict(sorted_cow)
    trip=[]
    result=[]
    TotalWieght=0
    for name in sorted_cow_dic.keys():
            if (TotalWieght+int(sorted_cow_dic[name])) <= limit:
                 TotalWieght += int(sorted_cow_dic[name])
                 trip.append(name)
    for char in trip:
            del sorted_cow_dic[char]
    result.append(trip)
    while sorted_cow_dic!={}:
        trip=[]
        TotalWieght=0
        for name in sorted_cow_dic.keys() :
            if (TotalWieght+int(sorted_cow_dic[name])) <= limit:
                 TotalWieght += int(sorted_cow_dic[name])
                 trip.append(name)
        for char in trip:
            del sorted_cow_dic[char]
        result.append(trip)
    return result

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
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
    possible_result=[]
    a=0
    imin=100000000000
    Total_Wieght=0
    cow_copy=cows.copy()
    sorted_cow = sorted(cow_copy.items(), key=operator.itemgetter(1),reverse=True)
    sorted_cow_dic=dict(sorted_cow)
    cow_name_list=list(sorted_cow_dic)
    for partition in get_partitions(cow_name_list):
        i=len(partition)
        a=0
        Total_Wieght=0
        for list_cow in partition:
            for cow_name in list_cow:
                Total_Wieght+=int(cow_copy[cow_name])
            if Total_Wieght < limit and a<i:
                a+=1
                Total_Wieght=0
            if a==i and Total_Wieght<limit:
                possible_result.append(partition)
    for cows_sets in possible_result:
        i=len(cows_sets)
        if i<imin:
            imin=i
            minimum_cow_set=cows_sets
    return minimum_cow_set
# Problem 4
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
    
    
    start=time.time()
    a=greedy_cow_transport(load_cows("ps1_cow_data.txt"),limit=10)
    print(a)
    end=time.time()
    print("The greedy algorithm took "+str(end-start)+ " seconds")
    
    
    start_2=time.time()
    i=brute_force_cow_transport(load_cows("ps1_cow_data.txt"),limit=10)        
    print(i)     
    end_2=time.time()
    print("The brute force algorithm took "+str(end_2-start_2)+" seconds")
compare_cow_transport_algorithms()

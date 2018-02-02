# Problem 1
print ('\nProblem 1\n')

q1_dict = {'list':[1,2,3,4], 'tuple':('cat', 'dog'), 'integer':1, 
              'float':99.99, 1:'integer', 2:'integer_2', 'Uppercase_string':'ABCD',
              'CHARACTER':'C'}

def q1_func(dictionary):
    import string
    print(dictionary)
    keys = list(dictionary.keys())
    keys = [str(i) for i in keys]
    modified_dict = {}
    for i in keys:
        lower_vowels = ("a", "e", "i", "o", "u")
        lower_consonants = ("b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z")    
        if i.startswith(lower_vowels):
            modified_dict[i] = "vowel"
        elif i.startswith(lower_consonants):
            modified_dict[i] = "consonant"
        else:
            modified_dict[i] = "remove"
    for k, v in list(modified_dict.items()):
        if v == "remove":
            modified_dict.pop(k)
    print(modified_dict)
    return modified_dict

q1_func(q1_dict)

# Problem 2
print ('\nProblem 2\n')

q2_dict = {'A':[1,2,3,4,5], 'B':[12.1, 14.2, 20.3, 25.4], 'C':[10, 25.5, 50.9, 101]}
q2_remainder = [2,3,4,5]

def q2_func(dictionary, remainder=[]):
    if remainder == []:
        remainder.append(2)
    print (dictionary)
    print (remainder)
    results = {}
    if len(remainder) == 1:
        for k, v in list(dictionary.items()):
            #to get remainder: x % y
            results[k] = {}
            for i in v:
                results[k][i] = [i % 2]
    else:
        for k, v in list(dictionary.items()):
            results[k] = {}
            # take each item from v (which is a list) and make it the key of results[k]
            # then divide each item from v by each item from remainder list 
            #and make a new list that is the value for the new key
            for i in v:
                second_remainder = []
                for x in remainder:
                    second_remainder.append(i % x)
                results[k][i] = second_remainder
    print (results)
    return results

output = q2_func(q2_dict)
output = q2_func(q2_dict, q2_remainder)

# Problem 3
print('\nProblem 3\n')

list_1 = [1.5, 3.5, 5.5, 7.5]
list_2 = [0, 4, 8, 12]

#list1, list2 are lists of numbers
def q3_func(list1, list2):
    multiplied = 0
    iteration = 1
    while multiplied < 300:
        print("Iteration: %s" % iteration)
        for value1, value2 in zip(list1, list2):    
            print ("Value 1: %s" % value1)
            print ("Value 2: %s" % value2)
            multiplied = value1 * value2
            print("Multiplied value: %s" % multiplied)
        #multiply all numbers in both lists by 2  
        new_list1 = []
        for item in list1:
            new_list1.append(item * 2)
        list1 = new_list1
        new_list2 = []
        for item in list2:
            new_list2.append(item * 2)
        list2 = new_list2
        iteration = iteration + 1
    print("Function complete.")

q3_func(list_1, list_2)

# Problem 4
print ('\nProblem 4\n')

def median_calculator(numbers):
    #sort
    #figure out if even or odd: if (num % 2) == 0:
    #pick middle 2 if even and return mean
    #pick middle if odd and return
    sorted_data = numbers.sort()
    half_length_of_data = int(len(numbers) / 2)
    if (half_length_of_data % 2) == 0:
        first_middle = numbers[half_length_of_data - 1]
        second_middle = numbers[half_length_of_data]
        #add mean of two middle numbers
        mean_of_middle = (first_middle + second_middle) / 2
        return mean_of_middle
    else:
        return numbers[half_length_of_data]

def q4_func(i, numbers):
# Takes in two arguments. 
# One will be a single number for the current iteration and 
# the second will be a list of numbers. 
    # Prints out the current iteration.
    iteration = i
    print("i is currently: %s" % iteration)
    # Calculates the mean of numbers without using numpy
    mean = (sum(numbers)) / len(numbers)
    # Calculates the median of numbers using the median_calculator function you created above. 
    median = median_calculator(numbers)
    # Prints out the mean and median.
    print("The mean is: %s" % mean)
    print("The median is: %s" % median)

for i in range(1, 15, 2):
    numbers = [x if not x % i == 0 else 0 for x in range(101)]
    q4_func(i, numbers)

# Problem 5
print ('\nProblem 5\n')

q5_predictions = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

q5_true_values = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]

def q5_func(true_values, predictions):
    import numpy as np
    #For each value in predictions and true_values, calculate the error 
    #(which is the prediction - the true value at each n-index). 
    #Store these values in a list called errors
    errors = []
    for v1, v2 in zip(true_values, predictions):
        errors.append(v2 - v1)
    #Square each element in errors 
    #(you should have a list of the same size with the squared elements instead of the differences)
    squared_errors = []
    for error in errors:
        squared_errors.append(error ** 2)
    mean_squared_errors = (sum(squared_errors)) / len(squared_errors)
    #Take the square root of the mean created in step 4 using np.sqrt(). 
    #Store this in a variable called rmse
    rmse = np.sqrt(mean_squared_errors)
    print("RMSE: %s" % rmse)
    return rmse


q5_func(q5_true_values, q5_predictions)   

# Problem 6
print ('\nProblem 6\n')

import matplotlib.pyplot as plt
import csv

path_to_csv = './assets/sat_scores.csv'

verbal_scores = []
math_scores = []
rates = []
states = []

with open('./assets/sat_scores.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        verbal_scores.append(row[2])
        math_scores.append(row[3])
        rates.append(row[1])
        states.append(row[0])

verbal_scores = verbal_scores[1:52]
math_scores = math_scores[1:52]
rates = rates[1:52]
states = states[1:52]

#Print out each state and its associated Verbal and Math scores as well as participation rate. 
#The format should be similar to:
#PA: Verbal: 500, Math: 499, Rate: 71
def print_state_stats(statelist, verballist, mathlist, ratelist):
    stats_list = []
    for s, v, m, r in list(zip(statelist, verballist, mathlist, ratelist)):
        stats_list.append("%s: Verbal: %s, Math: %s, Rate: %s" %(s, v, m, r))
    stats_list = sorted(stats_list)
    for i in stats_list:
        print(i)
    return stats_list
        
print_state_stats(states, verbal_scores, math_scores, rates)

# In a print statement following this, answer the two following questions:

# Are all states accounted for (and how do you know?)
# Are there any rows that should be dropped (and why)
# If there are any rows that should be dropped, do so at this point.
print("")
print("Are all states accounted for (and how do you know)? Using the len function we can see that the list of states equals 51, which includes DC. A double-check through the alphabetically sorted list verifies all states are included.")
print("Are there any rows that should be dropped (and why)? The header and final All rows were dropped early on via a list slice. The DC row could be dropped if DC is not considered a state. I would ask the client or the project manager whether they wanted DC in the data set. Or if my own project, I'd keep it as since it was in the original data set, it can offer useful comparative info. If I were really nerdy, I'd make two different versions, one with DC and one without.")

# Problem 7
print ('\nProblem 7\n')

#Generate and print out the:

# Minimum
# Maximum
# Mean
# Standard Deviation
# Median
# Mode
# of the Verbal, Math, and Rate columns.

def basic_stats(list):
    import numpy as np
    import scipy.stats as sps
    print("Minimum: ", min(list))
    print("Maximum: ", max(list))
    print("Mean: ", np.mean([float(x) for x in (list)]))
    print("Standard Deviation: ", np.std([float(x) for x in (list)]))
    print("Median: ", np.median([float(x) for x in (list)]))
    print("Mode: ", sps.mode([float(x) for x in (list)]))
    
print("Verbal Scores Stats:")
basic_stats(verbal_scores)
print("")
print("Math Scores Stats:")
basic_stats(math_scores)
print("")
print("Rates Stats:")
basic_stats(rates)

# Problem 8
print ('\nProblem 8\n')

#Generate and save to file a histogram of Verbal Scores. In a print statement, 
#print out anything you find interesting or distinctive about the histogram.

fig = plt.figure(figsize=(8,6), dpi=300)
ax1 = plt.subplot(1, 1, 1)
ax1.set_title('Verbal SAT Scores')
verbal_scores_hist = ax1.hist([int(x) for x in (verbal_scores)], bins=10, color="purple", edgecolor="black")

plt.savefig('verbal_scores_hist.png')

print("Observations about Verbal Scores Histogram: In trying several bin sizes, the shape of the histogram stays generally bimodal, but not sure how important this is. The data are clustered in a fairly tight group with a range of only slightly more than 100 between the min and max average scores and the frequency does not range widely either.")

# Problem 9
print ('\nProblem 9\n')

#Generate and save to file a histogram of Math Scores. In a print statement, 
#print out anything you find interesting or distinctive about the histogram.

fig = plt.figure(figsize=(8,6), dpi=300)
ax1 = plt.subplot(1, 1, 1)
ax1.set_title('Math SAT Scores')
math_scores_hist = ax1.hist([int(x) for x in (math_scores)], bins=20, color="orange", edgecolor="black")

plt.savefig('math_scores_hist.png')
print("Observations about Math Scores Histogram: The math scores ranged more widely than the verbal scores (a range of over 50% larger) which might indicate that some states do not have a curriculum in place that is skilled at teaching students math. However most states' scores fell within about a 100 point range. In playing around with the bin sizes, it becomes clear that one state in particular (which we can determine to be Ohio from the data) is substantially below the rest. As Ohio's verbal average was pretty middle of the pack (almost right at the median and mean, which were close together), we might conclude this has to do with how math is taught in Ohio. However, it is important to note that only 26% of students eligible to take the SAT in Ohio took it.")

# Problem 10
print ('\nProblem 10\n')

#Generate and save to file a scatterplot of Participation Rate by either Math or Verbal Scores (your choice). 
#Make sure that your axes are clearly labeled. In a print statement, 
#discuss any interesting trends you see with regards to their relationship.

fig = plt.figure(figsize=(8,6), dpi=300)
ax1 = plt.subplot(1, 1, 1)
ax1.set_title('Participation Rate by Math Scores')
ax1.set_ylabel('Math Scores')
ax1.set_xlabel('Participation Rate')

participation_math_scatter = ax1.scatter([int(x) for x in rates], [int(x) for x in math_scores])
plt.savefig('participation_math_scatter.png')

print("Observations about Participation Rate by Math Scores Scatter Plot: Generally it seems the higher the participation rate, the lower the math scores. This makes sense because in states with low participation rates, it is likely the most motivated students who take the SAT. As more students of varied academic levels take the test, it brings scores down. This chart clearly shows what an outlier the Ohio statistics are and it would be worth investigating whether something might have gone wrong in that state with either math teaching or test taking.")







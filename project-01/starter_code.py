# Problem 1
print '\nProblem 1\n'

q1_dict = {'list':[1,2,3,4], 'tuple':('cat', 'dog'), 'integer':1, 
              'float':99.99, 1:'integer', 2:'integer_2', 'Uppercase_string':'ABCD',
              'CHARACTER':'C'}

## Fill in q1_func

def q1_func(dictionary):
	pass

q1_func(q1_dict) # Should be the same as expected result

# Problem 2
print '\nProblem 2\n'

q2_dict = {'A':[1,2,3,4,5], 'B':[12.1, 14.2, 20.3, 25.4], 'C':[10, 25.5, 50.9, 101]}
q2_remainder = [2,3,4,5]

## Fill in q2_func

def q2_func(dictionary, remainder=[]):
	pass

output = q2_func(q2_dict) # Should be same as expected result 1
output = q2_func(q2_dict, q2_remainder) # Should be same as expected result 2

# Problem 3
print '\nProblem 3\n'

q1_list1 = [1.5,3.5,5.5,7.5]
q2_list2 = [0,4,8,12]

## Fill in q3_func

def q3_func(list1, list2):
	pass

q3_func(q1_list1, q2_list2) # Should be same as expected result

# Problem 4
print '\nProblem 4\n'

# Fill in median_calculator and q4_func

def median_calculator(numbers):
	pass

def q4_func(i, numbers):
	pass

for i in range(1, 15, 2):
    numbers = [x if not x % i == 0 else 0 for x in range(101)]
    q4_func(i, numbers) # should return same result as expected results

# Problem 5
print '\nProblem 5\n'

q5_predictions = [14.2,5.8,4.8,12.7,5.6,-1.2,5.3,11.9,4.8,8.1,1.5,8.5,14.9,6.1,
     6.8,12.6,15.5,24.3,15.6,16.8,22.3,22.6,26.2,19.0,24.3,26.3,
     25.3,31.6,27.3,33.0,32.6,30.7,29.6,34.7,32.7,43.1,40.1,35.4,49.6,38.6]

q5_true_values = [-15.5,-8.5,0.8,-3.9,4.9,12.7,10.0,16.5,5.7,13.1,10.3,12.4,-1.5,
     1.7,26.0,14.3,30.3,21.7,27.5,38.2,18.9,21.2,18.2,26.1,14.7,16.4,
     22.8,34.3,37.1,38.9,39.1,33.8,52.2,36.5,20.7,21.6,14.5,33.6,44.5,44.2]

# Fill in q5_func

def q5_func(true_values, predictions):
	pass

q5_func(q5_true_values, q5_predictions) # Should return same result as expected results

# Problem 6
print '\nProblem 6\n'

path_to_csv = './assets/sat_scores.csv'

## Path forward is up to you!

# Dropping those rows

# Problem 7
print '\nProblem 7\n'

## Path forward is up to you!

# Problem 8
print '\nProblem 8\n'

## Path forward is up to you!

# Problem 9
print '\nProblem 9\n'

## Path forward is up to you!

# Problem 10
print '\nProblem 10\n'

## Path forward is up to you!
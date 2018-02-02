# Project 1

Project 1 covers a couple of different tasks:

- Drills through Python programming further
- Basic practice of data analysis skills

For the first 5 problems, your deliverable will some sort of function written in your script. For the last 5 problems, you will be doing some basic data analysis using a provided CSV and some of the skills we have learned during the last week. 

## Deliverable

Your deliverable will be one script (`results.py`) that should include the following:

- Python Programming Questions
  - 5 functions (named `q1_func` through `q5_func`) that meet the parameters of that question.
  - Each function should be ran at least once during the script, taking in the provided test data and printing the result to screen.
  - The result should match the expected result provided in the write-up
- Basic data analysis skills
  - The first two questions ask for a specific set of numbers (averages, etc.) When you find these results, you should print them to screen with some sort of text identifying it (such as `print 'The mean of column X is %s' % mean_column_x` where `mean_column_x` is your answer)
  - The last three questions ask for visualizations. Your script should create the visualizations and save them to a new folder called `images` under the names `q8.png`, `q9.png`, and `q10.png` respectively. 

We will be running your script from top to bottom, so make sure that it completes successfully! Your pull request is expected by 10 AM on Tuesday morning.

## Set-up

- Fork this repo into your own library, then clone it to your local machine
- Create your submission file (`results.py`). How you develop that file is up to you (though some hints are provided below)
- When you are ready to submit, generate a pull request to this repository. We'll cover pull requests on Monday, so don't worry about this through the weekend. 

## Tips

- Add, commit, and push your intermediate work frequently! It's the best way to make sure that your code remains backed up.
- When you tackle each problem, make a new script that you can quickly iterate with. Once you're happy with a result, copy it into `results.py`.
  - For the data analysis portion, you might find it easier to work on your results in one file and copy the code over en masse.
- When developing the first 5 functions, I find it helpful to:
  - Identify each thing that the function needs to print
  - Once you've established what each step needs to return, work backwards to determine what you need to do to make that happen
  - Starting out with numerous print statements can help you keep mental track of what the function looks like at a given point in time. Those can be removed as the function starts behaving as you want it to.
- Ask for help early and often (particularly of your fellow coursemates!) While this project is designed to give you individual practice in Python, part of learning how to code is learning how to ask for (and give!) help. 

## Problem 1

Create a function named `q1_func` that accepts one argument (a dictionary) and does the following:

1. Prints the dictionary as it was received
2. Iterates through the dictionary and does the following:
	1. For each pair, if the *key* starts with a lowercase vowel, change the *value* of that pair to the string `'vowel'`
	  - Example: `'apricot': ['a', 'b', 'c']` -> `'apricot': 'vowel'`
	2. For each pair, if the *key* starts with a lowercase consonant, change the *value* of that pair to the string `'consonant'`.
	3. Remove the pair from the dictionary if it does not match criteria 1 or 2
3. Print the modified dictionary
4. Return the modified dictionary

### Notes and Hints

- `string.ascii_lowercase` contains all of the lowercase letters in the alphabet. Because it is part of the `string` library, you'll have to include `import string` at the beginning of your script.
- You can check if a string contains another string by using `in`
  - Example: `if 'a' in 'alphabet':` would return `True` if `a` is in the string `alphabet` and `False` if it was not.

### Test Dictionary

```python
{'Uppercase_string': 'ABCD', 1: 'integer', 2: 'integer_2', 'tuple': ('cat', 'dog'), 'integer': 1, 'CHARACTER': 'C', 'float': 99.99, 'list': [1, 2, 3, 4]}
```

### Your Function Should Return

```python
{'Uppercase_string': 'ABCD', 1: 'integer', 2: 'integer_2', 'tuple': ('cat', 'dog'), 'integer': 1, 'CHARACTER': 'C', 'float': 99.99, 'list': [1, 2, 3, 4]}
{'tuple': 'consonant', 'integer': 'vowel', 'float': 'consonant', 'list': 'consonant'}
```

## Problem 2

Create a function named `q2_func` that accepts 1 or 2 arguments. The first argument will be a dictionary (each value in this dictionary will be a list of numbers) and the second (optional) argument will be a list (also of numbers). The function should do the following:

1. Accept a dictionary as the first argument.
2. Accept a list as its second argument. This argument will be a keyword argument named `remainder` (see Notes and Hints below for what that means).
3. Check to see if remainder is empty; if it is, append the integer `2` to `remainder`.
4. Print the dictionary it received.
5. Print `remainder`.
6. Create a new dictionary within the function named `results`.
7. Iterate over each key and value pair in the dictionary:
	1. If there is only one value in `remainder`, return a list containing the remainder of each value in the list of numbers from each value in `remainder`. (Check Notes and Hints below for how to find a remainder!)
		- Example: if the value of one pair was the list `[1, 2, 3]` and `remainder` was `[2]`, we would want the results to be (`[remainder(1, 2), remainder(2, 2), remainder(3,3)]`)
	2. If there are multiple values in `remainder`, return a dictionary where each key is one of the original numbers and each value is the list of remainders:
		- Example: if the value of one pair was the list `[1, 2]` and `remainder` was `[2, 4]`, we would return `{1: [remainder(1, 2), remainder(1, 4)], 2: [remainder(2, 2), remainder(2, 4)]}`
	3. Assign all of these results to the new `results` dictionary. The key should be the original key of the starting dictionary and the value should be everything calculated in Steps 1 and 2.
8. Print out the `results` dictionary.
9. Return the `results` dictionary.

### Notes and Hints

- Keyword arguments let us create optional arguments that the user can choose to supply or not. They have to include a default value (in case they are not supplied) and must come after all other arguments. 
  - `def keyword_fun(argument1, keyword_argument=[]):` would create a function that required one argument (stored in `argument1`) and an optional second argument stored in `keyword_argument`. This argument would be `[]` if nothing was supplied, otherwise, it would be whatever value was supplied.
- The remainder is the number left over when one number is divided by a second. 
  - `14 % 5` would return the remainder of 14 divided by 5 (which in this case is 4). This is because 5 goes into 14 evenly twice (leaving 10), while 4 is "left behind"

### Test Dictionary

```python
{'A': [1, 2, 3, 4, 5], 'C': [10, 25.5, 50.9, 101], 'B': [12.1, 14.2, 20.3, 25.4]}
[2]
```

### Your Function Should Return

```python
{'A': [1, 2, 3, 4, 5], 'C': [10, 25.5, 50.9, 101], 'B': [12.1, 14.2, 20.3, 25.4]}
[2]
{'A': {1: [1], 2: [0], 3: [1], 4: [0], 5: [1]}, 'C': {25.5: [1.5], 10: [0], 50.9: [0.8999999999999986], 101: [1]}, 'B': {14.2: [0.1999999999999993], 20.3: [0.3000000000000007],
 12.1: [0.09999999999999964], 25.4: [1.3999999999999986]}}
{'A': {1: [1], 2: [0], 3: [1], 4: [0], 5: [1]}, 'C': {25.5: [1.5], 10: [0], 50.9: [0.8999999999999986], 101: [1]}, 'B': {14.2: [0.1999999999999993], 20.3: [0.3000000000000007],
 12.1: [0.09999999999999964], 25.4: [1.3999999999999986]}}
[2, 3, 4, 5]
{'A': {1: [1, 1, 1, 1], 2: [0, 2, 2, 2], 3: [1, 0, 3, 3], 4: [0, 1, 0, 4], 5: [1, 2, 1, 0]}, 'C': {25.5: [1.5, 1.5, 1.5, 0.5], 10: [0, 1, 2, 0], 50.9: [0.8999999999999986, 2.89
99999999999986, 2.8999999999999986, 0.8999999999999986], 101: [1, 2, 1, 1]}, 'B': {14.2: [0.1999999999999993, 2.1999999999999993, 2.1999999999999993, 4.199999999999999], 20.3:
[0.3000000000000007, 2.3000000000000007, 0.3000000000000007, 0.3000000000000007], 12.1: [0.09999999999999964, 0.09999999999999964, 0.09999999999999964, 2.0999999999999996], 25.
4: [1.3999999999999986, 1.3999999999999986, 1.3999999999999986, 0.3999999999999986]}}
```

## Problem 3

Create a function named `q3_func` that accepts two lists of numbers. Your function should do the following:

1. Accept two arguments that are lists of numbers (named `list1` and `list 2`)
2. Start a `while` loop that:
  1. Prints the current iteration, starting at `1`
  2. Create a nested `for` loop that takes the _n_-th element of each list and assigns it to `value1` and `value2`
    - If we had `list1 = [1, 2]` and `list2 = [3, 4]`, there would be two iterations at this point:
      - Iteration 1 would look at the 0th index, `value1` would be `1` and `value2` would be `3`
      - Iteration 2 would look at the 1st index, `value1` would be `2` and `value2` would be `4`
  3. Within the `for` loop:
    1. Print the numbers that are being used in this step
    2. Multiply those numbers together and assign them to a variable called `multiplied`
    3. If `multiplied` is greater than or equal to 300, break out of both the `for` and the `while` loop.
  4. If the loop is not broken, multiply all numbers in both lists by 2 and increase the iteration by 1.
3. Print "Function complete"

### Notes and Hints

- To break out of a loop, use the `break` command:
```python 
for thing in my_list:
if thing > 10:
 break
```
 - `zip()` will join the elements of any number of lists and tuples together by index. The result will be a list of tuples, where each tuple is (in order) the _n_th element of those collections:
```python
zip([1,2], [20, 40])
>> [(1, 20), (2, 40)]
```
- In a `for` list, you can assign multiple variables at once: `for value1, value2 in zip(list1, list2):`
- If you want a `while` loop to last until you break it, you can use `while True:` (because True will always be True). That said, this will run until it hits `break` or you end it from the command line. Be careful with this command!

### Test Lists

```python
list1 = [1.5, 3.5, 5.5, 7.5]
list2 = [0, 4, 8, 12]
```

### Your Function Should Return

```python
list 1:  [1.5, 3.5, 5.5, 7.5]
list 2:  [0, 4, 8, 12]
Iteration: 1
Value 1: 1.5
Value 2: 0
Multiplied value: 0.0
Value 1: 3.5
Value 2: 4
Multiplied value: 14.0
Value 1: 5.5
Value 2: 8
Multiplied value: 44.0
Value 1: 7.5
Value 2: 12
Multiplied value: 90.0
Iteration: 2
Value 1: 3.0
Value 2: 0
Multiplied value: 0.0
Value 1: 7.0
Value 2: 8
Multiplied value: 56.0
Value 1: 11.0
Value 2: 16
Multiplied value: 176.0
Value 1: 15.0
Value 2: 24
Multiplied value: 360.0
Function complete.
```

## Problem 4

Write two functions, one named `median_calculator` and one named `q4_func` that calculates summary statistics without using `numpy`. `median_calculator` should do the following:

1. Accept one argument that is a list of numbers
2. Determine if there is an even or odd number of items in the list.
3. Based on whether it is even or odd, return the correct value for the median. This should not be calculated using numpy.

`q4_func` should do the following:
1. Take in two arguments. One will be a single number for the current iteration and the second will be a list of numbers.
2. Prints out the current iteration.
3. Calculates the mean of `numbers` without using numpy
4. Calculates the median of `numbers` using the `median_calculator` function you created above.
5. Prints out the mean and median.

### Your Function Should Return

```python
i is currently: 1
The mean is: 0.0
The median is: 0
i is currently: 3
The mean is: 33.3366336634
The median is: 25
i is currently: 5
The mean is: 39.603960396
The median is: 37
i is currently: 7
The mean is: 42.7227722772
The median is: 41
i is currently: 9
The mean is: 44.1188118812
The median is: 43
i is currently: 11
The mean is: 45.099009901
The median is: 45
i is currently: 13
The mean is: 46.396039604
The median is: 46
```

### Notes and Hints

- Define both functions first
- Call the `q4_func` function within the provided `for` loop
- The provided `for` loop iterates over every 2nd number starting at 1 and ending at 15 and creates a list in each iteration that contains all numbers between 1 and 100 that do not divide evenly into the current value for `i`. If the current iteration can divide evenly into all numbers between 1 and 100, the list will have one value (0).
  - Before you begin, if we start with `i = 1`, how many numbers can 1 divide evenly into? What would our starting list look like?

## Problem 5

We're going to jump ahead just a tiny bit and create a function that calculates a value called *Root Mean Squared Error*. This is a value we will use a lot in the coming weeks, but basically, this function will create a value that tells us how close a set of "predictions" are to the "actual values" they are supposed to predict. 

Create a function called `q5_func` that does the following:

1. Accept two lists, one named `true_values` and one named `predictions`. Both will be lists of the same size populated with numbers. 
2. For each value in predictions and true_values, calculate the error (which is the prediction - the true value at each _n_-index). Store these values in a list called `errors`.
3. Square each element in `errors` (you should have a list of the same size with the squared elements instead of the differences)
4. Calculate the mean of the list created in step 3 (you should now have one number)
5. Take the square root of the mean created in step 4 using `np.sqrt()`. Store this in a variable called `rmse`
6. Print `RMSE: ` and the number stored in `rmse`. 
7. Return `rmse`.

### Your Function Should Return

```python
RMSE: 11.7997245731
```

# Problems 6-10

I bet you're ready to do some actual data work (versus defining functions and lists and all that!) Problems 6-10 deal with the [`sat_scores.csv`](./assets/sat_scores.csv) data, which is a list of average SAT scores from around the United States. The SAT is one of two major college entrance exams -- high school students are tested across Verbal (English language) and Math (mathematics). A score of 800 is perfect. The scores in this case are the average across a given state. We also include the Rate, which is the percent of eligible high school students in that state who took the test (if the rate is 100, that means every student who could take the test did).

We'll be importing this data using Python and using Python to provide some elementary understanding of this source of data.

As set-up to the next set of questions, you should do the following:

1. Import the data into Python using the `with` command that we've described before.
2. Store the values in the Verbal, Math, and Rate columns as three individual lists of values.

## Problem 6

Print out each state and its associated Verbal and Math scores as well as participation rate. The format should be similar to:

```python
PA: Verbal: 500, Math: 499, Rate: 71
```

In a print statement following this, answer the two following questions:

1. Are all states accounted for (and how do you know?)
2. Are there any rows that should be dropped (and why)

If there are any rows that should be dropped, do so at this point.

## Problem 7

Generate and print out the:

- Minimum
- Maximum 
- Mean
- Standard Deviation
- Median
- Mode 

of the Verbal, Math, and Rate columns. You may use NumPy and SciPy for this instead of rolling out your own.

## Problem 8

Generate and save to file a histogram of Verbal Scores. In a print statement, print out anything you find interesting or distinctive about the histogram.

## Problem 9

Generate and save to file a histogram of Math Scores. In a print statement, print out anything you find interesting or distinctive about the histogram.

## Problem 10

Generate and save to file a scatterplot of Participation Rate by either Math or Verbal Scores (your choice). Make sure that your axes are clearly labeled. In a print statement, discuss any interesting trends you see with regards to their relationship.
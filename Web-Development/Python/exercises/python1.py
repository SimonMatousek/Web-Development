## Task 1.1

# Given the string:
s = 'flask'

# Use indexing to print out the following:
# 'f'
print(s[0])
# 's'
print(s[3])
# 'ask'
print(s[2:5])
# 'las'
print(s[1:4])
# 'k'
print(s[4])
# Bonus: Use indexing to reverse the string])

## Task 1.2

# Given this nested list:
mylist = [3,7,[1,4,'hello']]

# Reassign "hello" to be "goodbye"
mylist[2][2] = "goodbye"
print(mylist[2][2])
## Task 1.3

# Using keys and indexing, grab the 'hello' from the following dictionaries:

d1 = {'simple_key':'hello'}
value1= d1.get('simple_key')
print(value1)

d2 = {'k1':{'k2':'hello'}}
value2 = d2.get('k1', {}).get('k2')
print(value2)

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}



## Task 1.4

# Use a set to find the unique values of the list below:
mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]
unique_values = set(mylist)
print(unique_values)


## Task 1.5

# You are given two variables:
age = 4
name = "Sammy"

# Use print formatting to print the following string:
"Hello my dog's name is Sammy and he is 4 years old"
print("hello my dog's name is "+name+" and he is "+ str(age)+" years old")

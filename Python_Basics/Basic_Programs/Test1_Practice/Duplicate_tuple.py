
# initialize list 
test_list = [(3, 4), (4, 5), (3, 4), 
			(3, 4), (4, 5), (6, 7)] 

# printing original list 
print("The original list : " + str(test_list)) 

# Get duplicate tuples from list 
# Using list comprehension + set() + count() 
res = list(set([ele for ele in test_list 
			if test_list.count(ele) > 1])) 

# printing result 
print("All the duplicates from list are : " + str(res)) 


test_list = [(3, 4), (4, 5), (3, 4), 
			(3, 4), (4, 5), (6, 7)] 




# Python3 code to demonstrate
# zipping lists of lists
# using map() + __add__

# initializing lists
test_list1 = [[1, 3], [4, 5], [5, 6]]
test_list2 = [[7, 9], [3, 2], [3, 10]]

# printing original lists
print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

# using map() + __add__
# zipping lists of lists
res = list(map(list.__add__, test_list1, test_list2))

# printing result
print("The modified zipped list is : " + str(res))

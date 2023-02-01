
"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here

import time
###


def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
  if right >= left:

    mid = left + (right - left)//2

        # If found at mid, then return it
    if mylist[mid] == key:
      return mid

        # Search the left half
    elif mylist[mid] > key:
      return _binary_search(mylist, key, left, mid-1)

        # Search the right half
    else:
      return _binary_search(mylist, key, mid + 1, right)

  else:
    return -1

"""
	Recursive implementation of binary search.

	Params:
	  mylist....list to search
	  key.......search key
	  left......left index into list to search
	  right.....right index into list to search

	Returns:
	  index of key in mylist, or -1 if not present.
"""   
	### TODO

	###

def test_binary_search():
  assert binary_search([11,12,13,14,15], 13) == 2
  assert binary_search([100,101,102,103,104], 105) == -1
  assert binary_search([1,2,3,4,5], 5) == 4
  assert binary_search([1,2,3,4,5], 1) == 0
  assert binary_search([1,2,3,4,5], 6) == -1
	### TODO: add two more tests here.
  
	###



def time_search(search_fn, mylist, key):
  start = time.time()
  search_fn(mylist, key)
  end = time.time()
  runtime = end - start
  return runtime*1000
  
  """
  def current_milli_time():
    return round(time.time() * 1000)
  """
    
  """
  Return the number of milliseconds to run this
	search function on this list.

	Note 1: `sort_fn` parameter is a function.
	Note 2: time.time() returns the current time in seconds. 
	You'll have to multiple by 1000 to get milliseconds.

	Params:
	  sort_fn.....the search function
	  mylist......the list to search
	  key.........the search key 

	Returns:
	  the number of milliseconds it takes to run this
	  search function on this input.
  """
	### TODO

	###

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
  final = []
  for size in sizes:
    mylist = range(int(size))
    time_linear = time_search(linear_search, mylist, key = -1)

    time_b = time_search(binary_search, mylist, key = -1)

    
    final.append([int(size), time_linear, time_b])
    
  return final
    
    
print(compare_search())


def print_results(results):
	 """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))
  """
  

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1

print_results(compare_search())

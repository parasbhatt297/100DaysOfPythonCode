a = 5 
b = 6
print(a and b)
print(a or b)
#Without Running Program , Tell what will be the Output of these Programs


""" 
Why does this happen?
1. a and b → 6
Python's and returns:
- The first falsy value, if one exists.
- Otherwise, the last value.
Here, a = 5 is truthy, so Python checks b. Since b = 6 is also truthy, it returns 6.
2. a or b → 5
Python's or returns:
- The first truthy value, if one exists.
- Otherwise, the last value.
Here, a = 5 is already truthy, so Python returns 5 without needing to evaluate b.
"""
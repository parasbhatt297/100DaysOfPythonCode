import random
a = 1 
b = 10
for i in range(3) :
      print("randint() function is Returning :",random.randint(a,b)) #Both a and b are included!
      print("randrange() function is Returning :",random.randrange(a,b)) #b is not included, only a is included!

age = 34
# print("You are "+age+" years old!")------->Error because int can't be concatinated with str
#Solution===>
print(f"You are {age} Years Old!")
print("You are",age,"Years Old!")
#Notice that ,age, gives space automatically
print(round(3.5))
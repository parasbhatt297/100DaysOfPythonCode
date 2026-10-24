print("Welcome to Python Pizza Deliveries!")
size = input("What Size Pizza you want? S , M , or L : ")
po = input("Do you want Pepperoni on your Pizza ? Y or N : ")
cheese = input("Do you want Extra Cheese on your Pizza ? Y or N : ")
bill = 0
if size=='S':
    if po=='Y' : bill+=2
    bill+=15
elif size=='M':
    if po=='Y' : bill+=3
    bill+=20
elif size=='L': 
    bill+=25 
    if po=='Y' : bill+=3
else :
    print("You typed a wrong Input! Please Try Again! ")
if cheese=='Y':bill+=1
print(f"Your final bill is ${bill}")

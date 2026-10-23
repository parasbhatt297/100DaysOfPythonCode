print("Welcome to rollercoaster!")
height = int(input("Enter you height : "))

if height>=120:
    age = int(input("What is Your Age ? "))
    print("You Can you Ride!")
    if age<12:
        print(f"You need to pay ${age/4} for Ride")
    elif age<18:
        print(f"You need to pay ${age/2} for Ride")
    else :
        print(f"You need to pay ${age} for Ride")
else :
    print("Sorry! You can't ride!")
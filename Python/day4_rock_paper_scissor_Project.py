import random
def setvalue():
    value = input("What do you Choose ? Type 0 for Rock , 1 for Paper or 2 for Scissors.\n")
    return value
value = setvalue()
while not(value=='0' or value=='1' or value=='2'):
    print("Please Choose Correct Option!")
    value = input()
computer = random.randint(0,2)
if value=='0':
   if computer==0 :
     print("You Chose : 🪨")
     print("Computer Chose :🪨")
     print("It's a Draw!")
   elif computer==1:
     print("You Chose : 🪨")
     print("Computer Chose :📄")
     print("You Lose!")
   else :
     print("You Chose : 🪨")
     print("Computer Chose :✂")
     print("You Win!") 
elif value=='1':
    if computer==0:
     print("You Chose :📄")
     print("Computer Chose :🪨")
     print("You Win!")
    elif computer==1:
     print("You Chose :📄")
     print("Computer Chose :📄")
     print("It's a Draw!")  
    else:
     print("You Chose :📄")
     print("Computer Chose :✂")
     print("You Lose!")  
elif value=='2':
  if computer==0:         
     print("You Chose :✂")
     print("Computer Chose :🪨")
     print("You Lose!")
  elif computer==1:
     print("You Chose :✂")
     print("Computer Chose :📄")
     print("You Win!") 
  else:
     print("You Chose :✂")
     print("Computer Chose :✂")
     print("It's a Draw!") 


     



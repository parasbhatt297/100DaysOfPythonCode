is_passed_the_exam = True if (input("Have You Passed our Exam? Y or N : ")=="Y") else False 
has_degree = True if (input("Do You have Your Degree? Y or N : ")=="Y") else False
has_certificates = True if (input("Do You have Your Certificates? Y or N : ")=="Y") else False
ans = 0
if is_passed_the_exam or has_degree or has_certificates:
    print("You are eligible to take Admission in Our college!")
    print("But We Need to check how many document you have!")
    if is_passed_the_exam :ans+=1
    if has_certificates : ans+=1
    if has_degree : ans+=1
    if ans == 3 :
        print("You Seems Very Responsible Student! We Allot you Section A")
    elif ans==2 :
        if is_passed_the_exam and has_certificates:
            print("Please Bring your degree As Soon as possible!")
        elif is_passed_the_exam and has_degree:
            print("Please bring Your Certificate As soon as Possible! ")
        else :
            print("Sorry! We can't give admission until You don't Pass the exam!")
    else :
        if is_passed_the_exam:
            print("Nice! This is Most Important Document! Don't Forget the other 2 Next Time!")
        else:
            print("Sorry! We can't give Admission until You don't  pass Exam!")
else :
    print("Sorry! You Need Atleast One Document to take Admission in Our College!")


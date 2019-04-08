def intro():
    print ("welcome to the Grading system That determines your grades \n ")
    print ("Please input your name:")
    username = input().upper()
    print("\n")
    print(f"Would you like to input your scores? {username} (y/n)")
    answer = input().lower()
    if answer == 'y':
        grades()
    else:
        print("Thank you and come again")

def grades():
    print("please input your scores")
    grades = input()
    new_grade = int(grades)
    if new_grade > 100:
        print("Please input a value under 100")
        grades()
    elif new_grade >= 70:
        print ("You have the grade A, Congrats")
    elif 70 > new_grade >= 60:
        print ("Your grade is B, You can achieve way more")
    elif 60 > new_grade >= 50  :
        print ("Your grade is C, Work Harder!")
    elif 50 > new_grade >=40:
        print ("our grade is D, Work Harder!")
    else:
        print ("You have a FAIL")
        print ("\n")
    
    print ("Would you like to input new scores? (y/n)")
    jibu=input().lower()
    if jibu == 'y':
        grad()
    else:
        print("Thank you for using our software!")

def grad():
    grades()

if __name__ == "__main__":
    intro()
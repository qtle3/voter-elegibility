# A program that determines eligibility to vote
# in the US elections.

def main() :
    print("This program will determine if you are eligible to vote in the US elections.")
    us = input("Are you a US citizen: yes/no? ")
    if us=="no" :
        print("You cannot vote.")
    else :
        age = float(input("What is your age? "))
        if age < 18 :
            print("You cannot vote.")
        else :
            state = input("Do you meet your state’s residency requirements: yes/no? ")
            if state=="no" :
                print("You cannot vote.")
            else :
                print("You can vote!")

main()

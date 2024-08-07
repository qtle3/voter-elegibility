# A program that determines eligibility to vote
# in the US elections.


def main():
    print(
        "This program will determine if you are eligible to vote in the US elections."
    )
    # Ask the user if they are a US citizen
    us = input("Are you a US citizen: yes/no? ")
    if us == "no":
        print("You cannot vote.")
        return
    # Ask the user for their age
    try:
        age = float(input("What is your age? "))
    except ValueError:
        print("Please enter a valid age.")
        return

    if age < 18:
        print("You cannot vote.")
        return

    # Ask the user if they meet their state's residency requirements
    state = input("Do you meet your state’s residency requirements: yes/no? ")
    if state == "no":
        print("You cannot vote.")
        return

    felony = input("Have you been convicted of a felony: yes/no? ")
    if felony == "yes":
        print("You cannot vote.")
        return

    registration = input("Are you registered to vote: yes/no? ")
    if registration == "no":
        print("You cannot vote.")
        return

    # Ask the user if they are registered to vote
    print("You can vote!")


main()

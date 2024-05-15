age=int(input("Enter your age:"))
voting_age=18
if(age>=voting_age):
    print("You are eligible to vote")
else:
    years_left=voting_age-age
    print("Not eligible to vote,you need to wait",years_left,"years")
    
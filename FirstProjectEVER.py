print("Hello! Welcome to the game I made!")

ans = input("Are you ready to play (yes/no)")
score = 0
total_q = 4

if ans.lower() == "yes":
    ans = input("1. What is my middle name?") 
    if ans.lower() == "blaze":
        score += 1
        print("Correct")
    else:
        print("Incorrect")


    ans = input("2. How old am I?") 
    if ans.lower() == "15":
        score += 1
        print("Correct")
    else:
        print("Incorrect")


    ans = input("3. What language was used to develop this game") 
    if ans.lower() == "python":
        score += 1
        print("Correct")
    else:
        print("Incorrect")


    ans = input("4. Who have I swam for in my life? ") 
    if ans.lower() == "york" or ans.lower() == "e-town" or ans.lower() == "dolphins":
        score += 1
        print("Correct")
    else:
        print("Incorrect")

print("Thank you for playing you got", score,"questions correct.") 
mark = (score/total_q) * 100

print("Mark,", mark)
print("Goodbye")

"""This program explores dialogues in Python
Written by Bec Alesech
2019"""

userName = input("What's your name?") #First dialogue

#Second dialogue
print("Hello " + userName)
response = input("Do you want to know my name")

#Check user response for third dialogue
if response == "y":
    print("It's Py!")
else:
    #print("fair enough")
    print("OK, let's move on")

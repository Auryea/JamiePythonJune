#Jamie's first Python Project | June 4th, 2022

#This program was built with Python version 3 in Visual Studio Code

#This simple program will review some of Jamie's interests in an interactive fashion

#Import Time Functions
from time import*
from tkinter.messagebox import YES
from datetime import*

#defining variables
name , occupation , location , age = "Jamie" , "Tech Professional" , "Fort Walton Beach, Florida" , 38
today = datetime.today()

#Countdown to program start
print( "\nStandby for the program to start..." )
i = 3
while i > -1:
    print( i )
    i -= 1
    sleep( 1 )

#Learn the user's name
user = input("\nWhat is your name?\n")

print("\nWelcome " + user + ", I'm so happy you are checking out my program.")

#Ask the user if they'd like to get to know me
question = input("\nWould you like to know who I am?\n\tPlease enter yes or no\n")

match question :
    case "yes" :
        print( "My name is " + name + " and I am a " + occupation + " I live in " + location + " and I am " + str(age) + " years old.")
    case "no" :
        print("\nAlright, " + user + " I won't bother you with that information")

intrests =  input("\nWhich interst would you like to hear about?\n\trunning, gardening, youtube, or cryptocurrency\n")

match intrests :
    case "running" :
        print("\nAlright, " + name + " has been running since age 12")
    case "gardening" :
        print("\nGardening is going well, sometimes it's hard to deal with the heat of summer here in " + location)
    case "youtube" :
        print("\nAnother thing that " + name + " likes to do is create YouTube content on two different channels")
    case "cryptocurrency" :
        print("\nOuch, this is a sore subject on this day, " + str(today) + " ,don't ya think?\nTruthfully, " + name + " started trying to learn programming in hopes to understand blockchain technology and ecosystems better.")        

sleep (2)

print("\nThank you," + user +  "for checking out my beginner program! I plan to continue learning and expanding my Python language skills.\nPlease feel free to reach out to me at jamielynn.greenwood@gmail.com")




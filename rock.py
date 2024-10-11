import random

# A list for computer to choose one of the options 
computer_list=["rock","paper","scissors"]

#while loop  with condition playing=true is provided for continuing the game
playing=True  
while playing:
    computer_input=random.choice(computer_list)   #computer randomly chooses from computer_list


# A users list is defined for checking and user insert one choice through keyboard
    users_list=["rock","paper","scissors","quit"]
    users_input=input("Enter rock,paper or scissors (or quit to Exit) : ")

#if user wants to exit from the game
    if users_input=="quit":
        playing = False
        print("Thank you for Playing")
        break

#if user insert an invalid option
    elif users_input not in users_list:
        print("You entered an  invalid option")

#if both choices from user and computer are same
    elif (users_input==computer_input):
        print("compter chose : ",computer_input)
        print("It's a Tie")    

# checking the conditions for user to win,if any of the condition satisfies user will win
    elif (users_input=="rock" and computer_input=="scissors") or (users_input=="scissors" and computer_input=="paper") or (users_input=="paper" and computer_input=="rock"):
        print("compter chose : ",computer_input)
        print("You win!")

#if any of the conditions in the above are not satisfied ,user will loose the game
    else:
        print("compter chose : ",computer_input)
        print("You Lose!!")    
         


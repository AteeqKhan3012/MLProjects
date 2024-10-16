# Week 2 Mini Project Problem 4
# 4. Advanced Number Guessing Game with Hints
# •	Description: Enhance the basic number guessing game by providing hints based on how close the guess is to the actual number
#  (e.g., "You're getting warmer" or "Too cold"). Use advanced conditional statements to handle the hint logic.
# •	Concepts Covered:
# •	Advanced use of if, else, and elif.
# •	Functions for encapsulating game logic.
# •	Git branching to add new features (e.g., hints).
# •	Stretch Goal: Add a scoring system based on the number of attempts


import random
guess = random.randint(1,50)
attempts=0
print("Welcome to the Number Guessing Game !")
print("I'm thinking of a number between 1 and 50")
def Guessing_game():
    global guess, attempts
    while attempts<11:
        user_guess=int(input("Enter the  number you think I'm thinking of:"))
        attempts+=1
       
        if user_guess < 0 or user_guess > 50:
            print("Invalid input. Please enter a number between 1 and 50")
            continue
        if user_guess < guess:
            print("You're getting warmer")
        elif user_guess > guess:
            print("You're getting colder")
        elif user_guess == guess:
            if attempts==1:
                print(f"Congratulations ! You won in just {attempts} attempt. Your score is 10/10 !")
            elif attempts>2 and attempts<5 :
                print(f"Congratulations ! You won in just {attempts}  attempts. Your score is 9/10 !")
            elif attempts>5 and attempts<8:
                print(f"Congratulations ! You won in just {attempts}  attempts. Your score is 8/10 !")
            elif attempts>8 and attempts<10:
                print(f"Congratulations ! You won in just {attempts}  attempts. Your score is 7/10 !")
            break
    else:
        print("Alas ! You've exceeded the number of attempts, as a result you've lost the game")
    answer=input("Would you like to play again?  (yes/no): ")
    if answer.lower() == "yes":
        Guessing_game()  
    elif answer.lower() == "no" :
        print("No Problem, May be it's not your day today")
    else:
        print("Invalid input. Please enter yes or no")
        print(answer)

Guessing_game()
                  


                        
              
            
            
      
    
    
    






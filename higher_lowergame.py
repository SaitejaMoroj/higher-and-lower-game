import random
from game_art import data

def get_data():
     return random.choice(data)
def prediction(details):
     x=details['name']
     y=details['follower_count']
     z=details['description']
     x_1=details['country']
     return {f"{x},{y},{z},{x_1}"}

def game():
     score=0
     account_a=get_data()
     account_b=get_data()
     while True:
        if account_a['follower_count']>account_b['follower_count']:
         winner="A"
        else:
            winner="B"
            print(f"Actual result: Account {winner} has more followers.")
        if guess==winner:
            score+=1
            print(f"Correct! Current score: {score}")
        else:
            print(f"Wrong! Final score: {score}")
            break
guess=input("enter the guess account A or B").lower()
game()
        
     
    
    
       

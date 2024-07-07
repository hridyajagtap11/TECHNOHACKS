import random

while True:
    user_choice=input("Enter a choice (rock, paper or scissors):")
    possible_actions=["rock","paper","scissors"]
    computer_choice=random.choice(possible_actions)
    print(f"You choose {user_choice}, Computer choose {computer_choice} ")

    if(user_choice==computer_choice):
        print(f"Both players selected {user_choice}, It's a Tie!")
    elif(user_choice=='rock'):
        if(computer_choice=='scissors'):
            print("Rock beats scissors, You win!")
        else:
            print("Paper beats rock, You lose!")     
    elif(user_choice=='paper'):
        if(computer_choice=='rock'):
            print("Paper beats rock, You win!")        
        else:
            print("Scissors beats paper, You lose!")          
    elif(user_choice=='scissors'):
        if(computer_choice=='paper'):
            print("Scissors beats paper, You win!")         
        else:
            print("Rock beats scissors, You lose!")  

    play_again=input("Do you want to play again?(y/n):")
    if(play_again.lower()!='y'):
        break          

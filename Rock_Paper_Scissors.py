# < instagram -> abbas_hz81 >
# < Rock paper scissors game >
import random 
choses = ['r' , 'p' ,'s' ]
choice_meaning = {
    'r' : 'Rock' ,
    'p' : 'Paper' ,
    's' : 'scissor'
}
user_score = 0
ai_score = 0
i = 0
while True :
    user_choice = input('select from Rock , Paper , Scissor : (r , p , s ) : ')
    ai_choice = random.choice(choses)
    if user_choice in choses :
        print(f'Youre chose is {choice_meaning[user_choice]} . ai choice is {choice_meaning[ai_choice]}.')
        if user_choice == ai_choice :
            print('Tie') 
        elif user_choice == 'r' and ai_choice == 's' :
            print('user+1')
            user_score += 1 
        elif user_choice == 'p' and ai_choice == 'r' :
            print('user+1')
            user_score += 1    
        elif user_choice == 's' and ai_choice == 'p' :
            print('user+1')
            user_score += 1
        else :
            print('Ai+1') 
            ai_score += 1  
    else : 
        print('invalid input !')
    if user_score == 5 or ai_score == 5 :
        break
    print(f'user score : {user_score} , Ai score : {ai_score}')
    print('\n' , '*'*10 , '\n' )
    i += 1
if user_score == 5 :
    print(f'User won! whit score -> {user_score}')
else :
    print('Ai won! whit score : {ai_score}')    
#Quiz type exercise where the user will be asked a question, evaluate it, and provide feedback
print("Test your geographical knowledge!")
print("Below is a test question")
User_answer = input("What is the capital of France?: ").lower() #This code is used to make the program case-insensitive.
#Otherwise, the program will only accept capitalized answers.
if User_answer == "paris":
    print("You're correct. The capital of France is Paris!")
else:
    print("Nice try. However, the capital of France is actually Paris.")
    print("That's okay, it's just a test quiz.")
#Extra question for Advanced Requirement    
capitals = {
    'United Kingdom': 'London',
    'Spain': 'Madrid',
    'Italy': 'Rome',
    'Denmark': 'Copenhagen',
    'Hungary': 'Budapest',
    'Portugal': 'Lisbon',
    'Georgia': 'Tbilisi',
    'Poland': 'Warsaw',
    'Netherlands': 'Amsterdam',
    'Romania': 'Bucharest'
}

user_score = 0
ques = len(capitals)
    
print("The official quiz has now started!")
    
    #This is where each country and capital pair are iterated
for country, correct_caps in capitals.items(): #This is where the questionnaire will collect the user's answers in every question
    answer = input(f"What is the capital of {country}? ").strip()
    #Where answer will be now evaluated through this code
    if answer.lower() == correct_caps.lower():
        print(f"Indeed, that is the capital of {country}")
        user_score +=1
    else:
        print(f"Unfortunately, that's incorrect. {correct_caps} is actually the capital of {country}")
        
print(f"Your score is: {user_score}/{ques}")
#Calculation of scores
final_per = (user_score/ques) * 100
print(f"Congrats, you've finally completed this mini quiz! Your final score is: {user_score} out of {ques}({final_per:.1f}%)")
    
if final_per == 100:
    print("Perfect score! You're must be an avid traveler, my friend")
elif final_per >= 80:
    print("That was fantastic! A little error here and there, but you still did amazing!")
elif final_per >= 60:
    print("That's not so bad! You know a few which is good enough.")
else:
    print("There's always room for improvement, so you're a-okay! Keep the room for knowledge open")
    
            
questions =[ 
{ 
        "question":"which is the capital city of Kenya?",
        "choices":["a.mombasa","b.waitethie","c.nairobi","d.thika"],
        "answer":"c"
    },
{
        "question":"who was the first president of Kenya?",
        "choices":["a.uhuru kenyatta","b.william ruto","c.raila odinga","d.jomo kenyatta"],
        "answer":"d"
},
{
        "question":"which president in kenya died while serving in power?",
        "choices":["a.uhuru kenyatta","b.william ruto","c.raila odinga","d.jomo kenyatta"],
        "answer":"d"
},
{
       "question":"In which year did Kenya gain independence?",
        "choices":["a.1963","b.1964","c.1965","d.1966"],
        "answer":"a"
},
{
        "question":"which country is landlocked in Africa?",
        "choices":["a.tanzania","b.kenya","c.somalia","d.uganda"],
        "answer":"d"
},     
]

score = 0

# go through each question
for q in questions:

    # show the question
    print(q["question"])

    # show the choices
    for choice in q["choices"]:
        print(choice)

    # get the user's answer
    user_answer = input("Enter your answer (a, b, c, d): ").lower()

    # compare the answer and update the score
    if user_answer == q["answer"]:
        print("Correct!")
        score = score + 1
    else:
        print("Wrong!")

# display the final score
print("Your final score is:", score, "out of", len(questions))

# give feedback based on the score
if score == len(questions):
    print("Excellent! You got all the questions right!")

elif score >= 3:
    print("Good job! You got more than half of the questions right!")

else:
    print("Try again! Keep practicing.")
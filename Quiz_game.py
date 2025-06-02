Quiz=[
   {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Rome", "D. Madrid"],
        "answer": "A"
    },
     {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Venus"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["A. Charles Dickens", "B. William Wordsworth", "C. William Shakespeare", "D. Mark Twain"],
        "answer": "C"
    },
    {
        "question": "What is 5 + 7?",
        "options": ["A. 10", "B. 11", "C. 12", "D. 13"],
        "answer": "C"
    }
]
score=0
print("Welcome to the Quiz Game!")
print("----------------------------")

for i,q in enumerate(Quiz,1):
    print(f"Questions {i} :{q['question']}")
    for option in q["options"]:
        print(option)
    answer = input("Your answer (A/B/C/D): ").strip().upper()
    if answer == q["answer"]:
        print(" Correct!")
        score += 1
    else:
        print(f" Wrong! The correct answer was {q['answer']}")

# Final score
print("\n----------------------------")
print(f"Your final score: {score}/{len(Quiz)}")

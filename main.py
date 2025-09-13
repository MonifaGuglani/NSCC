quiz = [
    {
        "question": "Q1. Which of the following is the correct format specifier to print an int in C ?",
        "options": ["A. %c" ,"B. %d" , "C. %f ","D. %lf"],
        "answer": "B"
    },
    {
        "question": "What is the size of int on most modern 32-bit systems?",
        "options": ["A. 2bytes", "B. 4bytes", "C. 8bytes", "D. depends upon compiler"],
        "answer": "B"
    },
    {
        "question": "Which operator is used to access the value at the address stored in a pointer?",
        "options": ["A. &", "B. *", "C. ->", "D. %"],
        "answer": "B"
    },
    {
        "question": "What will sizeof(char) return in C?",
        "options": ["A. 2", "B. 4", "C. 1", "D. Depends on system"],
        "answer": "C"
    },
    {
        "question": "Which keyword is used to exit from a loop in C?",
        "options": ["A. Stop", "B. Break", "C. Return", "D. Exit"],
        "answer": "B"
    }
]
print("***************************WELCOME**************************************")
print("                    ~INTERACTIVE QUIZ APP~                              ")
score = 0

for i,q in enumerate(quiz,1):
    print(f"Q{i}: {q['question']}")
    for option in q["options"]:
        print(option)
    answer = input("Your answer : ").upper()

    if answer == q["answer"]:
        print("CORRECT!")
        score += 1
        print(f"YOUR CURRENT SCORE IS:{score}/{5} ")
    else:
        print(f" WRONG , CORRECT ANSWER IS  {q['answer']}.\n")
        print(f"YOUR CURRENT SCORE IS :{score}/{5} ")
print(f"YOUR FINAL SCORE IS: {score}/{5}")
print("********************THANK YOU FOR THE INTERACTIVE QUIZ APP********************")

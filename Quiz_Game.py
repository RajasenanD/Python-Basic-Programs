questions = [
    {
        "prompt": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "prompt": "Which language is primarily spoken in London?",
        "options": ["A. Spanish", "B. Portuguese", "C. English", "D. French"],
        "answer": "C"
    },
    {
        "prompt": "What is the smallest prime number?",
        "options": ["A. 1", "B. 2", "C. 3", "D. 5"],
        "answer": "B"
    },
    {
        "prompt": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    }
]

def quiz_game(questions):
    score = 0
    for question in questions:
        print(question['prompt'])
        for option in question['options']:
            print(option)
        answer = input("Enter your answer (A , B, C OR D): ").upper()
        if answer == question['answer']:
            print('Hurray! Your are correct')
            score += 1
        else:
            print(f'Worng Answer.... correct answer is {question['answer']} \n ')
    print(f'Your score is {score} out of {len(questions)}')



quiz_game(questions)
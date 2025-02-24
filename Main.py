import time


def welcome_user():
    name = input("What is your name?").title()
    print(f"Welcome to Quiz for You's Matariki quiz, {name}"), time.sleep(1.5)
    print("There will be 10 Multi Choice questions to test your Matariki knowledge"), time.sleep(2.5)
    print("Good Luck!")



def ask_questions():
    welcome_user()
    for x in QUESTION_DATA:
        question = x["question"]
        options = x["options"]
        valid_answers = x["valid_answers"]

    print(question)
    for option in options:
        print(option)

    while True:
        questions_answer = input("What is your answer? (Or type quit to exit): ").strip().title()

        if questions_answer.lower() == "quit":
            print("Exiting the quiz, Goodbye!")
            break

        if questions_answer not in options:
            print("This is not a valid answer, please try again.")
            continue
        else:
            if questions_answer == valid_answers:
                print("Correct!")
                return False
            else:
                print("Incorrect!")
                return False




QUESTION_DATA =( {
      "question": "How many stars are in the Matariki star cluster",
      "options": ["9", "7", "12", "11", "8" ],
      "valid_answers": ("9", "7")
    },
                 {
      "question":"What is Matariki celebrating",
      "options": ["New Year", "End Of Winter", "Harvest", "", "" ],
      "valid_answers": "New Year"},
  )
def main():
    welcome_user()

    if __name__ == "__main__":
     main()

if not ask_questions()  == True:
 main()

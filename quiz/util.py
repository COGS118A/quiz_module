def record_quiz(quiz_id, option_id):
    """
    Helper method for recording the quiz to the local machine
    as a txt file so that we could grade it later on.
    """
    with open("record.txt", "a+") as f:
        output = {}
        output["quiz_id"] = quiz_id
        output["option_id"] = option_id
        f.write(str(output) + "\n")

def check_quiz_answer(quiz_id, correct_answer):
    """
    This method checks the correctness of someone's quiz response
    by looking at their records.txt

    param:
    quiz_id: str, the quiz_id that corresponding to the question we are checking
    correct_answer: int, the index of the correct answers.
    """
    correct = False
    with open("record.txt", "r") as f:
        record = f.read().split("\n")
        for i in range(len(record)-2, -1, -1):
            # For loop from the back to check the correctness of the choice
            dictRecord = eval(record[i])
            if dictRecord["quiz_id"] == quiz_id:
                correct_option_id = f"{quiz_id}-{correct_answer}"
                assert correct_option_id == dictRecord["option_id"], f"The correct option should be: {correct_option_id}, Your Answer: {dictRecord['option_id']}"
                correct = True
                break
        assert correct, f"No attempt have made for the question: {quiz_id}"

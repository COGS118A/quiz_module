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
        for i in range(len(record)-1, -1, -1):
            # For loop from the back to check the correctness of the choice
            try:
                dictRecord = eval(record[i])
            except SyntaxError:
                # make it robust to the record file that 
                # does not properly ends with a new line.
                continue
            if dictRecord["quiz_id"] == quiz_id:
                correct_option_id = f"{quiz_id}-{correct_answer}"
                assert correct_option_id == dictRecord["option_id"], f"The correct option should be: {correct_option_id}, Your Answer: {dictRecord['option_id']}"
                correct = True
                break
        assert correct, f"No attempt have made for the question: {quiz_id}"

def show_chosen_option(quiz_id):
    """
    This is a helper method for student to check their current selection
    of a specific quiz_id without checking the correctness of their choice.
    """
    chosen = False
    with open("record.txt", "r") as f:
        record = f.read().split("\n")
        for i in range(len(record)-1, -1, -1):
            # For loop from the back to check the correctness of the choice
            try:
                # robust to the format of record file.
                dictRecord = eval(record[i])
            except SyntaxError:
                continue
            if dictRecord["quiz_id"] == quiz_id:
                chosen = True
                print(f"Quiz: {quiz_id}, Chosen: {dictRecord['option_id']}")
                break
        if not chosen:
            print(f"Quiz: {quiz_id}, Chosen: NO RECORD FOUND")







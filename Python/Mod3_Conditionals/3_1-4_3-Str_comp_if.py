def tf_quiz (question , correct_ans ):
    correct_ans = input ("(T/F) Octupus have green blood: ")
    if correct_ans == "f":
        return "correct"
    else:
        return "incorrect"
quiz_eval = tf_quiz ( " Octupus have green blood" , " f " )
print("answer is" , quiz_eval)
class Validations:
    def does_get_questions_return_lists(self, questions):
        qn = isinstance(questions, list)
        if qn is True:
            return True
        else:
            return False

    def does_one_question_return_dict(self, question):
        qn = isinstance(question,dict)
        if qn is True:
            return True
        else:
            return False

    def is_post_question_a_string(self, question):
        if question.isdigit() is False:
            return True
        else:
            return False

    def is_post_answer_a_string(self, answer):
        if answer.isdigit() is False:
           return True
        else:
            return False
                       


import unittest
from validations import Validations

class TestValidations(unittest.TestCase):
    def setUp(self):
        self.val = Validations()

    def test_does_get_questions_return_lists(self):
        self.assertTrue([123,44155,667], self.val.does_get_questions_return_lists(["drrr","edrdtr","drdrd"]))

    def test_does_one_question_return_dict(self):
        self.assertTrue({'color': 'green'} ,self.val.does_one_question_return_dict({'yellow': 7}))   

    def test_is_post_question_a_string(self):
        self.assertTrue("abel", self.val.is_post_question_a_string("sdf gfe"))

    def test_is_post_answer_a_string(self):
       self.assertTrue("msldj", self.val.is_post_answer_a_string("drrr "))
       
        


if __name__=="__main__":
    unittest.main()
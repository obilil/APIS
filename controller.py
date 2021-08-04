from index import app
from flask import jsonify, request
from view import questions
from validations import Validations

validations = Validations()


@app.route('/api/v1/questions', methods=['GET'])
def get_allquestions():
    checking_all_questions = validations.does_get_questions_return_lists(questions)
    if checking_all_questions is True:
        return jsonify(questions), 200
    else:
        return("questions not found"), 400


@app.route('/api/v1/questions/<id>', methods=['GET'])
def get_question(id):
    if 'id' in request.args:
        id = int(request.args['id'])
    for question in questions:
        question_dict = validations.does_one_question_return_dict(question)
        if question_dict is True and (question['id'] == int(id)):
            return jsonify(question), 200
        else:
            return jsonify("question does not exist"), 400    
    
         

@app.route('/api/v1/questions', methods=['POST'])
def post_question():
    number_of_questions = len(questions)
    id = number_of_questions
    new_question = request.get_json()
    qn = new_question['question']
    is_string = validations.is_post_question_a_string(qn)
    if is_string is True:
        questions.append({'id': id, 'question': qn.strip(), 'answers': []})
        return jsonify(questions), 201
    else:
        return jsonify("bad string format"), 400    

@app.route('/api/v1/questions/<id>/answers', methods=['POST'])
def post_answer(id):
    if 'id' in request.args:
        id = int(request.args['id'])
    for question in questions:
        if question['id'] == int(id):
            question = question['question']
            new_answer = request.get_json()
            ans = new_answer['answer']
    is_string = validations.is_post_answer_a_string(ans)
    if is_string is True:        
        questions.append({'id': id, 'question': question, 'answers': [ans]}), 201
        return jsonify(questions)
    else:
        return jsonify("wrong format"), 400          

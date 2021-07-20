from flask import Flask, request, jsonify, json

# initializing the app
app = Flask(__name__)
app.config['DEBUG'] = True

# creating a small database
questions = [
{'id': 1, 'question': " qn1 what is your name?", 'answers': []},
{'id': 2, 'question': "qn2 where are you from?", 'answers': []},
{'id': 3, 'question': "qn3when were you born?", 'answers': []},
{'id': 4, 'question': "qn4 which schools did you attend to?", 'answers': []},
{'id': 5, 'question': "qn5 how many brothers do you have?", 'answers': []},
{'id': 6, 'question': "qn6 which country do you come from?", 'answers': []}
]

# writing the endpoints


@app.route('/api/v1/questions', methods=['GET'])
def get_allquestions():
    return jsonify(questions)


@app.route('/api/v1/questions/<id>', methods=['GET'])
def get_question(id):
    if 'id' in request.args:
        id = int(request.args['id'])
    for question in questions:
        if question['id'] == int(id):
            return jsonify(question)
    else:
        return jsonify({'mesg': 'question number not found'}), 


@app.route('/api/v1/questions', methods=['POST'])
def post_question():
    number_of_questions = len(questions)
    request_data = json.loads(request.data)
    qtn = request_data['question']
    qtn_id = number_of_questions + 1
    questions.append({'id': qtn_id, 'question': qtn, 'answers': []})
    return jsonify(questions)

@app.route('/api/v1/questions/<id>/answers', methods=['POST'])
def post_answer(id):
    if 'id' in request.args:
        id = int(request.args['id'])
    
    for question in questions:
        if question['id'] == int(id):
            answer_list = question['answers']
            request_data = json.loads(request.data)
            answer = request_data['answer']
            answer_list.append(answer)
    return jsonify(questions)

app.run(debug=True)

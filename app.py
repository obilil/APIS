from flask import Flask, request, jsonify

# initializing the app
app = Flask(__name__)
app.config['DEBUG'] = True

# creating a small database
questions = [{'id': 0, 'question': "yesssssssssssssssssssssssssssss", 'answers': []},
{'id': 1, 'question': "yesssssssssssssssssssssssssssss", 'answers': []},
{'id': 2, 'question': "yesssssssssssssssssssssssssssss", 'answers': []}
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
        return jsonify({'mesg': 'question number not found'}), 404



@app.route('/api/v1/questions', methods=['POST'])
def post_question():
    number_of_questions = len[questions]
    new_question = request.get_json()
    new_question['id'] = number_of_questions-1
    questions.append(request.get_json())
    return jsonify(new_question)


@app.route('/api/v1/questions/<id>/answers', methods=['POST'])
def post_answer(id):
    if 'id' in request.args:
        id = int(request.args['id'])

    for question in questions:
        if question['id'] == id:
            question = question.append(request.get_json())
    return jsonify(question)

app.run(debug=True)
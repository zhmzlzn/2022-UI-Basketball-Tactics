from flask import Flask, redirect, url_for
from flask import render_template
from flask import Response, request, jsonify

app = Flask(__name__)

quiz_questions = {
    "1": {
        "quiz_id": "1",
        "next_question": "2"
    },
    "2": {
        "quiz_id": "2",
        "next_question": "3",
        "question": "What kind of defense is shown in the video (2:00) below?",
        "answers": {
            "A": "Man-To-Man",
            "B": "Zone Defense"
        },
        "link": "https://www.youtube.com/embed/Eozrxys3UUM",
        "correctAnswer": "B"
    },
    "3": {
        "quiz_id": "3",
        "next_question": "4",
        "question": "Watch the video (0:15) and choose the correct tactic",
        "answers": {
            "A": "Horns",
            "B": "Pistol",
            "C": "Hammer"
        },
        "link": "https://www.youtube.com/embed/w5ThyZ69GO8?start=4",
        "correctAnswer": "C"
        }
}

numCorrectAnswers = 0

@app.route('/quiz/home')
def quizHome():
    return render_template('quizHome.html')


@app.route('/quiz/<quiz_id>')
def quiz(quiz_id):
    question = quiz_questions[quiz_id]
    if int(quiz_id) == 1:
        return render_template('quiz1.html', question=question)
    elif int(quiz_id) < 4:
        return render_template('quizMC.html', question=question)


@app.route('/count', methods=['GET', 'POST'])
def count():
    global numCorrectAnswers
    json_data = request.get_json()
    answer = json_data["answer"]
    if answer == "true":
        numCorrectAnswers += 1
    print(numCorrectAnswers)
    return str(numCorrectAnswers)


if __name__ == '__main__':
    app.run(debug=True)

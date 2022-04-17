from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


drag_data= {
    '4':{
        'id':'4',
        'action':'horn',
        'step':'1/2',
        'basketball': {'x':'270px','y':'255px'},
        'next':'5',
        'positions':[
            {
                'x':'35px',
                'y':'35px',
                'num':'2',
                'correct':'2'
            },
            {
                'x':'200px',
                'y':'70px',
                'num':'0',
                'correct':'0'
            },
            {
                'x':'150px',
                'y':'120px',
                'num':'0',
                'correct':'0'
            },
            {
                'x':'180px',
                'y':'180px',
                'num':'4',
                'correct':'0'
            },
            {
                'x':'240px',
                'y':'210px',
                'num':'0',
                'correct':'4'
            },
            {
                'x':'270px',
                'y':'240px',
                'num':'1',
                'correct':'1'
            },
            {
                'x':'240px',
                'y':'275px',
                'num':'0',
                'correct':'5'
            },
            {
                'x':'180px',
                'y':'300px',
                'num':'5',
                'correct':'0'
            },
            {
                'x':'150px',
                'y':'380px',
                'num':'0',
                'correct':'0'
            },
            {
                'x':'180px',
                'y':'420px',
                'num':'0',
                'correct':'0'
            },
            {
                'x':'35px',
                'y':'445px',
                'num':'3',
                'correct':'3'
            }

        ]
    },
    '5':{
        'id':'5',
        'action':'horn',
        'step':'2/2',
        'basketball': {'x':'270px','y':'255px'},
        'next':'6',
        'positions':[
            {
                'x':'35px',
                'y':'35px',
                'num':'2',
                'correct':'2'
            },
            {
                'x':'240px',
                'y':'210px',
                'num':'4',
                'correct':'0'
            },
            {
                'x':'270px',
                'y':'240px',
                'num':'1',
                'correct':'0'
            },
            {
                'x':'240px',
                'y':'275px',
                'num':'5',
                'correct':'0'
            },
            {
                'x':'35px',
                'y':'445px',
                'num':'3',
                'correct':'3'
            },
            {
                'x':'35px',
                'y':'120px',
                'num':'0',
                'correct':'0'
            },
            {
                'x':'120px',
                'y':'35px',
                'num':'0',
                'correct':'0'
            },
            {
                'x':'240px',
                'y':'110px',
                'num':'0',
                'correct':'5'
            },
            {
                'x':'320px',
                'y':'200px',
                'num':'0',
                'correct':'1'
            },
            {
                'x':'180px',
                'y':'270px',
                'num':'0',
                'correct':'4'
            }
        ]
    },
    '6':{
        'id':'6',
        'action':'pistol',
        'step':'1/2',
        'basketball': {'x':'270px','y':'255px'},
        'next':'7',
        'positions':[
            {
                'y':'35px',
                'x':'35px',
                'num':'3',
                'correct':'3'
            },
            {
                'x':'35px',
                'y':'445px',
                'num':'4',
                'correct':'4'
            },
            {
                'x':'270px',
                'y':'240px',
                'num':'1',
                'correct':'0'
            },
            {
                'y':'70px',
                'x':'200px',
                'num':'0',
                'correct':'0'
            },
            {
                'y':'130px',
                'x':'190px',
                'num':'0',
                'correct':'0'
            },
            {
                'y':'240px',
                'x':'170px',
                'num':'5',
                'correct':'0'
            },
            {
                'y':'280px',
                'x':'60px',
                'num':'0',
                'correct':'0'
            },
            {
                'y':'300px',
                'x':'180px',
                'num':'0',
                'correct':'5'
            },
            {
                'y':'380px',
                'x':'230px',
                'num':'0',
                'correct':'2'
            },
            {
                'y':'360px',
                'x':'210px',
                'num':'0',
                'correct':'1'
            }
        ]
    },
    '7':{
        'id':'7',
        'action':'pistol',
        'step':'2/2',
        'basketball': {'x':'380px','y':'210px'},
        'next':'end',
        'positions':[
            {
                'x':'35px',
                'y':'35px',
                'num':'3',
                'correct':'3'
            },
            {
                'x':'35px',
                'y':'445px',
                'num':'4',
                'correct':'4'
            },
            {
                'y':'300px',
                'x':'180px',
                'num':'5',
                'correct':'0'
            },
            {
                'y':'380px',
                'x':'230px',
                'num':'2',
                'correct':'0'
            },
            {
                'y':'360px',
                'x':'210px',
                'num':'1',
                'correct':'1'
            },
            {
                'y':'240px',
                'x':'270px',
                'num':'0',
                'correct':'0'
            },
            {
                'y':'210px',
                'x':'195px',
                'num':'0',
                'correct':'2'
            },
            {
                'y':'265px',
                'x':'85px',
                'num':'0',
                'correct':'5'
            },
            {
                'y':'35px',
                'x':'80px',
                'num':'0',
                'correct':'0'
            }
        ]
    }
}

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
    global numCorrectAnswers
    if quiz_id == "end":
        return render_template('quizRes.html', d=numCorrectAnswers)
    if int(quiz_id) == 1:
        return render_template('quiz1.html', question=quiz_questions[quiz_id])
    elif int(quiz_id) < 4:
        return render_template('quizMC.html', question=quiz_questions[quiz_id])
    elif int(quiz_id) < 9:
        return render_template('drag.html', d=drag_data[quiz_id])
    


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
   app.run(debug = True)

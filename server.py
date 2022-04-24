from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

drag_data= {
    '4':{
        'id':'4',
        'action':'horn',
        'step':'1/2',
        'basketball': '1',
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
        'basketball': '1',
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
                'y':'240px',
                'x':'110px',
                'num':'0',
                'correct':'5'
            },
            {
                'y':'320px',
                'x':'200px',
                'num':'0',
                'correct':'1'
            },
            {
                'y':'160px',
                'x':'270px',
                'num':'0',
                'correct':'4'
            }
        ]
    },
    '6':{
        'id':'6',
        'action':'pistol',
        'step':'1/2',
        'basketball': '1',
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
                'y':'395px',
                'x':'245px',
                'num':'0',
                'correct':'2'
            },
            {
                'y':'370px',
                'x':'220px',
                'num':'0',
                'correct':'1'
            },
            {
                'y':'420px',
                'x':'180px',
                'num':'2',
                'correct':'0'
            }
        ]
    },
    '7':{
        'id':'7',
        'action':'pistol',
        'step':'2/2',
        'basketball': '2',
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
                'y':'395px',
                'x':'245px',
                'num':'2',
                'correct':'0'
            },
            {
                'y':'370px',
                'x':'220px',
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
        "question": "What kind of defense is shown in the video below?",
        "answers": {
            "A": "Man-To-Man",
            "B": "Zone Defense"
        },
        "link": "/static/videos/p2.mp4",
        "correctAnswer": "B"
    },
    "3": {
        "quiz_id": "3",
        "next_question": "4",
        "question": "Watch the video and choose the correct tactic",
        "answers": {
            "A": "Horns",
            "B": "Pistol",
            "C": "Hammer"
        },
        "link": "/static/videos/p3.mp4",
        "correctAnswer": "C"
        }
}

numCorrectAnswers = 0

subTitleData = {
    "1":{
        "id": 1,
        "name": "Basketball Court"
    },
    "2":{
        "id": 2,
        "name": "Basketball Positions"
    },
}

titleData = {
    "1": {
         "id": 1,
         "name": "Basic Knowledge"
    },
    "2": {
         "id": 2,
         "name": "Defense",
         "descriptionOne":"-The man-to-man defense involves all 5 defensive players on the court being allocated one opposition player who they’re accountable for defending whenever they’re on defense.",
         "descriptionTwo":"-Zone defense is a type of defense, used in team sports, which is the alternative to man-to-man defense; instead of each player guarding a corresponding player on the other team, each defensive player is given an area (a zone) to cover."
    }
}


learn_tactic = {
    "3": {
        "pre_link": "/learn/2",
        "next_link": "/learn/4",
        "title": "Offense Tactic: Hammer Action",
        "description": "The essence of the 'hammer' action is that when the strong side (the side with the ball) cooperates with the ball, the weak side (the side without the ball) is also covering. Open weakside corners shoot 3-pointers.",
        "video_link": "/static/videos/hammer.mp4",
        "image": "/static/pic/hammer_board.png"
    },
    "4": {
        "pre_link": "/learn/3",
        "next_link": "/learn/5",
        "title": "Offense Tactic: Horns Action",
        "description": "A half-court set in which two bigs set ball-screens on both sides of the ball-handler with one big rolling and the other popping.",
        "video_link": "/static/videos/horns.mp4",
        "image": "/static/pic/horns_board.png"
    },
    "5": {
        "pre_link": "/learn/4",
        "next_link": "/quiz/home",
        "title": "Offense Tactic: Pistol Action",
        "description": "1 passes the ball to 2, then comes down to screen for the ball handler, 5 sets a screen near the free throw line, and then goes down. The 2 can make the most appropriate offensive choice based on the opponent's defense: he can drive the shot himself, or pass to a down center.",
        "video_link": "/static/videos/pistol.mp4",
        "image": "/static/pic/pistol_board.png"
    }
}

# ROUTES

@app.route('/')
def hello_world():
   return render_template('home.html')

@app.route('/learn/<learn_id>')
def learn_page(learn_id):
    if learn_id == '1':
        return render_template('learn.html', subTitleData = subTitleData)
    if learn_id == '2':
        return render_template('learn2.html', titleData = titleData)

    tactic = learn_tactic[learn_id]
    return render_template('learn_offense.html', tactic=tactic)

@app.route('/quiz/home')
def quizHome():
    return render_template('quizHome.html')

@app.route('/quiz/<quiz_id>')
def quiz(quiz_id):
    global numCorrectAnswers
    if quiz_id == "end":
        return render_template('quizRes.html', d=numCorrectAnswers)
    if int(quiz_id) == 1:
        return render_template('quiz1.html', question=quiz_questions[quiz_id], score=numCorrectAnswers)
    elif int(quiz_id) < 4:
        return render_template('quizMC.html', question=quiz_questions[quiz_id], score=numCorrectAnswers)
    elif int(quiz_id) < 9:
        return render_template('drag.html', d=drag_data[quiz_id], score=numCorrectAnswers)


@app.route('/review/<review_id>')
def review(review_id):
    if int(review_id) == 1:
        return render_template('review1.html', subTitleData=subTitleData)
    elif int(review_id) == 2:
        return render_template('review2.html', titleData=titleData)
    elif int(review_id) == 3:
        return render_template('reviewOffense.html', tactic=learn_tactic["3"])
    elif int(review_id) < 6:
        return render_template('reviewOffense.html', tactic=learn_tactic["4"])
    elif int(review_id) < 8:
        return render_template('reviewOffense.html', tactic=learn_tactic["5"])

@app.route('/count', methods=['GET', 'POST'])
def count():
    global numCorrectAnswers
    json_data = request.get_json()
    # answer = json_data["answer"]
    # if answer == "true":
    #     numCorrectAnswers += 1
    newScore = json_data["score"]
    numCorrectAnswers = newScore
    print(numCorrectAnswers)
    return str(numCorrectAnswers)


if __name__ == '__main__':
   app.run(debug = True)

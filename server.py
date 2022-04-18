from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


subTitleData = [
    {
        "id": 1,
        "name": "Basketball Court"
    },
    {
        "id": 2,
        "name": "Basketball Positions"
    },
]
titleData = [
                {
                    "id": 1,
                    "name": "Basic Knowledge"
                },
                {
                    "id": 2,
                    "name": "Defense"
                },
           ]

learn_tactic = {
    "3": {
        "pre_link": "/learn/2",
        "next_link": "/learn/4",
        "title": "Offense Tactic: Hammer Action",
        "description": "The essence of the 'hammer' action is that when the strong side (the side with the ball) cooperates with the ball, the weak side (the side without the ball) is also covering. Open weakside corners shoot 3-pointers.",
        "video_link": "https://www.youtube.com/embed/PwLQUsglKf4",
        "image": "/static/pic/hammer_board.png"
    },
    "4": {
        "pre_link": "/learn/3",
        "next_link": "/learn/5",
        "title": "Offense Tactic: Horns Action",
        "description": "A half-court set in which two bigs set ball-screens on both sides of the ball-handler with one big rolling and the other popping.",
        "video_link": "https://www.youtube.com/embed/FD08YxtV4q8",
        "image": "/static/pic/horns_board.png"
    },
    "5": {
        "pre_link": "/learn/4",
        "next_link": "/",
        "title": "Offense Tactic: Pistol Action",
        "description": "1 passes the ball to 2, then comes down to screen for the ball handler, 5 sets a screen near the free throw line, and then goes down. The 2 can make the most appropriate offensive choice based on the opponent's defense: he can drive the shot himself, or pass to a down center.",
        "video_link": "https://www.youtube.com/embed/I-cpRQxlBbo",
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


if __name__ == '__main__':
   app.run(debug = True)





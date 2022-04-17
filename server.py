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
                'num':'3',
                'correct':'3'
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
            },

        ]
    }
}



# ROUTES
@app.route('/')
def hello_world():
   return render_template('drag.html', d=drag_data['4'])

@app.route('/quiz/<id>')
def quiz(id=None):
    return render_template('drag.html', d=drag_data[id])
    



if __name__ == '__main__':
   app.run(debug = True)

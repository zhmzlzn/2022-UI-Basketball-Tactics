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

# ROUTES



@app.route('/')
def hello_world():
   return render_template('home.html')


@app.route('/learn/1')
def hello_name():
    return render_template('learn.html', subTitleData = subTitleData)

@app.route('/learn/2')
def second():
   return render_template('learn2.html', titleData = titleData)




if __name__ == '__main__':
   app.run(debug = True)





from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)




# ROUTES



@app.route('/')
def hello_world():
   return render_template('home.html')


@app.route('/learn/<id>')
def hello_name(id=1):
    return render_template('learn.html', id = id)




if __name__ == '__main__':
   app.run(debug = True)





from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)




# ROUTES



@app.route('/')
def hello_world():
   return render_template('home.html')


@app.route('/learn/1')
def hello_name():
    return render_template('learn.html')

@app.route('/learn/2')
def second():
   return render_template('learn2.html')




if __name__ == '__main__':
   app.run(debug = True)





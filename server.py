from flask import Flask,render_template

app = Flask(__name__)

@app.route('/<number>')
def single_board(number):
    return render_template('index.html', number = int(number))


@app.route('/<num1>/<num2>')
def index(num1,num2):
    return render_template('index2.html', num1 = int(num1), num2 = int(num2))

if __name__=="__main__":
    app.run(debug=True)

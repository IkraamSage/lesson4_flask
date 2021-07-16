from flask import Flask, render_template

app = Flask(__name__)
student_ages = {"Naeemah": 20, "godwin": 28, "Thapelo": 27, "Jason": 23, "Ikraam": 21}

@app.route('/<name>')
def homepage(name):
    return render_template("homepage.html", name=name, student_ages=student_ages)

@app.route('/loopy/<int:number>')
def loopy(number):
    return render_template('number.html', number=number)

if __name__ == '__main__':
    app.debug = True
    app.run()
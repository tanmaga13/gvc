from flask import Flask, request, render_template
from datetime import datetime

app = Flask(__name__)
mongodb+srv://tanmaga02:tranmay13@mytcluster.gdrwtvc.mongodb.net/?
appName=MyTCluster

@app.route('/')
def home():
    day_of_week = datetime.today().strftime('%A')
    current_time = datetime.now().strftime('%H:%M:%S')
    return render_template('index.html', day_of_week=day_of_week, current_time=current_time)

@app.route('/submit', methods = ['POST'])
def submit():
    name = request.form.get('name')
    print(request.args)
    return "Hello " + name + '!'


if __name__ == '__main__':
    app.run(debug=True)
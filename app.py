from flask import Flask, request, render_template
from datetime import datetime
from dotenv import load_dotenv
import os
import pymongo

load_dotenv()
MONGO_URL = os.getenv("MONGO_URL")
client = pymongo.MongoClient(MONGO_URL)
db = client.MyTCluster
collection = db['flask-assignment']

app = Flask(__name__)

@app.route('/')
def home():
    print("Welcome to FLASK!!!")
    current_time = datetime.now().strftime('%H:%M:%S')
    return render_template('index.html', day_of_week=day_of_week, current_time=current_time)

@app.route('/submittodoitem', methods = ['POST'])
def submittodoitem():
    form_data = dict(request.form)
    collection.insert_one(form_data)
    return "Data Submitted Successfully"

if __name__ == '__main__':
    app.run(debug=True)
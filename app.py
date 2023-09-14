from flask import Flask, request, jsonify, render_template
import sqlite3
from chat import get_response
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.get("/")
def home():
    return render_template("base.html")
connect = sqlite3.connect('database.db')
connect.execute(
    'CREATE TABLE IF NOT EXISTS GRIEVANCES (description TEXT, name TEXT)')
@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    message = get_response(text)
    print(message)
    # with sqlite3.connect("database.db") as users:
    #         cursor = users.cursor()
    #         cursor.execute("INSERT INTO GRIEVANCES \
    #         (description,name) VALUES (?,?)",
    #                        (text,"User"))
    #         users.commit()
    return jsonify({"answer": message})

@app.route('/messages')
def messages():
    connect = sqlite3.connect('database.db')
    cursor = connect.cursor()
    cursor.execute('SELECT * FROM GRIEVANCES')
  
    data = cursor.fetchall()
    return render_template("grievances.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)

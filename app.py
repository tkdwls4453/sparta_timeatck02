from datetime import timedelta
from datetime import datetime

from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.test

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detail/<idx>')
def detail(idx):
    # todo
		return

@app.route('/articleList', methods=['GET'])
def get_article_list():
    article_list = list(db.test.find({},{'_id':False}))

    for article in article_list:
        article['reg_date'] = article['reg_date'].strftime('%Y.%m.%d %H:%M:%S')

    return jsonify({"article_list": article_list})

# Create
@app.route('/article', methods=['POST'])
def create_article():
    title_receive = request.form['title']
    content_receive = request.form['content']
    pw_receive = request.form['pw']
    now = datetime.now()
    if len(list(db.test.find({}, {"_id": False}))) == 0:
        idx = 0
    else:
        idx = int(list(db.test.find({}, {"_id": False}))[-1]['idx']) + 1

    doc ={
        'idx' : idx,
        'title': content_receive,
        'content': content_receive,
        'pw' : pw_receive,
        'read_count': 0,
        'reg_date': now
    }
    db.test.insert_one(doc)
    return {"result": "success"}

# Read
@app.route('/article', methods=['GET'])
def read_article():
    article = list(db.test.find({},{'_id':False}))
    return jsonify({"article": article})

# Update
@app.route('/article', methods=['PUT'])
def update_article():
    # todo
    idx_receive = request.form['idx']

    return {"result": "success"}

# Delete
@app.route('/article', methods=['DELETE'])
def delete_article():
    # todo
    return {"result": "success"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
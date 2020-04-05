from flask import Flask
import DBConnector
import time

app = Flask(__name__)


@app.route('/')
def index():
  return 'Server Works!'
  
@app.route('/sos/<post_id>')
def record_sos(post_id):
  doc = {time.time() : post_id}
  DBConnector.push_data(doc)
  return "recorded" + str(doc)


@app.route('/all/')
def all():
    return DBConnector.get_all() 
from calendar import month
from flask import Flask, jsonify, render_template, request
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from dotenv import load_dotenv
from nltk.tokenize import word_tokenize
import nltk
from statistics import mean
from flask_migrate import Migrate
from textblob import TextBlob
import psycopg2

app = Flask(__name__)

try:
    con = psycopg2.connect(database="postgres", user="postgres", password="Rakhi@22072001", host="db.dalprpwxckshhsaisuxi.supabase.co", port="6543")
except:
    print('e')
print("Database opened successfully")

# class college(db.Model):
#     __tablename__ = 'college'

#     institute_id = db.Column(db.String(), primary_key=True)
#     name = db.Column(db.String())
#     tlr = db.Column(db.Integer())
#     rpc = db.Column(db.Integer())
#     go = db.Column(db.Integer())
#     oi = db.Column(db.Integer())
#     perception = db.Column(db.Integer())
#     city = db.Column(db.String())
#     state = db.Column(db.String())
#     rank = db.Column(db.Integer())
#     department= db.Column(db.String())
#     fees = db.Column(db.Integer())

#     def __init__(self, institute_id, name, tlr, rpc, go, oi, perception, city, state, rank, department, fees):
#         self.name = name
#         self.institute_id = institute_id
#         self.name = name
#         self.tlr = tlr
#         self.rpc = rpc
#         self.go = go
#         self.oi = oi
#         self.perception = perception
#         self.city = city
#         self.state = state
#         self.rank = rank
#         self.department = department
#         self.fees = fees

# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# load_dotenv()

# app = Flask(__name__)

# filename=''
# filename_for_database=''
# products=set

@app.route('/')
def index():
    con = psycopg2.connect(database="postgres", user="postgres", password="Rakhi@22072001", host="db.dalprpwxckshhsaisuxi.supabase.co", port="6543")
    cursor=con.cursor()
    cursor.execute('SELECT * FROM college;')
    col=cursor.fetchall()
    return col

@app.route('/get-data', methods=['GET','POST'])
def index2():
    fee=request.form.get('fee')
    state=request.form.get('state')
    city=request.form.get('city')
    course=request.form.get('course')
    ranking=request.form.get('ranking')
    check={'fee':0,'state':0,'city':0,'course':0,'ranking':0}
    s='SELECT * FROM college WHERE '
    if fee:
        fee_limit=fee.split('-')
        fee_lower=int(fee_limit[0])
        fee_upper=int(fee_limit[1])
        s=s+'fees < '+ fee_upper+' and fees > '+fee_lower
    elif state:
        s=s+' state like '+ state
    elif city:
        s=s+' city like '+ city
    elif course:
        s=s+' course like '+ course
    con = psycopg2.connect(database="postgres", user="postgres", password="Rakhi@22072001", host="db.dalprpwxckshhsaisuxi.supabase.co", port="6543")
    cursor=con.cursor()
    cursor.execute('SELECT * FROM college;')
    col=cursor.fetchall()
    return True


if __name__ == "__main__":
    app.run(debug=True)

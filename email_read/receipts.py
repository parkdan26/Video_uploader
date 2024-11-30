from flask import Flask, render_template, request
from twilio.rest import Client
from datetime import date
from_Number = '#'

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("picture.html")

@app.route('/', methods=['GET']) 
def foo():
    data = request
    account_sid = 'ACCOUNT'
    auth_token = 'AUTH TOKEN'
    client = Client(account_sid, auth_token)
    now = datetime.now()
    if data is not None:
        message = client.messages.create(
        
          from_=from_Number,
          body = now.strftime("%d/%m/%Y %H:%M:%S"),
          to = from_Number
        )



if __name__ == '__main__':
    app.run()
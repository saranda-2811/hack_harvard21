from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import os
import subprocess

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '').lower()
    resp = MessagingResponse()
    msg = resp.message()
    responded = False
    if 'quote' in incoming_msg:
        # return a quote
        r = requests.get('https://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{data["content"]} ({data["author"]})'
        else:
            quote = 'I could not retrieve a quote at this time, sorry.'
        msg.body(quote)
        responded = True
    if 'cat' in incoming_msg:
        # return a cat pic
        msg.media('https://cataas.com/cat')
        responded = True
    if 'hi' in incoming_msg:
        msg.body('Hi! I was created at HackHarvard21, and I will help you with school and other random stuff.')
    if 'transcribe' in incoming_msg:
        #transcribe from given youtube link
        lnk = incoming_msg[11:]
        os.putenv("LNK", lnk)
        os.system("test.bat")

    if not responded:
        msg.body('I only know about famous quotes and cats, sorry!')
    return str(resp)


if __name__ == '__main__':
    app.run()
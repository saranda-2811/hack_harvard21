from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import os
import subprocess
import wikipedia
import glob as glob

app = Flask(__name__)


@app.route('/bot', methods=['POST']) 
def bot():
    incoming_msg = request.values.get('Body', '')
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
        msg.body('Hi! I am a bot named Vixt, and I was created at HackHarvard21, and I will help you with school and other random stuff!')
        responded = True
    if 'transcribe' in incoming_msg:
        #transcribe from given youtube link
        lnk = incoming_msg[11:]
        os.putenv("LNK", lnk)
        os.system("test.bat")  #invoking batch file to run cli.py which will save transcripted .txt file in directory
    
        txtfiles=glob.glob("*.txt")

        with open(txtfiles[0]) as f: 
            contents = f.read() 
        #msg.body(contents) 
        msg.body(contents)

        #removing text file if user wants to transcribe again, to avoid confusion while reading files later
        os.remove(txtfiles[0])  
        responded = True

    if 'wiki' in incoming_msg:
        m = incoming_msg[5:] 
        #try:
        m = str(m) 
        ans = wikipedia.summary(m) 
        #except:
        #ans = 'Request was not found. Be more specific?'
        #msg.body(ans) 
        msg.body(ans)  
        responded = True

    return str(resp)


if __name__ == '__main__':
    app.run()
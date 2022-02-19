import slack
import os
from pathlib import Path
from flask import Flask, request, Response, make_response
from slackeventsapi import SlackEventAdapter
from dotenv import load_dotenv
import time
import json
import datetime
import pyodbc
import psycopg2

import modalReturner as mR
import shortcuts as st

app = Flask(__name__)
#creating flask's 'Application Object' 
#print ("Debug msg: App object created")

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)
slack_event_adapter = SlackEventAdapter(os.environ['SIGNING_SECRET'],'/slack/events', app)
client = slack.WebClient(token=os.environ['SLACK_TOKEN'])
BOT_ID = client.api_call("auth.test")['user_id']
#loading environment files
#print ("Debug msg: .env loading done")

@app.route('/shortcuts', methods=['POST'])
def shortcuts ():
    data = json.loads(request.form.get('payload'))
    return st.sortShortcut (client, data)
# The '/shortcut' endpoint redirects the request to the shortcuts.py file (imported as st), which handles all shortcut requests using the sortShortcut function.
# This makes the code easier to increment with new shortcuts, if need be.

if __name__ == "__main__":
    app.run(debug=True)
#automaticaly reruns webserver





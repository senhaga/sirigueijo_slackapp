from datetime import datetime
import pyodbc
from dotenv import load_dotenv
import os
import psycopg2
import json


def applyFine(client, data):
    #print ("Debug msg: Beggining fineApplier")
    #print (data)
    
    state = data['view']['state']['values']
    #print (state)
    #print ("Debug msg: state printed^\n")
   
    stValues=[]
    for value in state.values():
        stValues.append(value)
    # Organizing the relevant data in a not-so-neat list
    
    #for value in stValues:
    #    print (value)
    #print ("Debug msg: stValues prints^\n")


    fined_users_ID = stValues[0]['multi_users_select-action']['selected_users']
    custom_call = "@" + str(stValues[1]['plain_text_input-action']['value']).replace(" ", "")
    fine_reason = str(stValues[2]['plain_text_input-action']['value'])

    #print(fined_users_ID, custom_call, fine_reason)

    for x in range(len(fined_users_ID)):
        fined_users_ID[x] = "<@" + fined_users_ID[x] + ">"

    #print (fined_users_ID)
    
    fined_users_ID.append(custom_call)
    tuple_users = tuple(fined_users_ID)
    parsed_users = ", ".join(tuple_users)

    #print (parsed_users)

    doc = open('fineMessageBlocks.json', 'r')
    messageTemplate = json.loads(doc.read())
    doc.close()
    #print (messageTemplate)

    transfer =  messageTemplate["blocks"][0]["text"]["text"]
    transfer = transfer.format(parsed_users)
    messageTemplate["blocks"][0]["text"]["text"] = transfer
    #print(messageTemplate["blocks"][0]["text"]["text"],"\n")
   
    transfer = messageTemplate["blocks"][1]["text"]["text"]
    transfer = transfer.format(fine_reason)
    messageTemplate["blocks"][1]["text"]["text"] = transfer
    #print (messageTemplate["blocks"][1]["text"]["text"],"\n")

    print (messageTemplate["blocks"])

    messageReady = json.dumps(messageTemplate["blocks"])
    print (messageReady)

    channel_id = os.environ['SLACK_CHANNEL_ID']
    # The payload do not give the id of the channel from which the shortcut was prompted. 
    # I'll hardcode this as an environment variable for now, but I'm aware it is a dumb solution. My bad.

    client.chat_postMessage(channel = channel_id, blocks = messageReady)


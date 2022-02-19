import modalListener as mL
import modalReturner as mR
from flask import Response

def sortShortcut(client, data):
    trigger_id = data.get('trigger_id')
    shortcut = data.get("callback_id")
    type = data.get('type')
    #print (data)

    if type == "view_submission":
        #print (data['view'].keys())
        mL.listenModal(client, data)
    #If the payload is a submission from a modal, this will send it to the file modalListener, imported here as mL, which will extract the data.

    elif type == "block_actions":
        print ("Block actions is happening")
        pass
    #I don't know why this is here, but I believe my past self had a reason to add it, so I'm leaving it alone

    elif shortcut == 'sirigueijo_fine':
        mR.newFine(client, trigger_id)
    #This is where the request for the modal is captured and sent to it's rightful handling file: modalReturner, here imported as mR.

    else:
        print ("shortcut not yet implemented")
        print (data)

    return Response(), 200
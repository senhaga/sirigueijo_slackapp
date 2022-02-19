from flask import Response
import fineApplier as fA

def listenModal(client, data):
    #print("Debug msg: '\n' + "Beginning modalListener()")
    #print (data)
    #print ("Debug msg: Data printed^\n")
    
    if data['view']['title']['text'] == 'Seu Sirigueijo - Multar':
        return fA.applyFine(client, data)
    # This is probably NOT the best way to identify a form post, but I don't know a better way to do it, for now.
    # Given the way this is implemented, modals for different shortcuts CANNOT have the same title, or else their forms will be handled here as well. My bad.
    # Update - I believe this can be better done using the view id
    else:
        return Response(), 400
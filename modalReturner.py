from flask import Flask, request, Response, make_response
import json
import os


def newFine(client, tg_id):
    #print('\n' + "Beginning mR.newFine()")
    doc = open('newFineModal.json', 'r')
    modal = json.loads(doc.read())
    doc.close()
    client.views_open(token=os.environ['SLACK_TOKEN'], trigger_id=tg_id, view=modal)
    return Response(), 200
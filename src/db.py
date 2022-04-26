# This module contains all database interfacing methods for the funds aplication

import os
import json

from flask import Flask
from flask import jsonify
from distutils.log import error
from urllib import response
from bson import json_util
from flask_pymongo import pymongo


# Connection configuration
try:
    #user  = os.environ['user']
    #pwd  = os.environ['pwd']
    #driver = os.environ['driver']
    user  = 'Kevin'
    pwd  = 'BtgPactual2022'
    driver= 'cluster0.jw87x.mongodb.net/myFirstDatabase?retryWrites=true'
except: 
    user  = ''
    pwd  = ''
    driver= ''


CONNECTION_STRING = f"mongodb+srv://{user}:{pwd}@{driver}"
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('db-funds')


# Inserts a fund in the funds collection
def create_fund(fund_id, name, value_min, money,  category, date):
    
    fund_doc = {"_id":fund_id, "name":name, "value_min":value_min, "money":money, "category":category, "date":date}
    response = db.funds.insert_one(fund_doc)
    
    return response



# Given a Fund ID, return the fund with that ID
def get_fund(id):
    
    fund = db.funds.find({"_id": id}).limit(1)
    response = json_util.dumps(fund)
    
    return response


# Return alls funds
def get_funds():
    
    funds = db.funds.find()
    response = json_util.dumps(funds)
    return response


# Updates the fund in the funds collection
def update_fund(fund_id, name, value_min, money, category, date):

    response = db.funds.update_one(
        { "_id": fund_id },
        { "$set": { "name":name, "value_min":value_min, "money":money, "category":category, "date":date } }
    )

    return response


# Gives a fund Id, deletes that fund 
def delete_fund(fund_id):

    response = db.funds.delete_one({ "_id": fund_id})
    
    return response


# Inserts a client in the clients collection
def create_client(client_id, name, value, date, funds, trans):
    
    client_doc = {"_id":client_id, "name":name, "value":value, "date":date, "funds":funds, "trans":trans}
    response = db.clients.insert_one(client_doc)
    
    return response


# Given a client ID, return the client with that ID
def get_client(id):
    
    client = db.clients.find({"_id": id}).limit(1)
    response = json_util.dumps(client)
    
    return response


# Return alls clients
def get_clients():
    
    clients = db.clients.find()
    response = json_util.dumps(clients)
    return response


# Updates the client in the clients collection
def update_client(client_id, name, value, date, funds, trans):

    response = db.clients.update_one(
        { "_id": client_id },
        { "$set": { "name":name, "value":value, "date":date, "funds":funds, "trans":trans } }
    )

    return response


# Gives a client Id, deletes that client 
def delete_client(client_id):

    response = db.clients.delete_one({ "_id": client_id})
    
    return response
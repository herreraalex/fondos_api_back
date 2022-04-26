from email import message
import json
import logging
from turtle import position

from flask import Flask
from flask import request
from datetime import datetime
from db import  create_fund, get_fund, get_funds, update_fund, delete_fund
from db import create_client, get_client, get_clients, update_client, delete_client


app = Flask(__name__)


# Logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)


url_funds = "/funds"
url_clients = "/clients"


# Funtion to create a fund
@app.route(url_funds + "/create-fund", methods=['POST'])
def api_create_fund():
    try:
        name = request.json['name'] 
        value_min = request.json['value_min'] 
        money = request.json['money'] 
        category = request.json['category'] 
        date = datetime.today().strftime('%Y-%m-%d')
        
        data = json.loads(get_funds())
        count = len(data)
        if count == 0:
            fund_id = "1"
        else:
            fund_id = str(int(data[count-1]["_id"]) + 1)
        
        create_fund(fund_id, name, value_min, money, category, date)
        message = "Fund Created"
        
        return response(200, get_fund(fund_id), message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to get all funds
@app.route(url_funds + "/get-funds", methods=['GET'])
def api_get_funds():
    try:
        message = ""
        data = get_funds()
        
        if len(data) == 2: 
            message = "No funds"
        elif len(data) > 2:
            message = "Funds"
        else:
            message = "Error"
        
        return response(200, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to get a fund by id
@app.route(url_funds + "/get-fund/<id>", methods=['GET'])
def api_get_fund(id):
    try:
        message = ""
        data = get_fund(id)
        
        if len(data) == 2: 
            message = "Fund no exist"
        elif len(data) > 2:
            message = "Fund found"
        else:
            message = "Error"
        
        return response(200, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to update a fund by id
@app.route(url_funds + "/update-fund/<id>", methods=['PUT'])
def api_update_fund(id):
    try:
        name = request.json['name'] 
        value_min = request.json['value_min'] 
        money = request.json['money'] 
        category = request.json['category'] 
        date = datetime.today().strftime('%Y-%m-%d')
        
        message = ""
        data = get_fund(id)
        
        if len(data) == 2: 
            message = "Fund no exist"
        elif len(data) > 2:
            message = "Fund Updated"
            update_fund(id, name, value_min, money, category, date)
            data = get_fund(id)
        else:
            message = "Error"
        
        return response(200, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to delete a fund by id
@app.route(url_funds + "/delete-fund/<id>", methods=['DELETE'])
def api_delete_fund(id):
    
    try:
        message = ""
        data = get_fund(id)
        
        if len(data) == 2: 
            message = "Fund no exist"
        elif len(data) > 2:
            message = "Fund Deleted"
            delete_fund(id)
        else:
            message = "Error"
        
        return response(200, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to create a client
@app.route(url_clients + "/create-client", methods=['POST'])
def api_create_client():
    try:
        name = request.json['name'] 
        value = request.json['value'] 
        date = datetime.today().strftime('%Y-%m-%d')
        funds = request.json['funds'] 
        trans = request.json['trans'] 
        
        data = json.loads(get_clients())
        count = len(data)
        if count == 0:
            client_id = "1"
        else:
            client_id = str(int(data[count-1]["_id"]) + 1)
        
        create_client(client_id, name, value, date, funds, trans)
        message = "client Created"
        
        return response(200, get_client(client_id), message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to get all clients
@app.route(url_clients + "/get-clients", methods=['GET'])
def api_get_clients():
    try:
        message = ""
        data = get_clients()
        
        if len(data) == 2: 
            message = "No clients"
        elif len(data) > 2:
            message = "clients"
        else:
            message = "Error"
        
        return response(200, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to get a client by id
@app.route(url_clients + "/get-client/<id>", methods=['GET'])
def api_get_client(id):
    try:
        message = ""
        data = get_client(id)
        
        if len(data) == 2: 
            message = "client no exist"
        elif len(data) > 2:
            message = "client found"
        else:
            message = "Error"
        
        return response(200, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to update a client by id
@app.route(url_clients + "/update-client/<id>", methods=['PUT'])
def api_update_client(id):
    try:
        name = request.json['name'] 
        value = request.json['value'] 
        value = request.json['value'] 
        date = datetime.today().strftime('%Y-%m-%d')
        funds = request.json['funds'] 
        trans = request.json['trans'] 
        
        message = ""
        data = get_client(id)
        
        if len(data) == 2: 
            message = "client no exist"
        elif len(data) > 2:
            message = "client Updated"
            update_client(id, name, value, date, funds, trans)
            data = get_client(id)
        else:
            message = "Error"
        
        return response(200, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to delete a client by id
@app.route(url_clients + "/delete-client/<id>", methods=['DELETE'])
def api_delete_client(id):
    
    try:
        message = ""
        data = get_client(id)
        
        if len(data) == 2: 
            message = "client no exist"
        elif len(data) > 2:
            message = "client Deleted"
            delete_client(id)
        else:
            message = "Error"
        
        return response(200, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Funtion to subscribe a client to a fund
@app.route(url_clients + "/subscribe-client-fund", methods=['POST'])
def api_link_client_to_fund():
    try:
        client_id = request.json['client_id'] 
        fund_id = request.json['fund_id']
        operation = request.json['operation']
        
        client = json.loads(get_client(client_id))
        client = client[0]
        fund = json.loads(get_fund(fund_id))
        fund = fund[0]
        
        if operation == "link":
            count = 0
            find = False
            for i in client["funds"]:
                if i[count] == fund_id:
                    find = True
                    break       
                else: count += 1
            if not find:
                money = request.json['money']
                if money >= fund["value_min"] and client["value"] - money >= 0:
                    value = client["value"] - money
                    client["funds"].append(fund_id)
                    date = datetime.today().strftime('%Y-%m-%d')
                    trans = {"operation":operation, "fund":fund_id, "money":money, "date": date}
                    client["trans"].append(trans)
                    
                    update_client(client_id, client["name"], value, client["date"], client["funds"], client["trans"])
                    
                    name = fund["name"]
                    message = f"Client link to fund {name}"
                    
                else:
                    name = fund["name"]
                    message = f"You do not have an available balance to link to the fund {name}"
            else: 
                name = fund["name"]
                message = f"Client is alredy link to the fund {name}"
        
        elif operation == "un_link":
            count = 0
            find = False
            for i in client["funds"]:
                if i[count] == fund_id:
                    client["funds"].pop(count)
                    find = True
                    break       
                else: count += 1
                
            if find:
                money = 0
                count = 0
                for i in client["trans"]:
                    if i["fund"] == fund_id and i["operation"] == "link":
                        money = i["money"]
                    count += 1
                
                value = client["value"] + money
                date = datetime.today().strftime('%Y-%m-%d')
                trans = {"operation":operation, "fund":fund_id, "money":0-money, "date": date}
                client["trans"].append(trans)
                
                update_client(client_id, client["name"], value, client["date"], client["funds"], client["trans"])
                name = fund["name"]
                message = f"Client unlink to fund {name}"
            
            else: 
                name = fund["name"]
                message = f"Client is not link to fund {name}"
        
        else:
            message = "Invalid Operation"
            
        data = get_client(client_id)
            
        return response(200, data, message)
    
    except BaseException as e:
        return response(400, log_error(e), "Error")


# Function to response Api standard
def response(status_code, body, message):
    return {
            "message" : message,
            "statusCode": status_code,
            "body": body,
            "headers": {
                "content-type":"application/json",
                "Access-Control-Allow-Origin": "*"
            },
            "isBase64Encoded": False
        }


# Function to describe an error
def log_error(e):
    logger.info(str(e))
    logger.error('Error type: ' + type(e).__name__ +', file: '+__file__ +', line: '+ str(e.__traceback__.tb_lineno))
    dict_error = {'message': str(e).replace('\'','')}
    
    return json.dumps(dict_error)


if __name__ == '__main__':
    app.run(port=8000, debug=True)

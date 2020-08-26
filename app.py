#!flask/bin/python
# -*-coding:utf-8 -*-
from flask import Flask, request
import json
import time,datetime
import uuid
from datetime import datetime, timedelta
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

def error_403(mes):
    return {
        "code": 403,
        "status": "Forbidden",
        "message": mes,
    }

def ok_200(mes):
    return {
        "code": 200,
        "status": "OK",
        "message": mes,
    }

@app.route('/dorm/detail', methods=['POST'])
def dorm_detail():
    try:
        data = request.get_json()
    except:
        return error_403('No given data'), 403
    else:
        if 'user_id' not in data:
            return error_403('No given data'), 403
    
    flag = get_status(data['user_id'])
    if flag:
        mes = {
            'user_id': data['user_id'],
            'status': flag[data['user_id']],
            'status_code': 1,
            'data_detail': get_json()['data_detail'],
            'data_detail_url': get_json()['data_detail_url'],
        }
        return ok_200(mes), 200
    else:
        mes = {
            'user_id': data['user_id'],
            'status': '無任何紀錄',
            'status_code': 0,
            'data_detail': get_json()['data_detail'],
            'data_detail_url': get_json()['data_detail_url'],
        }
        return ok_200(mes), 200

def get_json():
    with open('dorm_id_list.json') as json_file:
        data = json.load(json_file)
        return data
    
def get_status(check_id):
    print('Now load - ' + check_id)
    json_data = get_json()
    flag = False
    mes = ''
    for data in json_data['full_data']:
        if check_id in data:
            flag = True
            mes = data
    if flag:
        print('mes:' + str(mes))
        return mes
    print('Not Found')
    return False

if __name__ == '__main__':
    app.run(debug=True)
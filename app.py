from flask import Flask, render_template, request, redirect, url_for, session, make_response, jsonify
from datetime import datetime, timedelta
from functools import wraps
import sqlite3
import ast
from editor import *
import httpx
import requests
import json
import io
app = Flask(__name__)

@app.route('/edit/restore', methods=['POST'])
async def restore():
    try:
        data = request.get_json()
        save_stats = data['save_stats']
    except Exception:
        return {"result" : False, "info" : "값을 정확하게 입력해주세요."}, 400
    if True:
        result = await restore_account(save_stats)
        if result is False:
            return {"result" : False, "info" : "계정 정보를 다시한번 확인해주세요."}, 400
        else:
            return {"result" : True, "info" : None, "transfercode" : result[0], "pin" : result[1], "savestats" : result[2]}, 200
    # except Exception as e:
    #     pass

@app.route('/edit/catfood', methods=['POST'])
async def catfood():
    try:
        data = request.get_json()
        transfer = data['transfer']
        pin = data['pin']
        version = data['version']
        catfood_value = int(data['value'])
    except Exception:
        return {"result" : False, "info" : "값을 정확하게 입력해주세요."}, 400
    try:
        result = await cat_food(version, transfer, pin, catfood_value)
        if result is False:
            return {"result" : False, "info" : "계정 정보를 다시한번 확인해주세요."}, 400
        else:
            return {"result" : True, "info" : None, "transfercode" : result[0], "pin" : result[1], "savestats" : result[2]}, 200
    except Exception:
        pass
@app.route('/edit/item', methods=['POST'])
async def item():
    try:
        data = request.get_json()
        transfer = data['transfer']
        pin = data['pin']
        item = data['item'] #아이템 인덱스 / 중복선택가능
        version = data['version']
        item_value = int(data['value'])
    except Exception:
        return {"result" : False, "info" : "값을 정확하게 입력해주세요."}, 400
    try:
        result = await battle_items(version, transfer, pin, item, item_value)
        if result is False:
            return {"result" : False, "info" : "계정 정보를 다시한번 확인해주세요."}, 400
        else:
            return {"result" : True, "info" : None, "transfercode" : result[0], "pin" : result[1], "savestats" : result[2]}, 200
    except Exception:
        pass

@app.route('/edit/catamin', methods=['POST'])
async def catamin():
    try:
        data = request.get_json()
        transfer = data['transfer']
        pin = data['pin']
        item = data['item'] #아이템 인덱스 / 중복선택가능
        version = data['version']
        item_value = int(data['value'])
    except Exception:
        return {"result" : False, "info" : "값을 정확하게 입력해주세요."}, 400
    try:
        result = await catamins(version, transfer, pin, item, item_value)
        if result is False:
            return {"result" : False, "info" : "계정 정보를 다시한번 확인해주세요."}, 400
        else:
            return {"result" : True, "info" : None, "transfercode" : result[0], "pin" : result[1], "savestats" : result[2]}, 200
    except Exception:
        pass
@app.route('/edit/catseye', methods=['POST'])
async def catseye():
    try:
        data = request.get_json()
        transfer = data['transfer']
        pin = data['pin']
        item = data['item'] #아이템 인덱스 / 중복선택가능
        version = data['version']
        item_value = int(data['value'])
    except Exception:
        return {"result" : False, "info" : "값을 정확하게 입력해주세요."}, 400
    try:
        result = await catseyes(version, transfer, pin, item, item_value)
        if result is False:
            return {"result" : False, "info" : "계정 정보를 다시한번 확인해주세요."}, 400
        else:
            return {"result" : True, "info" : None, "transfercode" : result[0], "pin" : result[1], "savestats" : result[2]}, 200
    except Exception:
        pass
@app.route('/edit/leadership', methods=['POST'])
async def _leadership():
    try:
        data = request.get_json()
        transfer = data['transfer']
        pin = data['pin']
        version = data['version']
        item_value = int(data['value'])
    except Exception:
        return {"result" : False, "info" : "값을 정확하게 입력해주세요."}, 400
    try:
        result = await leadership(version, transfer, pin, item_value)
        if result is False:
            return {"result" : False, "info" : "계정 정보를 다시한번 확인해주세요."}, 400
        else:
            return {"result" : True, "info" : None, "transfercode" : result[0], "pin" : result[1], "savestats" : result[2]}, 200
    except Exception:
        pass

@app.route('/edit/ticket1', methods=['POST'])
async def ticket1():
    try:
        data = request.get_json()
        transfer = data['transfer']
        pin = data['pin']
        version = data['version']
        item_value = int(data['value'])
    except Exception:
        return {"result" : False, "info" : "값을 정확하게 입력해주세요."}, 400
    try:
        result = await normal_tickets(version, transfer, pin, item_value)
        if result is False:
            return {"result" : False, "info" : "계정 정보를 다시한번 확인해주세요."}, 400
        else:
            return {"result" : True, "info" : None, "transfercode" : result[0], "pin" : result[1], "savestats" : result[2]}, 200
    except Exception:
        pass
@app.route('/edit/ticket2', methods=['POST'])
async def ticket2():
    try:
        data = request.get_json()
        transfer = data['transfer']
        pin = data['pin']
        version = data['version']
        item_value = int(data['value'])
    except Exception:
        return {"result" : False, "info" : "값을 정확하게 입력해주세요."}, 400
    try:
        result = await rare_tickets(version, transfer, pin, item_value)
        if result is False:
            return {"result" : False, "info" : "계정 정보를 다시한번 확인해주세요."}, 400
        else:
            return {"result" : True, "info" : None, "transfercode" : result[0], "pin" : result[1], "savestats" : result[2]}, 200
    except Exception:
        pass
@app.route('/edit/ticket3', methods=['POST'])
async def ticket3():
    try:
        data = request.get_json()
        transfer = data['transfer']
        pin = data['pin']
        version = data['version']
        item_value = int(data['value'])
    except Exception:
        return {"result" : False, "info" : "값을 정확하게 입력해주세요."}, 400
    try:
        result = await platinum_tickets(version, transfer, pin, item_value)
        if result is False:
            return {"result" : False, "info" : "계정 정보를 다시한번 확인해주세요."}, 400
        else:
            return {"result" : True, "info" : None, "transfercode" : result[0], "pin" : result[1], "savestats" : result[2]}, 200
    except Exception:
        pass
@app.route('/edit/ticket4', methods=['POST'])
async def ticket4():
    try:
        data = request.get_json()
        transfer = data['transfer']
        pin = data['pin']
        version = data['version']
        item_value = int(data['value'])
    except Exception:
        return {"result" : False, "info" : "값을 정확하게 입력해주세요."}, 400
    try:
        result = await legend_tickets(version, transfer, pin, item_value)
        if result is False:
            return {"result" : False, "info" : "계정 정보를 다시한번 확인해주세요."}, 400
        else:
            return {"result" : True, "info" : None, "transfercode" : result[0], "pin" : result[1], "savestats" : result[2]}, 200
    except Exception:
        pass
@app.route('/edit/np', methods=['POST'])
async def np():
    try:
        data = request.get_json()
        transfer = data['transfer']
        pin = data['pin']
        version = data['version']
        item_value = int(data['value'])
    except Exception:
        return {"result" : False, "info" : "값을 정확하게 입력해주세요."}, 400
    try:
        result = await edit_np(version, transfer, pin, item_value)
        if result is False:
            return {"result" : False, "info" : "계정 정보를 다시한번 확인해주세요."}, 400
        else:
            return {"result" : True, "info" : None, "transfercode" : result[0], "pin" : result[1], "savestats" : result[2]}, 200
    except Exception:
        pass
@app.route('/edit/xp', methods=['POST'])
async def xp():
    try:
        data = request.get_json()
        transfer = data['transfer']
        pin = data['pin']
        version = data['version']
        item_value = int(data['value'])
    except Exception:
        return {"result" : False, "info" : "값을 정확하게 입력해주세요."}, 400
    try:
        result = await edit_xp(version, transfer, pin, item_value)
        if result is False:
            return {"result" : False, "info" : "계정 정보를 다시한번 확인해주세요."}, 400
        else:
            return {"result" : True, "info" : None, "transfercode" : result[0], "pin" : result[1], "savestats" : result[2]}, 200
    except Exception:
        pass
@app.route('/edit/cat', methods=['POST'])
async def cat():
    try:
        data = request.get_json()
        transfer = data['transfer']
        pin = data['pin']
        version = data['version']
        item_value = int(data['value']) #고양이 id
    except Exception:
        return {"result" : False, "info" : "값을 정확하게 입력해주세요."}, 400
    try:
        result = await get_id_cat(version, transfer, pin, item_value)
        if result is False:
            return {"result" : False, "info" : "계정 정보를 다시한번 확인해주세요."}, 400
        else:
            return {"result" : True, "info" : None, "transfercode" : result[0], "pin" : result[1], "savestats" : result[2]}, 200
    except Exception:
        pass
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

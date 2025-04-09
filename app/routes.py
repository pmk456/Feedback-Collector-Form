"""
Author Name: Patan Musthakheem
Date & Time: 08-04-2025 12:15Am
File: routes.py
"""
from flask import Blueprint, render_template, jsonify, request

from . import utils
from . import db_handler
import datetime

routes = Blueprint("routes", __name__)

@routes.route("/")
def index():
    return render_template('index.html')

""" API Implementation - Pmk """

@routes.route('/api/feedback', methods=["POST"])
def api_feedback():
    data = request.get_json()
    success = False
    code = 400
    if not utils.validate_name(data['name']):
        message = "Please Enter Valid Name!"
    elif not utils.validate_email(data['email']):
        message = "Please Enter Valid Email!"  
    else:
        success = True
        code = 200
        message = "Feedback Successfully Sent!"
    
    # Updating to Database
    try:
        mongo_handler = db_handler.DBHandler()
    except:
        message = "Database Connection Error!"
        code = 400
        success = False
    else:
        db_status = mongo_handler.insert_record(
                {'Name': data['name'],
                'Email': data['email'],
                'Type': data['type'],
                'Message': data['msg'],
                'Time Stamp': datetime.datetime.now()})
        if not db_status:
            message = "Database Insertion Error!"
            code = 400
            success = False
    return jsonify({'success': success, 'message': message}), code
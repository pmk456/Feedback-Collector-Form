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
    handler = db_handler.DBHandler()
    handler.insert_record(
        {'Name': data['name'],
         'Email': data['email'],
         'Message': data['msg'],
         'Time Stamp': datetime.datetime.now() 
        }
    )

    return jsonify({'success': success, 'message': message}), code
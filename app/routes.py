"""
Author Name: Patan Musthakheem
Date & Time: 08-04-2025 12:15Am
File: routes.py
"""
from flask import Blueprint, render_template, jsonify, request

from . import utils

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
    elif not utils.validate_msg(data['msg']):
        message = "Please Enter Valid Message!"       
    else:
        success = True
        code = 200
        message = "Feedback Successfully Sent!"
    
    # Updating to Database

    return jsonify({'success': success, 'message': message}), code
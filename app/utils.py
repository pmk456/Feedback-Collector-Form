"""
Author Name: Patan Musthakheem
Date & Time: 08-04-2025 12:31AM
File: utils.py
"""
import regex as re

def validate_name(name):
    pattern = r'^[A-Za-z]+(?: [A-Za-z]+)*$'
    return re.fullmatch(pattern, name.strip()) is not None

def validate_email(email):
    pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.fullmatch(pattern, email.strip()) is not None

def validate_type(type):
    return type in ['bug-report', 'feature-request', 'general-comment']
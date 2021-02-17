from hashlib import sha3_512
from queries import get_user_password
from flask import flash

def hash_password(password):
    return sha3_512(password.encode('utf-8')).hexdigest()

def verify_password(user_name, password):
    '''checks if user's pasword matches with provided password'''
    user_password = get_user_password(user_name)
    entered_password = hash_password(password)

    if user_password:
        #user exists check if password correct
        if entered_password == user_password:
            flash("You are logged in", 'info')
            return True
        else:
            flash("Incorrect password", 'error')
            return False
    else:
        flash("Username not found", 'error')
        return False
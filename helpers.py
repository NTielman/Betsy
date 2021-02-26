from flask import flash
from hashlib import sha3_512
from queries import get_user_password, create_user


def hash_password(password):
    return sha3_512(password.encode('utf-8')).hexdigest()


def verify_signup(user_name, full_name, address, bio, avatar_url, password):
    '''checks if username is available and if user is able to be created'''
    username_available = not (get_user_password(user_name))
    if username_available:
        encrypted_password = hash_password(password)
        new_user = create_user(user_name, full_name,
                               address, bio, avatar_url, encrypted_password)
        if new_user:
            return True
        else:
            flash("Something went wrong. Couldn't create your account", 'error')
            return False
    else:
        flash("Username already exists", 'error')
        return False


def verify_signin(user_name, password):
    '''checks if user's pasword matches with provided password'''
    user_password = get_user_password(user_name)

    if user_password:  # user is existing user
        entered_password = hash_password(password)
        if entered_password == user_password:
            flash("You are logged in", 'info')
            return True
        else:
            flash("Incorrect password", 'error')
            return False
    else:
        flash("Username not found", 'error')
        return False

from database.user_operations import register_user, authenticate

def handle_login(username, password):
    return authenticate(username, password)

def handle_signup(username, password):
    return register_user(username, password)
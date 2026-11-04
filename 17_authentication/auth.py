users = {"admin": "1234", "user": "abcd"}

def login(username, password):
    if username in users and users[username] == password:
        return "Login Successful"
    return "Invalid Credentials"
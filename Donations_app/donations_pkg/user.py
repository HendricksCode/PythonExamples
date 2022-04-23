def login(database, username, password):
    if username in database:
        if database[username] == password:
            print(f"\nWelcome back {username}")
            return username
        print("Your password is not correct")
        return ""
    print("Username was not found")
    return ""

def register(database, username):
    if username in database:
        print("Username already registered")
        return ""
    else:
        print(f"{username} has been registered as your username")
        return username                                                                       
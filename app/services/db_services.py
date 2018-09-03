
"""
File is meant to simulate access to a database.
"""
users = {}


def save_user(user):
    users[user.username] = user


def find_by_username(username):
    if username in users:
        return users[username]
    else:
        return None


def get_all_users():
    if users:
        return list(users.values())
    else:
        return []


def delete_all_users():
    number_of_users = len(users)
    users.clear()
    return number_of_users

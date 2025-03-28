import tinydb

def new_user(db, username, email, password, tags):
    users = db.table('users')
    User = tinydb.Query()
    if users.get(User.username == username):
        return None
    user_record = {
            'username': username,
            'password': password,
            'friends': [],
            'email': email,
            'tags' : tags
            }
    return users.insert(user_record)

def get_user(db, username, password):
    users = db.table('users')
    User = tinydb.Query()
    return users.get((User.username == username) &
            (User.password == password))

def get_user_by_name(db, username):
    users = db.table('users')
    User = tinydb.Query()
    return users.get(User.username == username)

def delete_user(db, username, password):
    users = db.table('users')
    User = tinydb.Query()
    return users.remove((User.username == username) &
            (User.password == password))

def add_user_friend(db, user, friend):
    users = db.table('users')
    User = tinydb.Query()
    if friend not in user['friends']:
        if users.get(User.username == friend):
            user['friends'].append(friend)
            users.upsert(user, (User.username == user['username']) &
                    (User.password == user['password']))
            return 'Friend {} added successfully!'.format(friend), 'success'
        return 'User {} does not exist.'.format(friend), 'danger'
    return 'You are already friends with {}.'.format(friend), 'warning'

def remove_user_friend(db, user, friend):
    users = db.table('users')
    User = tinydb.Query()
    if friend in user['friends']:
        user['friends'].remove(friend)
        users.upsert(user, (User.username == user['username']) &
                (User.password == user['password']))
        return 'Friend {} successfully unfriended!'.format(friend), 'success'
    return 'You are not friends with {}.'.format(friend), 'warning'

def get_user_friends(db, user):
    users = db.table('users')
    User = tinydb.Query()
    friends = []
    for friend in user['friends']:
        friends.append(users.get(User.username == friend))
    return friends

def get_user_tags(db, user):
    users = db.table('users')
    User = tinydb.Query()
    user_data = users.get(User.username == user)
    return  user_data['tags']

def add_user_tag(db, username, new_tags):
    users = db.table('users')
    User = tinydb.Query()
    user_data = users.get(User.username == username)
    for tag in new_tags:
        user_data['tags'].append(tag)
    users.update(user_data, User.username == username)
    return True

def remove_user_tag(db, username, tags):
    users = db.table('users')
    User = tinydb.Query()
    user_data = users.get(User.username == username)
    for tag in tags:
        user_data['tags'].remove(tag)
    users.update(user_data, User.username == username)
    return True

def change_username(db, current_username, new_username):
    users = db.table('users')
    User = tinydb.Query()
    user_data = users.get(User.username == current_username)
    user_data['username'] = new_username
    users.update(user_data, User.username == current_username)
    return True

def change_password(db, username, new_password):
    users = db.table('users')
    User = tinydb.Query()
    user_data = users.get(User.username == username)
    user_data['password'] = new_password
    users.update(user_data, User.username == username)
    return True
import time
import tinydb

def add_post(db, user, text, tags):
    posts = db.table('posts')
    if isinstance(tags, str):
        tags = [tags]
    elif not isinstance(tags, list):
        tags = list(tags)
        
    posts.insert({'user': user['username'], 'text': text, 'time': time.time(), 'id' : user['username'] + str(time.time()), 'tags' : tags})

def get_posts(db, user):
    posts = db.table('posts')
    Post = tinydb.Query()
    return posts.search(Post.user==user['username'])

def delete_post(db, id):
    posts = db.table('posts')
    post = tinydb.Query()
    posts.remove(post.id == id)
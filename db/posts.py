import time
import tinydb

def add_post(db, user, text, tags):
    posts = db.table('posts')
    if isinstance(tags, str):
        tags = [tags]
    elif not isinstance(tags, list):
        tags = list(tags)
        
    posts.insert({'user': user['username'], 'text': text, 'time': time.time(), 'id' : user['username'] + str(time.time()), 'tags' : tags, 'likes' : [], 'dislikes' : [], 'comments' : []})

def get_posts(db, user):
    posts = db.table('posts')
    Post = tinydb.Query()
    return posts.search(Post.user==user['username'])

def delete_post(db, id):
    posts = db.table('posts')
    post = tinydb.Query()
    posts.remove(post.id == id)

def like_post(db, user, id):
    posts = db.table('posts')
    Post = tinydb.Query()
    post_data = posts.get(Post.id == id)
    post_data['likes'].append(user)
    posts.update(post_data, Post.id == id)

def remove_like(db, user, id):
    posts = db.table('posts')
    Post = tinydb.Query()
    post_data = posts.get(Post.id == id)
    post_data['likes'].remove(user)
    posts.update(post_data, Post.id == id)

def dislike_post(db, user, id):
    posts = db.table('posts')
    Post = tinydb.Query()
    post_data = posts.get(Post.id == id)
    post_data['dislikes'].append(user)
    posts.update(post_data, Post.id == id)

def remove_dislike(db, user, id):
    posts = db.table('posts')
    Post = tinydb.Query()
    post_data = posts.get(Post.id == id)
    post_data['dislikes'].remove(user)
    posts.update(post_data, Post.id == id)

'''def like_post(db, id):
    posts = db.table('posts')
    Post = tinydb.Query()
    post_data = posts.get(Post.id == id)
    post_data['likes'] += 1
    posts.update(post_data, Post.id == id)'''


'''def remove_like(db, id):
    posts = db.table('posts')
    Post = tinydb.Query()
    post_data = posts.get(Post.id == id)
    post_data['likes'] -= 1
    posts.update(post_data, Post.id == id)'''



'''def get_like(db, id):
    posts = db.table('posts')
    Post = tinydb.Query()
    post_data = posts.get(Post.id == id)

    if(post_data['likes'] > 0):
        return True

    return False'''

'''def dislike_post(db, id):
    posts = db.table('posts')
    Post = tinydb.Query()
    post_data = posts.get(Post.id == id)
    post_data['dislikes'] += 1
    posts.update(post_data, Post.id == id)




def get_dislike(db, id):
    posts = db.table('posts')
    Post = tinydb.Query()
    post_data = posts.get(Post.id == id)

    if(post_data['dislikes'] > 0):
        return True

    return False


def remove_dislike(db, id):
    posts = db.table('posts')
    Post = tinydb.Query()
    post_data = posts.get(Post.id == id)
    post_data['dislikes'] -= 1
    posts.update(post_data, Post.id == id)'''

def add_comment(db, user, post_id, comment_text):
    posts = db.table('posts')
    comment = {'user' : user['username'], 'text' : comment_text, 'time' : time.time(), 'id' : user['username'] + str(time.time())}
    Post = tinydb.Query()
    post_data = posts.get(Post.id == post_id)
    post_data['comments'].append(comment)
    posts.update(post_data, Post.id == post_id)

def delete_comment(db, post_id, comment_id):
    posts = db.table('posts')
    Post = tinydb.Query()
    post_data = posts.get(Post.id == post_id)
    updated_comments = [comment for comment in post_data.get('comments', []) if comment['id'] != comment_id]
    posts.update({'comments': updated_comments}, Post.id == post_id)
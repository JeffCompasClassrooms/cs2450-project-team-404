import flask
from db import posts, users, helpers
from handlers import copy
from handlers import verify

blueprint = flask.Blueprint("profile", __name__)

@blueprint.route('/profile')
def profile():

    db = helpers.load_db()

    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    user = users.get_user(db, username, password)
    if not user:
        flask.flash('You need to be logged in to do that.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))
    
    user_tags = users.get_user_tags(db, username)
    tags_table = db.table("tags")
    tags = {entry['tag'] for entry in tags_table.all()}
    
    has_all_tags = len(user_tags) == len(tags)

    # get users posts
    user_posts = posts.get_posts(db, user)

    # Get user's friends
    friends = users.get_user_friends(db, user)

    return flask.render_template('profile.html', title=copy.title, subtitle=copy.subtitle, user=user, username=username, user_tags=user_tags, tags=tags, has_all_tags=has_all_tags, posts=user_posts, friends=friends)
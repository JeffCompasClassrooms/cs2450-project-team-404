import flask

from handlers import copy
from db import posts, users, helpers
from handlers import verify

blueprint = flask.Blueprint("login", __name__)

@blueprint.route('/loginscreen')
def loginscreen():
    db = helpers.load_db()
    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    if username is not None and password is not None:
        if users.get_user(db, username, password):
            flask.flash('You are already logged in.', 'warning')
            return flask.redirect(flask.url_for('login.feed'))

    return flask.render_template('login.html', title=copy.title, subtitle=copy.subtitle)

@blueprint.route('/login', methods=['POST'])
def login():
    db = helpers.load_db()
    username = flask.request.form.get('username')
    password = flask.request.form.get('password')

    resp = flask.make_response(flask.redirect(flask.url_for('login.feed')))
    resp.set_cookie('username', username)
    resp.set_cookie('password', password)

    return resp

@blueprint.route('/register')
def register():
    db = helpers.load_db()
    username = flask.request.form.get('username')
    password = flask.request.form.get('password')

    tags_table = db.table('tags')
    tags = [tag['tag'] for tag in tags_table.all()]

    return flask.render_template('register.html', title=copy.title, subtitle=copy.subtitle, tags=tags)

@blueprint.route('/registeruser', methods=['POST'])
def registeruser():
    db = helpers.load_db()
    username = flask.request.form.get('username')
    email = flask.request.form.get('email')
    tags = flask.request.form.getlist('tags')
    password = flask.request.form.get('password')
    c_password = flask.request.form.get('cpassword')

    if c_password != password:
        flask.flash('Passwords do not match.', 'warning')
        return flask.redirect(flask.url_for('login.register'))

    message, isTrue = verify.verify_password(password)
    if not isTrue:
        flask.flash(message, 'warning')
        return flask.redirect(flask.url_for('login.register'))

    if not verify.verify_username(username):
        flask.flash('You are already logged in.', 'warning')
        return flask.redirect(flask.url_for('login.register'))

    if not tags or 'select' in tags:
        flask.flash('Must select one or more tags.', 'danger')
        return flask.redirect(flask.url_for('login.register'))

    users.new_user(db, username, email, password, tags)
    return flask.redirect(flask.url_for('login.feed'))

@blueprint.route('/logout', methods=['POST'])
def logout():
    db = helpers.load_db()
    resp = flask.make_response(flask.redirect(flask.url_for('login')))
    resp.set_cookie('username', '', expires=0)
    resp.set_cookie('password', '', expires=0)
    return resp

@blueprint.route('/')
def home():
    db = helpers.load_db()
    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    if username and password:
        user = users.get_user(db, username, password)
        if user:
            return flask.redirect(flask.url_for('login.feed'))

    return flask.render_template('home.html', title="Welcome to Taggle", subtitle="")

@blueprint.route('/feed')
def feed():
    db = helpers.load_db()
    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    if username is None or password is None:
        return flask.redirect(flask.url_for('login.loginscreen'))

    user = users.get_user(db, username, password)
    if not user:
        flask.flash('Invalid credentials. Please try again.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))

    friends = users.get_user_friends(db, user)
    posts_table = db.table("posts")
    all_posts = []
    user_tags = users.get_user_tags(db, username)
    selected_tag = flask.request.args.get('tag')

    for post in posts_table.all():
        if selected_tag:
            if selected_tag in post['tags']:
                all_posts.append(post)
        else:
            for tag in post['tags']:
                if tag in user_tags:
                    all_posts.append(post)

    sorted_posts = sorted(all_posts, key=lambda post: post['time'], reverse=True)
    tags_table = db.table("tags")
    tags = {entry['tag'] for entry in tags_table.all()}

    return flask.render_template('feed.html', title=copy.title, subtitle=copy.subtitle, user=user, username=username, friends=friends, posts=sorted_posts, tags=tags, user_tags=user_tags, selected_tag=selected_tag)

@blueprint.route('/delete', methods=['POST'])
def delete():
    db = helpers.load_db()
    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    resp = flask.make_response(flask.redirect(flask.url_for('login.loginscreen')))
    resp.set_cookie('username', '', expires=0)
    resp.set_cookie('password', '', expires=0)
    return resp

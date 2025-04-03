import flask

from handlers import copy
from db import posts, users, helpers

from handlers import verify

blueprint = flask.Blueprint("login", __name__)

@blueprint.route('/loginscreen')
def loginscreen():
    """Present a form to the user to enter their username and password."""
    db = helpers.load_db()

    # First check if already logged in
    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    if username is not None and password is not None:
        if users.get_user(db, username, password):
            # If they are logged in, redirect them to the feed page
            flask.flash('You are already logged in.', 'warning')
            return flask.redirect(flask.url_for('login.index'))

    print("Rendering login screen")  # Adding logging for debugging purposes
    return flask.render_template('login.html', title=copy.title,
            subtitle=copy.subtitle)

@blueprint.route('/login', methods=['POST'])
def login():
    """Log in the user.
    # Adding logging for debugging purposes

    Using the username and password fields on the form, create, delete, or
    log in a user, based on what button they click.
    """
    db = helpers.load_db()

    username = flask.request.form.get('username')
    password = flask.request.form.get('password')

    resp = flask.make_response(flask.redirect(flask.url_for('login.index')))
    resp.set_cookie('username', username)
    resp.set_cookie('password', password)

    return resp
    
@blueprint.route('/register')
def register():
    """Present a form to the user to create a new account."""
    db = helpers.load_db()

    username = flask.request.form.get('username')
    password = flask.request.form.get('password')

    tags_table = db.table('tags')
    tags = [tag['tag'] for tag in tags_table.all()]

    submit = flask.request.form.get('type')


    return flask.render_template('register.html', title=copy.title, subtitle=copy.subtitle, tags=tags)


@blueprint.route('/registeruser', methods=['POST'])
def registeruser():
    db = helpers.load_db()

    username = flask.request.form.get('username')
    email = flask.request.form.get('email')
    tags = flask.request.form.getlist('tags')
    password = flask.request.form.get('password')
    c_password = flask.request.form.get('cpassword') # Used to confirm if password was typed correctly





    if(c_password != password):
        flask.flash('Passwords do not match.', 'warning')
        return flask.redirect(flask.url_for('login.register'))

    message, isTrue = verify.verify_password(password)

    if(not isTrue):
        flask.flash(message, 'warning')
        return flask.redirect(flask.url_for('login.register'))

    if(not verify.verify_username(username)):
        flask.flash('You are already logged in.', 'warning')
        return flask.redirect(flask.url_for('login.register'))
    
    if not tags or 'select' in tags:
        flask.flash('Must select one or more tags.', 'danger')
        return flask.redirect(flask.url_for('login.register'))

    users.new_user(db, username, email, password, tags)

    return flask.redirect(flask.url_for('login.index'))


@blueprint.route('/logout', methods=['POST'])
def logout():
    """Log out the user."""
    db = helpers.load_db()

    resp = flask.make_response(flask.redirect(flask.url_for('login.loginscreen')))
    resp.set_cookie('username', '', expires=0)
    resp.set_cookie('password', '', expires=0)
    return resp

@blueprint.route('/')
def index():
    """Serves the main feed page for the user."""
    db = helpers.load_db()

    # make sure the user is logged in
    username = flask.request.cookies.get('username') # Check if the user has Cookies saved
    password = flask.request.cookies.get('password')
    if username is None and password is None: # If there are no Cookies saved, have them Log in. They may add Cookies if their browser allows it
        return flask.redirect(flask.url_for('login.loginscreen'))
    user = users.get_user(db, username, password)
    if not user:
        flask.flash('Invalid credentials. Please try again.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))

    # get the info for the user's feed
    friends = users.get_user_friends(db, user)
    posts_table = db.table("posts")
    all_posts = []
    user_tags = users.get_user_tags(db, username)
    # for post in posts_table.all():
    #     for tag in post['tags']:
    #         if tag in user_tags:
    #             all_posts.append(post)
    #for friend in friends + [user]:
        #all_posts += posts.get_posts(db, friend)

    # Retrieve the selected tag
    selected_tag = flask.request.args.get('tag')

    # Filter posts based on tag
    for post in posts_table.all():
        if selected_tag:
            # include only posts with the tag
            if selected_tag in post['tags']:
                all_posts.append(post)
        else:
            # include all posts with tags the user follows if no tag is selected
            for tag in  post['tags']:
                if tag in user_tags:
                    all_posts.append(post)

    # sort posts
    sorted_posts = sorted(all_posts, key=lambda post: post['time'], reverse=True)
    tags_table = db.table("tags")
    tags = {entry['tag'] for entry in tags_table.all()}

    return flask.render_template('feed.html', title=copy.title,
            subtitle=copy.subtitle, user=user, username=username,
            friends=friends, posts=sorted_posts, tags=tags, user_tags=user_tags, selected_tag=selected_tag)




@blueprint.route('/delete', methods=['POST'])
def delete():
    db = helpers.load_db()

    #TODO: Make this so that it does not rely on cookies, but rather on the saved information when the user is logged in (in case they don't want to use cookies)

    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    resp = flask.make_response(flask.redirect(flask.url_for('login.loginscreen')))
    resp.set_cookie('username', '', expires=0)
    resp.set_cookie('password', '', expires=0)

    #TODO: Add security feature where if a delete is unsuccessful, then it will redirect them back to the index page, and let them know that their account could not be deleted


    return resp

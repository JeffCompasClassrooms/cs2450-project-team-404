import flask
from db import posts, users, helpers
from handlers import copy
from handlers import verify

blueprint = flask.Blueprint("settings", __name__)

@blueprint.route('/settings')
def settings():

    db = helpers.load_db()

    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    user = users.get_user(db, username, password)
    if not user:
        flask.flash('You need to be logged in to do that.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))
    
    return flask.render_template('settings.html', title=copy.title, subtitle=copy.subtitle, user=user, username=username)

@blueprint.route('/change-user', methods=['POST'])
def change_username():
    db = helpers.load_db()

    username = flask.request.cookies.get('username')
    users_password = flask.request.cookies.get('password')

    current_username = flask.request.form.get('current-username')
    new_username = flask.request.form.get('new-username')
    entered_password = flask.request.form.get('password')

    if(current_username != username):
        flask.flash('Current username does not match!.', 'warning')
        return flask.redirect(flask.url_for('settings.settings'))
    
    if(entered_password != users_password):
        flask.flash('Passwords do not match.', 'warning')
        return flask.redirect(flask.url_for('settings.settings'))
    
    if (len(new_username) < 3 or len(new_username) > 20):
        flask.flash('New username must be more than 3 characters, and less than 20 characters.', 'warning')
        return flask.redirect(flask.url_for('settings.settings'))
    
    if(users.get_user_by_name(db, new_username)):
        flask.flash('New username is already taken.', 'warning')
        return flask.redirect(flask.url_for('settings.settings'))
    
    users.change_username(db, username, new_username)
    resp = flask.make_response(flask.redirect(flask.url_for('settings.settings')))
    resp.set_cookie('username', new_username)
    flask.flash('Username was successfully updated!', 'success')

    return resp

@blueprint.route('/change-password', methods=['POST'])
def change_password():
    db = helpers.load_db()

    username = flask.request.cookies.get('username')
    users_password = flask.request.cookies.get('password')

    current_password = flask.request.form.get('current-password')
    new_password = flask.request.form.get('new-password')
    confirm_new_password = flask.request.form.get('confirm-new-password')

    if current_password != users_password:
        flask.flash('Password is incorrect.', 'warning')
        return flask.redirect(flask.url_for('settings.settings'))
    
    if current_password == new_password:
        flask.flash('New password is the same as current password.', 'warning')
        return flask.redirect(flask.url_for('settings.settings'))

    if new_password != confirm_new_password:
        flask.flash('New password does not match.', 'warning')
        return flask.redirect(flask.url_for('settings.settings'))
    
    message, isValid = verify.verify_password(new_password)
    if not isValid:
        flask.flash(message, 'warning')
        return flask.redirect(flask.url_for('settings.settings'))
    
    
    users.change_password(db, username, new_password)
    resp = flask.make_response(flask.redirect(flask.url_for('settings.settings')))
    resp.set_cookie('password', new_password)
    flask.flash('Password was successfully changed!', 'success')

    return resp
import flask

from db import posts, users, helpers

blueprint = flask.Blueprint("posts", __name__)

@blueprint.route('/post', methods=['POST'])
def post():
    """Creates a new post."""
    db = helpers.load_db()

    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    user = users.get_user(db, username, password)
    if not user:
        flask.flash('You need to be logged in to do that.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))

    post = flask.request.form.get('post')
    tags = flask.request.form.getlist('tags')
    if not tags or 'select' in tags:
        flask.flash('Must select one or more tags.', 'danger')
        return flask.redirect(flask.url_for('login.index'))
    posts.add_post(db, user, post, tags)

    return flask.redirect(flask.url_for('login.index'))


@blueprint.route('/postdelete', methods=['POST'])
def delete():
    """Deletes a post."""
    db = helpers.load_db()

    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    user = users.get_user(db, username, password)
    if not user:
        flask.flash('You need to be logged in to do that.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))
    
    post_id = flask.request.form.get('post_id')
    posts.delete_post(db, post_id)

    return flask.redirect(flask.url_for('login.index'))

@blueprint.route('/likepost', methods=['POST'])
def like():
    db = helpers.load_db()

    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    user = users.get_user(db, username, password)
    if not user:
        flask.flash('You need to be logged in to do that.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))
    
    post_id = flask.request.form.get('post_id')

    if(not posts.get_like(db, post_id)):
        posts.like_post(db, post_id)

    else:
        posts.remove_like(db, post_id)

    return flask.redirect(flask.url_for('login.index'))

@blueprint.route('/dislikepost', methods=['POST'])
def dislike():
    db = helpers.load_db()

    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    user = users.get_user(db, username, password)
    if not user:
        flask.flash('You need to be logged in to do that.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))
    
    post_id = flask.request.form.get('post_id')

    if(not posts.get_dislike(db, post_id)):
        posts.dislike_post(db, post_id)

    else:
        posts.remove_dislike(db, post_id)

    return flask.redirect(flask.url_for('login.index'))
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
    likes = flask.request.form.get('likes')
    dislikes = flask.request.form.get('dislikes')

    if username in likes:
        posts.remove_like(db, username, post_id)
    else:
        posts.like_post(db, username, post_id)
        if dislikes:
            if username in dislikes:
                posts.remove_dislike(db, username, post_id)

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
    dislikes = flask.request.form.get('dislikes')
    likes = flask.request.form.get('likes')

    if username in dislikes:
        posts.remove_dislike(db, username, post_id)
    else:
        posts.dislike_post(db, username, post_id)
    
    if likes:
        if username in likes:
            posts.remove_like(db, username, post_id)

    return flask.redirect(flask.url_for('login.index'))

@blueprint.route('/comment', methods=['POST'])
def comment():
    db = helpers.load_db()

    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    user = users.get_user(db, username, password)
    if not user:
        flask.flash('You need to be logged in to do that.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))
    
    comment = flask.request.form.get('comment')
    post_id = flask.request.form.get('post_id')
    print(post_id)

    posts.add_comment(db, user, post_id, comment)

    return flask.redirect(flask.url_for('login.index'))

@blueprint.route('/commentdelete', methods=['POST'])
def comment_delete():
    """Deletes a comment."""
    db = helpers.load_db()

    username = flask.request.cookies.get('username')
    password = flask.request.cookies.get('password')

    user = users.get_user(db, username, password)
    if not user:
        flask.flash('You need to be logged in to do that.', 'danger')
        return flask.redirect(flask.url_for('login.loginscreen'))
    
    comment_id = flask.request.form.get('comment_id')
    post_id = flask.request.form.get('post_id')
    posts.delete_comment(db, post_id, comment_id)

    return flask.redirect(flask.url_for('login.index'))
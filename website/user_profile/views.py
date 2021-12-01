from flask import (
    render_template, redirect, flash, jsonify
)
from flask.helpers import url_for
from ..custom_decorators import admin_required
from website.auth.forms import NewProfilePicture
from website.auth.models import Avatar, User
from . import bp
from ..extensions import db
from random import randint
from flask_login import current_user

@bp.route('/profile/<username>')
def user_profile(username):
    user = User.query.filter_by(username=username).first()
    if user:
        return render_template('user_profile.html', user=user)
    else:
        return render_template('explore.html')

@bp.route('/add_new_pic', methods=['GET', 'POST'])
@admin_required
def add_new_pic():
    form = NewProfilePicture()
    avatars = Avatar.query.all()
    if form.validate_on_submit():
        new_avatar = Avatar(name=form.name.data, url=form.url.data, rarity=form.rarity.data)
        db.session.add(new_avatar)
        db.session.commit()
        flash('You can check new avatar on your own profile')
        return redirect(url_for('user.user_profile', username=current_user.username))
    return render_template('add_new_pic.html', form=form, characters=avatars)

@bp.route('/change_rarity_py', methods=['POST'])
def change_char_rarity():
    rarity = randint(0, 10)
    return jsonify({'rarity': rarity})

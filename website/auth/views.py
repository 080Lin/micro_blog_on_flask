from flask import (
    render_template, redirect, request, url_for, flash
)
from flask_login import login_user, current_user, logout_user
from flask_login.utils import login_required
from werkzeug.urls import url_parse
from . import bp
from .forms import RegisterForm, LoginForm
from .models import User
from ..extensions import db, login_manager
from ..custom_decorators import anonymous_user


@bp.route('/register', methods=['GET', 'POST'])
@anonymous_user
def register_page():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(username=form.username.data, email=form.email.data)
        new_user.set_password(password=form.password.data)
        db.session.add(new_user)
        db.session.commit()
        flash('You have been successfully registrated')
        return redirect(url_for('content.home_page'))
    return render_template('register_page.html', form=form)

@bp.route('/login', methods=['GET', 'POST'])
@anonymous_user
def login_page():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            flash(f'You have been entered to the blog as {user.username}')
            next = request.args.get('next')
            if not next or url_parse(next).netloc != '':
                return redirect(url_for('content.home_page'))
            return redirect(next)
    return render_template('login_page.html', form=form)

@bp.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("content.home_page"))

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
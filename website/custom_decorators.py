from flask import redirect, url_for, flash
from flask_login import current_user

def anonymous_user(func):
    def wrapper():
        if current_user.is_authenticated:
            return redirect(url_for('content.home_page'))
        return func()
    wrapper.__name__ = func.__name__
    return wrapper

def admin_required(func):
    def wrapper():
        if current_user.admin:
            return func()
        flash('You need admin rights to perform this action')
        return redirect(url_for('user.user_profile', username=current_user.username))
    wrapper.__name__ = func.__name__
    return wrapper
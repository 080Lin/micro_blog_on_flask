from datetime import datetime
from . import bp
from website.extensions import db
from website.auth.models import Post, Article, Comment
from website.auth.forms import PostForm
from .forms import ArticleForm, CommentToArticleForm
from flask_login import current_user
from flask import (
    render_template, redirect, url_for, flash
)
from flask_login import login_required

@bp.route('/home', methods=['GET', 'POST'])
@bp.route('/', methods=['GET', 'POST'])
@login_required
def home_page():
    form = PostForm()
    blogs = Post.query.all()
    if form.validate_on_submit():
        new_post = Post(body=form.post.data, author=current_user)
        db.session.add(new_post)
        db.session.commit()
        flash('You have been added new comment!')
        return redirect(url_for('content.home_page'))
    return render_template('home_page.html', posts=blogs, form=form)

@bp.route('/new_article', methods=["GET", 'POST'])
@login_required
def new_post_page():
    form = ArticleForm()
    if form.validate_on_submit():
        new_article = Article(body=form.body.data, theme=form.theme.data, art_author=current_user, name=form.name.data)
        db.session.add(new_article)
        db.session.commit()
        flash('Your new article is available by link ....')
        return redirect(url_for('content.home_page'))
    return render_template('new_post_page.html', form=form)

@bp.route('/article/<article_name>', methods=["GET", 'POST'])
@login_required
def view_article(article_name):
    form = CommentToArticleForm()
    article = Article.query.filter_by(name=article_name).first()
    comments = Comment.query.filter_by(article_id=article.id).all()
    if form.validate_on_submit():
        comment = Comment(body=form.body.data, com_author=current_user, article=article)
        db.session.add(comment)
        db.session.commit()
    return render_template('show_article_content.html', article=article, form=form, comments=comments)

@bp.route('/explore')
@login_required
def explore_articles():
    articles = Article.query.all()
    return render_template('explore.html', articles=articles)

@bp.before_request
def before_request():
    if current_user.is_authenticated:
        current_user.last_seen = datetime.utcnow()
        db.session.commit()

from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length
from wtforms.fields import StringField, BooleanField, SelectField

themes = ['IT', "Medicine", 'Politics', 'Games', 'Streaming', 'Show', 'Investment']

class ArticleForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=8, max=80)], render_kw={'placeholder': "how would you name it?"})
    body = StringField('Place to write smth beautiful', validators=[DataRequired(), Length(min=60)], render_kw={'placeholder': 'here'})
    theme = SelectField(label='Theme', validators=[DataRequired()], choices=themes)

class CommentToArticleForm(FlaskForm):
    body = StringField('What are you thinkin bout?', validators=[DataRequired(), Length(min=3)], render_kw={'placeholder': 'here'})
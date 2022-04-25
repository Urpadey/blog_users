from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import InputRequired, URL, EqualTo
from flask_ckeditor import CKEditorField


# WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[InputRequired()])
    subtitle = StringField("Subtitle", validators=[InputRequired()])
    img_url = StringField("Blog Image URL", validators=[InputRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[InputRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    name = StringField('NAME*')
    email = StringField('EMAIL*')
    password = PasswordField('PASSWORD*', [InputRequired(), EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('CONFIRM PASSWORD*', validators=[InputRequired()])
    submit = SubmitField('SIGN ME UP!')


class LoginForm(FlaskForm):
    email = StringField("EMAIL*")
    password = PasswordField("PASSWORD*")
    submit = SubmitField('LET ME IN')


class CommentForm(FlaskForm):
    comment = CKEditorField('Comment')
    submit = SubmitField('comment')

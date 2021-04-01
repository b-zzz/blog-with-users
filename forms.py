from flask_wtf import FlaskForm
from flask_ckeditor import CKEditorField
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email, URL, Length
from wtforms.fields.html5 import EmailField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class UserRegisterForm(FlaskForm):
    name = StringField(label='Name', validators=[DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password',
                             validators=[DataRequired(),
                                         Length(min=8),
                                         EqualTo('confirm',
                                         message='Passwords must match')])
    confirm = PasswordField(label='Repeat Password')
    submit = SubmitField(label='Submit')

class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='password',
                             validators=[DataRequired()])
    submit = SubmitField(label='Submit')

class CommentForm(FlaskForm):
    comment_text = StringField(label='Comment', validators=[DataRequired()])
    submit = SubmitField(label='SUBMIT COMMENT')

from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    TextAreaField,
    EmailField,
    PasswordField,
    SubmitField,
    FloatField,
    DateField,
    SelectField,
    BooleanField,
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    NumberRange,
    ValidationError,
)
from model import User

"""
3 Forms it will have:
1. RegisterForm
2. LoginForm
3. ExpenseForm
"""



class RegisterForm(FlaskForm):
    # name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This Username is already taken. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This Email is already taken. Please use a different one.')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=20)])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class ExpenseForm(FlaskForm):
    amount = FloatField('Amount', validators=[DataRequired(), NumberRange(min=0.01)])
    date = DateField('Date', validators=[DataRequired()])
    category = SelectField('Category', validators=[DataRequired()], choices=[
        ('food', 'Food'),
        ('transportation', 'Transportation'),
        ('entertainment', 'Entertainment'),
        ('housing', 'Housing'),
        ('shopping', 'Shopping'),
        ('other', 'Other')
    ])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=200)])
    submit = SubmitField('Add Expense')
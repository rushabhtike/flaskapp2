from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, IntegerField, DateField, \
    SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from app.models import User, UserProfile


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exists')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already exists')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class UpdateAccountForm(FlaskForm):
    # username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    # email = StringField('Email', validators=[DataRequired(), Email()])
    choices = [(' ', ' '), ('AK', 'Alaska'), ('AL', 'Alabama'), ('AR', 'Arkansas'), ('AS', 'American Samoa'),
               ('AZ', 'Arizona'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'),
               ('DC', 'District of Columbia'),
               ('DE', 'Delaware'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'),
               ('IA', 'Iowa'),
               ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('KS', 'Kansas'), ('KY', 'Kentucky'),
               ('LA', 'Louisiana'),
               ('MA', 'Massachusetts'), ('MD', 'Maryland'), ('ME', 'Maine'), ('MI', 'Michigan'), ('MN', 'Minnesota'),
               ('MO', 'Missouri'), ('MP', 'Northern Mariana Islands'), ('MS', 'Mississippi'), ('MT', 'Montana'),
               ('NA', 'National'),
               ('NC', 'NorthCarolina'), ('ND', 'NorthDakota'), ('NE', 'Nebraska'), ('NH', 'NewHampshire'),
               ('NJ', 'NewJersey'),
               ('NM', 'NewMexico'), ('NV', 'Nevada'), ('NY', 'NewYork'), ('OH', 'Ohio'), ('OK', 'Oklahoma'),
               ('OR', 'Oregon'),
               ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'),
               ('SD', 'SouthDakota'),
               ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VA', 'Virginia'), ('VI', 'Virgin Islands'),
               ('VT', 'Vermont'),
               ('WA', 'Washington'), ('WI', 'Wisconsin'), ('WV', 'WestVirginia'), ('WY', 'Wyoming')]
    full_name = StringField('Full Name', validators=[DataRequired(), Length(max=50)])
    address_one = StringField('Address 1', validators=[DataRequired(), Length(max=100)])
    address_two = StringField('Address 2', validators=[Length(max=100)])
    city = StringField('City', validators=[DataRequired(), Length(max=100)])
    state = SelectField('State', choices=choices, validators=[DataRequired()])
    zipcode = IntegerField('Zipcode', validators=[DataRequired()])

    submit = SubmitField('Update')

    # def validate_username(self, username):
    #     if username.data != current_user.username:
    #         user = User.query.filter_by(username=username.data).first()
    #         if user:
    #             raise ValidationError('Username already exists')
    #
    # def validate_email(self, email):
    #     if email.data != current_user.email:
    #         user = User.query.filter_by(email=email.data).first()
    #         if user:
    #             raise ValidationError('Email already exists')

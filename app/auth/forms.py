"""Auth application forms."""
import calendar
import datetime

from flask_wtf import FlaskForm
from wtforms import PasswordField, SelectField, StringField

from app.auth.validators import DataRequired

class LoginForm(FlaskForm):
    """Login form for our User."""

    username = StringField('Phone, email, or username', validators=[DataRequired()])
    password = StringField('Password', validators=[DataRequired()])

class RegistrationForm(FlaskForm):
    """Registration form for our User."""

    def __init__(self):
        """Creates a new RegistrationForm instance.
            The reason why we're overriding this is to provide dynamic creation of choices for our `year` select tag.
        """
        super().__init__()
        # Sets the year choices dynamically, so I don't have to update this every year.
        oldest_year = 1900
        current_year = datetime.date.today().year

        # This cannot be a tuple, as we want to force Python to evaluate the generator expression (otherwise WTForms will have problems rendering the field).
        self.year.choices = [
            (num, num) for num in range(current_year, oldest_year - 1, -1)
        ]


    name = StringField('Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    # This is a bit tricky, the DoB is separated into three select options.
    MONTH_CHOICES = [
        (num, calendar.month_name[num]) for num in range(1, 13)
    ]

    # This will have to do for now.
    DAY_CHOICES = [
        (num, num) for num in range(1, 32)
    ]

    month = SelectField(choices=MONTH_CHOICES)
    day = SelectField(choices=DAY_CHOICES)
    # See: __init__()
    year = SelectField()

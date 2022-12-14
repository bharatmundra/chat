
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import InputRequired,Length,EqualTo

from models import User

class RegistrationForm(FlaskForm):
    """Registration Form"""



    username = StringField(
        'username_label',
         validators=[InputRequired("Username Required"),
        Length(min=4,max=25,message="Username must be between 4 and 25 characters")
        ]
        )
    password =PasswordField('passwor-label',
    validators=[InputRequired("Password Required"),
        Length(min=4,max=25,message="password must be between 4 and 25 characters")
        ]
        )
    confirm_pswd =PasswordField('confirm_passwor-label',
    validators=[InputRequired("Username Required"),
        EqualTo('password',message="password must match")
        ])
    submit_button= SubmitField('Create')


    # def validate_username(self, username):
    #     user_object = User.query.filter_by(username=username.data).first()
    #     if user_object:
    #         raise ValidationError("Username already exists. Select a different username.")



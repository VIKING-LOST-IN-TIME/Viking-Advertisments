from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class CreateAdvertisementForm(FlaskForm):
    left_advertisement_url = StringField('Redirect url',
                                         validators=[DataRequired(message="Please define a redirect url")])
    left_advertisement_image = StringField('Image url',
                                           validators=[DataRequired(message="Please define a image")])
    right_advertisement_url = StringField('Redirect url',
                                          validators=[DataRequired(message="Please define a redirect url")])
    right_advertisement_image = StringField('Image url',
                                            validators=[DataRequired(message="Please define a image")])

    def validate(self):
        return True if not FlaskForm.validate(self) else False

from flask_wtf import FlaskForm
from wtforms.fields.simple import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from yacut.constants import (DATA_REQUIRED_VALIDATOR, LENGTH_LINK,
                             LENGTH_SHORT_LINK_USER, PLACEHOLDER_ORIGINAL_LINK,
                             PLACEHOLDER_SHORT_LINK, PLACEHOLDER_SUBMIT_BUTTON,
                             REGEXP_SHORT_VALIDATOR, URL_VALIDATOR, Errors)


class URLForm(FlaskForm):
    original_link = URLField(
        PLACEHOLDER_ORIGINAL_LINK,
        validators=[
            DataRequired(DATA_REQUIRED_VALIDATOR),
            Length(max=LENGTH_LINK, message=Errors.TOO_LONG_LINK),
            URL(message=URL_VALIDATOR)
        ],
    )
    custom_id = StringField(
        PLACEHOLDER_SHORT_LINK,
        validators=[
            Optional(),
            Length(
                max=LENGTH_SHORT_LINK_USER,
                message=Errors.TOO_LONG_SHORT_LINK
            ),
            Regexp(REGEXP_SHORT_VALIDATOR,
                   message=Errors.WRONG_FORMAT_SHORT_LINK)
        ]
    )
    submit = SubmitField(PLACEHOLDER_SUBMIT_BUTTON)

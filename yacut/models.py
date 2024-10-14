import random
import re
from datetime import datetime

from yacut import db
from yacut.constants import (ALLOWED_CHARS_SHORT_LINK, LENGTH_SHORT_LINK_AUTO,
                             LENGTH_SHORT_LINK_USER, REGEXP_SHORT_VALIDATOR,
                             Errors)
from yacut.error_handlers import (ShortLinkExistsException,
                                  TooLongShortLinkException,
                                  WrongFormatShortLinkException)


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String(LENGTH_SHORT_LINK_USER), unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.now)

    @staticmethod
    def get(short_link):
        return URLMap.query.filter_by(short=short_link).first()

    @staticmethod
    def validate(short_link):
        if short_link:
            if len(short_link) > LENGTH_SHORT_LINK_USER:
                raise TooLongShortLinkException(Errors.WRONG_FORMAT_SHORT_LINK)
            if not re.match(REGEXP_SHORT_VALIDATOR, short_link):
                raise WrongFormatShortLinkException(
                    Errors.WRONG_FORMAT_SHORT_LINK
                )
            if URLMap.get(short_link):
                raise ShortLinkExistsException(Errors.SHORT_LINK_EXISTS)
            return short_link
        else:
            while True:
                short_link = ''.join(
                    random.choice(ALLOWED_CHARS_SHORT_LINK)
                    for _ in range(LENGTH_SHORT_LINK_AUTO)
                )
                if not URLMap.get(short_link):
                    return short_link

    @staticmethod
    def creat_urlmap(original_link, short_link):
        url = URLMap(original=original_link, short=short_link)
        db.session.add(url)
        db.session.commit()

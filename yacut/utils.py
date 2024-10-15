import random
import re

from yacut import db
from yacut.constants import (
    ALLOWED_CHARS_SHORT_LINK,
    LENGTH_SHORT_LINK_AUTO,
    LENGTH_SHORT_LINK_USER,
    REGEXP_SHORT_VALIDATOR,
    Errors,
)
from yacut.error_handlers import (
    ShortLinkExistsException,
    TooLongShortLinkException,
    WrongFormatShortLinkException,
)
from yacut.models import URLMap


def get_link(short_link):
    return URLMap.query.filter_by(short=short_link).first()


def validate_short_link(short_link):
    if len(short_link) > LENGTH_SHORT_LINK_USER:
        raise TooLongShortLinkException(Errors.WRONG_FORMAT_SHORT_LINK)
    if not re.match(REGEXP_SHORT_VALIDATOR, short_link):
        raise WrongFormatShortLinkException(Errors.WRONG_FORMAT_SHORT_LINK)
    if get_link(short_link):
        raise ShortLinkExistsException(Errors.SHORT_LINK_EXISTS)
    return short_link


def creat_short_link():
    while True:
        short_link = "".join(
            random.choice(ALLOWED_CHARS_SHORT_LINK)
            for _ in range(LENGTH_SHORT_LINK_AUTO)
        )
        if not get_link(short_link):
            return short_link


def create_url_map(original_link, short_link):
    url = URLMap(original=original_link, short=short_link)
    db.session.add(url)
    db.session.commit()

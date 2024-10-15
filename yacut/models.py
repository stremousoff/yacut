from datetime import datetime

from yacut import db
from yacut.constants import LENGTH_SHORT_LINK_USER


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String, nullable=False)
    short = db.Column(db.String(LENGTH_SHORT_LINK_USER), unique=True)
    timestamp = db.Column(db.DateTime, default=datetime.now)

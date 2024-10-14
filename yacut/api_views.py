from http import HTTPStatus

from flask import jsonify, request

from yacut.error_handlers import (InvalidAPIUsage, ShortLinkExistsException,
                                  TooLongShortLinkException,
                                  WrongFormatShortLinkException)
from yacut.models import URLMap

from . import app
from .constants import Errors


@app.route('/api/id/', methods=('POST',))
def add_url():
    data = request.get_json(silent=True)
    if not data:
        raise InvalidAPIUsage(Errors.EMPTY_REQUEST, HTTPStatus.BAD_REQUEST)
    if not data.get('url'):
        raise InvalidAPIUsage(Errors.EMPTY_URL, HTTPStatus.BAD_REQUEST)
    try:
        short_link = URLMap.validate(data.get('custom_id'))
        URLMap.creat_urlmap(data.get('url'), short_link)
    except (TooLongShortLinkException, ShortLinkExistsException,
            WrongFormatShortLinkException, InvalidAPIUsage) as exception:
        return jsonify({'message': str(exception)}), HTTPStatus.BAD_REQUEST
    return jsonify(
        {
            'url': data.get('url'),
            'short_link': f'{request.url_root}{short_link}'
        }
    ), HTTPStatus.CREATED


@app.route('/api/id/<string:short_id>/', methods=('GET',))
def get_url(short_id):
    urlmap = URLMap.get(short_id)
    if not urlmap:
        raise InvalidAPIUsage(Errors.EMPTY_SHORT_LINK, HTTPStatus.NOT_FOUND)
    return jsonify({'url': urlmap.original}), HTTPStatus.OK

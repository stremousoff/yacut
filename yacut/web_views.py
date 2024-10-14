from http import HTTPStatus

from flask import flash, redirect, render_template, url_for

from . import app
from .error_handlers import (ShortLinkExistsException,
                             TooLongShortLinkException,
                             WrongFormatShortLinkException)
from .forms import URLForm
from .models import URLMap


@app.route('/', methods=('GET', 'POST'))
def index_view():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    try:
        short_link = URLMap.validate(form.custom_id.data)
        URLMap.creat_urlmap(form.original_link.data, short_link)
        return render_template(
            'index.html',
            form=form,
            result_url=url_for('redirect_view', short_id=short_link,
                               _external=True)
        )
    except (TooLongShortLinkException, ShortLinkExistsException,
            WrongFormatShortLinkException) as exception:
        flash(str(exception))
        return render_template('index.html', form=form)


@app.route('/<string:short_id>', methods=('GET',))
def redirect_view(short_id):
    url = URLMap.get(short_id)
    if url:
        return redirect(url.original)
    return render_template('error_pages/404.html'), HTTPStatus.NOT_FOUND

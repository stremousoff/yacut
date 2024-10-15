from flask import flash, redirect, render_template, url_for

from . import app
from .error_handlers import (
    ShortLinkExistsException,
    TooLongShortLinkException,
    WrongFormatShortLinkException,
)
from .forms import URLForm
from .models import URLMap
from .utils import creat_short_link, create_url_map, validate_short_link


@app.route("/", methods=("GET", "POST"))
def index_view():
    form = URLForm()
    if not form.validate_on_submit():
        return render_template("index.html", form=form)
    try:
        short_link = (
            validate_short_link(form.custom_id.data)
            if form.custom_id.data
            else creat_short_link()
        )
        create_url_map(form.original_link.data, short_link)
        return render_template(
            "index.html",
            form=form,
            result_url=url_for(
                "redirect_view", short_id=short_link, _external=True
            ),
        )
    except (
        TooLongShortLinkException,
        ShortLinkExistsException,
        WrongFormatShortLinkException,
    ) as exception:
        flash(str(exception))
        return render_template("index.html", form=form)


@app.route("/<string:short_id>", methods=("GET",))
def redirect_view(short_id):
    return redirect(
        URLMap.query.filter_by(short=short_id).first_or_404().original
    )


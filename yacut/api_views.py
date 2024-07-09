import re
from flask import request, jsonify, url_for

from . import app, db
from .constants import (
    MAX_CUSTOM_ID_LENGTH,
    CUSTOM_ID_REGEX,
    MAX_ORIGINAL_LINK_LENGTH,
    HTTP_BAD_REQUEST,
    HTTP_CREATED,
    HTTP_NOT_FOUND,
    HTTP_OK,
)
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id


@app.route("/api/id/", methods=["POST"])
def create_short_url():
    if not request.is_json:
        raise InvalidAPIUsage("Отсутствует тело запроса", HTTP_BAD_REQUEST)
    data = request.get_json(silent=True)
    if data is None:
        raise InvalidAPIUsage("Отсутствует тело запроса", HTTP_BAD_REQUEST)
    if "url" not in data:
        raise InvalidAPIUsage(
            '"url" является обязательным полем!',
            HTTP_BAD_REQUEST
        )
    original_link = data.get("url")
    if len(original_link) > MAX_ORIGINAL_LINK_LENGTH:
        raise InvalidAPIUsage("Ссылка слишком длинная", HTTP_BAD_REQUEST)
    custom_id = data.get("custom_id") or get_unique_short_id()
    if custom_id and (
        len(custom_id) > MAX_CUSTOM_ID_LENGTH
        or not re.match(CUSTOM_ID_REGEX, custom_id)
    ):
        raise InvalidAPIUsage(
            "Указано недопустимое имя для короткой ссылки",
            HTTP_BAD_REQUEST
        )
    if URLMap.query.filter_by(short=custom_id).first():
        raise InvalidAPIUsage(
            "Предложенный вариант короткой ссылки уже существует.",
            HTTP_BAD_REQUEST
        )
    url_map = URLMap()
    url_map.from_dict({"original": original_link, "short": custom_id})
    db.session.add(url_map)
    db.session.commit()
    short_link = url_for("redirect_to_original",
                         short_id=custom_id, _external=True)
    return jsonify({"url": original_link,
                    "short_link": short_link}
                   ), HTTP_CREATED


@app.route("/api/id/<short_id>/", methods=["GET"])
def get_original_url(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()
    if not url_map:
        raise InvalidAPIUsage("Указанный id не найден", HTTP_NOT_FOUND)
    return jsonify(url_map.to_dict_url_only()), HTTP_OK

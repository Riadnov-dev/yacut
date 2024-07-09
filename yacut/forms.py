from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL, Regexp

from .constants import (
    MAX_ORIGINAL_LINK_LENGTH,
    MAX_CUSTOM_ID_LENGTH,
    CUSTOM_ID_REGEX
)


class UrlMapForm(FlaskForm):
    original_link = StringField(
        "Длинная ссылка",
        validators=[
            DataRequired(message="Обязательное поле"),
            Length(1, MAX_ORIGINAL_LINK_LENGTH),
            URL(message="Введите корректный URL"),
        ],
    )
    custom_id = StringField(
        "Ваш вариант короткой ссылки",
        validators=[
            Length(max=MAX_CUSTOM_ID_LENGTH),
            Optional(),
            Regexp(
                CUSTOM_ID_REGEX,
                message="Cсылка может содержать лишь латинские буквы и цифры",
            ),
        ],
    )
    submit = SubmitField("Создать")

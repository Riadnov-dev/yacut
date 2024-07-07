from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length, Optional, URL


class UrlMapForm(FlaskForm):
    original_link = StringField(
        "Длинная ссылка",
        validators=[
            DataRequired(message="Обязательное поле"),
            Length(1, 2048),
            URL(message="Введите корректный URL"),],)
    custom_id = StringField(
        "Ваш вариант короткой ссылки",
        validators=[Length(max=16),
                    Optional()])
    submit = SubmitField("Создать")

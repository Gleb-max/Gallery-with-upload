from flask_wtf import FlaskForm
from wtforms import SubmitField, FileField
from wtforms.validators import DataRequired


class PhotoUpload(FlaskForm):
    photo = FileField("Добавить картинку", validators=[DataRequired()])
    submit = SubmitField("Отправить")

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    # index.htmlのimage_pathの入力フォーム設定
    image_path = StringField('image_path', validators=[DataRequired()])

from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, DecimalField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange

class ProductForm(FlaskForm):
    sku = StringField('SKU', validators=[DataRequired(), Length(max=64)])
    name = StringField('Name', validators=[DataRequired(), Length(max=200)])
    description = TextAreaField('Description', validators=[Length(max=2000)])
    quantity = IntegerField('Quantity', validators=[DataRequired(), NumberRange(min=0)])
    price = DecimalField('Price', validators=[DataRequired(), NumberRange(min=0)])
    supplier = StringField('Supplier', validators=[Length(max=200)])
    submit = SubmitField('Save')

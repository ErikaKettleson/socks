from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectMultipleField, widgets
from wtforms.validators import DataRequired

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class AddressForm(FlaskForm):
    sock_options = ['Mohair', 'Fur', 'Mesh', 'Tufted', 'Crochet']
    options = [(x, x) for x in sock_options]

    socks = MultiCheckboxField('Socks In Stock', choices=options)
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    street = StringField('Street', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])

    submit = SubmitField('Place 2-Hr Delivery Order')

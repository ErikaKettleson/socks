from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectMultipleField, widgets
from wtforms.validators import DataRequired

class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


class AddressForm(FlaskForm):
    sock_options = ['Mohair\rFur\rMesh\rCrochet\rTufted\n']
    list_of_socks = sock_options[0].split()
    # create a list of value/description tuples
    options = [(x, x) for x in list_of_socks]

    socks = MultiCheckboxField('Socks', choices=options)
    name = StringField('Name', validators=[DataRequired()])
    phone = StringField('Phone', validators=[DataRequired()])
    street = StringField('Street', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])

    submit = SubmitField('Check Delivery Availability')

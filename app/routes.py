from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import AddressForm
import requests
import json


@app.route('/')
@app.route('/index')
def index():
    socks = [
        {
            'name': 'Mohair',
            'size': 'One-Size'
        },
        {
            'name': 'Fur',
            'size': 'One-Size'
        },
        {
            'name': 'Mesh',
            'size': 'One-Size'
        },
        {
            'name': 'Tufted',
            'size': 'One-Size'
        },
        {
            'name': 'Crochet',
            'size': 'One-Size'
        },
    ]
    return render_template('index.html', title='Home', socks=socks)


@app.route('/order', methods=['GET', 'POST'])
def order():
    form = AddressForm()
    if form.validate_on_submit():
        dropoff_address = form.street.data + ' ' + \
            form.city.data + ' ' + form.state.data
        print('Quote Submitted for address {}'.format(dropoff_address))

        quote_data = {
            'dropoff_address': dropoff_address,
            'pickup_address': '155 Lexington St. San Francisco, CA'
        }
        auth = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic NGJkNTFmMWQtM2ViMS00ZTM0LTkyOWUtOGMxMGU1OTI2ZmNhOg=='
        }
        res = requests.post(
            'https://api.postmates.com/v1/customers/cus_MpuW-m0uomjj7F/delivery_quotes', data=quote_data, headers=auth)
        quote_id = res.json()['id']

        if res.status_code != 200:
            return _('We\'re Sorry: Delivery not available.')
        else:
            print('Submitted Quote, got id {}, about to Submit Order {}'.format(
                quote_id, dropoff_address))

            items = [
                {
                'name': 'Mohair',
                'quantity': 1,
                'size': 'small'
                }
            ]

            order_data = {
                'dropoff_address': dropoff_address,
                'dropoff_name': 'erika',
                'dropoff_phone_number': '9085918760',
                'pickup_address': '155 Lexington St. San Francisco, CA',
                'pickup_name': 'SF Socks Store',
                'pickup_phone_number': '9082477262',
                'quote_id': quote_id,
                'manifest': 'socks',
                'manifest_items': json.dumps(items),
            }

            resp = requests.post(
                'https://api.postmates.com/v1/customers/cus_MpuW-m0uomjj7F/deliveries', data=order_data, headers=auth)

            print(resp.status_code, resp.json())

    return render_template('order.html', title='Order Socks', form=form)

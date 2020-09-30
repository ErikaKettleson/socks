from flask import render_template, flash, redirect, url_for
from datetime import datetime, timedelta
from pytz import timezone, utc
from app import app
from app.forms import AddressForm
import requests
import json


@app.route('/debug-sentry', methods=['GET', 'POST'])
def trigger_error():
    division_by_zero = 1 / 0
    # trigger sentry error (visible in sentry dashboard)

@app.route('/', methods=['GET', 'POST'])
def order():
    form = AddressForm()
    if form.validate_on_submit():
        dropoff_address = form.street.data + ' ' + \
            form.city.data + ' ' + form.state.data
        
        current_utc = datetime.utcnow()
        deadline_utc = current_utc + timedelta(hours=2)
        time = utc.localize(deadline_utc, is_dst=None).astimezone(timezone('US/Pacific')).isoformat()

        quote_data = {
            'dropoff_address': dropoff_address,
            'pickup_address': '155 Lexington St. San Francisco, CA',
            'dropoff_deadline_dt': time
        }
        auth = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Authorization': 'Basic NGJkNTFmMWQtM2ViMS00ZTM0LTkyOWUtOGMxMGU1OTI2ZmNhOg=='
        }
        res = requests.post(
            'https://api.postmates.com/v1/customers/cus_MpuW-m0uomjj7F/delivery_quotes', data=quote_data, headers=auth)
        
        quote_id = res.json()['id']

        if res.status_code != 200:
            return ('We\'re Sorry: Delivery not available.')
        else:
            items = list()

            for i in range(len(form.socks.data)):
                items.append({
                    'name': form.socks.data[i],
                    'quantity': 1,
                    'size': 'small'
                })

            order_data = {
                'dropoff_address': dropoff_address,
                'dropoff_name': form.name.data,
                'dropoff_phone_number': form.phone.data,
                'pickup_address': '155 Lexington St. San Francisco, CA',
                'pickup_name': 'SF Socks Store',
                'pickup_phone_number': '9082477262',
                'quote_id': quote_id,
                'manifest': 'socks',
                'manifest_items': json.dumps(items),
                'dropoff_deadline_dt': time
            }

            resp = requests.post(
                'https://api.postmates.com/v1/customers/cus_MpuW-m0uomjj7F/deliveries', data=order_data, headers=auth)

            if resp.status_code != 200:
                return ('We\'re Sorry: Ordering not available')
            else:
                flash('Thank you for your order!')
    return render_template('order.html', title='Order Socks', form=form)

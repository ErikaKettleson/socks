import sentry_sdk
from flask import Flask
from config import Config
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="https://d1f90ec49f6b420d8a3eb17add7653b2@o453143.ingest.sentry.io/5441633",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)

# added sentry config info
# The above configuration captures both error and performance data. To reduce the volume of performance data captured, change traces_sample_rate to a value between 0 and 1.

app = Flask(__name__)
app.config.from_object(Config)

from app import routes
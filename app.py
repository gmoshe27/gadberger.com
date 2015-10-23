from flask import Flask
from app_start import register_views
import config

# create our little application :)
app = Flask(__name__)
app.config.from_object(config)

# create our views and routes
register_views.register_views(app)

from flask_flatpages import FlatPages
flatpages = FlatPages(app)

if __name__ == "__main__":
    app.run(debug=True)
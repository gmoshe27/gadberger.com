from flask import Flask
from app_start import register_views

# create our little application :)
app = Flask(__name__)
#app.config.from_object(__name__)

# create our views and routes
register_views.register_views(app)

if __name__ == "__main__":
    app.run(debug=True)
from views.home_view import HomeView

def register_views(app):
    HomeView.register(app, route_base="/")

from app.views.home_view import HomeView
from app.views.posts_view import PostsView

def register_views(app):
    HomeView.register(app, route_base="/")
    PostsView.register(app)

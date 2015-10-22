from flask import Flask, request, render_template, jsonify, g, current_app
from flask.ext.classy import FlaskView

class PostsView(FlaskView):
    def index(self):
        # return a list of posts available on the site
        return render_template("posts/index.html")

    def get(self, name):
        path = "{}/{}".format(POST_DIR, name)
        post = flatpages.get_or_404(path)
        return render_template("post.html", post=post)

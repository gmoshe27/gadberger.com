from flask import Flask, request, render_template, jsonify, g, current_app
from flask.ext.classy import FlaskView


class PostsView(FlaskView):
    def index(self):
        # return a list of posts available on the site
        return render_template("posts/index.html")

    def get(self, name):
        from app import flatpages

        post_dir = current_app.config["POST_DIR"]
        path = "{}/{}".format(post_dir, name)
        post = flatpages.get_or_404(path)
        return render_template("posts/index.html", post=post)

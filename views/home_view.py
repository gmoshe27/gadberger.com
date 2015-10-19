#from flask import Flask, request, render_template, jsonify, g, current_app
from flask.ext.classy import FlaskView

class HomeView(FlaskView):
    def index(self):
        return "¡hola, mundo!"

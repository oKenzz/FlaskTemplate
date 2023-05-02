from flask import jsonify, Blueprint, render_template

routes = Blueprint(__name__, "server")

@routes.route('/')
def Home():
    return "Hello World"



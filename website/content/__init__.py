from flask import Blueprint

bp = Blueprint('content', __name__, template_folder='templates')

from . import views
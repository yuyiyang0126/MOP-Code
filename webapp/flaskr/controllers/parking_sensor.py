import json
from flask import Blueprint, jsonify, render_template, request
from flask.helpers import send_file


bp = Blueprint('parking_sendor', __name__, url_prefix='/parking_sensor')
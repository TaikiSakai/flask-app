from flask import Blueprint, jsonify
# from service.spanish import conjugation
from . import auth
from . import logger

router = Blueprint('router', __name__)

@router.route("/api_health", methods=['GET'])
def health_check():
    return jsonify({"api_status": "ok"})

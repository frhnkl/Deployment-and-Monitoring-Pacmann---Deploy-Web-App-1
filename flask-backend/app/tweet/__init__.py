from flask import Blueprint
from flask_cors import CORS

tweetBp = Blueprint('tweet', __name__)
CORS(tweetBp, supports_credentials=True)
from app.tweet import routes
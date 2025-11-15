from flask_jwt_extended import JWTManager
from configs import CONFIG as config
from services.controller import *
from flask import Flask, Response
from services.controller import *
from flask_restful import Api
from flask_cors import CORS
import awsgi


app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = config.JWT_SECRET_KEY
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = config.JWT_ACCESS_TOKEN_EXPIRES
app.config['JWT_REFRESH_TOKEN_EXPIRES'] = config.JWT_REFRESH_TOKEN_EXPIRES

api = Api(app)
JWTManager(app)
CORS(app, supports_credentials=True)


api.add_resource(UserService, '/api/user')
api.add_resource(UserLoginService, '/api/login')


@app.after_request
def handle_after_request(response: Response) -> Response:
    # Add any headers or logging here if needed
    return response


def handler(event, context) -> dict:
    print(event)
    return awsgi.response(app, event, context)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

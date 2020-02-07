from flask import Flask, request
from flask_restful import Resource, Api
from model import predict

app = Flask(__name__)
api = Api(app)

class Demo(Resource):
    def get(self):        
        return {
            "status": 200
        }

    def post(self):
        req = request.get_json()
        ans = predict(req['url'])

        return {
            "status": 200,
            "req": req,
            "url": req['url'],
            "predict": ans
        }

class Multi(Resource):
    def get(self, num):
        return {
            "status": 200,
            "result": num * 100
        }


api.add_resource(Demo, "/")
api.add_resource(Multi, "/multi/<int:num>")

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=True,
        threaded=False
    )
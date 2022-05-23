from flask import Flask, request, jsonify
from VirtualAdapter import VirtualAdapter
from adapter import Adapter
from flask_restful import Api, Resource
from flask_ngrok import run_with_ngrok
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
api = Api(app)


@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())

class RadioData(Resource):
    def get(self):
        data = {}
        #adapter = VirtualAdapter(data)
        adapter = Adapter(data)
        print(adapter.result)
        return jsonify(adapter.result)

api.add_resource(RadioData, '/radioData')
run_with_ngrok(app)

# @app.route('/', methods=['GET', 'POST'])
# def call_adapter():
#     # this is where the node would call the external adapter.
#     # data = request.get_json()
#     # if data == '':
#     #     data = {}
#     data = {}
#     adapter = VirtualAdapter(data)
#     print(adapter.result)
#     return jsonify(adapter.result)

if __name__ == '__main__':
    app.run()

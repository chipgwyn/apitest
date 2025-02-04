import json
from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return f'Requested Path: {path}'

@app.after_request
def details(response):
    data = {
        'path': request.path,
        'method': request.method,
        'headers': dict(request.headers),
        'args': dict(request.args),
        'form': dict(request.form),
        'data': request.data.decode('utf-8'),
        'response': response.data.decode('utf-8')
    }
    response.data = json.dumps(data)
    return response

if __name__ == '__main__':
    app.run()
from flask import Flask, jsonify

app = Flask(__name__)

@app.errorhandler(404)
def not_found_error(error):
    response = jsonify({'error': 'Not found'})
    response.status_code = 404
    return response

if __name__ == '__main__':
    app.run()


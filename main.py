
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/request-data', methods=['GET', 'POST'])
def request_data():
  headers = request.headers
  method = request.method
  body = request.get_data()

  return jsonify({
    'headers': headers,
    'method': method,
    'body': body.decode('utf-8')
  })

if __name__ == '__main__':
  app.run(debug=True)

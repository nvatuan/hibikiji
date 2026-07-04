import os
from flask import Flask, request, jsonify

from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

from repo.calculation_history import CalculationHistoryStorage
storage = CalculationHistoryStorage()

HeaderKeySessionKey = 'X-Calc-Session-Key'

# Health check API
@app.route('/health', methods=['GET'])
@cross_origin()
def health_check():
  return jsonify({'message': 'ok'})

# Get History
@app.route('/api/v1/history', methods=['GET'])
@cross_origin()
def get_history():
  session_key = request.headers.get(HeaderKeySessionKey)  
  if session_key is None:
    return jsonify({'error': 'Session key must be set'}), 400

  try:
    history = storage.load_history(session_key)
  except Exception as e:
    print(f"Error: {e}")
    return jsonify({
      'message': 'Internal error',
    })

  return jsonify({
    'message': 'OK',
    'data': {
      'history': history,
    }
  })

# Save state API
@app.route('/api/v1/history', methods=['POST'])
@cross_origin()
def save_history():
  session_key = request.headers.get(HeaderKeySessionKey)  
  if session_key is None:
    return jsonify({'error': 'Session key must be set'}), 400
  
  data = request.get_json()
  if data.get('button') is None:
    return jsonify({'error': 'Button must be set'}), 400

  try:
    history = storage.append_to_history(session_key, data.get('button'), data.get('result'))
  except:
    return jsonify({
      'message': 'Internal error',
    })
    raise

  return jsonify({
    'message': 'State saved successfully',
    'data': {
      'history': history,
    }
  })

# Save state API
@app.route('/api/v1/history/delete', methods=['POST'])
@cross_origin()
def delete_history():
  session_key = request.headers.get(HeaderKeySessionKey)  
  if session_key is None:
    return jsonify({'error': 'Session key must be set'}), 400
  
  try:
    history = storage.delete_history(session_key)
  except:
    return jsonify({
      'message': 'Internal error',
    })
    raise

  return jsonify({
    'message': 'State saved successfully',
    'data': {
      'history': history,
    }
  })

if __name__ == '__main__':
  print(f"Storage backend: {storage.storage_backend}")

  if os.environ.get('FAIL_WITH_REDIS') == 'true':
    if storage.storage_backend != 'redis':
      raise Exception("Application is forced to run with Redis Redis is not available. Exiting.")

  if 'HOST' in os.environ and 'PORT' in os.environ:
    host = os.environ['HOST']
    port = int(os.environ['PORT'])
  else:
    host = '127.0.0.1'
    port = 5070

  app.run(host=host, port=port)
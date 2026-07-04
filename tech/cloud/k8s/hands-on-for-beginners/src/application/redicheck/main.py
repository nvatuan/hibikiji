from flask import Flask, jsonify
import redis
import os

app = Flask(__name__)

redis_host = os.environ.get('REDISHOST', 'localhost')
redis_port = int(os.environ.get('REDISPORT', '6379'))
redis_client = redis.Redis(host=redis_host, port=redis_port)

@app.route('/redicheck', methods=['GET'])
def check_redis_connection():
  try:
    redis_client.ping()
    return jsonify({'message': 'Redis connection is good'})
  except redis.exceptions.ConnectionError:
    return jsonify({'message': 'Unable to connect to Redis'}), 500

if __name__ == '__main__':
  app.run(host=os.environ.get('HOST', '0.0.0.0'), port=int(os.environ.get('PORT', '5071')))
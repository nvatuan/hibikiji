import redis
import os
import json

class RedisConfig:
  def __init__(self, host, port):
    self.host = host
    self.port = port
    self.validate()

  def validate(self):
    if not self.host or not self.port:
      raise ValueError("Redis host and port must be set")
  
  def get_host(self):
    return self.host
  
  def get_port(self):
    return self.port
  
  def init_redis_client(self):
    client = redis.Redis(host=self.host, port=self.port)
    if client.ping():
      return client
    else:
      raise redis.ConnectionError("Could not connect to Redis")
  
default_redis_config = RedisConfig(os.environ['REDIS_HOST'], os.environ['REDIS_PORT'])

class RedisStorage:
  def __init__(self, redis_config=default_redis_config):
    redis_client = redis_config.init_redis_client()
    self.redis_client = redis_client
  
  def update_history_add_entry(self, session_key, data):
    if session_key is None:
      print("History not avaible without session key.")
      return None

    history = self.load_history(session_key) 
    history.append(data)
    self.redis_client.set(session_key, json.dumps(history))
    return history
  
  def load_history(self, session_key):
    if session_key is None:
      print(f"session_key='{session_key}': No history available without session key.")
      return None
    
    print(f"session_key='{session_key}': Loading history from Redis")
    raw_data = self.redis_client.get(session_key)
    if raw_data is None:
      return []
    history = json.loads(raw_data)
    return history
  
  def delete_history(self, session_key):
    if session_key is None:
      print(f"session_key='{session_key}': No history available without session key.")
      return None

    self.redis_client.delete(session_key) 
    return []
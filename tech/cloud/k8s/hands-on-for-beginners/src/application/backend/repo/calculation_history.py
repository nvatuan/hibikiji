from datetime import datetime
import redis
from storage.redis import RedisStorage
from storage.local import LocalStorage

class CalculationHistoryEntry():
  def __init__(self, button, result):
    self.button = button
    self.result = result
    self.timestamp = datetime.now()
  
  def to_dict(self):
    return {
      'button': self.button,
      'result': self.result,
      'timestamp': self.timestamp.isoformat()
    }

class CalculationHistoryStorage():
  def __init__(self):
    try:
      self.storage = RedisStorage()
      self.storage_backend = 'redis'
      print("Connected to Redis successfully!")

    except redis.ConnectionError:
      print("Redis is not available. Falling back to in-memory storage.")
      self.storage = LocalStorage()
      self.storage_backend = 'local'
  
  def append_to_history(self, session_key, button, result):
    entry = CalculationHistoryEntry(button, result)
    return self.storage.update_history_add_entry(session_key, entry.to_dict())

  def load_history(self, session_key):
    return self.storage.load_history(session_key)
 
  def delete_history(self, session_key):
    return self.storage.delete_history(session_key)

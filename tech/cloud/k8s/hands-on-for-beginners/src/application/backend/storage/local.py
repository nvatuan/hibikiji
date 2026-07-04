import json

class LocalStorage:
  def __init__(self):
    self.entries = {}
  
  def update_history_add_entry(self, session_key, data):
    super().update_history_add_entry(session_key)

    history = self.load_history(session_key) 
    history.append(data)
    self.entries[session_key] = history
    return history
  
  def load_history(self, session_key):
    super().load_history(session_key)

    print(f"session_key='{session_key}': Loading history from Local")
    history = self.entries.get(session_key)
    if history is None:
      return []
    return history
  
  def delete_history(self, session_key):
    super().delete_history(session_key)
    del self.entries[session_key]
    return []
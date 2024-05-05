class Interface:
  def __init__(self):
    pass

  def validate(self, session_key):
    if not session_key:
      print(f"session_key='{session_key}': History not avaible without session key.")
      raise ValueError("Session key must be set")

  def update_history_add_entry(self, session_key):
    self.validate(session_key)
  
  def load_history(self, session_key):
    self.validate(session_key)
  
  def delete_history(self, session_key):
    self.validate(session_key)
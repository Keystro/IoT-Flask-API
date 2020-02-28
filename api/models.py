from datetime import datetime
from api import db, login_manager

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(20), unique=True, nullable = False)
  password = db.Column(db.String(60), nullable=False)

  def __repr__(self):
    return f"User('{self.username}')"

class Vault(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    device_name = db.Column(db.String(40), unique = True, nullable = False)
    low = db.Column(db.Integer, nullable=False)
    Lights_on = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    high = db.Column(db.Integer, nullable=False)
    Lights_off = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)

    def __repr__(self):
        return f"IOT('{self.device_name}','{self.low}','{self.Lights_on}','{self.high}','{self.Lights_off}')"



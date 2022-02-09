from application import db
from application.models import games
db.drop_all()
db.create_all()
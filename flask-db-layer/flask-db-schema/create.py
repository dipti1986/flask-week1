from app import db, Users,people

db.drop_all()
db.create_all()

testuser = Users(first_name='dipti',last_name='choudhary') 
testperson=people(name="John", alive=False,height=2.1)
db.session.add(testperson)
db.session.add(testuser)
db.session.commit()

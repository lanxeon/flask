from third import db

class Table1(db.Model):
	id=db.Column(db.Integer,primary_key=True, autoincrement=True)
	name=db.Column(db.String(20),nullable=False,unique=True)
	eye=db.Column(db.String(20))
	nose=db.Column(db.String(20))
	lips=db.Column(db.String(20))
	image=db.Column(db.String(20),nullable=False, default='default.jpg')

	def __repr__(self):
		return f"User(name:'{self.name}', eye:'{self.eye}', nose:'{self.nose}', lips:'{self.lips}')"
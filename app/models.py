from app import db
class Requirement(db.Model):
    __tablename__ = "requirements"
    __table_args__ = {"mysql_charset": "utf8"}
    id=db.Column(db.Integer,primary_key=True)
    text=db.Column(db.String(200))
    pinginfo_id=db.Column(db.Integer,db.ForeignKey("pinginfos.id"))

class PingInfo(db.Model):
    __tablename__="pinginfos"
    __table_args__ = {"mysql_charset": "utf8"}
    id=db.Column(db.Integer,primary_key=True)
    company=db.Column(db.SmallInteger)
    category=db.Column(db.SmallInteger)
    jobTitle=db.Column(db.String(100))
    time=db.Column(db.String(50))
    location=db.Column(db.String(100))
    link=db.Column(db.String(200))
    email=db.Column(db.String(100))
    requirements=db.relationship(Requirement)

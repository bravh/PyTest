from . import db
from flask_login import UserMixin



class Cabinets(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    cabname = db.Column(db.String(10000))
    cabwidth = db.Column(db.Float, nullable=False)
    cabhight = db.Column(db.Float,nullable=False)
    cabdepth = db.Column(db.Float, nullable=False)
    hinging = db.Column(db.String(10))
    endtypes = db.Column(db.String(10))
    quantity =  db.Column(db.Integer, nullable=False)
    comment = db.Column(db.String(10000))
    wallnum = db.Column(db.String(10000))
    offsetwallstart = db.Column(db.Float, nullable=False)
    distancefromfloor = db.Column(db.Float,nullable=False)
    outset = db.Column(db.Float, nullable=False)
    cabtype =  db.Column(db.Integer, nullable=False)
    fillmode =  db.Column(db.Integer, nullable=False)
    sectioncode = db.Column(db.String(10000))
    cabinetid = db.Column(db.String(10000))
    modifycode = db.Column(db.String(10000))
    


class User(db.Model , UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    address = db.Column(db.String(150))
    phone = db.Column(db.String(150))
    admin = db.Column(db.Boolean, default=False)
    
class ConMeths(db.Model):
     id = db.Column(db.Integer, primary_key=True, nullable=False)
     name = db.Column(db.String(150), unique=True)
     cvname = db.Column(db.String(150), unique=True)
   
class Sokels(db.Model):
     id = db.Column(db.Integer, primary_key=True, nullable=False)
     name = db.Column(db.String(150), unique=True)
     cvname = db.Column(db.String(150), unique=True)
     
class Doors(db.Model):
     id = db.Column(db.Integer, primary_key=True, nullable=False)
     name = db.Column(db.String(150), unique=True)
     cvname = db.Column(db.String(150), unique=True)
     ddb = db.Column(db.String(150), unique=True)
     
     
class CabMats(db.Model):
     id = db.Column(db.Integer, primary_key=True, nullable=False)
     name = db.Column(db.String(150), unique=True)
     cvname = db.Column(db.String(150), unique=True)
     
class Pulls(db.Model):
     id = db.Column(db.Integer, primary_key=True, nullable=False)
     name = db.Column(db.String(150), unique=True)
     cvname = db.Column(db.String(150), unique=True)
     
     
class RoolOuts(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(150), unique=True)
    cvname = db.Column(db.String(150), unique=True)
     
   
   
    
   
    
    

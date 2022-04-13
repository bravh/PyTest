from . import db
from flask_login import UserMixin


class User(db.Model , UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    last_name = db.Column(db.String(150))
    address = db.Column(db.String(150))
    phone = db.Column(db.String(150))
    admin = db.Column(db.Boolean, default=False)

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
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

class ConMeths(db.Model):
     id = db.Column(db.Integer, primary_key=True, nullable=False)
     name = db.Column(db.String(150), )
     cvname = db.Column(db.String(150), unique=True)
     CType = db.Column(db.String(150))
     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    
     
   
class Sokels(db.Model):
     id = db.Column(db.Integer, primary_key=True, nullable=False)
     name = db.Column(db.String(150), )
     cvname = db.Column(db.String(150), unique=True)
     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
     
class Doors(db.Model):
     id = db.Column(db.Integer, primary_key=True, nullable=False)
     name = db.Column(db.String(150), )
     cvname = db.Column(db.String(150), unique=True)
     DType = db.Column(db.String(150))
     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
          
class Materials(db.Model):
     id = db.Column(db.Integer, primary_key=True, nullable=False)
     name = db.Column(db.String(150), )
     cvname = db.Column(db.String(150), unique=True)
     MType = db.Column(db.String(150))
     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class Pulls(db.Model):
     id = db.Column(db.Integer, primary_key=True, nullable=False)
     name = db.Column(db.String(150), )
     cvname = db.Column(db.String(150), unique=True)
     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
     
class Drawers(db.Model):
     id = db.Column(db.Integer, primary_key=True, nullable=False)
     name = db.Column(db.String(150), )
     cvname = db.Column(db.String(150), unique=True)
     dwtype = db.Column(db.String(150))
     user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


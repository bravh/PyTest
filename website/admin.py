from flask import Blueprint, render_template, request, redirect, url_for
from .models import ConMeths, Sokels, Doors, Materials, Pulls, Drawers
from flask_login import  login_required, current_user, logout_user 
from flask import send_file
from flask_sqlalchemy import SQLAlchemy

from . import db

admin = Blueprint('admin', __name__)

@admin.route('/admin', methods=['GET', 'POST'])
@login_required
def Admin():
     return render_template("Admin.html", user = current_user)
     

@admin.route('/admin/Newuser', methods=['GET', 'POST'])
@login_required
def Newuser():
    if request.method == 'POST':
            g = request.form.get('selected')
            
         
            if g == 'newuser':
                logout_user()
                return redirect(url_for('auth.sign_up'))
           
            else:
                return redirect(url_for('views.home'))

@admin.route('/admin/createnewdb', methods=['GET', 'POST'])
@login_required
def createnewdb():
    if request.method == 'POST':
        g = request.form.get('selected')
        conmeth = request.form.get('constr')
        guide = request.form.get('mesila')
        webname =request.form.get('webname')
        cvname =request.form.get('cvname')
        print(g)
       
        if g == "CM" or g == "DWM" or g == "DNPM" or g == "DP":
            new_material = Materials( name=webname, cvname = cvname, MType = g, user_id = current_user.id)
            db.session.add(new_material)
            db.session.commit()
            return render_template('admin.html', user=current_user)
        
        if g == "CCM" or g == "CDWM":
            new_constract = ConMeths( name=webname, cvname = cvname, CType = g, user_id = current_user.id)
            db.session.add(new_constract)
            db.session.commit()
            return render_template('admin.html', user=current_user)

        if g == "XDP" or g == "XDNP":
            new_door = Doors( name=webname, cvname = cvname, DType = g, user_id = current_user.id)
            db.session.add(new_door)
            db.session.commit()
            return render_template('admin.html', user=current_user)

        if g == "MDW":
            new_ddrawed = Drawers( name=webname, cvname = cvname, dwtype = g, user_id = current_user.id)
            db.session.add(new_ddrawed)
            db.session.commit()
            new_guide = Materials( name=guide , cvname = guide , MType = "G", user_id = current_user.id)
            db.session.add(new_guide)
            db.session.commit()
            return render_template('admin.html', user=current_user)
            
        if g =="WDW":
           new_drawer = Drawers( name=webname, cvname = cvname, dwtype = g, user_id = current_user.id)
           db.session.add(new_drawer)
           db.session.commit()
           return render_template('admin.html', user=current_user)
        
      

        else:
            webname =request.form.get('webname')
            cvname =request.form.get('cvname')
            return (g)
   

   
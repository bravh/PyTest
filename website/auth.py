from multiprocessing.sharedctypes import Value
from xml.etree.ElementTree import tostring
from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Cabinets, User, ConMeths, Sokels, Doors, CabMats, Pulls, RoolOuts
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=False)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Email does not exist.', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/sign-up', methods=['GET', 'POST'])
   
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('first_name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        last_name = request.form.get('last_name')
        address = request.form.get('address')
        phone = request.form.get('phone')
        admin = request.form.get('admin')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists.', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, first_name=first_name, last_name=last_name,address=address,phone=phone, password=generate_password_hash(
                password1, method='sha256'),admin=bool(admin))
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)

@auth.route('/CheckList' ,methods=['GET', 'POST'])
@login_required
def CheckList(): 
    conm = ConMeths.query.order_by(ConMeths.name).all()
    sokel = Sokels.query.order_by(Sokels.name).all()
    doors = Doors.query.order_by(Doors.name).all()
    cabmats = CabMats.query.order_by(CabMats.name).all()
    rolls = RoolOuts.query.order_by(RoolOuts.name).all()
    pulls = Pulls.query.order_by(Pulls.name).all()
    
    if request.method == 'POST':
        vconm = request.form.get('conmval')
        vsokel =  request.form.get('sokelval')
        vdoors = request.form.get('doorval')
        vcabmats = request.form.get('cabmatval')
        vrolls = request.form.get('rollsval')
        vpulls = request.form.get('pullsval')
        pname = request.form.get('projname')
        phone = request.form.get('phonen')
        contact = request.form.get('contactname')
        gsokel = request.form.get('sokelgovaval')
        vconm = ConMeths.query.filter_by(cvname = vconm).first()
        vsokel = Sokels.query.filter_by(cvname = vsokel).first()
        vdoors = Doors.query.filter_by(cvname = vdoors).first()
        vcabmats = CabMats.query.filter_by(cvname = vcabmats).first()
        vrolls = RoolOuts.query.filter_by(cvname = vrolls).first()
        vpulls = Pulls.query.filter_by(cvname = vpulls).first()
        
        
        return render_template('ORDFile.ord', user=current_user,gsokel = gsokel, contact = contact ,phone = phone, pname = pname ,conm= vconm ,sokel = sokel, door = vdoors, cabmats = vcabmats, rolls = vrolls, pulls= vpulls)
          
             
    
    return render_template('CheckList.html', user=current_user, conm= conm ,sokel = sokel, doors = doors, cabmats = cabmats, rolls = rolls, pulls= pulls)
    





    

    

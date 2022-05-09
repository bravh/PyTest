from flask import Blueprint, render_template, request, redirect, url_for
from .models import ConMeths, Sokels, Doors, Materials, Pulls, Drawers
from flask_login import  login_required, current_user
from flask import send_file




checklist = Blueprint('checklist', __name__)
from . import db

@checklist.route('/CheckList' ,methods=['GET', 'POST'])
@login_required
def CheckList(): 
    conm = ConMeths.query.filter_by(CType = "CCM").all()#contruction method cabinets
    cabmats = Materials.query.filter_by(MType = "CM").all() #materials for cabinet
    doorfp = Doors.query.filter_by(DType = "XDP").all() #doors for pain
    doornp = Doors.query.filter_by(DType = "XDNP").all() #doors not gor paint
    dpm = Materials.query.filter_by(MType = "DPM").all()
    metaldrawerconst = ConMeths.query.filter_by(CType = "MCDWM").all()
    dnpm = Materials.query.filter_by(MType = "DNPM").all()#materials for doors not for paot
    rolls = Drawers.query.filter_by(dwtype = "MDW").all() #MetalDrawerType
    drawermat = Materials.query.filter_by(MType = "DWM").all() #materials for drawers
    pulls = Pulls.query.order_by(Pulls.name).all() #pulls pick
    sokel = Sokels.query.order_by(Sokels.name).all() #sokel pick
    conmdw = ConMeths.query.filter_by(CType = "CDWM").all() #construction method wooden drawer box
    
    if request.method == 'POST':

        vconm = request.form.get('conmval') #get contruction method cabinets selection

        vcabmats = request.form.get('cabmatval')
        vcabmatsopen = request.form.get('cabmatvalopen')
                 

        
        if request.form.get('rollsval') == 'wooden':
            vdconm = request.form.get('conmwd') #get contruction method wooden drawer selection
        elif request.form.get('rollsval') == 'metal':
            vdconm = request.form.get('conmmd')

       
        vsokel =  request.form.get('sokelval') #get sokel selected
        vdoors = request.form.get('doorval') 
        doorsmat = request.form.get('doorsmat') 
        
        vrolls = request.form.get('rollsval')
        vpulls = request.form.get('pullsval')
        pname = request.form.get('projname')
        phone = request.form.get('phonen')
        contact = request.form.get('contactname')
        gsokel = request.form.get('sokelgovaval')
        vconm = ConMeths.query.filter_by(cvname = vconm).first()
        vsokel = Sokels.query.filter_by(cvname = vsokel).first()
        vdoors = Doors.query.filter_by(cvname = vdoors).first()
        vcabmats = Materials.query.filter_by(cvname = vcabmats).first()
        vrolls = Drawers.query.filter_by(cvname = vrolls).first()
        vpulls = Pulls.query.filter_by(cvname = vpulls).first()
        vcabmatsopen = Materials.query.filter_by(cvname = vcabmatsopen).first()
        
        return render_template('ORDFile.html', user=current_user, doorsmat= doorsmat, gsokel = gsokel,
                                                contact = contact , vcabmatsopen = vcabmatsopen
                                                ,phone = phone, pname = pname ,conm= vconm ,sokel = sokel,
                                                 door = vdoors, cabmats = vcabmats, rolls = vrolls, pulls= vpulls)
      
             
             
    
    return render_template('CheckList.html', user=current_user, metaldrawerconst = metaldrawerconst,
                                doornp=doornp ,dpm=dpm, dnpm=dnpm ,conm= conm ,drawermat = drawermat ,sokel = sokel,
                               doorfp = doorfp, cabmats = cabmats, rolls = rolls, pulls= pulls, conmdw = conmdw)
                               
@checklist.route('/person' ,methods=['GET', 'POST'])  
def person(): 
   return render_template('person.html', user=current_user)

@checklist.route('/saveord' ,methods=['GET', 'POST'])  
@login_required
def saveord():
    content = request.form.get('contentv')
    content = content.encode("windows-1255" ,"ignore") 
    print(content)
    if request.method == 'POST':
        with open("website//order.ord", "wb") as fo:
           fo.write(content)
           fo.close()
           return send_file("order.ord", as_attachment=True)
    return render_template('home.html', user=current_user)


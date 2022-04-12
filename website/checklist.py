import encodings
from flask import Blueprint, render_template, request, redirect, url_for
from .models import ConMeths, Sokels, Doors, Materials, Pulls, Drawers
from flask_login import  login_required, current_user
from flask import send_file
from bs4 import BeautifulSoup



checklist = Blueprint('checklist', __name__)

@checklist.route('/CheckList' ,methods=['GET', 'POST'])
@login_required


def CheckList(): 
    conm = ConMeths.query.filter_by(CType = "C").all()
    conmdw = ConMeths.query.filter_by(CType = "DW").all()
    sokel = Sokels.query.order_by(Sokels.name).all()
    doorfp = Doors.query.filter_by(DType = "XDP").all()
    doornp = Doors.query.filter_by(DType = "XDNP").all()
    cabmats = Materials.query.filter_by(MType = "C").all()
    drawermat = Materials.query.filter_by(MType = "DW").all()
    dnpm = Materials.query.filter_by(MType = "DNP").all()
    dpm = Materials.query.filter_by(MType = "DP").all()
    rolls = Drawers.query.filter_by(DWType = "DW").all()
    innerroll = Drawers.query.filter_by(DWType = "IDW").all()
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
        vcabmats = Materials.query.filter_by(cvname = vcabmats).first()
        vrolls = Drawers.query.filter_by(cvname = vrolls).first()
        vpulls = Pulls.query.filter_by(cvname = vpulls).first()
        
        
        return render_template('ORDFile.html', user=current_user, gsokel = gsokel,   contact = contact ,phone = phone, pname = pname ,conm= vconm ,sokel = sokel, door = vdoors, cabmats = vcabmats, rolls = vrolls, pulls= vpulls)
      
             
             
    
    return render_template('CheckList.html', user=current_user, doornp=doornp ,dpm=dpm, dnpm=dnpm ,conm= conm ,drawermat = drawermat ,sokel = sokel, doorfp = doorfp, cabmats = cabmats, rolls = rolls, pulls= pulls, conmdw = conmdw)


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


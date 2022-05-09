from flask import Blueprint, render_template, request, redirect, url_for
from .models import ConMeths, Sokels, Doors, Materials, Pulls, Drawers
from flask_login import  login_required, current_user
from flask import send_file




gallery = Blueprint('gallery', __name__)
from . import db

@gallery.route('/gallery')
@login_required
def Gallery():
    return render_template("Gallery.html" , user=current_user)



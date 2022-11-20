import json
from application.database import User, Firmware, Report, db, migrate_db
from application.util import is_admin, extract_firmware
from flask import Blueprint, jsonify, redirect, render_template, request
from flask_login import current_user, login_required, login_user, logout_user
from application.bot import visit_report

web = Blueprint('web', __name__)
api = Blueprint('api', __name__)

def response(message):
    return jsonify({'message': message})

@web.route('/', methods=['GET'])
def login():
    return render_template('login.html')

@api.route('/login', methods=['POST'])
def user_login():
    if not request.is_json:
        return response('Missing required parameters!'), 401

    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')

    if not username or not password:
        return response('Missing required parameters!'), 401

    user = User.query.filter_by(username=username).first()

    if not user or not user.password == password:
        return response('Invalid username or password!'), 403

    login_user(user)
    return response('User authenticated successfully!')

@web.route('/register', methods=['GET'])
def register():
    return render_template('register.html')

@api.route('/register', methods=['POST'])
def user_registration():
    if not request.is_json:
        return response('Missing required parameters!'), 401

    data = request.get_json()
    username = data.get('username', '')
    password = data.get('password', '')

    if not username or not password:
        return response('Missing required parameters!'), 401

    user = User.query.filter_by(username=username).first()

    if user:
        return response('User already exists!'), 401

    new_user = User(username=username, password=password)
    db.session.add(new_user)
    db.session.commit()

    return response('User registered successfully!')

@web.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

@api.route('/firmware/list', methods=['GET'])
@login_required
def firmware_list():
    firmware_list = Firmware.query.all()
    return jsonify([row.to_dict() for row in firmware_list])

@api.route('/firmware/report', methods=['POST'])
@login_required
def report_issue():
    if not request.is_json:
        return response('Missing required parameters!'), 401

    data = request.get_json()
    module_id = data.get('module_id', '')
    issue = data.get('issue', '')

    if not module_id or not issue:
        return response('Missing required parameters!'), 401

    new_report = Report(module_id=module_id, issue=issue, reported_by=current_user.username)
    db.session.add(new_report)
    db.session.commit()

    visit_report()
    migrate_db()

    return response('Issue reported successfully!')

@api.route('/firmware/upload', methods=['POST'])
@login_required
@is_admin
def firmware_update():
    if 'file' not in request.files:
        return response('Missing required parameters!'), 401

    extraction = extract_firmware(request.files['file'])
    if extraction:
        return response('Firmware update initialized successfully.')

    return response('Something went wrong, please try again!'), 403

@web.route('/review', methods=['GET'])
@login_required
@is_admin
def review_report():
    Reports = Report.query.all()
    return render_template('review.html', reports=Reports)

@web.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin
from flask import current_app

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

class Firmware(db.Model, UserMixin, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    module = db.Column(db.String(100))
    hw_version = db.Column(db.String(100))
    fw_version = db.Column(db.String(100))
    serial = db.Column(db.String(100))
    hub_id = db.Column(db.String(100))

class Report(db.Model, UserMixin, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer)
    reported_by = db.Column(db.String(100))
    issue = db.Column(db.Text)

def clear_reports():
    db.session.query(Report).delete()
    db.session.commit()

def clear_db():
    meta = db.metadata
    for table in reversed(meta.sorted_tables):
        db.session.execute(table.delete())
    db.session.commit()

def migrate_db():
    clear_db()
    # admin user
    db.session.add(User(id=1, username=current_app.config['ADMIN_USERNAME'], password=current_app.config['ADMIN_PASSWORD']))

    # firmwares
    db.session.add(Firmware(id=1, module='Launch pod interface', hw_version='d3', fw_version='2408.b', serial='c6c3b20e', hub_id='17310'))
    db.session.add(Firmware(id=2, module='Oxidizer controller', hw_version='a4', fw_version='1801.c', serial='b20418fc', hub_id='33194'))
    db.session.add(Firmware(id=3, module='Propellant damper', hw_version='b6', fw_version='1705.e', serial='7fdee87d', hub_id='19696'))
    db.session.add(Firmware(id=4, module='RD-983 compressor', hw_version='a1', fw_version='0002.a', serial='b0dae2e3', hub_id='91284'))
    db.session.add(Firmware(id=5, module='Refinery interface', hw_version='g4', fw_version='4323.d', serial='d0f2798d', hub_id='31157'))
    db.session.add(Firmware(id=6, module='Condensation chamber', hw_version='k3', fw_version='3467.p', serial='2e1e7897', hub_id='19850'))
    db.session.add(Firmware(id=7, module='Fission reactor', hw_version='p3', fw_version='9031.g', serial='9c431d03', hub_id='12488'))
    db.session.add(Firmware(id=8, module='Booster core', hw_version='i7', fw_version='7651.g', serial='cd003b79', hub_id='12488'))
    db.session.add(Firmware(id=9, module='Surface calibrator', hw_version='a1', fw_version='4632.g', serial='b320babd', hub_id='14274'))
    db.session.add(Firmware(id=10, module='Nozzle controller', hw_version='f6', fw_version='8731.g', serial='8be939d9', hub_id='78804'))

    db.session.commit()

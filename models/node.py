import hashlib
import os

from . import ModelMixin
from . import db


class Node(db.Model, ModelMixin):
    __tablename__ = 'nodes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    topics = db.relationship('Topic', backref='node')

    def __init__(self, form):
        self.name = form.get('name', '')

    def update(self, form):
        self.name = form.get('name', '')
        self.save()


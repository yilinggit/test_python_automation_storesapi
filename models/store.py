from db import db


class StoreModel(db.Model):
    __tablename__ = 'stores'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    ## lazy=dynamic prevents the items object from automatically fetching items; will need to do a .all() as below to fetch the items
    items = db.relationship('ItemModel', lazy='dynamic') ##ORMs are helpful in mapping rships

    ## Only the init method is unit-testable
    def __init__(self, name):
        self.name = name

    ## Not unit-testable because this function has rship with items. DB
    def json(self):
        return {'id': self.id, 'name': self.name, 'items': [item.json() for item in self.items.all()]}

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

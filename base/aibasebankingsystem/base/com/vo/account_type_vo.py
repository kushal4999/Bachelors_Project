from base import db


class AccountTypeVO(db.Model):
    __tablename__ = 'account_type_table'
    account_type_id = db.Column('account_type_id', db.Integer, primary_key=True, autoincrement=True)
    account_type_name = db.Column('account_type_name', db.String(100), nullable=False)
    account_type_description = db.Column('account_type_description', db.String(100), nullable=False)

    def as_dict(self):
        return {
            'account_type_id': self.account_type_id,
            'account_type_name': self.account_type_name,
            'account_type_description': self.account_type_description
        }


db.create_all()

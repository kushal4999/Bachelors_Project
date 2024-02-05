from base import db


class LoantypeVO(db.Model):
    __tablename__ = 'loantype_table'
    loan_type_id = db.Column('loan_type_id', db.Integer, primary_key=True, autoincrement=True)
    loan_type_name = db.Column('loan_type_name', db.String(50), nullable=False)
    loan_type_description = db.Column('loan_type_description', db.String(100), nullable=False)

    def as_dict(self):
        return {
            'loan_type_id': self.loan_type_id,
            'loan_type_name': self.loan_type_name,
            'loan_type_description': self.loan_type_description
        }


db.create_all()

from base import db
from base.com.vo.loan_type_vo import LoantypeVO


class LoaninfoVO(db.Model):
    __tablename__ = 'loan_info_table'
    loan_info_id = db.Column('loan_info_id', db.Integer, primary_key=True, autoincrement=True)
    loan_info_rate = db.Column('loan_info_rate', db.String(100), nullable=False)
    loan_info_duration = db.Column('loan_info_duration', db.String(100), nullable=False)
    loan_info_income = db.Column('loan_info_income', db.String(100), nullable=False)
    loan_info_credit_score = db.Column('loan_info_credit_score', db.String(100), nullable=False)
    loan_info_fees = db.Column('loan_info_fees', db.String(100), nullable=False)
    loan_info_loan_type_id = db.Column('loan_info_loan_type_id', db.Integer, db.ForeignKey(LoantypeVO.loan_type_id))

    def as_dict(self):
        return {
            'loan_info_id': self.loan_info_id,
            'loan_info_rate': self.loan_info_rate,
            'loan_info_duration': self.loan_info_duration,
            'loan_info_income': self.loan_info_income,
            'loan_info_credit_score': self.loan_info_credit_score,
            'loan_info_fees': self.loan_info_fees,
            'loan_info_loan_type_id': self.loan_info_loan_type_id
        }


db.create_all()

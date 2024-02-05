from base import db
from base.com.vo.loan_type_vo import LoantypeVO


class LoantypeDAO:
    def insert_loan_type(self, loan_type_vo):
        db.session.add(loan_type_vo)
        db.session.commit()

    def view_loan_type(self):
        loan_type_vo_list = LoantypeVO.query.all()
        return loan_type_vo_list

    def delete_loan_type(self, loan_type_vo):
        loan_type_vo_list = LoantypeVO.query.get(loan_type_vo.loan_type_id)
        db.session.delete(loan_type_vo_list)
        db.session.commit()

    def edit_loan_type(self, loan_type_vo):
        loan_type_vo_list = loan_type_vo.query. \
            filter_by(loan_type_id=loan_type_vo.loan_type_id).all()
        return loan_type_vo_list

    def update_loan_type(self, loan_type_vo):
        db.session.merge(loan_type_vo)
        db.session.commit()

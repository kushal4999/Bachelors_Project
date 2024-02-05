from base import db

from base.com.vo.loan_info_vo import LoaninfoVO


class LoaninfoDAO:
    def insert_loan_info(self, loan_type_vo):
        db.session.add(loan_type_vo)
        db.session.commit()

    def view_loan_info(self):
        loan_info_vo_list = LoaninfoVO.query.all()
        return loan_info_vo_list

    def delete_loan_info(self, loan_info_vo):
        loan_info_vo_list = LoaninfoVO.query.get(loan_info_vo.loan_info_id)
        db.session.delete(loan_info_vo_list)
        db.session.commit()

    def edit_loan_info(self, loan_info_vo):
        loan_info_vo_list = loan_info_vo.query. \
            filter_by(loan_info_id=loan_info_vo.loan_info_id).all()
        return loan_info_vo_list

    def update_loan_info(self, loan_info_vo):
        db.session.merge(loan_info_vo)
        db.session.commit()

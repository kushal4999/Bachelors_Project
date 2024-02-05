from base import db
from base.com.vo.account_type_vo import AccountTypeVO


class AccountTypeDAO:
    def insert_account_type(self, account_type_vo):
        db.session.add(account_type_vo)
        db.session.commit()

    def view_account_type(self):
        account_type_vo_list = AccountTypeVO.query.all()
        return account_type_vo_list

    def delete_account_type(self, account_type_vo):
        account_type_vo_list = AccountTypeVO.query.get(account_type_vo.account_type_id)
        db.session.delete(account_type_vo_list)
        db.session.commit()

    def edit_account_type(self, account_type_vo):
        account_type_vo_list = account_type_vo.query. \
            filter_by(account_type_id=account_type_vo.account_type_id).all()
        return account_type_vo_list

    def update_account_type(self, account_type_vo):
        db.session.merge(account_type_vo)
        db.session.commit()

from base import db
from base.com.vo.account_info_vo import AccountInfoVO


class AccountInfoDAO:
    def insert_account_info(self, account_info_vo):
        db.session.add(account_info_vo)
        db.session.commit()

    def view_account_info(self):
        account_info_vo_list = AccountInfoVO.query.all()
        return account_info_vo_list

    def delete_account_info(self, account_info_vo):
        account_info_vo_list = AccountInfoVO.query.get(account_info_vo.account_info_id)
        db.session.delete(account_info_vo_list)
        db.session.commit()

    def edit_account_info(self, account_info_vo):
        account_info_vo_list = account_info_vo.query. \
            filter_by(account_info_id=account_info_vo.account_info_id).all()
        return account_info_vo_list

    def update_account_info(self, account_info_vo):
        db.session.merge(account_info_vo)
        db.session.commit()

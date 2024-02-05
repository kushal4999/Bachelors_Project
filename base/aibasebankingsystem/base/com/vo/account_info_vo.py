from base import db
from base.com.vo.account_type_vo import AccountTypeVO


class AccountInfoVO(db.Model):
    __tablename__ = 'account_info_table'
    account_info_id = db.Column('account_info_id', db.Integer, primary_key=True, autoincrement=True)
    account_info_minimum_balance = db.Column('account_info_minimum_balance', db.String(100), nullable=False)
    account_info_maximum_balance = db.Column('account_info_maximum_balance', db.String(100), nullable=False)
    account_info_description = db.Column('account_info_description', db.String(100), nullable=False)
    account_info_occupation_type = db.Column('account_info_occupation_type', db.String(100), nullable=False)
    account_info_rate = db.Column('account_info_rate', db.String(100), nullable=False)
    account_info_document = db.Column('account_info_document', db.String(100), nullable=True)
    account_info_foreign_trade = db.Column('account_info_foreign_trade', db.String(100), nullable=False)
    account_info_account_type_id = db.Column('account_info_account_type_id', db.Integer,
                                             db.ForeignKey(AccountTypeVO.account_type_id))

    def as_dict(self):
        return {
            'account_info_id': self.account_info_id,
            'account_info_minimum_balance': self.account_info_minimum_balance,
            'account_info_maximum_balance': self.account_info_maximum_balance,
            'account_info_description': self.account_info_description,
            'account_info_occupation_type': self.account_info_occupation_type,
            'account_info_rate': self.account_info_rate,
            'account_info_document': self.account_info_document,
            'account_info_foreign_trade': self.account_info_foreign_trade,
            'account_info_account_type_id': self.account_info_account_type_id,
        }


db.create_all()

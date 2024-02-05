from base import db
from base.com.vo.area_vo import AreaVO


class BranchVO(db.Model):
    __tablename__ = 'branches_table'
    branch_id = db.Column('branch_id', db.Integer, primary_key=True, autoincrement=True)
    branch_name = db.Column('branch_name', db.String(100), nullable=False)
    branch_address = db.Column('branch_address', db.String(100), nullable=False)
    branch_pincode = db.Column('branch_pincode', db.String(100), nullable=False)
    branch_contact_no = db.Column('branch_contact_no', db.String(100), nullable=False)
    branch_area_id = db.Column('branch_area_id', db.Integer, db.ForeignKey(AreaVO.area_id))

    def as_dict(self):
        return {
            'branch_id': self.branch_id,
            'branch_name': self.branch_name,
            'branch_address': self.branch_address,
            'branch_pincode': self.branch_pincode,
            'branch_contact_no': self.branch_contact_no,
            'branch_area_id': self.branch_area_id
        }


db.create_all()

from base import db


class FormVO(db.Model):
    __tablename__ = 'form_table'
    form_id = db.Column('form_id', db.Integer, primary_key=True, autoincrement=True)
    form_type = db.Column('form_type', db.String(255), nullable=False)
    form_attachment_name = db.Column('form_attachment_name', db.String(255), nullable=False)
    form_attachment_path = db.Column('form_attachment_path', db.String(255), nullable=False)

    def as_dict(self):
        return {
            'form_id': self.form_id,
            'form_type': self.form_type,
            'form_attachment_name': self.form_attachment_name,
            'form_attachment_path': self.form_attachment_path,
        }


db.create_all()

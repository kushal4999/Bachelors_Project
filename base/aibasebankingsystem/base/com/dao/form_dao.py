from  base import db
from base.com.vo.form_vo import FormVO


class FormDAO:
    def insert_form(self, form_vo):
        db.session.add(form_vo)
        db.session.commit()

    def view_form(self):
        form_vo_list = FormVO.query.all()
        return form_vo_list

    def delete_form(self, product_id):
        form_vo_list = FormVO.query.get(product_id)
        db.session.delete(form_vo_list)
        db.session.commit()
        return form_vo_list

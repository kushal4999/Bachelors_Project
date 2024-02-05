import os

from flask import render_template, request, redirect, url_for
from werkzeug.utils import secure_filename

from base import app
from base.com.controller.login_controller import admin_login_session
from base.com.dao.form_dao import FormDAO
from base.com.vo.form_vo import FormVO

FORM_FOLDER = 'base/static/adminResourses/forms/'

app.config['FORM_FOLDER'] = FORM_FOLDER


@app.route('/admin/load_form', methods=['GET'])
def admin_load_form():
    try:
        if admin_login_session() == "admin":
            return render_template('admin/addForms.html')
        else:
            return redirect('/admin/logout_session')
    except Exception as ex:
        print("admin_load_form route exception occured>>>>>>>>>>", ex)


@app.route('/admin/insert_form', methods=['POST'])
def admin_insert_form():
    try:
        if admin_login_session() == "admin":

            form_type = request.form.get('formType')
            form_attachment = request.files.get('formAttachment')

            form_attachment_name = secure_filename(form_attachment.filename)
            form_attachment_path = os.path.join(app.config['FORM_FOLDER'])
            form_attachment.save(os.path.join(form_attachment_path, form_attachment_name))

            form_vo = FormVO()
            form_dao = FormDAO()

            form_vo.form_type = form_type
            form_vo.form_attachment_name = form_attachment_name
            form_vo.form_attachment_path = form_attachment_path.replace("base", "..")

            form_dao.insert_form(form_vo)
            return redirect(url_for('admin_view_form'))
        else:
            return redirect('/admin/logout_session')
    except Exception as ex:
        print("admin_load_form route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_form')
def admin_view_form():
    try:
        if admin_login_session() == "admin":
            form_dao = FormDAO()
            form_vo_list = form_dao.view_form()
            return render_template('admin/viewForms.html', form_vo_list=form_vo_list)
        else:
            return redirect('/admin/logout_session')

    except Exception as ex:
        print("admin_view_product route exception occured>>>>>>>>>>", ex)


@app.route('/admin/delete_form', methods=['GET'])
def admin_delete_form():
    try:
        if admin_login_session() == "admin":
            form_vo = FormVO()
            form_dao = FormDAO()

            form_id = request.args.get('formId')
            form_vo.form_id = form_id
            form_vo_list = form_dao.delete_form(form_id)
            file_path = os.path.join(form_vo_list.form_attachment_path.replace("..", "base") + form_vo_list.form_attachment_name)
            os.remove(file_path)
            return redirect(url_for('admin_view_form'))
        else:
            return redirect('/admin/logout_session')
        
    except Exception as ex:
        print("admin_delete_product route exception occured>>>>>>>>>>", ex)

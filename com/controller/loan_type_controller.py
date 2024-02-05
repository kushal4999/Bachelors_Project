from flask import render_template, request, redirect

from base import app
from base.com.controller.login_controller import admin_login_session
from base.com.dao.loan_type_dao import LoantypeDAO
from base.com.vo.loan_type_vo import LoantypeVO


@app.route('/admin/load_loan_type', methods=['GET'])
def admin_load_loan_type():
    try:
        if admin_login_session() == "admin":
            return render_template('admin/addLoanType.html')
        else:
            return redirect('/admin/logout_session')
    except Exception as ex:
        print("admin_load_loan_type route exception occured>>>>>>>>>>", ex)


@app.route('/admin/insert_loan_type', methods=['POST'])
def admin_insert_loan_type():
    try:
        if admin_login_session() == "admin":
            loan_type_name = request.form.get("loanTypeName")
            loan_type_description = request.form.get("loanTypeDescription")

            loan_type_vo = LoantypeVO()
            loan_type_dao = LoantypeDAO()

            loan_type_vo.loan_type_name = loan_type_name
            loan_type_vo.loan_type_description = loan_type_description

            loan_type_dao.insert_loan_type(loan_type_vo)
            return redirect('/admin/view_loan_type')
        else:
            return redirect('/admin/logout_session')

    except Exception as ex:
        print("admin_insert_loan_type route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_loan_type')
def admin_view_loan_type():
    try:
        if admin_login_session() == "admin":
            loan_type_dao = LoantypeDAO()
            loan_type_vo_list = loan_type_dao.view_loan_type()

            return render_template('admin/viewLoanType.html', loan_type_vo_list=loan_type_vo_list)
        else:
            return redirect('/admin/logout_session')
    except Exception as ex:
        print("admin_view_loan_type route exception occured>>>>>>>>>>", ex)


@app.route('/admin/delete_loan_type', methods=['GET'])
def admin_delete_loan_type():
    try:
        if admin_login_session() == "admin":
            loan_type_id = request.args.get('loanTypeId')

            loan_type_vo = LoantypeVO()
            loan_type_vo.loan_type_id = loan_type_id

            loan_type_dao = LoantypeDAO()
            loan_type_dao.delete_loan_type(loan_type_vo)

            return redirect('/admin/view_loan_type')
        else:
            return redirect('/admin/logout_session')

    except Exception as ex:
        print("admin_delete_loan_type route exception occured>>>>>>>>>>", ex)


@app.route('/admin/edit_loan_type', methods=['GET'])
def admin_edit_loan_type():
    try:
        if admin_login_session() == "admin":
            loan_type_id = request.args.get('loanTypeId')

            loan_type_vo = LoantypeVO()
            loan_type_vo.loan_type_id = loan_type_id

            loan_type_dao = LoantypeDAO()
            loan_type_vo_list = loan_type_dao.edit_loan_type(loan_type_vo)

            return render_template('admin/editLoanType.html', loan_type_vo_list=loan_type_vo_list)
        else:
            return redirect('/admin/logout_session')
    except Exception as ex:
        print("admin_edit_loan_type route exception occured>>>>>>>>>>", ex)


@app.route('/admin/update_loan_type', methods=['POST'])
def admin_update_loan_type():
    try:
        if admin_login_session() == "admin":
            loan_type_id = request.form.get('loanTypeId')
            loan_type_name = request.form.get('loanTypeName')
            loan_type_description = request.form.get('loanTypeDescription')

            loan_type_vo = LoantypeVO()
            loan_type_vo.loan_type_id = loan_type_id
            loan_type_vo.loan_type_name = loan_type_name
            loan_type_vo.loan_type_description = loan_type_description

            loan_type_dao = LoantypeDAO()
            loan_type_dao.update_loan_type(loan_type_vo)

            return redirect('/admin/view_loan_type')
        else:
            return redirect('/admin/logout_session')
    except Exception as ex:
        print("admin_update_loan_type route exception occured>>>>>>>>>>", ex)

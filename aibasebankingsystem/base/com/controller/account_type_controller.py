from flask import render_template, request, redirect

from base import app
from base.com.controller.login_controller import admin_login_session
from base.com.dao.account_type_dao import AccountTypeDAO
from base.com.vo.account_type_vo import AccountTypeVO


@app.route('/admin/load_account_type', methods=['GET'])
def admin_load_account_type():
    try:
        if admin_login_session() == "admin":
            return render_template('admin/addAccountType.html')
        else:
            return redirect('/admin/logout_session')
    except Exception as ex:
        print("admin_load_account_type route exception occured>>>>>>>>>>", ex)


@app.route('/admin/insert_account_type', methods=['POST'])
def admin_insert_account_type():
    try:
        if admin_login_session() == "admin":
            account_type_name = request.form.get("accountTypeName")
            account_type_description = request.form.get("accountTypeDescription")

            account_type_vo = AccountTypeVO()
            account_type_dao = AccountTypeDAO()

            account_type_vo.account_type_name = account_type_name
            account_type_vo.account_type_description = account_type_description

            account_type_dao.insert_account_type(account_type_vo)
            return redirect('/admin/view_account_type')
        else:
            return redirect('/admin/logout_session')

    except Exception as ex:
        print("admin_insert_area route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_account_type')
def admin_view_account_type():
    try:
        if admin_login_session() == "admin":
            account_type_dao = AccountTypeDAO()
            account_type_vo_list = account_type_dao.view_account_type()
            return render_template('admin/viewAccountType.html', account_type_vo_list=account_type_vo_list)
        else:
            return redirect('/admin/logout_session')

    except Exception as ex:
        print("admin_view_account_type route exception occured>>>>>>>>>>", ex)


@app.route('/admin/delete_account_type', methods=['GET'])
def admin_delete_account_type():
    try:
        if admin_login_session() == "admin":
            account_type_id = request.args.get('accountTypeId')

            account_type_vo = AccountTypeVO()
            account_type_vo.account_type_id = account_type_id

            account_type_dao = AccountTypeDAO()
            account_type_dao.delete_account_type(account_type_vo)

            return redirect('/admin/view_account_type')
        else:
            return redirect('/admin/logout_session')

    except Exception as ex:
        print("admin_delete_account_type route exception occured>>>>>>>>>>", ex)


@app.route('/admin/edit_account_type', methods=['GET'])
def admin_edit_account_type():
    try:
        if admin_login_session() == "admin":
            account_type_id = request.args.get('accountTypeId')

            account_type_vo = AccountTypeVO()
            account_type_vo.account_type_id = account_type_id

            account_type_dao = AccountTypeDAO()
            account_type_vo_list = account_type_dao.edit_account_type(account_type_vo)

            return render_template('admin/editAccountType.html', account_type_vo_list=account_type_vo_list)
        else:
            return redirect('/admin/logout_session')

    except Exception as ex:
        print("admin_edit_route exception occured>>>>>>>>>>", ex)


@app.route('/admin/update_account_type', methods=['POST'])
def admin_update_account_type():
    try:
        if admin_login_session() == "admin":
            account_type_id = request.form.get("accountTypeId")
            account_type_name = request.form.get("accountTypeName")
            account_type_description = request.form.get("accountTypeDescription")

            account_type_vo = AccountTypeVO()
            account_type_dao = AccountTypeDAO()

            account_type_vo.account_type_id = account_type_id
            account_type_vo.account_type_name = account_type_name
            account_type_vo.account_type_description = account_type_description

            account_type_dao.update_account_type(account_type_vo)
            return redirect('/admin/view_account_type')
        else:
            return redirect('/admin/logout_session')

    except Exception as ex:
        print("admin_update_account_type route exception occured>>>>>>>>>>", ex)

from flask import render_template, request, redirect

from base import app
from base.com.controller.login_controller import admin_login_session
from base.com.dao.account_info_dao import AccountInfoDAO
from base.com.dao.account_type_dao import AccountTypeDAO
from base.com.vo.account_info_vo import AccountInfoVO


@app.route('/admin/load_account_info', methods=['GET'])
def admin_load_account_info():
    try:
        if admin_login_session() == "admin":
            account_type_dao = AccountTypeDAO()
            account_type_vo_list = account_type_dao.view_account_type()
            print(account_type_vo_list)

            return render_template('admin/addAccountInfo.html', account_type_vo_list=account_type_vo_list)
        else:
            return redirect('/admin/logout_session')
    except Exception as ex:
        print("admin_load_account_info route exception occured>>>>>>>>>>", ex)


@app.route('/admin/insert_account_info', methods=['POST', 'GET'])
def admin_insert_account_info():
    try:
        if admin_login_session() == "admin":
            account_info_vo = AccountInfoVO()
            account_info_dao = AccountInfoDAO()
            account_info_vo.account_info_account_type_id = request.form.get("accountInfoAccountTypeId")
            account_info_vo.account_info_minimum_balance = request.form.get("accountInfoMinimumBalance")
            account_info_vo.account_info_maximum_balance = request.form.get("accountInfoMaximumBalance")
            account_info_vo.account_info_description = request.form.get("accountInfoDescription")
            account_info_vo.account_info_occupation_type = request.form.get("accountInfoOccupationType")
            account_info_vo.account_info_rate = request.form.get("accountInfoRate")
            account_info_vo.account_info_document = request.form.get("accountInfoDocument")
            account_info_vo.account_info_foreign_trade = request.form.get("accountInfoForeignTrade")

            account_info_dao.insert_account_info(account_info_vo)
            return redirect('/admin/view_account_info')
        else:
            return redirect('/admin/logout_session')

    except Exception as ex:
        print("admin_insert_account_info route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_account_info')
def admin_view_account_info():
    try:
        if admin_login_session() == "admin":
            account_info_dao = AccountInfoDAO()
            account_type_dao = AccountTypeDAO()
            account_type_vo_list = account_type_dao.view_account_type()
            account_info_vo_list = account_info_dao.view_account_info()
        else:
            return redirect('/admin/logout_session')
        return render_template('admin/viewAccountInfo.html', account_info_vo_list=account_info_vo_list,
                               account_type_vo_list=account_type_vo_list)

    except Exception as ex:
        print("admin_view_account_info route exception occured>>>>>>>>>>", ex)


@app.route('/admin/delete_account_info', methods=['GET'])
def admin_delete_account_info():
    try:
        if admin_login_session() == "admin":
            account_info_id = request.args.get('accountInfoId')
            account_info_vo = AccountInfoVO()
            account_info_vo.account_info_id = account_info_id

            account_info_dao = AccountInfoDAO()
            account_info_dao.delete_account_info(account_info_vo)

            return redirect('/admin/view_account_info')
        else:
            return redirect('/admin/logout_session')
    except Exception as ex:
        print("admin_delete_account_info route exception occured>>>>>>>>>>", ex)


@app.route('/admin/edit_account_info', methods=['GET'])
def admin_edit_account_info():
    try:
        if admin_login_session() == "admin":
            account_info_id = request.args.get('accountInfoId')

            account_info_vo = AccountInfoVO()
            account_info_vo.account_info_id = account_info_id
            account_type_dao = AccountTypeDAO()
            account_type_vo_list = account_type_dao.view_account_type()

            account_info_dao = AccountInfoDAO()
            account_info_vo_list = account_info_dao.edit_account_info(account_info_vo)

            return render_template('admin/editAccountInfo.html', account_info_vo_list=account_info_vo_list,
                                   account_type_vo_list=account_type_vo_list)
        else:
            return redirect('/admin/logout_session')
    except Exception as ex:
        print("admin_edit_ route exception occured>>>>>>>>>>", ex)


@app.route('/admin/update_account_info', methods=['POST'])
def admin_update_account_info():
    try:
        if admin_login_session() == "admin":
            account_info_vo = AccountInfoVO()
            account_info_dao = AccountInfoDAO()
            account_info_vo.account_info_id = request.form.get("accountInfoId")
            print(account_info_vo.account_info_id)
            print(account_info_vo.account_info_id)
            print(account_info_vo.account_info_id)
            account_info_vo.account_info_account_type_id = request.form.get("accountInfoAccountTypeId")
            account_info_vo.account_info_minimum_balance = request.form.get("accountInfoMinimumBalance")
            account_info_vo.account_info_maximum_balance = request.form.get("accountInfoMaximumBalance")
            account_info_vo.account_info_description = request.form.get("accountInfoDescription")
            account_info_vo.account_info_occupation_type = request.form.get("accountInfoOccupationType")
            account_info_vo.account_info_rate = request.form.get("accountInfoRate")
            account_info_vo.account_info_document = request.form.get("accountInfoDocument")
            account_info_vo.account_info_foreign_trade = request.form.get("accountInfoForeignTrade")

            account_info_dao.update_account_info(account_info_vo)
            return redirect('/admin/view_account_info')
        else:
            return redirect('/admin/logout_session')
    except Exception as ex:
        print("admin_update_account_info route exception occured>>>>>>>>>>", ex)

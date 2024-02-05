from flask import *

from base import app
from base.com.controller.login_controller import admin_login_session
from base.com.dao.loan_info_dao import LoaninfoDAO
from base.com.dao.loan_type_dao import LoantypeDAO
from base.com.vo.loan_info_vo import LoaninfoVO


@app.route('/admin/load_loan_info', methods=['GET'])
def admin_load_loan_info():
    try:
        if admin_login_session() == "admin":
            loan_type_dao = LoantypeDAO()
            loan_type_vo_list = loan_type_dao.view_loan_type()
            print(loan_type_vo_list)
            return render_template('admin/addLoanInfo.html', loan_type_vo_list=loan_type_vo_list)
        else:
            return redirect('/admin/logout_session')
    except Exception as ex:
        print("in admin_load_loan_info route exception occured>>>>>>>>>>", ex)


@app.route('/admin/insert_loan_info', methods=['POST'])
def admin_insert_loan_info():
    try:
        if admin_login_session() == "admin":
            loan_info_rate = request.form.get('loanInfoRate')
            print(loan_info_rate)
            loan_info_income = request.form.get('loanInfoIncome')
            loan_info_loan_type_id = request.form.get('loanInfoLoanTypeId')
            print(loan_info_loan_type_id)
            loan_info_duration = request.form.get('duration')
            loan_info_credit_score = request.form.get('creditScore')
            loan_info_fees = request.form.get('fees')
            loan_info_vo = LoaninfoVO()
            loan_info_dao = LoaninfoDAO()

            loan_info_vo.loan_info_loan_type_id = loan_info_loan_type_id
            loan_info_vo.loan_info_rate = loan_info_rate
            loan_info_vo.loan_info_income = loan_info_income
            loan_info_vo.loan_info_duration = loan_info_duration
            loan_info_vo.loan_info_credit_score = loan_info_credit_score
            loan_info_vo.loan_info_fees = loan_info_fees

            loan_info_dao.insert_loan_info(loan_info_vo)
            return redirect(url_for('admin_view_loan_info'))
        else:
            return redirect('/admin/logout_session')
    except Exception as ex:
        print("in admin_insert_loan_info route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_loan_info')
def admin_view_loan_info():
    try:
        if admin_login_session() == "admin":
            loan_info_dao = LoaninfoDAO()
            loan_type_dao = LoantypeDAO()
            loan_type_vo_list = loan_type_dao.view_loan_type()
            loan_info_vo_list = loan_info_dao.view_loan_info()
            print(loan_info_vo_list)
            return render_template('admin/viewLoanInfo.html', loan_info_vo_list=loan_info_vo_list,
                                   loan_type_vo_list=loan_type_vo_list)
        else:
            return redirect('/admin/logout_session')

    except Exception as ex:
        print("admin_view_loan_type route exception occured>>>>>>>>>>", ex)


@app.route('/admin/delete_loan_info', methods=['GET'])
def admin_delete_loan_info():
    try:
        if admin_login_session() == "admin":
            loan_info_id = request.args.get('loanInfoId')
            print(loan_info_id)
            loan_info_vo = LoaninfoVO()
            loan_info_vo.loan_info_id = loan_info_id

            loan_info_dao = LoaninfoDAO()
            loan_info_dao.delete_loan_info(loan_info_vo)

            return redirect('/admin/view_loan_info')
        else:
            return redirect('/admin/logout_session')

    except Exception as ex:
        print("admin_delete_loan_info route exception occured>>>>>>>>>>", ex)


@app.route('/admin/edit_loan_info', methods=['GET'])
def admin_edit_loan_info():
    try:
        if admin_login_session() == "admin":
            loan_info_id = request.args.get('loanInfoId')

            loan_info_vo = LoaninfoVO()
            loan_info_vo.loan_info_id = loan_info_id

            loan_type_dao = LoantypeDAO()
            loan_type_vo_list = loan_type_dao.view_loan_type()

            loan_info_dao = LoaninfoDAO()
            loan_info_vo_list = loan_info_dao.edit_loan_info(loan_info_vo)

            return render_template('admin/editLoanInfo.html', loan_info_vo_list=loan_info_vo_list,
                                   loan_type_vo_list=loan_type_vo_list)
        else:
            return redirect('/admin/logout_session')
    except Exception as ex:
        print("admin_edit_loan_type route exception occured>>>>>>>>>>", ex)


@app.route('/admin/update_loan_info', methods=['POST'])
def admin_update_loan_info():
    try:
        if admin_login_session() == "admin":
            loan_info_id = request.form.get('loanInfoId')
            loan_info_rate = request.form.get('loanInfoRate')
            loan_info_income = request.form.get('loanInfoIncome')
            loan_info_loan_type_id = request.form.get('loanInfoLoanTypeId')
            loan_info_duration = request.form.get('loanInfoDuration')
            loan_info_credit_score = request.form.get('loanInfoCreditScore')
            loan_info_fees = request.form.get('loanInfoFees')
            loan_info_vo = LoaninfoVO()
            loan_info_dao = LoaninfoDAO()

            loan_info_vo.loan_info_id = loan_info_id
            loan_info_vo.loan_info_loan_type_id = loan_info_loan_type_id
            loan_info_vo.loan_info_rate = loan_info_rate
            loan_info_vo.loan_info_income = loan_info_income
            loan_info_vo.loan_info_duration = loan_info_duration
            loan_info_vo.loan_info_credit_score = loan_info_credit_score
            loan_info_vo.loan_info_fees = loan_info_fees
            loan_info_dao.update_loan_info(loan_info_vo)
            return redirect(url_for('admin_view_loan_info'))
        else:
            return redirect('/admin/logout_session')

    except Exception as ex:
        print("admin_update_loan_info route exception occured>>>>>>>>>>", ex)

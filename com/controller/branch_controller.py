from flask import *

from base import app
from base.com.controller.login_controller import admin_login_session
from base.com.dao.area_dao import AreaDAO
from base.com.dao.branch_dao import BranchDAO
from base.com.vo.branch_vo import BranchVO


@app.route('/admin/load_branch', methods=['GET'])
def admin_load_branch():
    try:
        if admin_login_session() == "admin":
            area_dao = AreaDAO()
            area_vo_list = area_dao.search_area()
            print(area_vo_list)
            return render_template('admin/addBranch.html', area_vo_list=area_vo_list)
        else:
            return redirect('/admin/logout_session')
    except Exception as ex:
        print("in admin_load_branch route exception occured>>>>>>>>>>", ex)


@app.route('/admin/insert_branch', methods=['POST'])
def admin_insert_branch():
    try:
        if admin_login_session() == "admin":
            branch_name = request.form.get('branchName')
            branch_pincode = request.form.get('BranchPincode')
            branch_area_id = request.form.get('branchAreaId')
            branch_address = request.form.get('BranchAddress')
            branch_contact_no = request.form.get('ContactNo')
            branch_vo = BranchVO()
            branch_dao = BranchDAO()

            branch_vo.branch_area_id = branch_area_id
            branch_vo.branch_name = branch_name
            branch_vo.branch_pincode = branch_pincode
            branch_vo.branch_address = branch_address
            branch_vo.branch_contact_no = branch_contact_no
            branch_dao.insert_branch(branch_vo)
            return redirect(url_for('admin_view_branch'))
        else:
            return redirect('/admin/logout_session')

    except Exception as ex:
        print("in admin_insert_subcategory route exception occured>>>>>>>>>>", ex)


@app.route('/admin/view_branch')
def admin_view_branch():
    try:
        if admin_login_session() == "admin":
            branch_dao = BranchDAO()
            area_dao = AreaDAO()
            area_vo_list = area_dao.search_area()
            branch_vo_list = branch_dao.search_branch()
            print(branch_vo_list)
            return render_template('admin/viewBranch.html', branch_vo_list=branch_vo_list, area_vo_list=area_vo_list)
        else:
            return redirect('/admin/logout_session')

    except Exception as ex:
        print("admin_view_area route exception occured>>>>>>>>>>", ex)


@app.route('/admin/delete_branch', methods=['GET'])
def admin_delete_branch():
    try:
        if admin_login_session() == "admin":
            branch_id = request.args.get('branchId')
            print(branch_id)
            branch_vo = BranchVO()
            branch_vo.branch_id = branch_id

            branch_dao = BranchDAO()
            branch_dao.delete_branch(branch_vo)

            return redirect('/admin/view_branch')
        else:
            return redirect('/admin/logout_session')

    except Exception as ex:
        print("admin_delete_branch route exception occured>>>>>>>>>>", ex)


@app.route('/admin/edit_branch', methods=['GET'])
def admin_edit_branch():
    try:
        if admin_login_session() == "admin":
            branch_id = request.args.get('branchId')

            branch_vo = BranchVO()
            branch_vo.branch_id = branch_id

            area_dao = AreaDAO()
            area_vo_list = area_dao.search_area()

            branch_dao = BranchDAO()
            branch_vo_list = branch_dao.edit_branch(branch_vo)

            return render_template('admin/editBranch.html', branch_vo_list=branch_vo_list, area_vo_list=area_vo_list)
        else:
            return redirect('/admin/logout_session')

    except Exception as ex:
        print("admin_edit_area route exception occured>>>>>>>>>>", ex)


@app.route('/admin/update_branch', methods=['POST'])
def admin_update_branch():
    try:
        if admin_login_session() == "admin":
            branch_id = request.form.get('branchId')
            branch_name = request.form.get('branchName')
            branch_pincode = request.form.get('BranchPincode')
            branch_area_id = request.form.get('branchAreaId')
            branch_address = request.form.get('BranchAddress')
            branch_contact_no = request.form.get('ContactNo')
            branch_vo = BranchVO()
            branch_dao = BranchDAO()

            branch_vo.branch_id = branch_id
            branch_vo.branch_area_id = branch_area_id
            branch_vo.branch_name = branch_name
            branch_vo.branch_pincode = branch_pincode
            branch_vo.branch_address = branch_address
            branch_vo.branch_contact_no = branch_contact_no
            branch_dao.update_branch(branch_vo)
            return redirect(url_for('admin_view_branch'))
        else:
            return redirect('/admin/logout_session')

    except Exception as ex:
        print("admin_update_area route exception occured>>>>>>>>>>", ex)

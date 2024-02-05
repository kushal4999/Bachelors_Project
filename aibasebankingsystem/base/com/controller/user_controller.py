import random
import smtplib
import string
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from flask import render_template, request, flash, redirect

from base import app
from base.com.dao.area_dao import AreaDAO
from base.com.dao.login_dao import LoginDAO
from base.com.dao.user_dao import UserDAO
from base.com.vo.login_vo import LoginVO
from base.com.vo.user_vo import UserVO


@app.route('/user/load_user', methods=['GET'])
def admin_load_user():
    try:
        area_dao = AreaDAO()
        area_vo_list=area_dao.search_area()
        print(area_vo_list)
        return render_template('user/addUser.html',area_vo_list=area_vo_list)
    except Exception as ex:
        print("in admin_load_user route exception occured>>>>>>>>>>", ex)


@app.route('/admin/insert_user', methods=['POST'])
def admin_insert_user():
    try:
        login_vo = LoginVO()
        login_dao = LoginDAO()

        user_vo = UserVO()
        user_dao = UserDAO()

        login_username = request.form.get('loginUsername')
        user_firstname = request.form.get('userFirstname')
        user_lastname = request.form.get('userLastname')
        user_gender = request.form.get('userGender')
        user_contact = request.form.get('userContact')
        user_address = request.form.get('userAddress')
        user_area_id = request.form.get('userAreaId')
        print(">>>>>>>>>>",login_username,user_firstname,user_lastname,user_gender,user_contact,user_address,user_area_id)


        login_password = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(8))
        print("in admin_insert_user login_password>>>>>>>>>", login_password)

        sender = "kushalprajapati4999@gmail.com"
        receiver = login_username
        msg = MIMEMultipart()
        msg['From'] = sender
        msg['To'] = receiver
        msg['Subject'] = "PYTHON PASSWORD"
        msg.attach(MIMEText(login_password, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender, "kp@12345")
        text = msg.as_string()
        server.sendmail(sender, receiver, text)
        server.quit()

        login_secretkey = ''.join((random.choice(string.ascii_letters + string.digits)) for x in range(32))
        print("in admin_insert_user login_secretkey>>>>>>>", login_secretkey)
        login_vo_list = login_dao.view_login()
        print("in admin_insert_user login_vo_list>>>>>>", login_vo_list)
        if len(login_vo_list) != 0:
            for i in login_vo_list:
                if i.login_secretkey == login_secretkey:
                    login_secretkey = ''.join(
                        (random.choice(string.ascii_letters + string.digits)) for x in range(32))
                if i.login_username == login_username:
                    error_message = "The username is already exists !"
                    flash(error_message)
                    return redirect('/user/load_user')

        login_vo.login_username = login_username
        login_vo.login_password = login_password
        login_vo.login_role = "user"
        login_vo.login_status = "active"
        login_vo.login_secretkey = login_secretkey
        login_dao.insert_login(login_vo)

        user_vo.user_firstname = user_firstname
        user_vo.user_lastname = user_lastname
        user_vo.user_gender = user_gender
        user_vo.user_address = user_address
        user_vo.user_contact = user_contact
        user_vo.user_area_id = user_area_id
        user_vo.user_login_id = login_vo.login_id
        user_dao.insert_user(user_vo)

        return render_template("admin/login.html")
    except Exception as ex:
        print("in admin_insert_user route exception occured>>>>>>>>>>", ex)


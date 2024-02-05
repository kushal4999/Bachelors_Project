from flask import render_template

from base import app



@app.route('/user/login')
def userLogin():
    return render_template('user/login.html')


@app.route('/user/register')
def userRegister():
    return render_template('user/addUser.html')


@app.route('/user/complain')
def userComplain():
    return render_template('user/addComplain.html')


@app.route('/user/feedback')
def userFeedback():
    return render_template('user/addFeedback.html')


@app.route('/user/index')
def userIndex():
    return render_template('user/index.html')


from flask import Blueprint, request, jsonify, session

from app.Models.user import UserInfo

user = Blueprint('user', __name__)


@user.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    username =data.get('name')
    password = data.get('password')
    logininf = UserInfo.query.filter(UserInfo.name == username).first()
    if logininf:
        if int(logininf.password)==password:
            session['username'] = username
            return jsonify(msg='Login success')
        else:
            return jsonify(msg='Login Failed')
    else:
        return jsonify(msg='Login Failed')

@user.route('/sessionjudge', methods=['GET'])
def sessionjudge():
    if session.get('username'):
        return jsonify(msg='Login')
    else:
        return jsonify(msg='Logout')


@user.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return jsonify(msg='Login out success')
from flask import Flask, Response, request, jsonify
from src.database import Database, User

app = Flask(__name__)

Database.init_database("mysql://root:123456@localhost/python-flask-poc");
Database.init_session();
Database.init_schema();

@app.route('/user', methods=["GET"])
def getUser():

    try:

        payments = Database.session.query(User).all()
        return jsonify( [payment.to_json() for payment in payments] )

    except Exception as e:
        
        return e.msg

@app.route('/user', methods=["POST"])
def saveUser():

    try:
        data = request.json
        obj = User(nome = data['nome'], sobrenome = data['sobrenome'], descricao = data['descricao']);
        Database.session.add(obj);
        Database.session.commit();
        
        return obj.to_json();

    except Exception as e:
        
        return e.msg
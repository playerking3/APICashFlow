from flask import Flask, request, jsonify, session
from main import app, db
from models import Receitas
from models import Despesas

@app.route('/Receitas', methods=['GET'])
def get_receita():
    Receita = Receitas.query.all()
    receitas_dic = []
    for receitas in Receita:
        receita_dic = {
            'id_receita': receitas.id_receita,
            'data': receitas.data,
            'valor': receitas.valor,
            'descricao': receitas.descricao,
            'id_usuario': receitas.id_usuario
        }
        receitas_dic.append(receita_dic)
    return jsonify(
        mensagem='Lista de Receitas',
        receitas= receitas_dic
    )
@app.route('/Despesas', methods=['GET'])
def get_despesa():
    Despesa = Despesas.query.all()
    despesas_dic = []
    for despesas in Despesa:
        despesa_dic = {
            'id_despesa': despesas.id_despesa,
            'data': despesas.data,
            'valor': despesas.valor,
            'descricao': despesas.descricao,
            'id_usuario': despesas.id_usuario
        }
        despesas_dic.append(despesa_dic)
    return jsonify(
        mensagem='Lista de Despesas',
        receitas= despesas_dic
    )

@app.route('/Receitas', methods=['POST'])
def post_receita():
    receita = request.json
    nova_receita = Receitas(
        id_receita=receita.get('id_receita'),
        data=receita.get('data'),
        valor=receita.get('valor'),
        descricao=receita.get('descricao')
    )
    db.session.add(nova_receita)
    db.session.commit()

    return jsonify(
        mensagem='Receita Cadastrada com Sucesso',
        receita={
            'id_receita': nova_receita.id_receita,
            'data': nova_receita.data,
            'valor': nova_receita.valor,
            'descricao': nova_receita.descricao
        }
    )


@app.route('/Despesas', methods=['POST'])
def post_despesa():
    despesas = request.json
    nova_despesa = Despesas(
        id_despesa=despesas.get('id_despesa'),
        data=despesas.get('data'),
        valor=despesas.get('valor'),
        descricao=despesas.get('descricao')
    )
    db.session.add(nova_despesa)
    db.session.commit()

    return jsonify(
        mensagem='Despesa Cadastrada com Sucesso',
        despesa={
            'id_receita': nova_despesa.id_despesa,
            'data': nova_despesa.data,
            'valor': nova_despesa.valor,
            'descricao': nova_despesa.descricao
        }
    )
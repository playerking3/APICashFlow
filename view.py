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
            'id_despesa': despesas.id_receita,
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

@app.route('/livro', methods=['POST'])
def post_valor():
    livro = request.json
    novo_livro = Livro(
        id_livro=livro.get('id_livro'),
        titulo=livro.get('titulo'),
        autor=livro.get('autor'),
        ano_publicacao=livro.get('ano_publicacao')
    )
    db.session.add(novo_livro)
    db.session.commit()

    return jsonify(
        mensagem='Livro Cadastrado com Sucesso',
        livro={
            'id_livro': novo_livro.id_livro,
            'titulo': novo_livro.titulo,
            'autor': novo_livro.autor,
            'ano_publicacao': novo_livro.ano_publicacao
        }
    )
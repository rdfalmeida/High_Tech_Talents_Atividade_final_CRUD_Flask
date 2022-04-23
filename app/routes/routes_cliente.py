from flask import request, flash, url_for, redirect, render_template
from app import app, db
from models.classes import Cliente

# Função visão geral.
@app.route('/cliente')
def show_cliente():
    # order_by para poder ser exibido em ordem já que HTML não aceita método PUT,
    # e quando fazemos POST ele joga para o fim dos resultados exibidos
    return render_template('show_cliente.html', cliente=Cliente.query.order_by(Cliente.id).all())

# Função visualizar cadastro habilitada para retornar a tela principal do módulo
# em caso de ID inválido.
@app.route('/cliente/<id>/id_cliente')
def id_cliente(id):
    cliente=Cliente.query.filter_by(id=id).first()
    if cliente:
        return render_template('id_cliente.html', cliente=cliente)
    return f" O Cliente ID={id} não existe. Você pode voltar e criar/atualizar para obter este ID.{render_template('voltar_cliente.html')}"

# Função novo cadastro.    
@app.route('/cliente/new_cliente', methods=['GET', 'POST'])
def new_cliente():
    
    if request.method == 'GET':
        return render_template('new_cliente.html')

    if request.method == 'POST':
        if not request.form['nome'] or not request.form['documento'] or not request.form['imoveis_proprios']\
            or not request.form['imoveis_em_locacao']:
            flash('Preencha todos os campos.')
        else:
            cliente=Cliente(request.form['nome'], request.form['documento'], request.form['imoveis_proprios'],\
            request.form['imoveis_em_locacao'])
            db.session.add(cliente)
            db.session.commit()
            flash('Cliente adicionado!')
            return redirect(url_for('show_cliente'))
    return render_template('new_cliente.html')

# Função editar cadastro habilitada para retornar a tela principal do módulo
# em caso de ID inválido.
# Como dito antes, fazendo só por HTML temos que fazer pelo POST e não PUT.
@app.route('/cliente/<id>/update', methods=['GET', 'POST'])
def update_cliente(id):
    cliente=Cliente.query.filter_by(id=id).first()
    
    if request.method == 'GET':
        return render_template('update_cliente.html', cliente=cliente)

    if request.method == 'POST':
        id=request.form.get("id")
        nome=request.form.get("nome")
        documento=request.form.get("documento")
        imoveis_proprios=request.form.get("imoveis_proprios")
        imoveis_em_locacao=request.form.get("imoveis_em_locacao")

        if id and nome and documento and imoveis_proprios and imoveis_em_locacao:
            cliente.id=id
            cliente.nome=nome
            cliente.documento=documento
            cliente.imoveis_proprios=imoveis_proprios
            cliente.imoveis_em_locacao=imoveis_em_locacao
            db.session.commit()
            flash('Cliente atualizado!')
        return redirect(url_for('show_cliente'))
    # Ainda vou descobrir como fazer a linha abaixo rodar. Só funciona a primeira f" string, da função id_cliente, linha 19.
    return f" O Cliente ID={id} não existe. Você pode voltar e criar/atualizar para obter este ID.{render_template('voltar_cliente.html')}"

@app.route('/cliente/<id>/delete_cliente', methods=['GET', 'POST'])
def delete_cliente(id):
    cliente=Cliente.query.filter_by(id=id).first()
    
    if request.method == 'POST':
        if cliente:
            if True:
                db.session.delete(cliente)
                db.session.commit()
                flash('Cliente excluído!')
                return redirect(url_for('show_cliente'))
        else:
            # Ainda vou descobrir como fazer a linha abaixo rodar. Só funciona a primeira f" string, da função id_cliente, linha 19.
            return f" O Cliente ID={id} não existe. Você pode voltar e criar/atualizar para obter este ID.{render_template('voltar_cliente.html')}"
    return render_template('delete_cliente.html')
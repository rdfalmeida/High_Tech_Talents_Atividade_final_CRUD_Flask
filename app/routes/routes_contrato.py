from flask import request, flash, url_for, redirect, render_template
from app import app, db
from models.classes import Contrato

# Função visão geral.
@app.route('/contrato')
def show_contrato():
    # order_by para poder ser exibido em ordem já que HTML não aceita método PUT,
    # e quando fazemos POST ele joga para o fim dos resultados exibidos
    return render_template('show_contrato.html', contrato=Contrato.query.order_by(Contrato.id).all())

# Função visualizar cadastro habilitada para retornar a tela principal do módulo
# em caso de ID inválido. Minha intenção é futuramente melhorar essa função para
# gerar contratos selecionando dados de outras tabelas, conforme arquivos na pasta 'sqldata'.
@app.route('/contrato/<id>/id_contrato')
def id_contrato(id):
    contrato=Contrato.query.filter_by(id=id).first()
    if contrato:
        return render_template('id_contrato.html', contrato=contrato)
    return f" O Contrato ID={id} não existe. Você pode voltar e criar/atualizar para obter este ID.{render_template('voltar_contrato.html')}"

# Função novo cadastro.
@app.route('/contrato/new_contrato', methods=['GET', 'POST'])
def new_contrato():
    
    if request.method == 'GET':
        return render_template('new_contrato.html')

    if request.method == 'POST':
        if not request.form['locador'] or not request.form['locatario'] or not request.form['imovel_contratado']\
            or not request.form['vigencia_contrato'] or not request.form['termos']:
            flash('Preencha todos os campos.')
        else:
            contrato=Contrato(request.form['locador'], request.form['locatario'],
            request.form['imovel_contratado'], request.form['vigencia_contrato'], request.form['termos'])
            db.session.add(contrato)
            db.session.commit()
            flash('Contrato adicionado!')
            return redirect(url_for('show_contrato'))
    return render_template('new_contrato.html')

# Função editar cadastro habilitada para retornar a tela principal do módulo
# em caso de ID inválido.
# Como dito antes, fazendo só por HTML temos que fazer pelo POST e não PUT.
@app.route('/contrato/<id>/update', methods=['GET', 'POST'])
def update_contrato(id):
    contrato=Contrato.query.filter_by(id=id).first()
    
    if request.method == 'GET':
        return render_template('update_contrato.html', contrato=contrato)

    if request.method == 'POST':
        id=request.form.get("id")
        locador=request.form.get("locador")
        locatario=request.form("locatario")
        imovel_contratado=request.form.get("imovel_contratado")
        vigencia_contrato=request.form.get("vigencia_contrato")
        termos=request.form.get("termos")

        if id and locador and imovel_contratado and vigencia_contrato and termos:
            contrato.id=id
            contrato.locador=locador
            contrato.locatario=locatario
            contrato.imovel_contratado=imovel_contratado
            contrato.vigencia_contrato=vigencia_contrato
            contrato.termos=termos
            db.session.commit()
            flash('Contrato atualizado!')
        return redirect(url_for('show_contrato'))
    # Ainda vou descobrir como fazer a linha abaixo rodar. Só funciona a primeira f" string, da função id_contrato, linha 19.
    return f" O Contrato ID={id} não existe. Você pode voltar e criar/atualizar para obter este ID.{render_template('voltar_contrato.html')}"

# Função deletar cadastro habilitada para retornar a tela principal do módulo
# em caso de ID inválido.
@app.route('/contrato/<id>/delete_contrato', methods=['GET', 'POST'])
def delete_contrato(id):
    contrato=Contrato.query.filter_by(id=id).first()
    
    if request.method == 'POST':
        if contrato:
            if True:
                db.session.delete(contrato)
                db.session.commit()
                flash('Contrato excluído!')
                return redirect(url_for('show_contrato'))
        else:
            # Ainda vou descobrir como fazer a linha abaixo rodar. Só funciona a primeira f" string, da função id_contrato, linha 19.
            return f" O Contrato ID={id} não existe. Você pode voltar e criar/atualizar para obter este ID.{render_template('voltar_contrato.html')}"
    return render_template('delete_contrato.html')
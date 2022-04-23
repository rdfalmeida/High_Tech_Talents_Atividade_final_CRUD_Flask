from flask import request, flash, url_for, redirect, render_template
from app import app, db
from models.classes import Imovel

# Página principal dos imóveis que mostra os imóveis e fornece redirecionamento
# para incluir, editar e apagar imóveis do banco de dados.

# A maioria está como tipo string para fins de prototipagem, e podem/vão ser adequados conforme necessidade.

# Página principal do módulo e visualização dos dados.
@app.route('/imovel')
def show_imovel():
    # .order_by() para poder ser exibido em ordem já que HTML não aceita método PUT,
    # e quando fazemos POST para update ele joga para o fim dos resultados exibidos.
    return render_template('show_imovel.html', imovel=Imovel.query.order_by(Imovel.id).all())

# Função visualizar cadastro habilitada para retornar a tela principal do módulo
# em caso de ID inválido.
@app.route('/imovel/<id>/id_imovel')
def id_imovel(id):
    imovel=Imovel.query.filter_by(id=id).first()
    if imovel:
        return render_template('id_imovel.html', imovel=imovel)
    return f" O Imóvel ID={id} não existe. Você pode voltar e criar/atualizar para obter este ID.{render_template('voltar_imovel.html')}"

# Inserção de novo cadastro.
@app.route('/imovel/new_imovel', methods=['GET', 'POST'])
def new_imovel():
    
    if request.method == 'GET':
        return render_template('new_imovel.html')

    if request.method == 'POST':
        if not request.form['tipo'] or not request.form['cep']\
            or not request.form['endereco'] or not request.form['area']:
            flash('Preencha todos os campos.')     
        else:
            imovel=Imovel(request.form['tipo'], request.form['cep'],
            request.form['endereco'], request.form['area'])
            db.session.add(imovel)
            db.session.commit()
            flash('Imóvel adicionado!')
            return redirect(url_for('show_imovel'))
    return render_template('new_imovel.html')

# Editar cadastro 
# Como dito antes, fazendo só por HTML temos que fazer pelo POST e não PUT.
@app.route('/imovel/<id>/update', methods=['GET', 'POST'])
def update_imovel(id):
    imovel=Imovel.query.filter_by(id=id).first()
    
    if request.method == 'GET':
        return render_template('update_imovel.html', imovel=imovel)

    if request.method == 'POST':
        id=request.form.get("id")
        tipo=request.form.get("tipo")
        cep=request.form.get("cep")
        endereco=request.form.get("endereco")
        area=request.form.get("area")

        if id and tipo and cep and endereco and area:
            imovel.id=id
            imovel.tipo=tipo
            imovel.cep=cep
            imovel.endereco=endereco
            imovel.area=area
            db.session.commit()
            flash('Imóvel atualizado!')
        return redirect(url_for('show_imovel'))
    # Ainda vou descobrir como fazer a linha abaixo rodar. Só funciona a primeira f" string, da função id_imovel, linha 19.
    return f" O Imóvel ID={id} não existe. Você pode voltar e criar/atualizar para obter este ID.{render_template('voltar_imovel.html')}"
#Função deletar
@app.route('/imovel/<id>/delete_imovel/', methods=['GET', 'POST'])
def delete_imovel(id):
    imovel=Imovel.query.filter_by(id=id).first()
    
    if request.method == 'POST':
        if imovel:
            if True:
                db.session.delete(imovel)
                db.session.commit()
                flash('Imóvel excluído!')
                return redirect(url_for('show_imovel'))
        else:
            # Ainda vou descobrir como fazer a linha abaixo rodar. Só funciona a primeira f" string, da função id_imovel, linha 19.
            return f" O Imóvel ID={id} não existe. Você pode voltar e criar/atualizar para obter este ID.{render_template('voltar_imovel.html')}"
    return render_template('delete_imovel.html')
from flask_sqlalchemy import SQLAlchemy
from app import db

# Aqui podemos atender quaisquer necessidades de CRUD criando classes nos critérios em que forem demandadas.
# Para este projeto temos "Imovel", "Cliente", que pode ser usado para PF, PJ, locador e locatário, e "Contrato".

# A maioria está como tipo string para fins de prototipagem, e podem/vão ser adequados conforme necessidade.
class Cliente(db.Model):
    
    id = db.Column('cliente_id', db.Integer, primary_key = True)
    nome = db.Column(db.String())
    documento = db.Column(db.String())
    imoveis_proprios = db.Column(db.String())
    imoveis_em_locacao = db.Column(db.String())

    def __init__(self, nome, documento, imoveis_proprios, imoveis_em_locacao):
        self.nome = nome
        self.documento = documento
        self.imoveis_proprios = imoveis_proprios
        self.imoveis_em_locacao = imoveis_em_locacao

# A minha intenção é futuramente melhorar essa função para gerar contratos
# selecionando dados de outras tabelas, conforme arquivos na pasta 'sqldata'.  
class Contrato(db.Model):
    
    id = db.Column('contrato_id', db.Integer, primary_key = True)
    locador = db.Column(db.String())
    locatario = db.Column(db.String())
    imovel_contratado = db.Column(db.String())
    vigencia_contrato = db.Column(db.String())
    termos = db.Column(db.String())
    
    def __init__(self, locador, locatario, imovel_contratado, vigencia_contrato, termos):
        self.locador = locador
        self.locatario = locatario
        self.imovel_contratado = imovel_contratado
        self.vigencia_contrato = vigencia_contrato
        self.termos = termos

class Imovel(db.Model):
        
    id = db.Column('imovel_id', db.Integer, primary_key = True)
    tipo = db.Column(db.String(20))
    cep = db.Column(db.String(10))
    endereco = db.Column(db.String(200))
    area = db.Column(db.String(10))

    def __init__(self, tipo, cep, endereco, area):
        self.tipo = tipo
        self.cep = cep
        self.endereco = endereco
        self.area = area
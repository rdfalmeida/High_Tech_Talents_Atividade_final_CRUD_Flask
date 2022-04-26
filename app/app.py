from flask import Flask, request, flash, url_for, redirect, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:1234@localhost:5432/postgres"
app.config['SECRET_KEY'] = "1234"

db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Separei as routes de cada categoria em arquivos em uma pasta também chamada routes.
# E a classe num único arquivo chamado classes.py na pasta models, na tentativa
# de deixar mais organizado.

# Os comentários feitos em routes_index e routes_imóvel, e templates index e
# do tipo _imovel servem basicamente para todos os outros a eles similares.

# I can also present this in english.
  
# Preferi deixar assim para praticar o procedimento.
from routes.routes_index import *
from routes.routes_imovel import *
from routes.routes_cliente import *
from routes.routes_contrato import *
if __name__ == '__main__':
    app.run(debug=True)

from flask import redirect, url_for
from app import app 


@app.route('/')
def home():
    return 'Ok'


#-----Outra maneira de criar rotas---------
def teste():
    return "<h1> Testando </h1>"
app.add_url_rule("/teste","teste",teste)

#-----Redirecionando URL-------------------

@app.route("/admin")
def admin():
    return "<h1>Admin</h1>"

@app.route("/guest/<name>")
def guest(name):
    return 'Ola guest %s' % name

@app.route("/user/<name>")
@app.route("/user/")
def user(name):
    if name == "admin":
        return redirect(url_for('admin'))
    else:
        redirect(url_for('guest', guest=name))
#----------------------------------------------
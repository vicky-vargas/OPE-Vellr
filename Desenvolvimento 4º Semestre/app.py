from flask import Flask, jsonify, request


app = Flask(__name__)
acessos =[
		{'login':'ewerton','senha':123},
		{'login':'luan','senha':123},
		{'login':'luis','senha':123},
		{'login':'roni','senha':123},
		{'login':'victoria','senha':123}
		]

@app.route("/", methods=['POST'])
def login():
    dic_login = request.json #dicionario vindo do frontend
        
    if dic_login in acessos:
        session['username'] = dic_login['login']#insere nome da pessoa logada na sessao
        return redirect(url_for('/menu'))#acesso a tela de menus
    return "Usuário ou Senha incorretas, tente novamente!"


@app.route('/menu')
def menu():
    if 'username' in session:#verifica se a pessoa já logou
        return '%s está online' % escape(session['username'])
        #caixa
        #comanda
        #pedido
    return redirect(url_for('/'))

#pedido|A/F/P/X aberto/finalizado/pago/cancelado
#pizza |F
@app.route('/comanda')
def comanda():
    if 'username' in session:#verifica se a pessoa já logou
        return '%s está online' % escape(session['username'])
        #importar banco de dados 
        #linkar banco com backend, backend com frontend
        #acesso ao cardapio banco de dados
        #
        #botão finalizar pedido -> vai pra tela de pedidos,
        #e salva no BD como ==A. DATE dia mes ano horario, coluna data.
        #quando cancelado nao faz o insert
        # só insert
    return redirect(url_for('/'))

@app.route('/pedidos')
def pedidos():
    if 'username' in session:#verifica se a pessoa já logou
        return '%s está online' % escape(session['username'])
        #fazer get no BD
        #pedidos em aberto == A
        #fazer update do pedido finalizado == F
        #update quando cancelado == x
    return redirect(url_for('/'))


@app.route('/caixa')
def caixa():
    if 'username' in session:#verifica se a pessoa já logou
        return '%s está online' % escape(session['username'])
        #get no BD
        #fechamento diario get status == p, dia/mes/ano (coluna) == date dia/mes/ano . valor total
        #fechamento mensal get status == p, data (mes) like month(mes). valor total 
        
        #pedidos finalizado == F
        #update quando pago == P
        #update quando cancelado == x
    return redirect(url_for('/'))


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('/'))
	



if __name__ = '__main__':
app.run(host = 'localhost', port = 5002, debug = True)

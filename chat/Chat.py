from bottle import run, get, post, view, request, redirect

messages = [("", "Iniciando conversa em grupo...")]
nome = ""

@get('/')
@view('index')
def index():
    return {'messages': messages, 'nome': nome}


@post('/send')
def sendMessage():
    global nome
    m = request.forms.get('message')
    n = request.forms.get('nome')
    messages.append([n, m])
    nome = n
    redirect('/')


run(host='localhost', port=8080)
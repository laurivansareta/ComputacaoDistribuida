import urllib
import requests
import bottle
import json
import threading
import time
import sys
from bottle import run, get, post, view, request, redirect



peers = sys.argv[2:]
meuPeers = sys.argv[1]
meuHost = 'localhost'

@bottle.route('/peers/<host>/<port>')
def index(host, port):
    #decodificar
    peers.append("http://" + host + ':' + port)
    #remove os repetidos
    peers[:] = list(set(peers))
    return json.dumps(peers)


def client_peer():
    time.sleep(5)
    while True:
        time.sleep(5)
        np = []
        for p in peers:
            r = requests.get(p + '/peers/' + meuHost + '/' + str(meuPeers)) #codificar
            np = np + json.loads(r.text)
            print(np)
            time.sleep(1)
        peers[:] = list(set(np + peers))
        print(peers)


t = threading.Thread(target=client_peer)
t.start()


messages = [("", "Iniciando conversa em grupo...")]
nome = ""

@get('/')
@view('index')
def index():
    return {'messages': messages, 'nome': nome}

@get('/messages')
def get_messages():
    return json.dumps(messages)

@post('/send')
def sendMessage():
    global nome
    m = request.forms.get('message')
    n = request.forms.get('nome')
    messages.append([n, m])
    nome = n
    redirect('/')


def list_to_tuple(lista):
    return [tuple(x) for x in lista]



def client_message():
    time.sleep(5)
    while True:
        time.sleep(1)
        np = []
        for p in peers:
            r = requests.get(p + '/messages')
            print(r.text)
            np = json.loads(r.text)
            print('->>', np)
            time.sleep(1)
        messages[:] = list(set(list_to_tuple(messages + np)))
        #print(messages)

t2 = threading.Thread(target=client_message)
t2.start()


bottle.run(host='localhost', port=int(meuPeers))

#para compilar
#python3 Peer_to_peer.py 8080 http://localhost:8081


'''
Aplicação Web de Chat em Grupo, com vários servidores:
Servidores precisam se comunicar para manter a rede conexa, espamando as urls dos servidores.
Servidores precisam se comunicar para espamando o histório de mensagens.
Para simplificar a implementação (por enquanto):
-Mensagens não precisam estar ordenadas.
-Mensagens podem ser únicas.
-Algoritmo síncrono (com o sleep), O(n3), onde n é o número de mensagens.

'''
from flask import Flask, request
from zeep import Client
from zeep.transports import Transport

app = Flask(__name__)

# Configuração do cliente SOAP
wsdl = 'http://exemplo.com/soap?wsdl'  # Substitua pela URL do seu serviço SOAP
client = Client(wsdl, transport=Transport(timeout=10))

# Rota para listar os dados de todos os usuários
@app.route('/usuarios')
def listar_usuarios():
    response = client.service.listar_usuarios()
    return response

# Rota para listar os dados de todas as músicas
@app.route('/musicas')
def listar_musicas():
    response = client.service.listar_musicas()
    return response

# Rota para listar os dados de todas as playlists de um determinado usuário
@app.route('/playlists/usuario/<int:usuario_id>')
def listar_playlists_usuario(usuario_id):
    response = client.service.listar_playlists_usuario(usuario_id)
    return response

# Rota para listar os dados de todas as músicas de uma determinada playlist
@app.route('/musicas/playlist/<int:playlist_id>')
def listar_musicas_playlist(playlist_id):
    response = client.service.listar_musicas_playlist(playlist_id)
    return response

# Rota para listar os dados de todas as playlists que contêm uma determinada música
@app.route('/playlists/musica/<int:musica_id>')
def listar_playlists_musica(musica_id):
    response = client.service.listar_playlists_musica(musica_id)
    return response

if __name__ == '__main__':
    app.run()

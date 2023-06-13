from suds.client import Client

# URL do serviço SOAP
url = 'http://localhost:8000/api.service?wsdl'

# Criação do cliente SOAP
client = Client(url)


def listar_usuarios():
    usuarios = client.service.listar_usuarios()
    for usuario in usuarios:
        print(f"ID: {usuario.id}, Nome: {usuario.nome}, Idade: {usuario.idade}")


def listar_musicas():
    musicas = client.service.listar_musicas()
    for musica in musicas:
        print(f"ID: {musica.id}, Nome: {musica.nome}, Artista: {musica.artista}")


def listar_playlists_por_usuario(usuario_id):
    playlists = client.service.listar_playlists_por_usuario(usuario_id)
    for playlist in playlists:
        print(f"ID: {playlist.id}, Nome: {playlist.nome}")


def listar_musicas_por_playlist(playlist_id):
    musicas = client.service.listar_musicas_por_playlist(playlist_id)
    for musica in musicas:
        print(f"ID: {musica.id}, Nome: {musica.nome}, Artista: {musica.artista}")


def listar_playlists_com_musica(musica_id):
    playlists = client.service.listar_playlists_com_musica(musica_id)
    for playlist in playlists:
        print(f"ID: {playlist.id}, Nome: {playlist.nome}")


# Exemplo de uso das funções

print("Listagem de todos os usuários:")
listar_usuarios()

print("\nListagem de todas as músicas:")
listar_musicas()

print("\nListagem das playlists de um determinado usuário (ID: 1):")
listar_playlists_por_usuario(1)

print("\nListagem das músicas de uma determinada playlist (ID: 1):")
listar_musicas_por_playlist(1)

print("\nListagem das playlists que contêm uma determinada música (ID: 1):")
listar_playlists_com_musica(1)

import grpc
import api_pb2
import api_pb2_grpc

def main():
    channel = grpc.insecure_channel('localhost:5555')  # Endereço e porta do servidor gRPC
    client = api_pb2_grpc.MyApiStub(channel)

    # Listar todos os usuários
    usuarios = client.ListarUsuarios(api_pb2.EmptyMessage())
    print('=== Usuários ===')
    for usuario in usuarios:
        print('Nome:', usuario.nome)
        print('ID:', usuario.id)
        print('Idade:', usuario.idade)
        print('---')

    # Listar todas as músicas
    musicas = client.ListarMusicas(api_pb2.EmptyMessage())
    print('=== Músicas ===')
    for musica in musicas:
        print('Nome:', musica.nome)
        print('ID:', musica.id)
        print('Artista:', musica.artista)
        print('---')

    # Listar todas as playlists de um determinado usuário
    id_usuario = 2 # ID do usuário desejado
    usuarios = []
    usuario = ''
    usuarios = client.ListarUsuarios(api_pb2.EmptyMessage())
    playlists_usuario = []
    playlists = client.ListarPlaylists(api_pb2.EmptyMessage())
    for usuarios_lista in usuarios:
        if(usuarios_lista.id == id_usuario):
            usuario = usuarios_lista
    for playlist in playlists:
        if playlist.id in usuario.id_playlist:
            playlists_usuario.append(playlist)
    print('=== Playlists do Usuário (ID:', id_usuario, ') ===')
    for playlist in playlists_usuario:
        print('ID:', playlist.id)
        print('Nome:', playlist.nome)
        print('---')


    # Listar todas as playlists que contêm uma determinada música
    id_musica = 1  # ID da música desejada
    playlists_musica = []
    playlists = client.ListarPlaylists(api_pb2.EmptyMessage())
    for playlist in playlists:
        if id_musica in playlist.id_musica:
            playlists_musica.append(playlist)
    print('=== Playlists da Música (ID:', id_musica, ') ===')
    for playlist in playlists_musica:
        print('ID:', playlist.id)
        print('Nome:', playlist.nome)
        print('---')

    # listar todas as musicas de uma playlist
 
    id_playlist = 1
    musicas = []
    musicas = client.ListarMusicas(api_pb2.EmptyMessage())
    print('=== Musicas da playlist (ID:', id_playlist, ') ===')
    playlists_musica = []
    playlists = client.ListarPlaylists(api_pb2.EmptyMessage())
    playlist = ''
    for playlist_lista in playlists:
        if(playlist_lista.id == id_playlist):
            playlist = playlist_lista

    for musica in musicas:
        if(musica.id in playlist.id_musica):
             print('Nome:', musica.nome)
             print('ID:', musica.id)
             print('Artista:', musica.artista)
             print('---')
    

if __name__ == '__main__':
    main()

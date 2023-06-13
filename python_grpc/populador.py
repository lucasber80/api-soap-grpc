import grpc
import api_pb2
import api_pb2_grpc

def main():
    channel = grpc.insecure_channel('localhost:5555')  # Endereço e porta do servidor gRPC
    client = api_pb2_grpc.MyApiStub(channel)

    # Popula a tabela de usuários
    usuario1 = client.CriarUsuario(api_pb2.Usuario(nome='Usuário 1', id=1, idade=25,id_playlist = [1,2]))
    usuario2 = client.CriarUsuario(api_pb2.Usuario(nome='Usuário 2', id=2, idade=30,id_playlist = [1]))

    # Popula a tabela de músicas
    musica1 = client.CriarMusica(api_pb2.Musica(nome='Música 1', id=1, artista='Artista 1'))
    musica2 = client.CriarMusica(api_pb2.Musica(nome='Música 2', id=2, artista='Artista 2'))
    musica3 = client.CriarMusica(api_pb2.Musica(nome='Música 3', id=3, artista='Artista 1'))

    # Popula a tabela de playlists
    playlist1 = client.CriarPlaylist(api_pb2.Playlist(id=1, nome='Playlist 1',id_musica = [1,2,3]))
    playlist1 = client.CriarPlaylist(api_pb2.Playlist(id=2, nome='Playlist 2',id_musica = [1]))

   

    print('Dados populados com sucesso.')

if __name__ == '__main__':
    main()

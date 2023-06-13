import grpc
from concurrent import futures
import api_pb2
import api_pb2_grpc

class MyApiServicer(api_pb2_grpc.MyApiServicer):
    def __init__(self):
        self.usuarios = []
        self.musicas = []
        self.playlists = []

    def CriarUsuario(self, request, context):
        self.usuarios.append(request)
        return request

    def ListarUsuarios(self, request, context):
        for usuario in self.usuarios:
            yield usuario

    def CriarMusica(self, request, context):
        self.musicas.append(request)
        return request

    def ListarMusicas(self, request, context):
        for musica in self.musicas:
            yield musica

    def CriarPlaylist(self, request, context):
        self.playlists.append(request)
        return request

    def ListarPlaylists(self, request, context):
        for playlist in self.playlists:
            yield playlist

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    api_pb2_grpc.add_MyApiServicer_to_server(MyApiServicer(), server)
    server.add_insecure_port('[::]:5555')  # Define a porta do servidor
    server.start()
    print('Servidor gRPC iniciado na porta 5555...')
    server.wait_for_termination()

if __name__ == '__main__':
    serve()

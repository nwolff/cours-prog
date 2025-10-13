"""
ChatGPT 4o-Mini: écris un jeu d'aventure simple en python qui accepte des connexions sur un socket et permet de jouer avec telnet

Puis ajout de la possibilité de se connecter à plusieurs avec :
https://www.techwithtim.net/tutorials/python-online-game-tutorial/server
"""

import socket
import sys
from _thread import start_new_thread

rooms = {
    "salon": "Vous êtes dans le salon. Il y a une porte au nord et une porte au sud.",
    "cuisine": "Vous êtes dans la cuisine. Il y a un frigo et une porte au sud.",
    "jardin": "Vous êtes dans le jardin. Il y a un chien.",
    "paradis": "Vous êtes au paradis. Cocas et tacos infinis",
}


class GameServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self.clients = []

    def start(self):
        # Création d'un socket TCP
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        print(f"Serveur en attente de connexion sur {self.host}:{self.port}...")

        while True:
            client_socket, client_address = self.socket.accept()
            self.clients.append(client_socket)
            print(f"Connexion établie avec {client_address}")
            start_new_thread(self.handle_client, (client_socket,))

    def handle_client(self, client_socket: socket.socket):

        def send(text):
            client_socket.sendall((text + "\n").encode())

        def describe_room():
            send(rooms[current_room])

        send("Bienvenue dans le jeu d'aventure !")
        current_room = "salon"
        describe_room()

        while True:
            try:
                send("Que voulez-vous faire ?")
                command = client_socket.recv(1024).decode().strip().lower()

                if current_room == "salon" and command == "nord":
                    current_room = "cuisine"
                    describe_room()
                elif current_room == "cuisine" and command.startswith("ouvrir"):
                    current_room = "paradis"
                    describe_room()
                    client_socket.close()
                elif current_room == "cuisine" and command == "sud":
                    current_room = "salon"
                    describe_room()
                elif current_room == "salon" and command == "sud":
                    current_room = "jardin"
                    describe_room()
                elif current_room == "jardin" and command.startswith("caresse"):
                    send("WOOF!")
                elif current_room == "jardin" and command == "nord":
                    current_room = "salon"
                    describe_room()
                else:
                    send("Commande inconnue.")

            except (ConnectionResetError, BrokenPipeError):
                print("Le client a été déconnecté.")
                break

        client_socket.close()
        self.clients.remove(client_socket)


if __name__ == "__main__":
    host = "0.0.0.0"
    port = 12345

    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    server = GameServer(host, port)
    server.start()

#!/usr/bin/env python3

"""
ChatGPT 4o-Mini: écris un jeu d'aventure simple en python qui accepte des connexions sur un socket et permet de jouer avec telnet

Puis ajout de la possibilité de se connecter à plusieurs avec :
https://www.techwithtim.net/tutorials/python-online-game-tutorial/server
"""


import socket
import sys
from _thread import start_new_thread


# Création du serveur de jeu
class GameServer:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = None
        self.clients = []

    def start(self):
        # Création d'un socket TCP
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((self.host, self.port))
        self.socket.listen(1)
        print(f"Serveur en attente de connexion sur {self.host}:{self.port}...")

        while True:
            client_socket, client_address = self.socket.accept()
            self.clients.append(client_socket)
            print(f"Connexion établie avec {client_address}")
            client_socket.sendall(b"Bienvenue dans le jeu d'aventure !\n")
            start_new_thread(self.handle_client, (client_socket,))

    def handle_client(self, client_socket):
        # Exemple d'aventure textuelle très simple
        current_room = "salon"

        rooms = {
            "salon": "Vous êtes dans le salon. Il y a une porte au nord et une porte au sud.",
            "cuisine": "Vous êtes dans la cuisine. Il y a une porte au sud.",
            "jardin": "Vous êtes dans le jardin. Ca ne sent pas très bon",
            "paradis": "Vous êtes dans au paradis. Cocas et tacos infinis",
        }

        # Envoi de la première description
        client_socket.sendall(
            f"Vous êtes dans une maison. {rooms[current_room]}\n".encode()
        )

        # Boucle de gestion des commandes
        while True:
            try:
                client_socket.sendall(
                    b"Que voulez-vous faire ? (nord, sud, est, ouest)\n"
                )
                command = client_socket.recv(1024).decode().strip().lower()

                if command == "nord" and current_room == "salon":
                    current_room = "cuisine"
                    client_socket.sendall(
                        f"Vous allez au {current_room}. {rooms[current_room]}\n".encode()
                    )
                elif command == "ouvrir frigo" and current_room == "cuisine":
                    current_room = "paradis"
                    client_socket.sendall(
                        f"Vous allez au {current_room}. {rooms[current_room]}\n".encode()
                    )
                elif command == "sud" and current_room == "cuisine":
                    current_room = "salon"
                    client_socket.sendall(
                        f"Vous allez au {current_room}. {rooms[current_room]}\n".encode()
                    )
                elif command == "sud" and current_room == "salon":
                    current_room = "jardin"
                    client_socket.sendall(
                        f"Vous allez au {current_room}. {rooms[current_room]}\n".encode()
                    )
                elif command == "nord" and current_room == "jardin":
                    current_room = "salon"
                    client_socket.sendall(
                        f"Vous allez au {current_room}. {rooms[current_room]}\n".encode()
                    )
                else:
                    client_socket.sendall(b"Commande inconnue. Essayez nord ou sud.\n")

            except (ConnectionResetError, BrokenPipeError):
                print("Le client a été déconnecté.")
                break

        client_socket.close()


# Code principal
def main():
    host = "0.0.0.0"
    port = 12345

    if len(sys.argv) > 1:
        port = int(sys.argv[1])

    server = GameServer(host, port)
    server.start()


if __name__ == "__main__":
    main()

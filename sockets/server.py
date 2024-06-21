import pickle
from queue import Queue
from typing import Any
from socket import *

HOST_NAME: str = '127.0.0.1'


class QCarRecordServer:
    def __init__(self, port: int) -> None:
        self.server: socket = socket(AF_INET, SOCK_STREAM)
        self.running: bool = False
        self.server.bind((HOST_NAME, port))
        self.server.listen(1)

    def terminate(self) -> None:
        self.server.close()

    def execute(self, callback) -> None:
        print("The server is ready to accept information...")
        client, address = self.server.accept()
        print(f"Connected to {address}")

        self.running = True
        while self.running:
            try:
                receive_from_client: bytes = client.recv(8_071_000)
                if receive_from_client is not None:
                    received_data: Any = pickle.loads(receive_from_client)
                    callback(received_data)
                    print("Exit for the callback")
                    client.sendall(pickle.dumps("200"))
                    print("Sending response to the client")
            except Exception as e:
                print(e)
                self.running = False

        client.close()

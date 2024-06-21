import pickle
from socket import *
from queue import Queue
from typing import Any

HOST_NAME: str = '127.0.0.1'


class QCarRecordClient:
    def __init__(self, port: int) -> None:
        self.client: socket = socket(AF_INET, SOCK_STREAM)  # tcp protocal
        self.port: int = port

    def connect_to_server(self) -> None:
        self.client.connect((HOST_NAME, self.port))
        print("Successfully connected to the server")

    def execute(self, data_queue: Queue) -> None:
        try:
            if not data_queue.empty():
                # transmit data to the server
                data: dict = data_queue.get()
                pickle_data: bytes = pickle.dumps(data)
                print(f"Sending {len(pickle_data)} bytes...")
                self.client.sendall(pickle_data)
                # get the response from the server
                response: Any = self.client.recv(1024)
                print(f"Code {pickle.loads(response)}") # temp response handle
        except ConnectionResetError:
            print("Server connection reset. Reconnecting...")
            self.client: socket = socket(AF_INET, SOCK_STREAM)
            self.connect_to_server() # attempt to reconnect
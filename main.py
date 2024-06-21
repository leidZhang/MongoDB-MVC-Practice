import os
import time
from typing import List
from multiprocessing import Process
from queue import Queue

from utils import prepare_mock_online_data
from utils import MOCK_TIMESTAMPS, MOCK_TASKS
from client import QCarRecordClient
from server import QCarRecordServer
from controllers import QCarDataController

PORT: int = 8080


def start_server() -> None: # server lifecycle
    server: QCarRecordServer = QCarRecordServer(PORT)
    controller: QCarDataController = QCarDataController()

    start_time: float = time.time()
    while time.time() - start_time <= 64:
        server.execute(controller.save_data_online)
    server.terminate()


def start_client() -> None: # client lifecycle
    pointer: int = 0
    data_queue: Queue = Queue()
    client: QCarRecordClient = QCarRecordClient(port=PORT)

    client.connect_to_server()
    start_time: float = time.time()
    while time.time() - start_time <= 60:
        steps: List[dict] = prepare_mock_online_data(
            MOCK_TIMESTAMPS[pointer], MOCK_TASKS[pointer]
        ) # step will repeat periodically
        pointer = (pointer + 1) % 2 # avoid index error
        for step in steps:
            comm_start: float = time.time()
            data_queue.put(step)
            client.execute(data_queue)
            comm_end: float = time.time() - comm_start
            time.sleep(max(0, 0.01 - comm_end)) # mock delay


if __name__ == "__main__":
    try:
        mock_server_process: Process = Process(target=start_server)
        mock_server_process.start()
        time.sleep(4) # wait for sever starts
        start_client()
    except Exception as e:
        print(e)
    finally:
        os._exit(0)
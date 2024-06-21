from typing import List

from services import QCarDataService


class QCarDataController:
    def __init__(self) -> None:
        self.service: QCarDataService = QCarDataService()

    def save_data_offline(self, data: dict) -> None:
        # Save data from npz, pkl, etc
        self.service.save_data_offline(data)

    def save_data_online(self, data: dict) -> None:
        # Save data in real time
        self.service.save_data_online(data)
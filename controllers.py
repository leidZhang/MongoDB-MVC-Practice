from typing import List

from services import QCarDataService


class QCarDataController:
    def __init__(self) -> None:
        self.service: QCarDataService = QCarDataService()

    def save_data(self, data: List[dict]) -> None:
        # Save data using the service layer
        self.service.save_data(data)
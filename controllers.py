from services import QCarDataService


class QCarDataController:
    def __init__(self) -> None:
        self.service: QCarDataService = QCarDataService()

    def save_data(self, data: dict) -> None:
        try:
            # Save data using the service layer
            self.service.save_data(data)
        except Exception as e:
            print(f"An error occurred while saving data: {e}")
from entities import Episode, Step
from models import QCarDataModel


class QCarDataService:
    def __init__(self) -> None:
        self.model: QCarDataModel = QCarDataModel()

    def save_data(self, data: dict) -> None:
        # Unpack the simple data transmitted from the QCar
        episode_data: dict = {
            "timestamp": data["timestamp"],
            "task": data["task"],
            "steps": [Step(step_data) for step_data in data["steps"]]
        }
        # Create Episode instance
        episode: Episode = Episode(episode_data)
        # Save data using the service layer
        self.model.save_data(episode)
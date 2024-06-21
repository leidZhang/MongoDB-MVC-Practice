import hashlib
from datetime import datetime

import cv2

from common.entities import Step, Episode
from .models import QCarDataModel


class QCarDataService:
    def __init__(self) -> None:
        self.model: QCarDataModel = QCarDataModel()
        self.last_timestamp: datetime = None
        self.current_episode_data: dict = None

    def _handle_image_data(self, step: Step) -> None:
        # Generate a unique hash for the image based on the current timestamp
        current_time = datetime.now().strftime('%Y%m%d%H%M%S%f')
        hash_object = hashlib.sha256(current_time.encode())
        hex_dig = hash_object.hexdigest()

        image_path: str = f"images/{hex_dig}.jpg"
        cv2.imwrite(image_path, step.front_csi_image) # save image to disk
        step.front_csi_image = image_path # save image path instead of image

    def _handle_convert_episode(self, episode_data: dict) -> Episode:
        # pack the data to Step objects
        episode: Episode = Episode(episode_data)
        # Save image to the disk
        for step in episode.steps:
            self._handle_image_data(step)
        return episode

    def save_data_offline(self, episode_data: dict) -> None:
        # convert dict to Episode data type
        episode: Episode = self._handle_convert_episode(episode_data)
        # Save data list using the model layer
        self.model.save_data(episode)

    def save_data_online(self, step_data: dict) -> None:
        timestamp: datetime = step_data["timestamp"] # episode timestamp
        if timestamp == self.last_timestamp:
            self.current_episode_data["steps"].append(step_data)
        else:
            # Convert raw data to Episode and Step type
            if self.current_episode_data is not None:
                print("Saving data to the database...")
                # convert dict to Episode data type
                episode: Episode = self._handle_convert_episode(self.current_episode_data)
                # Let the model layer handle the data save
                self.model.save_data(episode)
            # Update the state
            print("Start recording new episode")
            self.last_timestamp = timestamp
            self.current_episode_data = {
                "timestamp": timestamp,
                "task": step_data["task"],
                "steps": [step_data]
            }

            print("Complete new episode data initialization")
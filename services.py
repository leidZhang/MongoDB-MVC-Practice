import hashlib
from datetime import datetime

import cv2

from entities import Step, Episode
from models import QCarDataModel


class QCarDataService:
    def __init__(self) -> None:
        self.model: QCarDataModel = QCarDataModel()

    def save_data(self, data: dict) -> None:
        # pack the data to Step objects
        episode: Episode = Episode(data)
        # Save image to the disk
        for step in episode.steps:
            # Generate a unique hash for the image based on the current timestamp
            current_time = datetime.now().strftime('%Y%m%d%H%M%S%f')
            hash_object = hashlib.sha256(current_time.encode())
            hex_dig = hash_object.hexdigest()
            
            image_path: str = f"assets/{hex_dig}.jpg"
            cv2.imwrite(image_path, step.front_csi_image) # save image to disk
            step.front_csi_image = image_path # save image path instead of image
        # Save data list using the model layer
        self.model.save_data(episode)
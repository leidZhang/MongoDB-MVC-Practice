from typing import List, Union
from datetime import datetime

import numpy as np


class Step:
    def __init__(self, step_data: dict) -> None:
        self.id: int = step_data["id"] if "id" in step_data.keys() else 0 # step index
        self.state: np.ndarray = step_data["state"] # x, y, yaw, vx, vy, omega
        self.waypoints: np.ndarray = step_data["waypoints"] # 200 waypoints
        self.motor_tach: float = step_data["motor_tach"] # current motor tach
        self.reward: float = step_data["reward"] # step reward
        self.front_csi_image: Union[np.ndarray, str] = step_data["front_csi_image"] # image
        self.action: np.ndarray = step_data["action"] # [throttle, steering]
        self.noise: np.ndarray = step_data["noise"] # [noise_t, noise_s]

    def to_bson(self, counter: int) -> dict:
        return {
            "id": counter,
            "state": self.state.tolist(),
            "waypoints": self.waypoints.tolist(),
            "motor_tach": self.motor_tach,
            "reward": self.reward,
            "front_csi_image": self.front_csi_image,
            "action": self.action.tolist(),
            "noise": self.noise.tolist()
        }


class Episode:
    def __init__(self, episode_data: dict) -> None:
        self.timestamp: datetime = episode_data["timestamp"] # episode start time
        self.task: List[int] = episode_data["task"] # current node sequence
        self.steps: List[Step] = [Step(step_data) for step_data in episode_data["steps"]] # all steps in episode

    def to_bson(self) -> dict:
        bson_steps: dict = [self.steps[i].to_bson(i) for i in range(len(self.steps))]
        return {
            "timestamp": self.timestamp,
            "task": self.task,
            "steps": bson_steps
        }
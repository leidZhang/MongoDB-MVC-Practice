from typing import List
from datetime import datetime

import numpy as np

MOCK_TIMESTAMPS = [
    datetime(2024, 6, 20, 23, 21, 2),
    datetime(2024, 6, 20, 23, 22, 1),
]
MOCK_TASKS = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
]


def prepare_mock_steps_data() -> List[dict]:
    step_1: dict = {
        "id": 1,
        "state": np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
        "waypoints": np.array([0.0] * 200),
        "motor_tach": 0.0,
        "reward": 0.0,
        "current_waypoint": 0,
        "front_csi_image": np.zeros((410, 820, 3)),
        "action": np.array([0.0, 0.0]),
        "noise": np.array([0.0, 0.0])
    }

    step_2: dict = {
        "id": 2,
        "state": np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
        "waypoints": np.array([0.0] * 200),
        "motor_tach": 0.0,
        "reward": 0.0,
        "current_waypoint": 1,
        "front_csi_image": np.zeros((410, 820, 3)),
        "action": np.array([0.0, 0.0]),
        "noise": np.array([0.0, 0.0])
    }

    step_3: dict = {
        "id": 2,
        "state": np.array([0.0, 0.0, 0.0, 0.0, 0.0, 0.0]),
        "waypoints": np.array([0.0] * 200),
        "motor_tach": 0.0,
        "reward": 0.0,
        "current_waypoint": 2,
        "front_csi_image": np.zeros((410, 820, 3)),
        "action": np.array([0.0, 0.0]),
        "noise": np.array([0.0, 0.0])
    }

    return [step_1, step_2, step_3]


def prepare_mock_online_data(mock_time: datetime, mock_task: List[int]) -> List[dict]:
    steps: List[dict] = prepare_mock_steps_data()
    for step in steps:
        step["timestamp"] = mock_time
        step["task"] = mock_task
    return steps


def prepare_mock_episode_data(raw_steps: List[dict]) -> dict:
    return {
        "timestamp": "2021-01-01T00:00:00",
        "task": [0, 1, 2],
        "steps": raw_steps
    }
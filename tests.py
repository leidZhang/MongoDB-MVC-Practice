from typing import List, Tuple

import numpy as np

from entities import Step, Episode
from controllers import QCarDataController


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


def prepare_mock_episode_data(raw_steps: List[dict]) -> dict:
    return {
        "timestamp": "2021-01-01T00:00:00",
        "task": [0, 1, 2],
        "steps": raw_steps
    }


def test_step_to_bson() -> None:
    raw_steps: List[dict] = prepare_mock_steps_data()
    steps: List[Step] = [Step(step_data) for step_data in raw_steps]
    for i in range(len(steps)):
        converted_data: dict = steps[i].to_bson(i)
        assert converted_data['id'] is not None
        assert type(converted_data) is dict
        assert len(converted_data.keys()) == 9


def test_episode_to_bson() -> None:
    raw_steps: List[dict] = prepare_mock_steps_data()
    raw_episode: dict = prepare_mock_episode_data(raw_steps)
    episode: Episode = Episode(raw_episode)
    converted_data: dict = episode.to_bson()
    assert converted_data['timestamp'] is not None
    assert type(converted_data) is dict
    assert len(converted_data.keys()) == 3

    print(converted_data["steps"])


def mock_save_data() -> None:
    # prepare the mock data
    raw_steps: List[dict] = prepare_mock_steps_data()
    raw_episode: dict = prepare_mock_episode_data(raw_steps)
    # prepare the data controller
    controller: QCarDataController = QCarDataController()
    controller.save_data(raw_episode)


if __name__ == "__main__":
    mock_save_data()
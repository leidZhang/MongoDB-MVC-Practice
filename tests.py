from typing import List, Tuple

import numpy as np
from pymongo import MongoClient

from entities import Step, Episode
from controllers import QCarDataController
from utils import prepare_mock_episode_data, prepare_mock_steps_data


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


def test_save_data() -> None:
    # prepare the mock data
    raw_steps: List[dict] = prepare_mock_steps_data()
    raw_episode: dict = prepare_mock_episode_data(raw_steps)
    # prepare the data controller
    controller: QCarDataController = QCarDataController()
    controller.save_data_offline(raw_episode)


def test_connection() -> None:
    try:
        client: MongoClient = MongoClient("mongodb://localhost:27017/")
        databases: list = client.list_database_names()
        print(f"Connection successful, database list: {databases}")
    except Exception:
        print("Connection failed, please check your MongoDB Server")


if __name__ == "__main__":
    test_save_data()
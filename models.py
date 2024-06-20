from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

from entities import Episode


class QCarDataModel:
    def __init__(self) -> None:
        client: MongoClient = MongoClient("mongodb://localhost:27017/")
        self.database: Database = client["qcardb"]
        self.collection: Collection = self.database["qcarTestRecords"]

    def save_data(self, episode_data: Episode) -> None:
        data_for_save: dict = episode_data.to_bson()
        self.collection.insert_one(data_for_save)
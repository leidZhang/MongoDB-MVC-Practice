import bson

from pymongo import MongoClient
from pymongo.database import Database
from pymongo.collection import Collection

from entities import Step, Episode


class QCarDataModel:
    def __init__(self) -> None:
        client: MongoClient = MongoClient("mongodb://localhost:27017/")
        self.database: Database = client["qcardb"]
        self.collection: Collection = self.database["qcarTestRecords"]

    def save_data(self, data: Episode) -> None:
        data_for_save: dict = data.to_bson()
        data_size: int = len( bson.BSON.encode(data_for_save))
        self.collection.insert_one(data_for_save)
        print(f"Saved {data_size} bytes to the database.")
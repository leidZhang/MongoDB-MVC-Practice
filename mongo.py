from pymongo import MongoClient

def test_connection() -> None:
    try:
        client: MongoClient = MongoClient("mongodb://localhost:27017/")
        databases: list = client.list_database_names()
        print(f"Connection successful, database list: {databases}")
    except Exception:
        print("Connection failed, please check your MongoDB Server")

if __name__ == "__main__":
    test_connection()
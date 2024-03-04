import os
from pydantic import BaseModel
from utils.constants import DATASTORE_BASE_DIRECTORY

class Entity(BaseModel):
    key: str
    data: str

def get_entity_processor(shard_id: str, table_name: str, key: str):
    table_directory = os.path.join(DATASTORE_BASE_DIRECTORY, shard_id + table_name)
    if (os.path.exists(table_directory)):
        file_path = os.path.join(table_directory, f"{key}.txt")
        
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Entity with key '{key}' not found")
        
        try:
            with open(file_path, "r") as file:
                data = file.read()
            return Entity(key=key, data=data)
        except Exception as e:
            raise ValueError(f"Error reading entity with key '{key}': {str(e)}")
    else:
        raise IsADirectoryError(f"Table '{table_name}' not found")

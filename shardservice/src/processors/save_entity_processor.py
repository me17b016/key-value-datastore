import os
import json
from pydantic import BaseModel
from utils.constants import DATASTORE_BASE_DIRECTORY
from processors.get_entity_processor import get_entity_processor
from exceptions import OptimisticVersionConflict


def save_entity_processor(shard_id: str, table_name: str, key: str, entity: dict):
    table_directory = os.path.join(DATASTORE_BASE_DIRECTORY, shard_id + table_name)
    # os.makedirs(table_directory, exist_ok=True)
    if (os.path.exists(table_directory)):
        file_path = os.path.join(table_directory, f"{key}.txt")
        if (os.path.exists(file_path)):
            t = get_entity_processor(shard_id, table_name, key).data
            tt = t.replace("'", "\"")
            print(tt)
            existing_entity = json.loads(tt)
            print(existing_entity)
            print(entity)
            if (is_key_none(entity, 'version') or existing_entity['version'] != entity['version']):
                 raise OptimisticVersionConflict("Version conflict during update")
            else:
                entity['version'] += 1
        else:
            entity['version'] = 0
        try:
            with open(file_path, "w") as file:
                    file.write(str(entity))
        except Exception as e:
             raise ValueError(f"Error saving entity with key '{key}': {str(e)}")
    else:
        raise IsADirectoryError(f"Table '{table_name}' not found")
    

def is_key_none(dict, key):
    return dict.get(key) is None
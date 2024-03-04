import os
from pydantic import BaseModel
from constants import TABLES_BASE_DIRECTORY, EMPTY_STRING


def get_shard_id_processor(table_name: str, key: str):
    try:
        shards = get_no_of_shards(table_name=table_name)
        hash_value = hash(key)
        shard_id = hash_value % shards
        return f"shard{str(shard_id)}"
    except Exception as e:
        raise


def get_no_of_shards(table_name: str):
    table_path = os.path.join(TABLES_BASE_DIRECTORY, f"{table_name}.txt")
    if (os.path.exists(table_path)):
        try:
            with open(table_path, "r") as file:
                first_line = file.readline().strip()
                if first_line.startswith('SHARDS:'):
                    shards = int(first_line[len('SHARDS:'):])
                    return shards
                else:
                    raise ValueError("Invalid file format. The first line should start with 'SHARDS:'")
        except Exception as e:
            raise ValueError(f"Error reading table config '{table_name}': {str(e)}")
    else:
        raise FileNotFoundError(f"Config for table'{table_name}' not found")
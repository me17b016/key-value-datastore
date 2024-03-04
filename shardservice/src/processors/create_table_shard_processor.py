import os
from utils.constants import DATASTORE_BASE_DIRECTORY

def create_table_shard_processor(shard_id: str, table_name: str):
    table_directory = os.path.join(DATASTORE_BASE_DIRECTORY, shard_id + table_name)
    try:
        os.makedirs(table_directory, exist_ok=True)
    except Exception as e:
        print(f"Error occurred while creating table shard for table {table_name} and shard {shard_id}")
        raise e

        
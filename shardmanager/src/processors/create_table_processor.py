import os
import requests
from typing import Optional
from constants import TABLES_BASE_DIRECTORY, SHARDS, COLON, DEFAULT_SHARDS
from utils.shard_util import get_shards, get_shards_url
from clients.shard_service_client import ShardServiceClient

async def create_table_processor(table_name: str, no_of_shards: Optional[int]=DEFAULT_SHARDS):
    table_path = os.path.join(TABLES_BASE_DIRECTORY, f"{table_name}.txt")
    if (os.path.exists(table_path)):
        raise FileExistsError(f"The table '{table_name}' already exists.")
    
    try:
        shard_ids = get_shard_ids(no_of_shards)
        with open(table_path, "w") as file:
                file.write(f"{SHARDS}{COLON}{str(no_of_shards)}\n")
                file.write(':'.join(shard_ids))
        await intialize_table_in_shards(shard_ids, table_name)
    except Exception as e:
            raise ValueError(f"Error creating table '{table_name}': {str(e)}")
    

def get_shard_ids(no_of_shards: int):
    shards = get_shards()
    return [key for key, _ in list(shards)[:no_of_shards]]


async def intialize_table_in_shards(shard_ids: list, table_name: str):
    for shard_id in shard_ids:
        try:
            await ShardServiceClient.create_table_shard(shard_id, table_name)
        except Exception as e:
            print(f"Failed to initializetable {table_name} for shard {shard_id}")
            raise e
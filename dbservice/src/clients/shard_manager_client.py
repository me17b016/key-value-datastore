from clients.http_client import HttpClient
from typing import Optional

class ShardManagerClient:
    _client = None
    BASE_URL = "http://127.0.0.1:8000"

    def get_instance():
        if ShardManagerClient._client is None:
           ShardManagerClient._client = HttpClient(base_url=ShardManagerClient.BASE_URL)
        return ShardManagerClient._client

    async def create_table(table_name: str, no_of_shards: Optional[int]):
        ShardManagerClient.get_instance()
        try:
            body = {"table_name": table_name, "no_of_shards": no_of_shards}
            response = await ShardManagerClient._client.post("/v1/create_table", data=body)
            return {"data_from_external_service": response.json()}
        except Exception as e:
            print(f"Error while creating table {table_name}")
            raise e
            
    async def get_shard_id(table_name: str, key: str):
        ShardManagerClient.get_instance()
        try:
            body = {"table_name": table_name, "key": key}
            response = await ShardManagerClient._client.post("/v1/get_shard_id", data=body)
            return {"data_from_external_service": response.json()}
        except Exception as e:
            print("Error while getting shard id from shard manager")
            raise e
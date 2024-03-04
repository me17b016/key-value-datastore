from clients.http_client import HttpClient
from utils import shard_util

class ShardServiceClient:

    async def create_table_shard(shard_id: str, table_name: str):
        shard_url = shard_util.get_shard_url(shard_id)
        client = HttpClient(shard_url)
        try:
            body = {"shard_id": shard_id, "table_name": table_name}
            response = await client.post("v1/create_table_shard", data=body)
            return {"response": response.json()}
        except Exception as e:
            print(f"Error while creating table {table_name}")
            raise e
            
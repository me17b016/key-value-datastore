from clients.shard_manager_client import ShardManagerClient
from clients.shard_service_client import ShardServiceClient


async def save_entity(table_name: str, key: str, entity: dict):
    shard_id = await ShardManagerClient.get_shard_id(table_name=table_name,
                                                   key=key)
    print(shard_id)
    return await ShardServiceClient.save_entity(shard_id=shard_id, 
                                                table_name=table_name, 
                                                key=key, 
                                                entity=entity)
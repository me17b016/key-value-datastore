from fastapi import APIRouter
from pydantic import BaseModel
from clients.shard_manager_client import ShardManagerClient, MyHttpClient
from utils import shard_util
router = APIRouter()

class GetEntityRequestModel(BaseModel):
    table_name: str
    key: str

@router.post("/v1/get_entity")
async def get_entity(
    requestModel: GetEntityRequestModel
):
    table_name = requestModel.table_name
    key = requestModel.key
    try:
        shard_id = ShardManagerClient.get_shard_id(table_name=table_name,
                                                   key=key)
        shards_url = shard_util.get_shards_url()
        shard_url = shards_url[shard_id]
        print(shard_url)
        client = MyHttpClient(shard_url)
        body  = {"table_name": table_name, "key": key}
        # response = client.post(endpoint="/v1/get_entity",
        #             data=body)
        return body
    except Exception as e:
       raise e
 
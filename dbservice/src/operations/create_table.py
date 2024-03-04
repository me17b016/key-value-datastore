from fastapi import APIRouter
from pydantic import BaseModel
from typing import Optional
from clients.shard_manager_client import ShardManagerClient

router = APIRouter()

class CreateTableRequestModel(BaseModel):
    table_name: str
    no_of_shards: Optional[int]

@router.post("/v1/create_table")
async def create_table(
    requestModel: CreateTableRequestModel
):
    table_name = requestModel.table_name
    no_of_shards = requestModel.no_of_shards
    try:
        # ShardManagerClient.create_table(table_name=table_name,
        #                                 no_of_shards=no_of_shards)
        return {"k": "v"}
    except Exception as e:
       raise e

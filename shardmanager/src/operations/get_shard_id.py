from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from processors.get_shard_id_processor import get_shard_id_processor

router = APIRouter()

class GetShardIdRequestModel(BaseModel):
    table_name: str
    key: str

class GetShardIdResponseModel(BaseModel):
    shard_id: str

@router.post("/v1/get_shard_id")
async def get_shard_id(
    requestModel: GetShardIdRequestModel
):
    table_name = requestModel.table_name
    key = requestModel.key
    try:
        shard_id = get_shard_id_processor(table_name, key)
        return GetShardIdResponseModel(shard_id=shard_id)
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Entity with key '{key}' not found")
    except ValueError as ve:
        raise HTTPException(status_code=500, detail=str(ve))


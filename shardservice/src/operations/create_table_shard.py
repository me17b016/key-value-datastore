from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from processors.create_table_shard_processor import create_table_shard_processor
from fastapi.responses import JSONResponse

router = APIRouter()

class CreateTableShardRequestModel(BaseModel):
    shard_id: str
    table_name: str

@router.post("/v1/create_table_shard")
async def create_table_shard(
    requestModel: CreateTableShardRequestModel
):
    shard_id = requestModel.shard_id
    table_name = requestModel.table_name
    try:
        create_table_shard_processor(shard_id=shard_id,
                                     table_name=table_name)
        return JSONResponse(content={"message": "success"}, status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
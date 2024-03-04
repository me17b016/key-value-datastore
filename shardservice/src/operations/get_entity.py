from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from processors.get_entity_processor import get_entity_processor
from fastapi.responses import JSONResponse

router = APIRouter()

class GetEntityRequestModel(BaseModel):
    shard_id: str
    table_name: str
    key: str

class GetEntityResponseModel(BaseModel):
    key: str
    data: str

@router.post("/v1/get_entity")
async def get_entity(
    requestModel: GetEntityRequestModel
):
    shard_id = requestModel.shard_id
    table_name = requestModel.table_name
    key = requestModel.key
    try:
        entity = get_entity_processor(shard_id, table_name, key)
        return JSONResponse(status_code=200, content={"key" : entity.key, "data" : entity.data})
    except IsADirectoryError:
        raise HTTPException(status_code=404, detail=f"Table with name '{table_name}' not found")
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Entity with key '{key}' not found")
    except ValueError as ve:
        raise HTTPException(status_code=500, detail=str(ve))
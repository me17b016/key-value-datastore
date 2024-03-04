from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from processors.save_entity_processor import save_entity_processor
from exceptions import OptimisticVersionConflict

router = APIRouter()

class SaveEntityRequestModel(BaseModel):
    shard_id: str
    table_name: str
    key: str
    entity: dict

@router.post("/v1/save_entity")
async def save_entity(
    requestModel: SaveEntityRequestModel
):
    shard_id = requestModel.shard_id
    table_name = requestModel.table_name
    key = requestModel.key
    entity = requestModel.entity

    try:
        save_entity_processor(shard_id, table_name, key, entity)
        return {"message": f"Entity '{key}' saved or updated in table '{table_name}'"} 
    except IsADirectoryError:
        raise HTTPException(status_code=404, detail=f"Table with name '{table_name}' not found")   
    except OptimisticVersionConflict as ovc:
        raise HTTPException(status_code=409, detail=str(ovc))
    except ValueError as ve:
        raise HTTPException(status_code=500, detail=str(ve))
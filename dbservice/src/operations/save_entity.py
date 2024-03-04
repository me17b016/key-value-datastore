from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from processors import save_entity_processor


router = APIRouter()

class SaveEntityRequestModel(BaseModel):
    table_name: str
    key: str
    entity: dict

@router.post("/v1/save_entity")
async def create_table(
    requestModel: SaveEntityRequestModel
):
    table_name = requestModel.table_name
    key = requestModel.key
    entity = requestModel.entity
    try:
        response = await save_entity_processor.save_entity(table_name=table_name,
                    key=key,
                    entity=entity)
        return JSONResponse(content=response.json(), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
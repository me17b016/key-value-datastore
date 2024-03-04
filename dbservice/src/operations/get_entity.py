from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from processors import get_entity_processor
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
        response = await get_entity_processor.get_entity(table_name=table_name,
                         key=key)
        return JSONResponse(content=response.json(), status_code=200)
    except Exception as e:
       raise e
 
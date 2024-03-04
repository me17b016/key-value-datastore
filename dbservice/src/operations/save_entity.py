from fastapi import APIRouter, HTTPException
from pydantic import BaseModel



router = APIRouter()

class CreateTableRequestModel(BaseModel):
    table_name: str
    no_of_shards: Optional[int]

@router.post("/save")
async def create_table(
    requestModel: CreateTableRequestModel
):
    table_name = requestModel.table_name
    try:
        create_table_processor(table_name, no_of_shards)
    except FileExistsError:
        raise HTTPException(status_code=409, detail=f"Table with name '{table_name}' already exists")
    except ValueError as ve:
        raise HTTPException(status_code=500, detail=str(ve))
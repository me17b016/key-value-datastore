from fastapi import APIRouter, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from processors.create_table_processor import create_table_processor
from typing import Optional

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
        res = await create_table_processor(table_name, no_of_shards)
        return JSONResponse(content={"message": "success"}, status_code=200)
    except FileExistsError:
        raise HTTPException(status_code=409, detail=f"Table with name '{table_name}' already exists")
    except ValueError as ve:
        raise HTTPException(status_code=500, detail=str(ve))

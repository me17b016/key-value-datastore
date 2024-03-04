from fastapi import FastAPI
from operations import create_table, get_entity

app = FastAPI()

app.include_router(create_table.router)
app.include_router(get_entity.router)
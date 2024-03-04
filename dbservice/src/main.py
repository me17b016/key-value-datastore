from fastapi import FastAPI
from operations import create_table, save_entity, get_entity

app = FastAPI()

app.include_router(create_table.router)
app.include_router(save_entity.router)
app.include_router(get_entity.router)
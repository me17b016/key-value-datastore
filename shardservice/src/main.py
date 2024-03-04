from fastapi import FastAPI
from operations import save_entity, get_entity, create_table_shard

app = FastAPI()

app.include_router(save_entity.router)
app.include_router(get_entity.router)
app.include_router(create_table_shard.router)
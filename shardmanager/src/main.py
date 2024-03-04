from fastapi import FastAPI
from operations import create_table, get_shard_id

app = FastAPI()

app.include_router(create_table.router)
app.include_router(get_shard_id.router)
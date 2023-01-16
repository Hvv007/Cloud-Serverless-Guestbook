import os

from fastapi import FastAPI
from config import BACKEND_VERSION
from YDB_Client import YDBClient
from models_schemes import InfoOutput, MessageOutput, CreateOutput, Message
import uvicorn

app = FastAPI()

ydb_client = YDBClient()

replica_id = str(ydb_client.get_replica())


@app.get("/")
async def root():
    return {"description": "Guestbook", "type": "api"}


@app.get("/api/info", response_model=InfoOutput)
async def api_info():
    return {"backend_version": BACKEND_VERSION, "replica_id": replica_id}


@app.get("/api/messages", response_model=MessageOutput)
async def get_messages():
    items, response = await ydb_client.get_messages()
    return {"messages": items, "count": response.get("Count", 0)}


@app.post("/api/messages", response_model=CreateOutput)
async def add_message(msg: Message):
    guest_id = await ydb_client.create_message(msg)
    return {"created_id": guest_id, "replica_id": replica_id, "backend_version": BACKEND_VERSION}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

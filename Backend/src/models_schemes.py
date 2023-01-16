from pydantic import BaseModel


class Message(BaseModel):
    guest_name: str
    guest_message: str


class MessageOutputName(BaseModel):
    guest_name: str
    guest_message: str
    guest_id: str


class MessageOutput(BaseModel):
    messages: list[MessageOutputName]
    count: int


class CreateOutput(BaseModel):
    created_id: str
    replica_id: str
    backend_version: str


class InfoOutput(BaseModel):
    replica_id: str
    backend_version: str

from pydantic import BaseModel


class SignalResponse(BaseModel):
    signal: int

from pydantic import BaseModel

# class that contains parameters needed when user uses multiplication endpoints
class Numbers(BaseModel):
    number1: float
    number2: float

class LoginRequest(BaseModel):
    id_token: str

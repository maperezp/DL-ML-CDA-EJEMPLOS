from pydantic import BaseModel

class DataModel(BaseModel):
    credit_score: int
    age: int
    balance: float
    country: str
    products_number: int
    active_member: int

from pydantic import BaseModel


class CarCreate(BaseModel):
    brand: str
    model: str
    year: int
    price: int
    fuel_type: str
    transmission: str
    kilometers: int


class CarResponse(CarCreate):
    id: int

    model_config = {
        "from_attributes": True
    }
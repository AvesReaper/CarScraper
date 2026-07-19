from pydantic import BaseModel


class CarCreate(BaseModel):
    brand: str
    model: str
    year: int
    price: str
    fuel_type: str
    transmission: str
    kilometers: int
    insurance: str
    ownership: str
    displacement: str
    power: str
    drive_type: str

class CarResponse(CarCreate):
    id: int

    model_config = {
        "from_attributes": True
    }

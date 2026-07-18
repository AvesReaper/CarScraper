from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import get_db
from schemas.car import CarCreate, CarResponse
from crud.car import create_car, get_cars, get_car

router = APIRouter(prefix="/cars", tags=["Cars"])

@router.post("/", response_model=CarResponse)
def create_new_car(
    car: CarCreate,
    db: Session = Depends(get_db)
):
    return create_car(db, car)

@router.get("/", response_model=list[CarResponse])
def read_cars(
    db: Session = Depends(get_db)
):
    return get_cars(db)

@router.get("/{car_id}", response_model=CarResponse)
def read_car(
    car_id: int,
    db: Session = Depends(get_db)
):
    car = get_car(db, car_id)

    if not car:
        raise HTTPException(
            status_code=404,
            detail="Car not found"
        )

    return car
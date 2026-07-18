from sqlalchemy.orm import Session

from models import Car
from schemas.car import CarCreate


def create_car(db: Session, car: CarCreate):
    db_car = Car(**car.model_dump())

    db.add(db_car)
    db.commit()
    db.refresh(db_car)

    return db_car

def get_cars(db: Session):
    return db.query(Car).all()

def get_car(db: Session, car_id: int):
    return db.query(Car).filter(Car.id == car_id).first()
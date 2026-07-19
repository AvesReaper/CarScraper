from datetime import datetime

from sqlalchemy import DateTime, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base


class Car(Base):
    __tablename__ = "cars"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    brand: Mapped[str] = mapped_column(String(100), nullable=False)
    model: Mapped[str] = mapped_column(String(100), nullable=False)
    year: Mapped[int] = mapped_column(Integer, nullable=False)
    price: Mapped[str] = mapped_column(String(50), nullable=False)
    fuel_type: Mapped[str] = mapped_column(String(50), nullable=False)
    transmission: Mapped[str] = mapped_column(String(50), nullable=False)
    kilometers: Mapped[str] = mapped_column(Integer, nullable=False)
    insurance: Mapped[str] = mapped_column(String(50), nullable=False)
    ownership: Mapped[str] = mapped_column(String(50), nullable=False)
    displacement: Mapped[str] = mapped_column(String(50), nullable=False)
    power: Mapped[str] = mapped_column(String(50), nullable=False)    
    drive_type: Mapped[str] = mapped_column(String(50), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        nullable=False,
    )
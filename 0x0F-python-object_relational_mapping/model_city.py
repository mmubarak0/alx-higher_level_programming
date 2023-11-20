#!/usr/bin/python3
"""Contains the class definition of a City."""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """City base class."""

    __tablename__ = "cities"
    id = Column(
        Integer, primary_key=True, autoincrement=True,
        nullable=False, unique=True
    )
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('state.id'), nullable=False)

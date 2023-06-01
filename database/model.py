#Improting needed libraries
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#Constructing a base class for declarative class definitions
Base = declarative_base()
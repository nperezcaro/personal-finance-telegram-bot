#Importing the needed libraries
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model import Base
import environ

#Reading enviroment variables
env = environ.Env()
environ.Env().read_env()

user = env('postgres_user')
password = env('postgres_password')
host = env('postgres_host')
database = env('postgres_database')
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


# Configure the database connection
database_url = f"postgresql://{user}:{password}{host}:5432/{database}"

# Create the database engine
engine = create_engine(database_url)

# Create a session factory
Session = sessionmaker(bind=engine)

def get_session():
    """
    Creates a new database session.

    Returns:
        session: A new session object.
    """
    return Session()
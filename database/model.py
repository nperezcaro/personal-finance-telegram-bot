#Improting needed libraries
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

#Constructing a base class for declarative class definitions
Base = declarative_base()


class User(Base):
    """
    Represents a user in the system.

    Attributes:
        id (int): The unique identifier for the user.
        name (str): The name of the user.
        email (str): The email address of the user.
        created_at (datetime): The timestamp of when the user was created.
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    email = Column(String(255))
    created_at = Column(DateTime)

class PaymentMethod(Base):
    """
    Represents a payment method associated with a user.

    Attributes:
        id (int): The unique identifier for the payment method.
        name (str): The name of the payment method.
        user_id (int): The foreign key referencing the user associated with the payment method.
        institution_name (str): The name of the financial institution associated with the payment method.
        user (User): The relationship to the User object, representing the user associated with the payment method.
    """
    __tablename__ = 'payment_methods'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255))
    user_id = Column(Integer, ForeignKey('users.id'))
    institution_name = Column(String(255))
    user = relationship('User', backref='payment_methods')


class Expense(Base):
    """
    Represents an expense recorded in the system.

    Attributes:
        id (int): The unique identifier for the expense.
        date (datetime): The date of the expense.
        amount (float): The amount of the expense.
        category (str): The category of the expense.
        subcategory (str): The subcategory of the expense.
        payment_method_id (int): The foreign key referencing the payment method used for the expense.
        payment_method (PaymentMethod): The relationship to the PaymentMethod object representing the payment method used.
        user_id (int): The foreign key referencing the user associated with the expense.
        user (User): The relationship to the User object representing the user associated with the expense.
    """
    __tablename__ = 'expenses'

    id = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(DateTime)
    amount = Column(Float)
    category = Column(String(255))
    subcategory = Column(String(255))
    payment_method_id = Column(Integer, ForeignKey('payment_methods.id'))
    payment_method = relationship('PaymentMethod', backref='expenses')
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref='expenses')
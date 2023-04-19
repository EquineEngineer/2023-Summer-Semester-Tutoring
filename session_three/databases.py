from __future__ import annotations


from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import Integer
from sqlalchemy import String

from sqlalchemy.orm.decl_api import DeclarativeMeta
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


# Create an in-memory SQLite database
engine = create_engine("sqlite://", echo=True)


# Create a session factory
Session = sessionmaker(bind=engine)


# Base is the base class for all SQLAlchemy models
# Declarative base returns a CLASS
# (In this case, DeclarativeMeta is a metaclass, which is the class of a class.)
Base: DeclarativeMeta = declarative_base()


class Person(Base):
    """
    Person represents a table containing people.

    Each person has a name and an age.

    (Notice the lack of the `__init__` method.
    This is because SQLAlchemy handles the creation of objects for us.)
    """

    __tablename__ = "person"

    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    age = Column(Integer, nullable=False)

    def __repr__(self):
        """Returns a string representation of the Person object.

        Returns:
            A string representation of the form "<Person(name='...', age='...')>".
        """
        return "<Person(name='{}', age='{}')>".format(self.name, self.age)


def main() -> int:
    # add the tables to the database
    Base.metadata.create_all(engine)

    # create a new session
    with Session().no_autoflush as session:
        # John is 18 years old
        john = Person(name="John", age=18)

        # Persist John to the database
        session.add(john)

        # Find all people with the name "John" and an age less than 19
        # This is a list of Person objects
        print(
            session.query(Person).filter(Person.name == "John", Person.age < 19).all()
        )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

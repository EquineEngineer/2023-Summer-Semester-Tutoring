import asyncio

from prisma import Prisma
from prisma.models import Person, Pizza


# Generate the Prisma client (Switch log_queries to True to see the generated SQL queries)
prisma = Prisma(log_queries=False)


# Async function to test the Prisma client
async def test_prisma() -> None:
    # Connect to the database
    await prisma.connect(50)

    buffalo_margherita: Pizza = await prisma.pizza.create(
        {
            "name": "Margherita con Bufala",
            "price": 750,  # Price in cents
        }
    )

    # Create a new person
    # Antonino is 40 years old and likes Margherita pizza
    antonino: Person = await prisma.person.create(
        {
            "name": "Antonino",
            "age": 23,
            "gender": "male",
            "favouritePizza": {
                # The "connect" field is used to connect to an existing object
                "connect": {
                    # The "name" field is used to find the object by its name
                    # Because it is declared as @id in the schema, it is unique
                    "name": buffalo_margherita.name,
                }
            },
        }
    )

    # Find the (first) person with the name "Antonino"
    fetched_antonino = await prisma.person.find_first(where={"name": "Antonino"})

    assert antonino == fetched_antonino

    print(fetched_antonino)


asyncio.run(test_prisma())

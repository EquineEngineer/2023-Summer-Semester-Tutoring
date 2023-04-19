# Session Three

## Prisma

### What is Prisma?

Prisma is an open-source database toolkit that makes it easy for developers to reason about data and how it relates to their applications.

It is one of the most commonly used ORM's for Python, Typescript and more languages.

It leverages type annotations to generate a schema and then generates a client that can be used to interact with the database. (We'll do this next session!).

### Useful links:

[Prisma Docs (Typescript)](https://www.prisma.io/docs/)
[Prisma client Python](https://prisma-client-py.readthedocs.io/en/stable/)
[Prisma client Rust](https://prisma.brendonovich.dev)

### How to use Prisma

* Make a `/prisma` directory and add a `schema.prisma` file inside of it.
* Take inspiration from the schema in the [`example`](prisma/schema.prisma) file.
* Run the following commands:

  - Install prisma for python
    ```bash
    pip install prisma
    ```
  - Generate the client and the database
    ```bash
    prisma migrate dev --name <name>
    ```
  - Run the example script (or make your own)
    ```bash
    python prisma_example.py
    ```
# Session Two

## Relational Algebra

### Sets
A **set** of elements which share a property
    - Integers: set of integers (0 and its successors)  N
    - Booleans: { true, false }
    - Strings: the set of all combinations of characters of any length
    ...

### Algebraic Types
You can imagine relational algebra as a language for describing sets of tuples.

Tuple: product type
    A tuple is a fixed-length sequence of elements of different types. (Massive simplification)

You may see functions as a way to transform tuples into other tuples.

Ex.
```python
def add(n, m): return n + m
```

The add function can be seen as taking a tuple of two integers and returning a tuple of one integer. 

We will be using this notation:

```(Int, Int) -> Int```

Given two sets, you can generate all possible tuples from them using the *cartesian product*.

In general:
```A x B = { (a, b) | a ∈ A, b ∈ B }```

All possible tuples of two integers:
```Int x Int = { (n, m) | n ∈ Z, m ∈ Z }```


### Relational algebra (simplified)

We can try to define operations in relational algebra as functions that operate on sets and tuples and that describe syntactical concepts.

**π ::= Tuple projection**

We can imagine the π operation as a function that takes a tuple and returns a tuple with a subset of the original elements.

```π (column) (table)``` ::= Give me the column of the table

**σ ::= Selection**

We can imagine the σ operation as a function that takes a tuple and returns a tuple with a subset of the original elements.

```σ (condition) (table)``` ::= Give me the table where the condition is true

**⋈ ::= Relative clause**

We can imagine the ⋈ operation as a function that combines two tuples into a new tuple.

```table1 ⋈ table2``` ::= Give me elements of table1 that are related to elements of table2.


### How to reason about queries

In order to understand a query, you can split it into smaller parts and reason about them. (divide and conquer).

In real life you will be given sentences as such:

*What pizzerias have minors as customers?*

And you should reason about them (using notions from first order logic) and translate them into a query:

*Find all pizzerias frequented by at least one person under the age of 18.*

Now, let's solve the problem.

*Under the age of 18*

σ (age<18) ::= Select such that age is less than 18

*Person under the age of 18*

σ (age<18) (Person) ::= Select people such that their age is less than 18

*frequented by at least one person under the age of 18.*

σ (age<18) (Person) **⋈** (Frequents) ::= Select people such that their age is less than 18 **that** frequent pizzerias (and give me the entire tuple)

π (pizzeria) σ (age<18) (Person) **⋈** (Frequents) ::= Select such that age is less than 18 from table Person **that** frequent pizzerias (and give me the pizzeria's name)


Another example:

*Find all pizzerias that are frequented by only female persons or only male persons.*

σ (gender == Female) ::= Select individual whose gender is female

σ (gender == Male) ::= Select individual whose gender is male

σ (gender == Female) (Person) ::= Select individual whose gender is female from the person table

σ (gender == Male) ::= Select people whose gender is male

π (pizzeria) ( σ (gender == Female) (Person) ⋈ (Frequents)) - π (pizzeria) ( σ (gender == Male) (Person) ⋈ (Frequents)) ::=
Give me all pizzerias who are frequented by females AND NOT pizzerias which are frequented by males (logical language, artificial) OR Give me all pizzerias whose customers are female only (prosaic, natural language)

π (pizzeria) ( σ (gender == Female) (Person) ⋈ (Frequents)) - π (pizzeria) ( σ (gender != Female) (Person) ⋈ (Frequents)) ⋃ π (pizzeria) ( σ (gender == Male) (Person) ⋈ (Frequents)) - π (pizzeria) ( σ (gender != Male) (Person) ⋈ (Frequents)) ::= Find all pizzerias that are frequented by only female persons or only male persons

(Find my solved solutions in the [linked pdf](PizzeriaAlgebra.pdf))

## Data Structures

Complete our dynamic array (Vector) [implementation](ads/self-learning/dynamic_array_datastructures.py).
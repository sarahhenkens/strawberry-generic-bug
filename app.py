import typing
import strawberry
from typing import Generic, TypeVar

T = TypeVar("T")

@strawberry.interface
class Node(Generic[T]):
    id: strawberry.ID

@strawberry.type
class Book(Node[str]):
    pass

@strawberry.type
class Query:
    books: typing.List[Book]

@strawberry.type
class Query:

    @strawberry.field
    def jobs() -> typing.List[Book]:
        return list()

schema = strawberry.Schema(query=Query)

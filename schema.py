import typing
import strawberry

from strawberry_types import Berry, Pokemon
from resolvers import get_berry_by_name, get_pokemon_by_name


@strawberry.type
class Query:
    berry_by_name: typing.Optional[Berry] = strawberry.field(resolver=get_berry_by_name)
    pokemon_by_name: typing.Optional[Pokemon] = strawberry.field(
        resolver=get_pokemon_by_name
    )


schema = strawberry.Schema(query=Query)

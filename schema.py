import strawberry
import typing

from datasource import PokemonDataSource


@strawberry.type
class Berry:
    id: int
    name: str
    growth_time: int
    max_harvest: int
    size: int


def hello() -> str:
    return "Hello! This is the pokeql GraphQL API"


async def get_berry_by_name(name: str) -> typing.Optional[Berry]:
    data = await PokemonDataSource.get("berry", name)
    if not data:
        return None

    return Berry(
        id=data.get('id'),
        name=data.get('name'),
        growth_time=data.get('growth_time'),
        max_harvest=data.get('max_harvest'),
        size=data.get('size')
    )


@strawberry.type
class Query:
    hello: str = strawberry.field(resolver=hello)
    berry_by_name: typing.Optional[Berry] = strawberry.field(resolver=get_berry_by_name)


schema = strawberry.Schema(query=Query)

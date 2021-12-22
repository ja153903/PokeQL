import typing
import strawberry

from datasource import PokemonDataSource


@strawberry.type
class Berry:
    id: strawberry.ID
    name: str
    growth_time: int
    max_harvest: int
    natural_gift_power: int
    smoothness: int
    soil_dryness: int
    size: int


@strawberry.type
class Pokemon:
    id: strawberry.ID
    name: str
    base_experience: int
    height: int
    order: int
    weight: int


async def get_berry_by_name(name: str) -> typing.Optional[Berry]:
    data = await PokemonDataSource.get("berry", name)
    if not data:
        return None

    return Berry(
        id=data.get("id"),
        name=data.get("name"),
        growth_time=data.get("growth_time"),
        max_harvest=data.get("max_harvest"),
        natural_gift_power=data.get("natural_gift_power"),
        smoothness=data.get("smoothness"),
        soil_dryness=data.get("soil_dryness"),
        size=data.get("size"),
    )


async def get_pokemon_by_name(name: str) -> typing.Optional[Pokemon]:
    data = await PokemonDataSource.get("pokemon", name)
    if not data:
        return None

    return Pokemon(
        id=data.get("id"),
        name=data.get("name"),
        base_experience=data.get("base_experience"),
        height=data.get("height"),
        order=data.get("order"),
        weight=data.get("weight"),
    )


@strawberry.type
class Query:
    berry_by_name: typing.Optional[Berry] = strawberry.field(resolver=get_berry_by_name)
    pokemon_by_name: typing.Optional[Pokemon] = strawberry.field(
        resolver=get_pokemon_by_name
    )


schema = strawberry.Schema(query=Query)

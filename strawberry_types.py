import typing
import strawberry


@strawberry.type
class BerryFlavor:
    name: str


@strawberry.type
class BerryFlavorMap:
    potency: int
    flavor: BerryFlavor


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
    flavors: typing.List[BerryFlavorMap]


@strawberry.type
class Ability:
    id: strawberry.ID
    name: str


@strawberry.type
class PokemonAbility:
    is_hidden: bool
    ability: Ability


@strawberry.type
class Pokemon:
    id: strawberry.ID
    name: str
    base_experience: int
    height: int
    order: int
    weight: int
    abilities: typing.List[PokemonAbility]

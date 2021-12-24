import typing

from datasource import PokemonDataSource

from strawberry_types import Berry, BerryFlavor, BerryFlavorMap, Pokemon


def format_berry_flavor(
    flavors: typing.List[typing.Dict[str, typing.Any]]
) -> typing.List[BerryFlavorMap]:
    """
    format_berry_flavor formats the list of flavors that get from the PokeAPI
    when we query for berries.

    :param flavors: a list of dictionaries containing data about the berry flavor
    :return: A list of BerryFlavorMap objects
    """
    result = []

    for flavor_dict in flavors:
        potency = flavor_dict.get("potency")
        berry_flavor_dict = flavor_dict.get("flavor")
        berry_flavor_name = berry_flavor_dict.get("name")

        berry_flavor = BerryFlavor(name=berry_flavor_name)
        berry_flavor_map = BerryFlavorMap(potency=potency, flavor=berry_flavor)

        result.append(berry_flavor_map)

    return result


async def get_berry_by_name(name: str) -> typing.Optional[Berry]:
    """
    get_berry_by_name creates a Berry object for querying based on
    the berry's name.

    :param name: a string denoting the name of a berry
    :return: None | a Berry object
    """
    data = await PokemonDataSource.get("berry", name)
    if not data:
        return None

    flavors = format_berry_flavor(data.get("flavors", []))

    return Berry(
        id=data.get("id"),
        name=data.get("name"),
        growth_time=data.get("growth_time"),
        max_harvest=data.get("max_harvest"),
        natural_gift_power=data.get("natural_gift_power"),
        smoothness=data.get("smoothness"),
        soil_dryness=data.get("soil_dryness"),
        size=data.get("size"),
        flavors=flavors,
    )


async def get_pokemon_by_name(name: str) -> typing.Optional[Pokemon]:
    """
    get_pokemon_by_name creates a Pokemon object for querying based on
    the pokemon's name

    :param name: a string denoting the name of a pokemon
    :return: None | a Pokemon object
    """
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

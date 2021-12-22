from __future__ import annotations

import requests

from constants import POKEAPI_ENDPOINT


class PokemonDataSource:
    @staticmethod
    async def get(category: str, name_or_id: int | str):
        resp = requests.get(f'{POKEAPI_ENDPOINT}/{category}/{name_or_id}')
        return resp.json()

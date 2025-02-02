"""
MIT License

Copyright (c) 2025-present PaxxPatriot

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import logging
from typing import List

from .game import Game
from .http import HTTPClient
from .match import Match
from .organizer import Organizer
from .player import Player

__all__ = ("Client",)


_log = logging.getLogger(__name__)


class Client:
    def __init__(self, debug: bool = False):
        self.http: HTTPClient = HTTPClient()

    def set_api_key(self, *, api_key: str):
        self.http.set_api_key(api_key)

    async def close(self) -> None:
        """*coroutine*
        Closes the `aiohttp.ClientSession`.
        """
        await self.http.close()

    async def get_games(self, *, offset: int = 0, limit: int = 20) -> List[Game]:
        """*coroutine*
        Return a list of all available games.

        Parameters
        ----------
        offset: :class:`int`
            The starting item position. Defaults to 0.
        limit: :class:`int`
            The number of items to return. Defaults to 20.

        Returns
        -------
        List[:class:`Game`]
        """
        params = {
            "offset": offset, 
            "limit": limit
        }
        data = await self.http.get_games(params=params)
        return [Game(data=game_data) for game_data in data["items"]]

    async def get_player_by_nickname(self, nickname: str) -> Player:
        """*coroutine*
        Return a player.

        Parameters
        ----------
        nickname: :class:`str`
            The nickname of the player.

        Returns
        -------
        :class:`Player`
        """
        params = {
            "nickname": nickname,
        }
        data = await self.http.get_players(params=params)
        return Player(data=data)
    
    async def get_player_by_game_and_game_player_id(self, game: str, game_player_id: str) -> Player:
        """*coroutine*
        Return a player.

        Parameters
        ----------
        game: :class:`str`
            The game of the corresponding player ID.
        game_player_id: :class:`str`
            The ID for the player, e.g. SteamID64 for Valve games like Team Fortress 2 or Counter-Strike 2.

        Returns
        -------
        :class:`Player`
        """
        params = {
            "game": game,
            "game_player_id": game_player_id,
        }
        data = await self.http.get_players(params=params)
        return Player(data=data)

    async def get_player_by_id(self, player_id: str) -> Player:
        """*coroutine*
        Return a specific player.

        Parameters
        ----------
        player_id: :class:`str`
            The ID of the player.

        Returns
        -------
        :class:`Player`
        """
        data = await self.http.get_player(player_id=player_id)
        return Player(data=data)

    async def get_organizer_by_name(self, name: str) -> Organizer:
        """*coroutine*
        Return an organization by their name.

        Parameters
        ----------
        name: :class:`str`
            The name of the organization.

        Returns
        -------
        :class:`Organizer`
        """
        params = {
            "name": name,
        }
        data = await self.http.get_organizer_by_name(params=params)
        return Organizer(data=data)

    async def get_match(self, match_id: str) -> Match:
        """*coroutine*
        Return a specific match.

        Parameters
        ----------
        match_id: :class:`str`
            The ID of the match.

        Returns
        -------
        :class:`Match`
        """
        data = await self.http.get_match(match_id)
        return Match(data=data)

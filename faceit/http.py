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

import asyncio
import json
import logging
import ssl
import sys
from typing import Any, Dict, Iterable, List, Optional, Union

import aiohttp

from faceit import __version__

from .errors import Forbidden, HTTPException, NotFound, ServiceUnavailable, Unauthorized

_log = logging.getLogger(__name__)


async def json_or_text(response: aiohttp.ClientResponse) -> Union[Dict[str, Any], str]:
    text = await response.text(encoding="utf-8")
    try:
        if "application/json" in response.headers["content-type"]:
            return json.loads(text)
    except KeyError:
        pass

    return text


class Route:
    BASE = "https://open.faceit.com/data/v4"

    def __init__(self, method: str, path: str) -> None:
        self.path: str = path
        self.method: str = method
        self.url: str = self.BASE + self.path


class HTTPClient:
    def __init__(
        self,
        *,
        proxy: Optional[str] = None,
        proxy_auth: Optional[aiohttp.BasicAuth] = None,
    ) -> None:
        # Checks if the faceit.Client was initialized before or after the event loop started
        # If it was not initialized, you have to call start_session()
        try:
            asyncio.get_running_loop()
            self.__session = aiohttp.ClientSession()
        except RuntimeError:
            self.__session = None
        self.auth = None
        self.proxy: Optional[str] = proxy
        self.proxy_auth: Optional[aiohttp.BasicAuth] = proxy_auth
        self.ratelimit_lock: asyncio.Lock = asyncio.Lock()

        user_agent = "faceit.py {0}) Python/{1[0]}.{1[1]} aiohttp/{2}"
        self.user_agent: str = user_agent.format(__version__, sys.version_info, str(aiohttp.__version__))  #

    def set_api_key(self, api_key: str) -> None:
        self.api_key = f"Bearer {api_key}"

    async def close(self) -> None:
        if self.__session:
            await self.__session.close()

    async def start_session(self):
        self.__session = aiohttp.ClientSession()

    async def request(
        self,
        route: Route,
        params: Optional[Iterable[Dict[str, Any]]] = None,
        **kwargs: Any,
    ) -> Any:
        method = route.method
        url = route.url

        # header creation
        headers: Dict[str, str] = {
            "Accept": "application/json",
            "User-Agent": self.user_agent,
        }

        if self.api_key is not None:
            headers["Authorization"] = self.api_key

        kwargs["headers"] = headers

        if params:
            kwargs["params"] = params

        async with self.ratelimit_lock:
            for _ in range(2):
                async with self.__session.request(method, url, auth=self.auth, **kwargs) as response:
                    _log.debug(f"{method} {url} with {params} has returned {response.status}")

                    data = await json_or_text(response)

                    if 300 > response.status >= 200:
                        _log.debug(f"{method} {url} has received {data}")
                        return data

                    if response.status in {500, 503}:
                        raise ServiceUnavailable(response, data)

                    if response.status == 401:
                        raise Unauthorized(response, data)
                    if response.status == 403:
                        raise Forbidden(response, data)
                    if response.status == 404:
                        raise NotFound(response, data)
                    if response.status == 429:
                        # We are getting rate-limited, read retry-after header and try again
                        retry_after = int(headers.get("Retry-After", 60))
                        _log.debug(f"{method} {url} is getting rate-limited, retry after {retry_after} seconds")
                        await asyncio.sleep(retry_after)
                        continue
                    raise HTTPException(response, data)

    # Championships

    # Games
    async def get_games(self, **parameters: Dict[str, Any]) -> List[Dict[str, Any]]:
        return await self.request(Route("GET", "/games"), **parameters)

    async def get_game_matchmakings(self, game_id: str, **parameters: Dict[str, Any]) -> List[Dict[str, Any]]:
        return await self.request(Route("GET", f"/games/{game_id}/matchmakings"), **parameters)

    async def get_game_details(self, game_id: str, **parameters: Dict[str, Any]) -> List[Dict[str, Any]]:
        return await self.request(Route("GET", f"/games/{game_id}"), **parameters)

    async def get_game_parent(self, game_id: str, **parameters: Dict[str, Any]) -> List[Dict[str, Any]]:
        return await self.request(Route("GET", f"/games/{game_id}/parent"), **parameters)

    async def get_game_queues(self, game_id: str, **parameters: Dict[str, Any]) -> List[Dict[str, Any]]:
        return await self.request(Route("GET", f"/games/{game_id}/queues"), **parameters)

    async def get_game_queue_details(
        self, game_id: str, queue_id: str, **parameters: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        return await self.request(Route("GET", f"/games/{game_id}/queues/{queue_id}"), **parameters)

    async def get_game_queue_bans(self, game_id: str, queue_id: str, **parameters: Dict[str, Any]) -> List[Dict[str, Any]]:
        return await self.request(Route("GET", f"/games/{game_id}/queues/{queue_id}/bans"), **parameters)

    async def get_game_queue_by_region(
        self, game_id: str, region_id: str, **parameters: Dict[str, Any]
    ) -> List[Dict[str, Any]]:
        return await self.request(Route("GET", f"/games/{game_id}/regions/{region_id}/queues"), **parameters)

    # Hubs
    # Leaderboards
    # Leagues

    # Matches
    async def get_match(self, match_id: str) -> Dict[str, Any]:
        return await self.request(Route("GET", f"/matches/{match_id}"))

    async def get_match_stats(self, match_id: str) -> Dict[str, Any]:
        return await self.request(Route("GET", f"/matches/{match_id}/stats"))

    # Matchmakings
    async def get_matchmaking(self, matchmaking_id: str) -> Dict[str, Any]:
        return await self.request(Route("GET", f"/matchmakings/{matchmaking_id}"))

    # Organizers
    async def get_organizer_by_name(self, **parameters: Dict[str, Any]) -> Dict[str, Any]:
        return await self.request(Route("GET", "/organizers"), **parameters)

    async def get_organizer_by_id(self, organizer_id: str) -> Dict[str, Any]:
        return await self.request(Route("GET", f"/organizers/{organizer_id}"))

    # Players
    async def get_players(self, **parameters: Dict[str, Any]) -> List[Dict[str, Any]]:
        return await self.request(Route("GET", "/players"), **parameters)

    async def get_player(self, player_id: str) -> Dict[str, Any]:
        return await self.request(Route("GET", f"/players/{player_id}"))

    # Rankings
    # Search
    # Teams
    # Tournaments

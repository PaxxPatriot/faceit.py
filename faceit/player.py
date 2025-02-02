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

from typing import Dict, Any, List

__all__ = (
    "PlayerGame",
    "Player",
)

class PlayerGame:
    __slots__ = (
        "_region",
        "_game_player_id",
        "_skill_level",
        "_faceit_elo",
        "_game_player_name",
        "_skill_level_label",
        "_regions",
        "_game_profile_id",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._region = data.get("region")
        self._game_player_id = data.get("game_player_id")
        self._skill_level = data.get("skill_level")
        self._faceit_elo = data.get("faceit_elo")
        self._game_player_name = data.get("game_player_name")
        self._skill_level_label = data.get("skill_level_label")
        self._regions = data.get("regions")
        self._game_profile_id = data.get("game_profile_id")

    def __repr__(self) -> str:
         return f"PlayerGame(data={{'region': '{self._region}', 'game_player_id': '{self._game_player_id}', 'skill_level': {self._skill_level}, 'faceit_elo': {self._faceit_elo}, 'game_player_name': '{self._game_player_name}', 'skill_level_label': '{self._skill_level_label}', 'regions': {self._regions}, 'game_profile_id': '{self._game_profile_id}'}})"

    @property
    def region(self) -> str:
        return self._region

    @property
    def game_player_id(self) -> str:
        return self._game_player_id

    @property
    def skill_level(self) -> int:
        return self._skill_level

    @property
    def faceit_elo(self) -> int:
        return self._faceit_elo

    @property
    def game_player_name(self) -> str:
        return self._game_player_name

    @property
    def skill_level_label(self) -> str:
        return self._skill_level_label

    @property
    def regions(self) -> Dict[str, Any]:
        return self._regions

    @property
    def game_profile_id(self) -> str:
        return self._game_profile_id

class Player:
    __slots__ = (
        "_player_id",
        "_nickname",
        "_avatar",
        "_country",
        "_cover_image",
        "_platforms",
        "_games",
        "_settings",
        "_friends_ids",
        "_new_steam_id",
        "_steam_id_64",
        "_steam_nickname",
        "_memberships",
        "_faceit_url",
        "_membership_type",
        "_cover_featured_image",
        "_infractions",
        "_verified",
        "_activated_at",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._player_id = data.get("player_id")
        self._nickname = data.get("nickname")
        self._avatar = data.get("avatar")
        self._country = data.get("country")
        self._cover_image = data.get("cover_image")
        self._platforms = data.get("platforms")
        self._games = data.get("games")
        self._settings = data.get("settings")
        self._friends_ids = data.get("friends_ids")
        self._new_steam_id = data.get("new_steam_id")
        self._steam_id_64 = data.get("steam_id_64")
        self._steam_nickname = data.get("steam_nickname")
        self._memberships = data.get("memberships")
        self._faceit_url = data.get("faceit_url")
        self._membership_type = data.get("membership_type")
        self._cover_featured_image = data.get("cover_featured_image")
        self._infractions = data.get("infractions")
        self._verified = data.get("verified", False)
        self._activated_at = data.get("activated_at")

    def __repr__(self) -> str:
        return f"Player(data={{'player_id': '{self._player_id}', 'nickname': '{self._nickname}', 'avatar': '{self._avatar}', 'country': '{self._country}', 'cover_image': '{self._cover_image}', 'platforms': {self._platforms}, 'games': {self._games}, 'settings': {self._settings}, 'friends_ids': {self._friends_ids}, 'new_steam_id': '{self._new_steam_id}', 'steam_id_64': '{self._steam_id_64}', 'steam_nickname': '{self._steam_nickname}', 'memberships': {self._memberships}, 'faceit_url': '{self._faceit_url}', 'membership_type': '{self._membership_type}', 'cover_featured_image': '{self._cover_featured_image}', 'infractions': {self._infractions}, 'verified': {self._verified}, 'activated_at': '{self._activated_at}'}})"

    @property
    def player_id(self) -> str:
        return self._player_id

    @property
    def nickname(self) -> str:
        return self._nickname

    @property
    def avatar(self) -> str:
        return self._avatar

    @property
    def country(self) -> str:
        return self._country

    @property
    def cover_image(self) -> str:
        return self._cover_image

    @property
    def platforms(self) -> Dict[str, str]:
        return self._platforms

    @property
    def games(self) -> Dict[str, PlayerGame]:
        return {key: PlayerGame(data=self._games[key]) for key in self._games.keys()}

    @property
    def settings(self) -> Dict[str, str]:
        return self._settings

    @property
    def friends_ids(self) -> List[str]:
        return self._friends_ids

    @property
    def new_steam_id(self) -> str:
        return self._new_steam_id

    @property
    def steam_id_64(self) -> str:
        return self._steam_id_64

    @property
    def steam_nickname(self) -> str:
        return self._steam_nickname

    @property
    def memberships(self) -> List[str]:
        return self._memberships

    @property
    def faceit_url(self) -> str:
        return self._faceit_url

    @property
    def membership_type(self) -> str:
        return self._membership_type

    @property
    def cover_featured_image(self) -> str:
        return self._cover_featured_image

    @property
    def infractions(self) -> Dict[str, str]:
        return self._infractions

    @property
    def verified(self) -> bool:
        return self._verified

    @property
    def activated_at(self) -> str:
        return self._activated_at

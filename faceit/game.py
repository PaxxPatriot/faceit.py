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

from typing import Any, Dict, List

__all__ = (
    "GameAssets",
    "Game",
)


class GameAssets:

    __slots__ = (
        "_cover",
        "_featured_img_l",
        "_featured_img_m",
        "_featured_img_s",
        "_flag_img_icon",
        "_flag_img_l",
        "_flag_img_m",
        "_flag_img_s",
        "_landing_page",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._cover = data.get("cover")
        self._featured_img_l = data.get("cover")
        self._featured_img_m = data.get("featured_img_l")
        self._featured_img_s = data.get("featured_img_s")
        self._flag_img_icon = data.get("flag_img_icon")
        self._flag_img_l = data.get("flag_img_l")
        self._flag_img_m = data.get("flag_img_m")
        self._flag_img_s = data.get("flag_img_s")
        self._landing_page = data.get("landing_page")

    def __repr__(self) -> str:
        return f"GameAssets(data={{'cover': '{self._cover}', 'featured_img_l': '{self._featured_img_l}', '_featured_img_m': '{self._featured_img_m}', 'featured_img_s': '{self._featured_img_s}', 'flag_img_icon': '{self._flag_img_icon}', 'flag_img_l': '{self._flag_img_l}', 'flag_img_m': '{self._flag_img_m}', 'flag_img_s': '{self._flag_img_s}', 'landing_page': '{self._landing_page}'}})"

    @property
    def cover(self) -> str:
        return self._cover

    @property
    def featured_img_l(self) -> str:
        return self._featured_img_l

    @property
    def featured_img_m(self) -> str:
        return self._featured_img_m

    @property
    def featured_img_s(self) -> str:
        return self._featured_img_s

    @property
    def flag_img_icon(self) -> str:
        return self._flag_img_icon

    @property
    def flag_img_l(self) -> str:
        return self._flag_img_l

    @property
    def flag_img_m(self) -> str:
        return self._flag_img_m

    @property
    def flag_img_s(self) -> str:
        return self._flag_img_s

    @property
    def landing_page(self) -> str:
        return self._landing_page


class Game:
    """Represents a game."""

    __slots__ = (
        "_assets",
        "_game_id",
        "_long_label",
        "_order",
        "_parent_game_id",
        "_platforms",
        "_regions",
        "_short_label",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._assets = data.get("assets")
        self._game_id = data.get("game_id")
        self._long_label = data.get("long_label")
        self._order = data.get("order")
        self._parent_game_id = data.get("parent_game_id")
        self._platforms = data.get("platforms")
        self._regions = data.get("regions")
        self._short_label = data.get("short_label")

    def __repr__(self) -> str:
        return f"Game(data={{'assets': {self._assets}, 'game_id': '{self._game_id}', 'long_label': '{self._long_label}', 'order': {self._order}, 'parent_game_id': '{self._parent_game_id}', 'platforms': {self._platforms}, 'regions': {self._regions}, 'short_label': '{self._short_label}'}})"

    @property
    def assets(self) -> GameAssets:
        return GameAssets(data=self._assets)

    @property
    def game_id(self) -> str:
        return self._game_id

    @property
    def long_label(self) -> str:
        return self._long_label

    @property
    def order(self) -> int:
        return self._order

    @property
    def parent_game_id(self) -> str:
        return self._parent_game_id

    @property
    def platforms(self) -> List[str]:
        return self._platforms

    @property
    def regions(self) -> List[str]:
        return self._regions

    @property
    def short_label(self) -> str:
        return self._short_label

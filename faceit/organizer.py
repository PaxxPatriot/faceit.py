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

from typing import Any, Dict

__all__ = ("Organizer",)


class Organizer:
    """Represents an organizer."""

    __slots__ = (
        "_avatar",
        "_cover",
        "_description",
        "_facebook",
        "_faceit_url",
        "_followers_count",
        "_name",
        "_organizer_id",
        "_twitch",
        "_twitter",
        "_type",
        "_vk",
        "_website",
        "_youtube",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._avatar = data.get("avatar")
        self._cover = data.get("cover")
        self._description = data.get("description")
        self._facebook = data.get("facebook")
        self._faceit_url = data.get("faceit_url")
        self._followers_count = data.get("followers_count")
        self._name = data.get("name")
        self._organizer_id = data.get("organizer_id")
        self._twitch = data.get("twitch")
        self._twitter = data.get("twitter")
        self._type = data.get("type")
        self._vk = data.get("vk")
        self._website = data.get("website")
        self._youtube = data.get("youtube")

    def __repr__(self) -> str:
        return f"Organizer(data={{'avatar': '{self._avatar}', 'cover': '{self._cover}', 'description': '{self._description}', 'facebook': '{self._facebook}', 'faceit_url': '{self._faceit_url}', 'followers_count': {self._followers_count}, 'name': '{self._name}', 'organizer_id': '{self._organizer_id}', 'twitch': '{self._twitch}', 'twitter': '{self._twitter}', 'type': '{self._type}', 'vk': '{self._vk}', 'website': '{self._website}', 'youtube': '{self._youtube}'}})"

    @property
    def avatar(self) -> str:
        return self._avatar

    @property
    def cover(self) -> str:
        return self._cover

    @property
    def description(self) -> str:
        return self._description

    @property
    def facebook(self) -> str:
        return self._facebook

    @property
    def faceit_url(self) -> str:
        return self._faceit_url

    @property
    def followers_count(self) -> int:
        return self._followers_count

    @property
    def name(self) -> str:
        return self._name

    @property
    def organizer_id(self) -> str:
        return self._organizer_id

    @property
    def twitch(self) -> str:
        return self._twitch

    @property
    def twitter(self) -> str:
        return self._twitter

    @property
    def type(self) -> str:
        return self._type

    @property
    def vk(self) -> str:
        return self._vk

    @property
    def website(self) -> str:
        return self._website

    @property
    def youtube(self) -> str:
        return self._youtube

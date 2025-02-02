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

import datetime
from typing import Any, Dict, List, Optional

__all__ = (
    "DetailedMatchResult",
    "MatchResult",
    "SkillLevelRange",
    "SkillLevel",
    "Stats",
    "Roster",
    "Faction",
    "VotingEntity",
    "VotingPick",
    "Voting",
    "Match",
)


class DetailedMatchResult:
    __slots__ = (
        "_asc_score",
        "_winner",
        "_factions",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._asc_score = data.get("asc_score")
        self._winner = data.get("winner")
        self._factions = data.get("factions")

    def __repr__(self) -> str:
        return f"DetailedMatchResult(data={{'asc_score': {self._asc_score}, 'winner': '{self._winner}', 'factions': {self._factions}}})"

    @property
    def asc_score(self) -> bool:
        return self._asc_score

    @property
    def winner(self) -> Dict[str, int]:
        return self._winner

    @property
    def factions(self) -> Dict[str, Dict[str, int]]:
        return self._factions


class MatchResult:
    __slots__ = (
        "_winner",
        "_score",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._winner = data.get("winner")
        self._score = data.get("score")

    def __repr__(self) -> str:
        return f"MatchResult(data={{'winner': '{self._winner}', 'score': {self._score}}})"

    @property
    def winner(self) -> str:
        return self._winner

    @property
    def score(self) -> Dict[str, int]:
        return self._score


class SkillLevelRange:
    __slots__ = (
        "_min",
        "_max",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._min = data.get("min")
        self._max = data.get("max")

    def __repr__(self) -> str:
        return f"SkillLevelRange(data={{'min': {self._min}, 'max': {self._max}}})"

    @property
    def min(self) -> int:
        return self._min

    @property
    def max(self) -> int:
        return self._max


class SkillLevel:
    __slots__ = (
        "_average",
        "_range",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._average = data.get("average")
        self._range = data.get("range")

    def __repr__(self) -> str:
        return f"SkillLevel(data={{'average': {self._average}, 'range': {self._range}}})"

    @property
    def average(self) -> int:
        return self._average

    @property
    def range(self) -> SkillLevelRange:
        return SkillLevelRange(data=self._range)


class Stats:
    __slots__ = (
        "_rating",
        "_skill_level",
        "_win_probability",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._rating = data.get("rating")
        self._skill_level = data.get("skillLevel")
        self._win_probability = data.get("winProbability")

    def __repr__(self) -> str:
        return f"Stats(data={{'rating': {self._rating}, 'skillLevel': {self._skill_level}, 'winProbability': {self._win_probability}}})"

    @property
    def rating(self) -> int:
        return self._rating

    @property
    def skill_level(self) -> SkillLevel:
        return SkillLevel(data=self._skill_level)

    @property
    def win_probability(self) -> float:
        return self._win_probability


class Roster:
    __slots__ = (
        "_anticheat_required",
        "_avatar",
        "_game_player_id",
        "_game_player_name",
        "_game_skill_level",
        "_membership",
        "_nickname",
        "_player_id",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._anticheat_required = data.get("anticheat_required")
        self._avatar = data.get("avatar")
        self._game_player_id = data.get("game_player_id")
        self._game_player_name = data.get("game_player_name")
        self._game_skill_level = data.get("game_skill_level")
        self._membership = data.get("membership")
        self._nickname = data.get("nickname")
        self._player_id = data.get("player_id")

    def __repr__(self) -> str:
        return f"Roster(data={{'anticheat_required': {self._anticheat_required}, 'avatar': '{self._avatar}', 'game_player_id': '{self._game_player_id}', 'game_player_name': '{self._game_player_name}', 'game_skill_level': '{self._game_skill_level}', 'membership': '{self._membership}', 'nickname': '{self._nickname}', 'player_id': '{self._player_id}'}})"

    @property
    def anticheat_required(self) -> bool:
        return self._anticheat_required

    @property
    def avatar(self) -> str:
        return self._avatar

    @property
    def game_player_id(self) -> str:
        return self._game_player_id

    @property
    def game_player_name(self) -> str:
        return self._game_player_name

    @property
    def game_skill_level(self) -> int:
        return self._game_skill_level

    @property
    def membership(self) -> str:
        return self._membership

    @property
    def nickname(self) -> str:
        return self._nickname

    @property
    def player_id(self) -> str:
        return self._player_id


class Faction:
    __slots__ = (
        "_avatar",
        "_faction_id",
        "_leader",
        "_name",
        "_roster",
        "_stats",
        "_substituted",
        "_type",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._avatar = data.get("avatar")
        self._faction_id = data.get("faction_id")
        self._leader = data.get("leader")
        self._name = data.get("name")
        self._roster = data.get("roster")
        self._stats = data.get("stats")
        self._substituted = data.get("substituted")
        self._type = data.get("type")

    def __repr__(self) -> str:
        return f"Faction(data={{'avatar': '{self._avatar}', 'faction_id': '{self._faction_id}', 'leader': '{self._leader}', 'name': '{self._name}', 'roster': {self._roster}, 'stats': {self._stats}, 'substituted': {self._substituted}, 'type': '{self._type}'}})"

    @property
    def avatar(self) -> str:
        return self._avatar

    @property
    def faction_id(self) -> str:
        return self._faction_id

    @property
    def leader(self) -> str:
        return self._leader

    @property
    def name(self) -> str:
        return self._name

    @property
    def roster(self) -> List[Roster]:
        return [Roster(data=roster_data) for roster_data in self._roster]

    @property
    def stats(self) -> Optional[Stats]:
        return Stats(data=self._stats) if self._stats is not None else None

    @property
    def substituted(self) -> bool:
        return self._substituted

    @property
    def type(self) -> str:
        return self._type


class VotingEntity:
    __slots__ = (
        "_class_name",
        "_game_map_id",
        "_guid",
        "_image_lg",
        "_image_sm",
        "_name",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._class_name = data.get("class_name")
        self._game_map_id = data.get("game_map_id")
        self._guid = data.get("guid")
        self._image_lg = data.get("image_lg")
        self._image_sm = data.get("image_sm")
        self._name = data.get("name")

    def __repr__(self) -> str:
        return f"VotingEntity(data={{'class_name': '{self._class_name}', 'game_map_id': '{self._game_map_id}', 'guid': '{self._guid}', 'image_lg': '{self._image_lg}', 'image_sm': '{self._image_sm}', 'name': '{self._name}'}})"

    @property
    def class_name(self) -> str:
        return self._class_name

    @property
    def game_map_id(self) -> str:
        return self._game_map_id

    @property
    def guid(self) -> str:
        return self._guid

    @property
    def image_lg(self) -> str:
        return self._image_lg

    @property
    def image_sm(self) -> str:
        return self._image_sm

    @property
    def name(self) -> str:
        return self._name


class VotingPick:
    __slots__ = (
        "_entities",
        "_pick",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._entities = data.get("entities")
        self._pick = data.get("pick")

    def __repr__(self) -> str:
        return f"VotingPick(data={{'entities': {self._entities}, 'pick': {self._pick}}})"

    @property
    def entities(self) -> List[VotingEntity]:
        return [VotingEntity(data=entity_data) for entity_data in self._entities]

    @property
    def pick(self) -> List[str]:
        return self._pick


class Voting:
    __slots__ = (
        "_voted_entity_types",
        "_location",
        "_map",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._voted_entity_types = data.get("voted_entity_types")
        self._location = data.get("location")
        self._map = data.get("map")

    def __repr__(self) -> str:
        return f"Voting(data={{'voted_entity_types': {self._voted_entity_types}, 'location': {self._location}, 'map': {self._map}}})"

    @property
    def voted_entity_types(self) -> List[str]:
        return self._voted_entity_types

    @property
    def location(self) -> VotingPick:
        return VotingPick(data=self._location)

    @property
    def map(self) -> VotingPick:
        return VotingPick(data=self._map)


class Match:
    __slots__ = (
        "_best_of",
        "_broadcast_start_time",
        "_broadcast_start_time_label",
        "_calculate_elo",
        "_chat_room_id",
        "_competition_id",
        "_competition_name",
        "_competition_type",
        "_configured_at",
        "_demo_url",
        "_detailed_results",
        "_faceit_url",
        "_finished_at",
        "_game",
        "_group",
        "_match_id",
        "_organizer_id",
        "_region",
        "_results",
        "_round",
        "_scheduled_at",
        "_started_at",
        "_status",
        "_teams",
        "_version",
        "_voting",
    )

    def __init__(self, *, data: Dict[str, Any]) -> None:
        self._best_of = data.get("best_of")
        self._broadcast_start_time = data.get("broadcast_start_time")
        self._broadcast_start_time_label = data.get("broadcast_start_time_label")
        self._calculate_elo = data.get("calculate_elo")
        self._chat_room_id = data.get("chat_room_id")
        self._competition_id = data.get("competition_id")
        self._competition_name = data.get("competition_name")
        self._competition_type = data.get("competition_type")
        self._configured_at = data.get("configured_at")
        self._demo_url = data.get("demo_url")
        self._detailed_results = data.get("detailed_results")
        self._faceit_url = data.get("faceit_url")
        self._finished_at = data.get("finished_at")
        self._game = data.get("game")
        self._group = data.get("group")
        self._match_id = data.get("match_id")
        self._organizer_id = data.get("organizer_id")
        self._region = data.get("region")
        self._results = data.get("results")
        self._round = data.get("round")
        self._scheduled_at = data.get("scheduled_at")
        self._started_at = data.get("started_at")
        self._status = data.get("status")
        self._teams = data.get("teams")
        self._version = data.get("version")
        self._voting = data.get("voting")

    def __repr__(self) -> str:
        return f"Match(data={{'best_of': {self._best_of}, 'broadcast_start_time': {self._broadcast_start_time}, 'broadcast_start_time_label': {self._broadcast_start_time_label}, 'calculate_elo': {self._calculate_elo}, 'chat_room_id': '{self._chat_room_id}', 'competition_id': '{self._competition_id}', 'competition_name': '{self._competition_name}', 'competition_type': '{self._competition_type}', 'configured_at': {self._configured_at}, 'demo_url': {self._demo_url}, 'detailed_results': {self._detailed_results}, 'faceit_url': '{self._faceit_url}', 'finished_at': {self._finished_at}, 'game': '{self._game}', 'group': {self._group}, 'match_id': '{self._match_id}', 'organizer_id': '{self._organizer_id}', 'region': '{self._region}', 'results': {self._results}, 'round': {self._round}, 'scheduled_at': {self._scheduled_at}, 'started_at': {self._started_at}, 'status': '{self._status}', 'teams': {self._teams}, 'version': {self._version}, 'voting': {self._voting}}})"

    @property
    def best_of(self) -> int:
        return self._best_of

    @property
    def broadcast_start_time(self) -> Optional[int]:
        return self._broadcast_start_time

    @property
    def broadcast_start_time_label(self) -> Optional[str]:
        return self._broadcast_start_time_label

    @property
    def calculate_elo(self) -> bool:
        return self._calculate_elo

    @property
    def chat_room_id(self) -> str:
        return self._chat_room_id

    @property
    def competition_id(self) -> str:
        return self._competition_id

    @property
    def competition_name(self) -> str:
        return self._competition_name

    @property
    def competition_type(self) -> str:
        return self._competition_type

    @property
    def configured_at(self) -> datetime.datetime:
        return datetime.datetime.fromtimestamp(self._configured_at)

    @property
    def demo_url(self) -> List[str]:
        return self._demo_url

    @property
    def detailed_results(self) -> List[DetailedMatchResult]:
        return [DetailedMatchResult(data=detailed_results_data) for detailed_results_data in self._detailed_results]

    @property
    def faceit_url(self) -> str:
        return self._faceit_url

    @property
    def finished_at(self) -> Optional[datetime.datetime]:
        return datetime.datetime.fromtimestamp(self._finished_at) if self._finished_at is not None else None

    @property
    def game(self) -> str:
        return self._game

    @property
    def group(self) -> Optional[int]:
        return self._group

    @property
    def match_id(self) -> str:
        return self._match_id

    @property
    def organizer_id(self) -> str:
        return self._organizer_id

    @property
    def region(self) -> str:
        return self._region

    @property
    def results(self) -> Optional[MatchResult]:
        return MatchResult(data=self._results) if self._results is not None else None

    @property
    def round(self) -> Optional[int]:
        return self._round

    @property
    def scheduled_at(self) -> Optional[datetime.datetime]:
        return datetime.datetime.fromtimestamp(self._scheduled_at) if self._scheduled_at is not None else None

    @property
    def started_at(self) -> Optional[datetime.datetime]:
        return datetime.datetime.fromtimestamp(self._started_at) if self._started_at is not None else None

    @property
    def status(self) -> str:
        return self._status

    @property
    def teams(self) -> Dict[str, Faction]:
        return {key: Faction(data=self._teams[key]) for key in self._teams.keys()}

    @property
    def version(self) -> int:
        return self._version

    @property
    def voting(self) -> Voting:
        return Voting(data=self._voting)

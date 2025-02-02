"""
Faceit API Wrapper
~~~~~~~~~~~~~~~~~~~
A basic wrapper for the Faceit API.
:copyright: (c) 2025-present PaxxPatriot
:license: MIT, see LICENSE for more details.
"""

__title__ = "faceit"
__author__ = "PaxxPatriot"
__license__ = "MIT"
__copyright__ = "Copyright 2025 PaxxPatriot"
__version__ = "0.0.1"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import logging
from typing import NamedTuple

from .client import *
from .errors import *
from .game import *
from .match import *
from .organizer import *
from .player import *


class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: str
    serial: int


version_info: VersionInfo = VersionInfo(major=0, minor=0, micro=1, releaselevel="alpha", serial=0)

logging.getLogger(__name__).addHandler(logging.NullHandler())

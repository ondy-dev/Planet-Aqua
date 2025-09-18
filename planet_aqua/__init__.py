"""
Planet Aqua - Stop the Trash Tide

A simulation game about ocean plastic pollution and sustainable fishing.
The player acts as "The Important Decision Maker" on a mostly-water planet,
making choices that affect pollution, fish health, and the economy over 150 years.
"""

__version__ = "1.0.0"
__author__ = "Planet Aqua Team"

from .models import GameState, Event, Action
from .engine import PlanetAquaGame

__all__ = ["GameState", "Event", "Action", "PlanetAquaGame"]

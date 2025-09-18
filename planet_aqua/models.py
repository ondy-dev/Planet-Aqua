"""
Data models for Planet Aqua game.
"""

from dataclasses import dataclass
from typing import Dict, Any


@dataclass
class GameState:
    """Core game state tracking all statistics."""
    year: int = 0
    money: int = 100
    ocean_toxicity: int = 10
    fish_health: int = 80
    public_support: int = 60
    pollution_growth_modifier: float = 0.0
    yearly_income: int = 20          # Passive yearly income
    last_action: str = ""            # Track the last action taken
    used_actions: set = None         # Track which actions have been used
    last_event: str = ""             # Track the last event that occurred
    last_event_choice: str = ""      # Track the choice made for the last event
    last_action_consequences: dict = None  # Track detailed consequences of last action
    
    def __post_init__(self):
        if self.used_actions is None:
            self.used_actions = set()
        if self.last_action_consequences is None:
            self.last_action_consequences = {}
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert game state to dictionary for serialization."""
        return {
            "year": self.year,
            "money": self.money,
            "ocean_toxicity": self.ocean_toxicity,
            "fish_health": self.fish_health,
            "public_support": self.public_support,
            "pollution_growth_modifier": self.pollution_growth_modifier,
            "yearly_income": self.yearly_income,
            "last_action": self.last_action,
            "used_actions": list(self.used_actions),
            "last_event": self.last_event,
            "last_event_choice": self.last_event_choice,
            "last_action_consequences": self.last_action_consequences
        }
    
    def from_dict(self, data: Dict[str, Any]) -> None:
        """Load game state from dictionary."""
        self.year = data.get("year", 0)
        self.money = data.get("money", 100)
        self.ocean_toxicity = data.get("ocean_toxicity", 10)
        self.fish_health = data.get("fish_health", 80)
        self.public_support = data.get("public_support", 60)
        self.pollution_growth_modifier = data.get("pollution_growth_modifier", 0.0)
        self.yearly_income = data.get("yearly_income", 20)
        self.last_action = data.get("last_action", "")
        self.used_actions = set(data.get("used_actions", []))
        self.last_event = data.get("last_event", "")
        self.last_event_choice = data.get("last_event_choice", "")
        self.last_action_consequences = data.get("last_action_consequences", {})


@dataclass
class Event:
    """Represents a random event that occurs during gameplay."""
    id: str
    year_min: int
    year_max: int
    era_weight: int
    name: str
    text: str
    event_type: str  # "auto" or "interactive"
    effect_money: int
    effect_ocean_toxicity: int
    effect_fish: int
    effect_support: int
    effect_pollution_growth: float
    choice_a_text: str = ""
    choice_a_effects: Dict[str, float] = None
    choice_b_text: str = ""
    choice_b_effects: Dict[str, float] = None
    choice_c_text: str = ""
    choice_c_effects: Dict[str, float] = None
    
    def __post_init__(self):
        """Initialize default values for interactive event fields."""
        if self.choice_a_effects is None:
            self.choice_a_effects = {}
        if self.choice_b_effects is None:
            self.choice_b_effects = {}
        if self.choice_c_effects is None:
            self.choice_c_effects = {}
    
    @classmethod
    def from_csv_row(cls, row: Dict[str, str]) -> 'Event':
        """Create Event from CSV row data."""
        def parse_effects(effects_str: str) -> Dict[str, float]:
            """Parse effects string into dictionary."""
            if not effects_str or effects_str.strip() == "":
                return {}
            import json
            import re
            
            # Clean up the string
            effects_str = effects_str.strip('"')
            
            # Try to fix common CSV parsing issues
            if effects_str.startswith('{') and not effects_str.endswith('}'):
                # Try to find the end of the JSON object
                brace_count = 0
                for i, char in enumerate(effects_str):
                    if char == '{':
                        brace_count += 1
                    elif char == '}':
                        brace_count -= 1
                        if brace_count == 0:
                            effects_str = effects_str[:i+1]
                            break
            
            try:
                # Try to parse as JSON
                return json.loads(effects_str)
            except json.JSONDecodeError:
                # Fallback to regex parsing for malformed JSON
                effects = {}
                # Look for key: value patterns
                pattern = r'["\']?([^"\':\s]+)["\']?\s*:\s*(-?\d+(?:\.\d+)?)'
                matches = re.findall(pattern, effects_str)
                for key, value in matches:
                    try:
                        effects[key] = float(value)
                    except ValueError:
                        effects[key] = 0.0
                return effects
        
        return cls(
            id=row["id"],
            year_min=int(row["year_min"]),
            year_max=int(row["year_max"]),
            era_weight=int(row["era_weight"]),
            name=row["name"],
            text=row["text"],
            event_type=row["event_type"],
            effect_money=int(row["effect_money"]),
            effect_ocean_toxicity=int(row["effect_ocean_toxicity"]),
            effect_fish=int(row["effect_fish"]),
            effect_support=int(row["effect_support"]),
            effect_pollution_growth=float(row["effect_pollution_growth"]),
            choice_a_text=row.get("choice_a_text", ""),
            choice_a_effects=parse_effects(row.get("choice_a_effects", "")),
            choice_b_text=row.get("choice_b_text", ""),
            choice_b_effects=parse_effects(row.get("choice_b_effects", "")),
            choice_c_text=row.get("choice_c_text", ""),
            choice_c_effects=parse_effects(row.get("choice_c_effects", ""))
        )


@dataclass
class Action:
    """Represents a player action/decision."""
    id: str
    unlock_year: int
    requires_support: int
    cost: int
    name: str
    desc: str
    effect_money: int
    effect_ocean_toxicity: int
    effect_fish: int
    effect_support: int
    effect_pollution_growth: float
    effect_yearly_income: int
    is_repeatable: bool
    
    @classmethod
    def from_csv_row(cls, row: Dict[str, str]) -> 'Action':
        """Create Action from CSV row data."""
        return cls(
            id=row["id"],
            unlock_year=int(row["unlock_year"]),
            requires_support=int(row["requires_support"]),
            cost=int(row["cost"]),
            name=row["name"],
            desc=row["desc"],
            effect_money=int(row["effect_money"]),
            effect_ocean_toxicity=int(row["effect_ocean_toxicity"]),
            effect_fish=int(row["effect_fish"]),
            effect_support=int(row["effect_support"]),
            effect_pollution_growth=float(row["effect_pollution_growth"]),
            effect_yearly_income=int(row.get("effect_yearly_income", 0)),
            is_repeatable=row["is_repeatable"].lower() == "true"
        )



"""
Game systems and mechanics for Planet Aqua.
"""

from typing import List, Dict, Any, Optional
from .models import GameState, Event, Action


class GameSystems:
    """Handles game mechanics and systems."""
    
    def __init__(self, config: Dict[str, Any]):
        """Initialize with game configuration."""
        self.config = config
    
    def clamp_stat(self, value: int, min_val: int = 0, max_val: int = 100) -> int:
        """Clamp a statistic to valid range."""
        return max(min_val, min(max_val, value))
    
    def apply_effects(self, state: GameState, effects: Dict[str, float]) -> None:
        """Apply effects to game state with proper clamping."""
        if "money" in effects:
            state.money = max(0, state.money + int(effects["money"]))
        
        if "ocean_toxicity" in effects:
            state.ocean_toxicity = self.clamp_stat(
                state.ocean_toxicity + int(effects["ocean_toxicity"])
            )
        
        if "fish_health" in effects:
            state.fish_health = self.clamp_stat(
                state.fish_health + int(effects["fish_health"])
            )
        
        if "support" in effects:
            state.public_support = self.clamp_stat(
                state.public_support + int(effects["support"])
            )
        
        if "pollution_growth" in effects:
            state.pollution_growth_modifier += effects["pollution_growth"]
        
        if "yearly_income" in effects:
            state.yearly_income = max(0, state.yearly_income + int(effects["yearly_income"]))
    
    def get_available_events(self, events: List[Event], year: int) -> List[Event]:
        """Get events available for the current year."""
        available = []
        for event in events:
            if year >= event.year_min and year <= event.year_max:
                available.extend([event] * event.era_weight)
        return available
    
    def get_available_interactive_events(self, events: List[Event], year: int) -> List[Event]:
        """Get interactive events available for the current year."""
        available = []
        for event in events:
            if (year >= event.year_min and year <= event.year_max and 
                event.event_type == "interactive"):
                available.extend([event] * event.era_weight)
        return available
    
    def get_available_actions(self, actions: List[Action], state: GameState) -> List[Action]:
        """Get 5 random actions available for the current year and state."""
        # First filter by requirements
        eligible = []
        for action in actions:
            if (state.year >= action.unlock_year and 
                state.public_support >= action.requires_support and
                state.money >= action.cost and
                action.id not in state.used_actions):
                eligible.append(action)
        
        # Return 5 random actions from eligible ones
        if len(eligible) <= 5:
            return eligible
        else:
            import random
            return random.sample(eligible, 5)
    
    def apply_yearly_drift(self, state: GameState) -> None:
        """Apply baseline yearly changes based on research findings."""
        # Exponential pollution growth (Lebreton et al., 2018)
        # Pollution grows faster over time, especially microplastics
        base_growth = self.config["base_pollution_growth"] + state.pollution_growth_modifier
        
        # Exponential growth factor based on current ocean toxicity
        exponential_factor = 1 + (state.ocean_toxicity / 100.0) * 0.5
        pollution_growth = int(base_growth * exponential_factor)
        
        # Update ocean toxicity
        state.ocean_toxicity = self.clamp_stat(
            state.ocean_toxicity + pollution_growth
        )
        
        # Fish health decline based on ocean toxicity - more gradual decline
        # The more toxic the ocean, the more fish health decreases
        if state.ocean_toxicity >= 80:
            fish_decline = 8  # High decline for very toxic ocean
        elif state.ocean_toxicity >= 60:
            fish_decline = 5  # Medium-high decline
        elif state.ocean_toxicity >= 40:
            fish_decline = 3  # Medium decline
        elif state.ocean_toxicity >= 20:
            fish_decline = 1  # Low decline
        else:
            fish_decline = 0  # No decline for clean ocean
        
        state.fish_health = self.clamp_stat(
            state.fish_health - fish_decline
        )
        
        # Ocean is the lifeblood of society - fish health affects income
        # When mother ocean hurts, we hurt too
        if state.fish_health >= 80:
            # Thriving ocean - full income
            income_multiplier = 1.0
        elif state.fish_health >= 60:
            # Healthy ocean - good income
            income_multiplier = 0.8
        elif state.fish_health >= 40:
            # Struggling ocean - reduced income
            income_multiplier = 0.6
        elif state.fish_health >= 20:
            # Dying ocean - poor income
            income_multiplier = 0.4
        else:
            # Collapsed ocean - minimal income
            income_multiplier = 0.2
        
        # Calculate income based on fish health
        base_income = int(state.yearly_income * income_multiplier)
        
        # Public support affects income - low support means economic disruption
        if state.public_support >= 80:
            support_multiplier = 1.0  # Full income with high support
        elif state.public_support >= 60:
            support_multiplier = 0.9  # Slight reduction
        elif state.public_support >= 40:
            support_multiplier = 0.7  # Moderate reduction
        elif state.public_support >= 20:
            support_multiplier = 0.5  # Significant reduction
        else:
            support_multiplier = 0.3  # Major economic disruption
        
        final_income = int(base_income * support_multiplier)
        state.money += final_income
    
    def check_endings(self, state: GameState) -> Optional[str]:
        """Check for win/lose conditions. Returns ending type or None."""
        if state.fish_health <= 0:
            return "fish_collapse"
        elif state.ocean_toxicity >= 100:
            return "toxic_seas"
        elif state.public_support <= 0:
            return "uprising"
        elif (state.year >= self.config["end_year"] and
              state.ocean_toxicity < self.config["win_pollution_threshold"] and
              state.fish_health >= self.config["win_fish_threshold"]):
            return "victory"
        return None
    
    def get_ending_narrative(self, ending: str) -> str:
        """Get narrative text for game endings."""
        narratives = {
            "fish_collapse": """
🐟 THE SILENT DEPTHS - The ocean has fallen silent...

The once-teeming waters of Planet Aqua have been emptied of life. Your failure to protect
the marine ecosystem has led to the collapse of the food chain. The fishing villages
have been abandoned, the economy has crumbled, and the ocean's song has been silenced.

The Council of Depths has stripped you of your title. You are remembered only as
the Guardian who let the ocean die. The Great Garbage Vortex continues to grow,
a monument to your failed stewardship.

The currents whisper your name in shame...
            """,
            "toxic_seas": """
☠️ THE POISONED REALM - The ocean has become a toxic wasteland...

Your negligence has allowed the ocean to become so polluted that it can no longer
support life. The waters that once sustained Planet Aqua now poison everything
they touch. The very essence of your world has been corrupted.

The Council of Depths has banished you to the deepest trenches. You watch from
the abyss as the surface world struggles to survive in a poisoned ocean.

The garbage patches have claimed victory over life itself...
            """,
            "uprising": """
⚡ THE PEOPLE'S REVOLT - The citizens have risen against you!

Your failure to listen to the people's cries for help has sparked a revolution.
The Council of Depths has been overthrown, and you have been cast out of power.
The citizens have taken matters into their own hands, but it may be too late.

You watch from exile as the new leaders struggle to undo the damage of your
failed reign. The ocean's fate now rests in the hands of those you failed to serve.

A Guardian who loses the people's trust is no Guardian at all...
            """,
            "victory": """
🏆 THE ETERNAL GUARDIAN - You have achieved the impossible!

Through wisdom, courage, and unwavering dedication, you have guided Planet Aqua
to a golden age of harmony. The ocean teems with life, the people prosper,
and the balance between nature and civilization has been restored.

The Council of Depths bestows upon you the highest honor: Guardian Eternal.
Your name will be remembered in the currents for all time. The ocean sings
your praises, and the people tell stories of your wisdom.

You have proven that true leadership means protecting both the people
and the planet that sustains them. The ocean's song is strong and clear,
and Planet Aqua flourishes under your eternal watch.

The currents whisper your name in reverence...
            """
        }
        return narratives.get(ending, "Unknown ending.")

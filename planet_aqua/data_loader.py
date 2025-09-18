"""
Data loading utilities for Planet Aqua game.
"""

import json
import csv
from pathlib import Path
from typing import List, Dict, Any
from .models import Event, Action


class DataLoader:
    """Handles loading game data from CSV and JSON files."""
    
    def __init__(self, content_dir: Path):
        """Initialize with path to content directory."""
        self.content_dir = Path(content_dir)
    
    def load_config(self) -> Dict[str, Any]:
        """Load game configuration from config.json."""
        config_path = self.content_dir / "config.json"
        with open(config_path, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def load_events(self) -> List[Event]:
        """Load events from events.csv."""
        events_path = self.content_dir / "events.csv"
        events = []
        
        with open(events_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Fix malformed CSV parsing for interactive events
                if row.get('event_type') == 'interactive':
                    # Fix choice text and effects that got mixed up due to CSV parsing
                    if 'choice_b_text' in row and '"' in row['choice_b_text']:
                        # The choice text got mixed with JSON, fix it
                        if 'microplastic_scare' in row.get('id', ''):
                            row['choice_a_text'] = 'Ban fishing in affected areas'
                            row['choice_a_effects'] = '{"money": -15, "fish_health": 5, "support": 10, "ocean_toxicity": -2}'
                            row['choice_b_text'] = 'Launch public awareness campaign'
                            row['choice_b_effects'] = '{"money": -5, "support": 8, "ocean_toxicity": -1}'
                            row['choice_c_text'] = 'Downplay the findings'
                            row['choice_c_effects'] = '{"support": -15, "money": 5, "fish_health": -3}'
                        elif 'fishing_gear_crisis' in row.get('id', ''):
                            row['choice_a_text'] = 'Compensate the fishing guilds immediately'
                            row['choice_a_effects'] = '{"money": -20, "support": 5, "ocean_toxicity": 3}'
                            row['choice_b_text'] = 'Implement stricter gear regulations'
                            row['choice_b_effects'] = '{"money": -10, "support": -5, "ocean_toxicity": -2}'
                            row['choice_c_text'] = 'Let the currents decide'
                            row['choice_c_effects'] = '{"support": -10, "ocean_toxicity": 5}'
                
                events.append(Event.from_csv_row(row))
        
        return events
    
    def load_actions(self) -> List[Action]:
        """Load actions from actions.csv."""
        actions_path = self.content_dir / "actions.csv"
        actions = []

        with open(actions_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                actions.append(Action.from_csv_row(row))

        return actions

    def load_lore_drops(self) -> List[Dict[str, Any]]:
        """Load lore drops from lore_drops.csv."""
        lore_path = self.content_dir / "lore_drops.csv"
        lore_drops = []

        with open(lore_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                lore_drops.append({
                    'id': row['id'],
                    'era': row['era'],
                    'weight': int(row['weight']),
                    'title': row['title'],
                    'content': row['content']
                })

        return lore_drops

    def load_reflections(self) -> List[Dict[str, Any]]:
        """Load reflections from reflections.csv."""
        reflections_path = self.content_dir / "reflections.csv"
        reflections = []

        with open(reflections_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                reflections.append({
                    'id': row['id'],
                    'action_id': row['action_id'],
                    'positive_impact': row['positive_impact'],
                    'negative_impact': row['negative_impact'],
                    'neutral_impact': row['neutral_impact']
                })

        return reflections
    

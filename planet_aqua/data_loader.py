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
    

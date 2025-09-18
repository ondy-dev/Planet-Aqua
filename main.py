#!/usr/bin/env python3
"""
Planet Aqua - Stop the Trash Tide
A meaningful simulation game about ocean plastic pollution and sustainable fishing.

Planet Aqua is a generational simulation game where you play as the Ocean Guardian,
chosen by the Council of Depths to lead this water-world. Each generation of fish-people
lives for 5 years, and you must guide Planet Aqua through 30 generations (150 years)
of challenges.

The game is presented as The Ocean Guardian's Diary, chronicling your decisions and
their consequences across the ages. Each diary entry represents 5 years of your
guardianship, with rich lore about the floating cities, fishing guilds, and the
mysterious depths.

As Ocean Guardian, you must balance the needs of the people, the economy, and the
ocean's health. The fate of an entire world rests in your hands...
"""

from pathlib import Path
from planet_aqua import PlanetAquaGame


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(description="Planet Aqua - Stop the Trash Tide")
    parser.add_argument("--seed", type=int, help="Random seed for reproducible runs")
    parser.add_argument("--content-dir", type=Path, help="Path to content directory")
    args = parser.parse_args()
    
    game = PlanetAquaGame(content_dir=args.content_dir, seed=args.seed)
    game.play()


if __name__ == "__main__":
    main()

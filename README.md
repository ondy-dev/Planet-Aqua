# Planet Aqua — Stop the Trash Tide

🌊 A meaningful simulation game about ocean plastic pollution and sustainable fishing

## Overview

Planet Aqua is a generational simulation game where you play as the **Ocean Guardian**, chosen by the Council of Depths to lead this water-world. Each generation of fish-people lives for 5 years, and you must guide Planet Aqua through 30 generations (150 years) of challenges.

The game is presented as **The Ocean Guardian's Diary**, chronicling your decisions and their consequences across the ages. Each diary entry represents 5 years of your guardianship, with rich lore about the floating cities, fishing guilds, and the mysterious depths.

The game features **34 evidence-based actions** ranging from simple plastic bag bans ($25) to complex global treaties ($320), each with realistic trade-offs and public opinion impacts. You'll learn which real-world solutions actually work through trial and error, with actions grounded in the latest ocean plastic pollution research.

As Ocean Guardian, you must balance the needs of the people, the economy, and the ocean's health. The fate of an entire world rests in your hands...

The game teaches systems thinking: how values, technology, and choices compound into long-term consequences across generations.

## World-Building & Lore

Planet Aqua is a water-world where you serve as the **Ocean Guardian**, chosen by the **Council of Depths** to lead the floating settlements. The world features:

- **Floating Cities**: Settlements built on the ocean surface
- **Fishing Guilds**: Powerful organizations that control the fishing industry
- **Tide-Walkers**: Citizens who live on the coastlines and beaches
- **Ocean Scholars**: Scientists who study the depths and currents
- **The Great Garbage Vortex**: A massive accumulation of waste in the ocean currents
- **The Council of Depths**: The governing body that oversees the ocean's health

The game's events and actions are framed within this rich, immersive world where every decision affects the delicate balance between civilization and the ocean's health.

## Research Alignment

This game is grounded in real-world research about the **Great Pacific Garbage Patch** and ocean plastic pollution, incorporating findings from the latest scientific studies:

- **Fishing Gear Focus**: A large share of floating macroplastic in Earth's garbage patches comes from fishing-related gear, which is reflected in the game's events and mechanics
- **Recycling Reality**: Only 9% of plastic waste is actually recycled globally - the game reflects this harsh reality
- **Regional Differences**: China produces 32% of global plastics, while the US consumes 130kg per person annually (highest globally)
- **Cleanup Effectiveness**: Research shows that 80% cleanup can bring pollution to safe levels for marine life
- **Upstream Prevention**: Prevention at the source is far more effective than downstream cleanup efforts
- **Systems Thinking**: Emphasizes how convenience culture, industrial practices, and weak governance create complex environmental problems
- **Trade-offs**: Teaches the balance between short-term production and long-term ecosystem health
- **Unintended Consequences**: Shows how well-intentioned actions can have unexpected environmental impacts

### Academic Frameworks

The game incorporates several key concepts from environmental studies and systems thinking:

- **Development = Values + Technology + Consequences**: Every decision reflects underlying values, uses available technology, and produces measurable outcomes
- **Unintended Consequences**: Actions often have effects beyond their immediate purpose
- **Liberation vs Control**: Balancing economic freedom with environmental protection
- **Technological Determinism**: How technology choices shape environmental outcomes
- **Medium is the Message**: The game itself teaches through its mechanics, not just its content

## Game Mechanics

### Core Stats
- **Year**: Current game year (0-150)
- **Money**: Economic resources for taking actions (starts at $100) - **Strategic Resource Management Required**
- **Ocean Toxicity**: Total ocean pollution level (0-100%, game over at 100%)
- **Fish Health**: Marine ecosystem health (0-100%, game over at 0%)
- **Public Support**: Political capital and public approval (0-100%, game over at 0% - uprising!)
- **Yearly Income**: Passive income received each year (starts at $20)
- **Pollution Growth Modifier**: Cumulative effect of long-term policies

### Strategic Resource Management
The game requires careful financial planning and strategic decision-making:

**Cost Structure Philosophy:**
- **No Free Actions**: Every action has a meaningful cost (ranging from $20 to $350)
- **Cost vs. Effectiveness**: More expensive actions generally provide greater benefits
- **Early Game Constraint**: Limited budget forces careful prioritization of immediate needs
- **Long-term Investment**: Expensive actions require saving and planning across multiple generations
- **Trade-off Decisions**: Every choice involves balancing cost, effectiveness, and timing

**Economic Decision-Making:**
- **Budget Management**: Players must balance immediate needs with long-term investments
- **Resource Scarcity**: Money becomes a meaningful limiting factor, not an afterthought
- **Strategic Planning**: Expensive but effective actions require multi-generation planning
- **Risk vs. Reward**: Cheaper actions have limited impact; expensive actions provide significant benefits

### Generational Gameplay Loop
1. **Diary Entry**: Read the current generation's story and world state
2. **Generation Report**: See the effects of your previous generation's decision
3. **Generation Event**: One major event affects the entire 5-year period
4. **Guardian's Decision**: Choose one action from 5 random options (no repeats)
5. **Apply Effects**: Action affects the entire 5-year period
6. **Generation Drift**: Apply 5 years of passive changes (pollution growth, income)
7. **Generation Transition**: Pass the diary to the next Ocean Guardian
8. **Check Endings**: Determine if the game should end

### Diary System
The game is presented as a living diary, with each entry containing:
- **Generation Lore**: Rich descriptions of the floating cities and fish-people culture
- **Random Lore Drops**: Humorous and world-building snippets that add flavor to each era
- **Historical Context**: References to previous generations' decisions
- **Reflections**: Analysis of how previous decisions impacted the world over 5 years
- **Current Events**: 5 years of world events and crises
- **Guardian's Choice**: One major decision that will shape the generation
- **Consequences**: The long-term impact of your choices

### Lore System
The game features a rich lore system with **30 unique lore drops** across 5 eras, including research-based discoveries:
- **Early Era (Generations 1-5)**: The dawn of synthetic materials and floating cities
- **Discovery Era (Generations 6-10)**: The revelation of pollution and its effects
- **Awakening Era (Generations 11-20)**: Environmental awareness and activism
- **Transformation Era (Generations 21-25)**: The shift toward sustainable solutions
- **Late Era (Generations 26-30)**: The culmination of environmental efforts

Each lore drop includes humorous references to our world with an aquatic twist, such as:
- "The Fish" - a cooking show about an underwater chef
- Hairless monkey tourists who can't swim
- The Great Kelp Shortage and synthetic alternatives
- The Ocean's Song changing to reflect environmental distress

**Research-Based Lore Drops:**
- **The Recycling Myth**: Ocean scholars discover that only 9% of plastic waste is actually recycled globally
- **The Eastern Production Boom**: Distant floating cities in the eastern waters have become the world's largest producers of synthetic materials
- **The Western Consumption Crisis**: Floating cities in the western waters consume 130kg of synthetic materials per person annually
- **The Cleanup Revelation**: Ocean scholars have discovered that aggressive cleanup operations are actually less harmful to marine life than leaving pollution in place

### Generational Mechanics
- **5-Year Lifespans**: Each generation of fish-people lives for exactly 5 years
- **Diary Continuity**: Each new Ocean Guardian inherits the diary of their predecessor
- **Legacy Building**: Decisions made by one generation affect all future generations
- **Realistic Timeline**: Environmental policies take years to implement and show results
- **Long-term Thinking**: Forces players to consider consequences beyond their lifetime

### Win/Lose Conditions
- **Lose**: Fish health drops to 0 (ecosystem collapse)
- **Lose**: Ocean toxicity reaches 100% (toxic seas)
- **Lose**: Public support drops to 0 (uprising!)
- **Win**: Reach Generation 30 (Year 150) with ocean toxicity < 60% and fish health ≥ 50%

## Installation & Usage

### Requirements
- Python 3.10 or higher
- No external dependencies required

### Running the Game

```bash
# Basic game
python main.py

# With random seed for reproducible runs
python main.py --seed 42

# With custom content directory
python main.py --content-dir /path/to/content
```

### Game Controls
- Enter numbers to select actions (1-6)
- Press Enter to continue between generations
- Use Ctrl+C to quit anytime
- Each generation offers 5 random actions (no repeats once used)

**Note**: The game displays a lot of text. You may need to scroll up or expand your terminal window to see all the content, especially during generation reports and diary entries.

## Project Structure

```
Planet-Aqua/
├── main.py              # CLI entry point
├── README.md            # This file
└── planet_aqua/         # Game package
    ├── __init__.py      # Package initialization
    ├── engine.py        # Main game engine
    ├── models.py        # Data models (GameState, Event, Action)
    ├── data_loader.py   # CSV/JSON data loading
    ├── systems.py       # Game mechanics and systems
    └── content/         # Game data files
        ├── events.csv   # Random events with effects
        ├── actions.csv  # Player actions and policies
        ├── lore_drops.csv # Random world-building snippets by era
        └── config.json  # Game balance settings
```

## Content Design

### Events (events.csv)
Unified event system with both automatic and interactive events:

**Automatic Events** (happen automatically - parallel real-world plastic pollution history):

**Early Era (Years 0-25):**
- **The Synthetic Revolution**: The floating cities embrace a new wonder material that never degrades
- **The Age of Convenience**: Single-use items become the norm across settlements
- **The Return Vessel Program**: Container return systems reduce waste in the currents

**Discovery Era (Years 25-50):**
- **The Vortex Revealed**: Ocean scholars discover a massive accumulation of waste in the northern currents
- **The Invisible Threat**: Tiny particles of synthetic material are found throughout the food chain
- **The Black Tide's End**: The source of synthetic materials becomes scarce, forcing alternatives

**Awakening Era (Years 50-75):**
- **The Artisan's Renaissance**: A new generation perfects the art of transforming waste into useful materials
- **The Currents' Warning**: Ocean temperature rises, threatening marine life balance
- **The Depth-Sweepers**: Revolutionary technology allows removal of synthetic materials from the ocean

**Transformation Era (Years 75-120):**
- **The Eternal Cycle**: Visionary leaders propose a circular economy where nothing is wasted
- **The Living Materials**: Ocean scholars develop materials that truly return to the ocean's embrace
- **The World's Realization**: All floating cities unite in recognition that ocean health is essential

**Research-Based Events:**
- **The Recycling Illusion**: Ocean scholars discover that only 9% of synthetic materials are actually recycled globally
- **The Eastern Tide**: Distant floating cities in the eastern waters have become the world's largest producers of synthetic materials
- **The Western Excess**: Floating cities in the western waters consume 130kg of synthetic materials per person annually
- **The Cleanup Revelation**: Ocean scholars discover that aggressive cleanup operations are less harmful to marine life than leaving pollution in place
- **The Source Revelation**: Ocean scholars realize that preventing pollution at its source is far more effective than cleaning up after it enters the ocean

**Interactive Crises** (Crises of the Depths - require player choice):
- **The Storm's Wrath**: Fishing guilds lose gear - compensate, regulate, or let the currents decide?
- **Microplastics Found in Local Fish**: Microplastics found in fish - ban fishing, educate, or downplay?
- **Cleanup Operation Faces Opposition**: Community opposes cleanup - proceed, scale back, or cancel?
- **Fishing Quotas Under Review**: Fishing quotas under review - increase, maintain, or reduce?
- **Plastic Tax Causes Public Unrest**: Plastic tax causes unrest - repeal, keep, or modify?
- **Recycling Program Fails**: Recycling program fails - invest more, switch methods, or abandon?

### Actions (actions.csv)
Evidence-based policy decisions with real-world trade-offs and strategic cost management:

**Cost Structure Design:**
- **Budget Actions ($20-$50)**: Quick, limited-impact solutions for immediate needs
- **Mid-Range Actions ($60-$150)**: Balanced effectiveness with moderate investment
- **High-Investment Actions ($160-$350)**: Powerful, long-term solutions requiring significant planning
- **No Free Actions**: Every decision has financial consequences, forcing strategic thinking

**Budget Actions ($20-$50) - Quick Solutions:**
- **Emergency Ocean Tax** ($20): Impose heavy taxes on polluting industries - generates money but reduces public support
- **Ban Single-Use Plastic Bags** ($25): Immediate pollution reduction but cultural resistance - research shows effective
- **Implement Austerity** ($30): Cut government spending to save money - reduces costs but hurts public services and support
- **Behavioral Nudge Campaign** ($32): Research shows limited effectiveness without structural support - information alone isn't enough
- **Community Beach Cleanup** ($40): Visible action that boosts public support but limited long-term impact
- **Impose Fishing Quotas** ($40): Limit fishing catches to protect fish populations - improves ocean health but angers fishing industry
- **Public Awareness Campaign** ($50): Build public support but research shows information alone has limited impact

**Mid-Range Actions ($60-$150) - Balanced Investment:**
- **Expand Fishing Fleet** ($60): Increase fishing capacity for immediate economic gains - short-term profit, long-term harm
- **Install River Interceptors** ($60): Prevent plastic from reaching the ocean - effective upstream solution
- **Emergency Ocean Cleanup** ($80): Quick pollution removal - immediate visual impact
- **Enforce Manufacturing Standards** ($80): Require all synthetic material producers to use ocean-safe designs and materials - costly but prevents pollution at source
- **Ban Plastic Waste Exports** ($80): Stop exporting plastic waste to other countries - reduces global pollution
- **Install Microplastic Filters** ($90): Advanced filtration systems in water treatment plants
- **Subsidize Fishing Industry** ($100): Economic gain but increases gear pollution
- **Corporate Bailout** ($100): Bail out struggling industries with public money - costs money but maintains jobs and support
- **Recycling-Only Strategy** ($100): Focuses only on recycling without reducing production - research shows only 9% of plastic is actually recycled globally
- **US Waste Management Reform** ($110): Address western floating cities' 130kg/person consumption - highest globally
- **Southeast Asia Infrastructure** ($130): Build waste management systems in regions with 50%+ mismanaged waste
- **Extended Producer Responsibility** ($140): Make manufacturers pay for waste disposal
- **China Plastic Production Agreement** ($150): Negotiate with eastern floating cities to reduce their 32% share of global synthetic material production

**High-Investment Actions ($160-$350) - Strategic Planning Required:**
- **Upgrade Waste Management** ($160): Comprehensive recycling infrastructure
- **Heavy Ocean Cleanup** ($180): Research shows 80% cleanup can bring pollution to safe levels for marine life
- **Circular Economy Initiative** ($200): Redesign products for reuse
- **Create Marine Protected Areas** ($200): Establish zones where fishing is restricted to allow ecosystem recovery
- **Develop Biodegradable Plastics** ($240): R&D for truly biodegradable alternatives
- **Deploy Ocean Restoration Technology** ($280): Advanced bioremediation and cleanup technologies
- **Global Plastic Treaty** ($320): International agreement to reduce production
- **Release Plastic-Eating Bacteria** ($350): Genetically modified bacteria that consume plastic waste

**Risky/Less Effective Actions:**
- **Build Waste Incineration** ($120): Reduces ocean pollution but creates air emissions and health concerns
- **Promote False Biodegradables** ($140): Claims to be biodegradable but doesn't degrade in ocean - false environmental claims

**Additional Cleanup Actions:**
- **Surface Cleanup Operations** ($120): Focus only on removing visible pollution from ocean surface without addressing root causes
- **Deploy Ocean Plastic Collectors** ($120): Autonomous floating collectors - proven effective for macroplastics

### Strategic Decision-Making Philosophy

The game's cost structure teaches real-world environmental policy decision-making through resource scarcity, opportunity costs, and strategic planning across generations.

### Configuration (config.json)
Tunable game balance parameters:
- Starting statistics
- Win/lose thresholds
- Economic and environmental baselines
- Difficulty scaling

## Educational Value

Planet Aqua teaches important concepts including systems thinking, evidence-based policy, trade-offs, public opinion management, time delays, resource management, and cost-benefit analysis.

## Real-World Connections

The game is based on actual research about ocean plastic pollution, incorporating findings from the latest scientific studies:

- **Fishing Gear**: 75-86% of the Great Pacific Garbage Patch mass comes from fishing equipment
- **Exponential Growth**: Plastic pollution in the GPGP has been growing exponentially since 1970
- **Microplastics**: 94% of plastic pieces by count are microplastics, but only 8% by mass
- **Macroplastics**: 92% of plastic mass comes from larger items, mostly fishing gear
- **Economic Incentives**: Market forces often conflict with environmental protection
- **Public Opinion**: Environmental policies require public support to be effective

### Evidence-Based Solutions

All actions in the game are based on real-world research from the latest scientific studies:

**Key Research Sources:**
- **Global Plastics Supply Chain Analysis** (2025): Reveals that only 9% of plastic waste is actually recycled globally
- **China's Plastic Consumption Trends** (2025): Shows China's 32% share of global production and 76kg/person consumption
- **US Role in Global Ocean Plastic Waste** (2022): Documents US's 130kg/person consumption - highest globally
- **North Pacific Garbage Patch Cleanup Study** (2025): Proves that 80% cleanup can bring pollution to safe levels for marine life
- **Plastic Waste Behavior Meta-Analysis** (2022): Shows that information alone isn't enough - need incentives and infrastructure

- **Extended Producer Responsibility**: Based on successful EPR programs that shift costs to manufacturers
- **Single-Use Plastic Bans**: Proven to reduce plastic waste by up to 40% in some regions
- **River Interceptors**: Real technology deployed by The Ocean Cleanup and others
- **Waste Management Upgrades**: Critical for preventing "leakage" of waste into the environment
- **Global Treaties**: Modeled after successful international environmental agreements
- **False Biodegradables**: Based on research showing many "biodegradable" plastics don't degrade in ocean conditions

### Historical Parallels

The automatic events parallel real-world milestones in plastic pollution history:

- **The Synthetic Revolution** (1950s): Parallels the invention and mass adoption of plastic
- **The Age of Convenience** (1960s-70s): Reflects the rise of disposable culture
- **The Vortex Revealed** (1988): Based on the discovery of the Great Pacific Garbage Patch
- **The Invisible Threat** (2000s): Mirrors the discovery of microplastics in marine life
- **The Black Tide's End** (1970s): References the oil crisis that affected plastic production
- **The Artisan's Renaissance** (1980s-90s): Parallels the rise of recycling programs
- **The Currents' Warning** (2000s-2010s): Reflects climate change awareness
- **The Eternal Cycle** (2010s-2020s): Based on circular economy concepts
- **The Living Materials** (2020s): References biodegradable plastic development
- **The World's Realization** (2020s): Mirrors global plastic pollution awareness

## Development

### Adding Content
- **Events**: Add rows to `content/events.csv` with appropriate year ranges and effects
- **Actions**: Add rows to `content/actions.csv` with costs, requirements, and effects
  - Include realistic cost-benefit trade-offs based on real-world evidence
  - Consider public opinion impacts and unlock requirements
  - Balance short-term vs. long-term effectiveness
- **Balance**: Modify `content/config.json` to adjust game difficulty and pacing

### Code Structure
- **Modular Design**: Separate concerns into different modules
- **Data-Driven**: All content loaded from external files
- **Type Hints**: Full type annotation for better code clarity
- **Error Handling**: Graceful handling of invalid inputs and edge cases

## Future Enhancements

Potential improvements and expansions:
- **Difficulty Modes**: Easy, Normal, Hard settings with different action costs and effectiveness
- **Era System**: Different event weights for different time periods (1970s-2020s)
- **Save/Load**: Persistent game state across sessions
- **Scoreboard**: Track high scores and best strategies
- **Action Effectiveness Tracking**: Show players which actions they've used and their success rates
- **Research Integration**: Add more detailed citations and links to supporting research
- **Web Version**: Streamlit or web-based interface
- **Multiplayer**: Collaborative or competitive modes

## Contributing

This project is designed to be educational and easily modifiable. Feel free to:
- Add new events and actions based on real-world research
- Adjust game balance and action effectiveness
- Improve the user interface and educational content
- Add new features like difficulty modes or save/load
- Create educational content and research citations
- Suggest new evidence-based solutions to include

## License

This project is created for educational purposes and is open for use in academic and educational contexts.

---

*"The ocean is not a garbage can, but we've been treating it like one. Planet Aqua helps us understand why this matters and what we can do about it."*

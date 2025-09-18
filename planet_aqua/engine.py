"""
Main game engine for Planet Aqua.
"""

import random
from pathlib import Path
from typing import List, Optional
from .models import GameState, Event, Action
from .data_loader import DataLoader
from .systems import GameSystems


class PlanetAquaGame:
    """Main game engine for Planet Aqua."""
    
    def __init__(self, content_dir: Optional[Path] = None, seed: Optional[int] = None):
        """Initialize the game with optional seed for reproducible runs."""
        if seed is not None:
            random.seed(seed)
        
        # Set up content directory
        if content_dir is None:
            content_dir = Path(__file__).parent / "content"
        
        # Load game data
        self.data_loader = DataLoader(content_dir)
        self.config = self.data_loader.load_config()
        self.events = self.data_loader.load_events()
        self.actions = self.data_loader.load_actions()
        self.lore_drops = self.data_loader.load_lore_drops()
        self.reflections = self.data_loader.load_reflections()
        
        # Initialize game systems
        self.systems = GameSystems(self.config)
        
        # Initialize game state
        self.state = GameState(
            year=self.config["start_year"],
            money=self.config["start_money"],
            ocean_toxicity=self.config["start_ocean_toxicity"],
            fish_health=self.config["start_fish"],
            public_support=self.config["start_support"],
            yearly_income=self.config["yearly_income"]
        )
    
    def print_stats(self) -> None:
        """Print current game statistics."""
        # Calculate income multiplier based on fish health
        if self.state.fish_health >= 80:
            fish_multiplier = 1.0
            ocean_status = "Thriving"
        elif self.state.fish_health >= 60:
            fish_multiplier = 0.8
            ocean_status = "Healthy"
        elif self.state.fish_health >= 40:
            fish_multiplier = 0.6
            ocean_status = "Struggling"
        elif self.state.fish_health >= 20:
            fish_multiplier = 0.4
            ocean_status = "Dying"
        else:
            fish_multiplier = 0.2
            ocean_status = "Collapsed"
        
        # Calculate support multiplier
        if self.state.public_support >= 80:
            support_multiplier = 1.0
            support_status = "Strong"
        elif self.state.public_support >= 60:
            support_multiplier = 0.9
            support_status = "Good"
        elif self.state.public_support >= 40:
            support_multiplier = 0.7
            support_status = "Weak"
        elif self.state.public_support >= 20:
            support_multiplier = 0.5
            support_status = "Poor"
        else:
            support_multiplier = 0.3
            support_status = "Critical"
        
        actual_income = int(self.state.yearly_income * fish_multiplier * support_multiplier)
        
        # Calculate pollution growth rate
        base_growth = self.config["base_pollution_growth"] + self.state.pollution_growth_modifier
        exponential_factor = 1 + (self.state.ocean_toxicity / 100.0) * 0.5
        current_growth_rate = int(base_growth * exponential_factor)
        
        print(f"\n{'='*80}")
        print(f"🌊 YEAR {self.state.year} | 💰 Treasury: ${self.state.money} | ☠️ Ocean Toxicity: {self.state.ocean_toxicity}% | 🐟 Marine Life: {self.state.fish_health}% | 👥 Public Trust: {self.state.public_support}%")
        print(f"💵 Yearly Income: ${actual_income} (Base: ${self.state.yearly_income} × Fish: {fish_multiplier:.1f} × Support: {support_multiplier:.1f})")
        print(f"🌊 Ocean Status: {ocean_status} | 👥 Support Status: {support_status}")
        print(f"📈 Pollution Growth Rate: {current_growth_rate}% per year (Base: {self.config['base_pollution_growth']} + Modifier: {self.state.pollution_growth_modifier:+.1f})")
        print(f"🌊 The ocean is the lifeblood of our society. When mother ocean thrives, we thrive. When she hurts, we hurt too.")
        print(f"👥 Public trust drives economic stability. Low support means economic disruption and reduced income.")
        print(f"{'='*80}")
    
    def print_event(self, event: Event) -> None:
        """Print event information."""
        print(f"\n📰 WORLD EVENT: {event.name}")
        print(f"{event.text}")
        print(f"Consequences: Treasury {event.effect_money:+d}, Ocean Toxicity {event.effect_ocean_toxicity:+d}, Marine Life {event.effect_fish:+d}, Public Trust {event.effect_support:+d}")
    
    def print_actions(self, actions: List[Action]) -> None:
        """Print available actions menu."""
        print(f"\n⚔️ GUARDIAN'S DECISIONS:")
        for i, action in enumerate(actions, 1):
            cost_str = f" (Cost: ${action.cost})" if action.cost > 0 else " (Free)"
            print(f"{i}. {action.name}{cost_str}")
            print(f"   {action.desc}")
        print(f"{len(actions) + 1}. Wait and observe")
    
    def print_interactive_event(self, event: Event) -> None:
        """Print interactive event with choices."""
        print(f"\n⚡ CRISIS OF THE DEPTHS: {event.name}")
        print(f"{event.text}")
        print(f"\nAs Ocean Guardian, how do you respond?")
        print(f"A. {event.choice_a_text}")
        print(f"B. {event.choice_b_text}")
        print(f"C. {event.choice_c_text}")
    
    def handle_interactive_event(self, event: Event) -> None:
        """Handle an interactive event with player choice."""
        self.print_interactive_event(event)
        
        while True:
            choice = input("\nChoose (A/B/C): ").strip().upper()
            
            if choice == 'A':
                effects = event.choice_a_effects
                choice_text = event.choice_a_text
                print(f"\n✅ You chose: {choice_text}")
                break
            elif choice == 'B':
                effects = event.choice_b_effects
                choice_text = event.choice_b_text
                print(f"\n✅ You chose: {choice_text}")
                break
            elif choice == 'C':
                effects = event.choice_c_effects
                choice_text = event.choice_c_text
                print(f"\n✅ You chose: {choice_text}")
                break
            else:
                print("Please choose A, B, or C.")
        
        # Track the event and choice for reporting
        self.state.last_event = event.name
        self.state.last_event_choice = choice_text
        
        # Apply effects
        self.systems.apply_effects(self.state, effects)
        
        # Show effects summary in the same format as actions
        print(f"Consequences: Treasury {effects.get('money', 0):+d}, Ocean Toxicity {effects.get('ocean_toxicity', 0):+d}, Marine Life {effects.get('fish_health', 0):+d}, Public Trust {effects.get('support', 0):+d}")
    
    def print_diary_entry(self, generation: int) -> None:
        """Print a diary entry header with generation info and lore."""
        generation_name = self.config["generation_names"][generation % len(self.config["generation_names"])]
        year_range = f"{self.state.year + 1}-{self.state.year + self.config['generation_length']}"
        
        print("\n" + "=" * 80)
        print(f"📖 DIARY ENTRY - GENERATION {generation + 1}")
        print(f"🌊 {generation_name} ({year_range})")
        print("=" * 80)
        
        # Determine era based on generation
        era = self.get_era_for_generation(generation)
        
        # Add random lore drop for this era
        self.print_lore_drop(era)
        
        # Add generation report on previous generation's actions if not first generation
        if generation > 0:
            self.print_generation_report(generation)
        else:
            # First generation introduction
            print("\n" + "~" * 80)
            print("WELCOME, NEW OCEAN GUARDIAN")
            print("~" * 80)
            print()
            print("You have been chosen by the Council of Depths to serve as Ocean Guardian.")
            print("The fate of Planet Aqua rests in your hands. Each generation of fish-people")
            print("lives for 5 years, and you must guide this water-world through 30 generations")
            print("of challenges and opportunities.")
            print()
            print("The ocean is vast and mysterious, but it is also fragile. The choices you")
            print("make today will echo through the ages, affecting not just this generation,")
            print("but all those that follow.")
            print()
            print("Your first decision as Ocean Guardian will set the tone for your entire")
            print("guardianship. Choose wisely...")
            print()
            
            # Show initial stats for first generation
        print("\n" + "-" * 80)
        print("CURRENT STATE OF PLANET AQUA:")
        print("-" * 80)
        self.print_stats()
        
    
    def get_era_for_generation(self, generation: int) -> str:
        """Determine the era based on generation number."""
        if generation < 5:
            return "early"
        elif generation < 10:
            return "discovery"
        elif generation < 20:
            return "awakening"
        elif generation < 25:
            return "transformation"
        else:
            return "late"
    
    def print_lore_drop(self, era: str) -> None:
        """Print a random lore drop for the current era."""
        # Filter lore drops by era
        era_lore = [lore for lore in self.lore_drops if lore['era'] == era]
        
        if not era_lore:
            return
        
        # Weighted random selection
        weighted_lore = []
        for lore in era_lore:
            weighted_lore.extend([lore] * lore['weight'])
        
        if weighted_lore:
            selected_lore = random.choice(weighted_lore)
            print(f"\n📰 {selected_lore['title']}")
            print(f"{selected_lore['content']}")
            print()
    
    def print_generation_report(self, generation: int) -> None:
        """Print a detailed report on what happened during the previous generation."""
        print("\n" + "~" * 80)
        print("GENERATION REPORT - WHAT HAPPENED DURING THE LAST 5 YEARS")
        print("~" * 80)
        
        # Report on events that occurred
        if self.state.last_event:
            print(f"\n📰 MAJOR EVENT: {self.state.last_event}")
            if self.state.last_event_choice != "Automatic Event":
                print(f"   The Ocean Guardian chose: {self.state.last_event_choice}")
            print("   This event had significant consequences for the floating cities...")
            print()
        
        if self.state.last_action:
            print(f"\n📋 DECREE ENACTED: {self.state.last_action}")
            print("The previous Ocean Guardian issued this decree at the beginning of their term.")
            print("Over the past 5 years, the effects of this decision have become clear...")
            
            # Show actual consequences if available
            if self.state.last_action_consequences:
                print("\n📊 CONSEQUENCES OF THE DECREE:")
                consequences = self.state.last_action_consequences
                if consequences.get("money", 0) != 0:
                    print(f"   💰 Treasury: {consequences['money']:+d}")
                if consequences.get("ocean_toxicity", 0) != 0:
                    print(f"   ☠️ Ocean Toxicity: {consequences['ocean_toxicity']:+d}%")
                if consequences.get("fish_health", 0) != 0:
                    print(f"   🐟 Marine Life: {consequences['fish_health']:+d}%")
                if consequences.get("support", 0) != 0:
                    print(f"   👥 Public Trust: {consequences['support']:+d}%")
                if consequences.get("yearly_income", 0) != 0:
                    print(f"   💵 Yearly Income: {consequences['yearly_income']:+d}")
                if consequences.get("pollution_growth", 0) != 0:
                    print(f"   📈 Pollution Growth Rate: {consequences['pollution_growth']:+.2f}")
            print()
            
            # Generate contextual report based on the action
            if "Ban Single-Use Plastic Bags" in self.state.last_action:
                print("🌊 The plastic bag ban has been implemented across all floating settlements.")
                print("   Citizens initially grumbled about bringing their own containers, but")
                print("   they've adapted well. The reduction in plastic waste is visible")
                print("   in the cleaner currents around the cities.")
                
            elif "Community Beach Cleanup" in self.state.last_action:
                print("🧹 Community cleanup efforts have mobilized thousands of citizens.")
                print("   The beaches are noticeably cleaner, and the initiative has")
                print("   brought communities together in shared purpose.")
                
            elif "River Interceptor" in self.state.last_action:
                print("🚧 The river interceptors have been deployed and are working effectively.")
                print("   They're catching significant amounts of plastic before it reaches")
                print("   the open ocean, though maintenance costs are ongoing.")
                
            elif "Public Awareness Campaign" in self.state.last_action:
                print("📢 The awareness campaign has educated citizens about plastic pollution.")
                print("   Public understanding of the issue has increased, and many")
                print("   are now making more conscious choices about their consumption.")
                
            elif "Emergency Ocean Cleanup" in self.state.last_action:
                print("🚢 Emergency cleanup vessels have removed tons of plastic debris.")
                print("   The immediate visual impact is significant, though the")
                print("   underlying problem of ongoing pollution remains.")
                
            elif "Extended Producer Responsibility" in self.state.last_action:
                print("🏭 Manufacturers are now responsible for their plastic waste.")
                print("   This has forced many companies to redesign their products")
                print("   for better recyclability and reduced packaging.")
                
            elif "Waste Management Upgrade" in self.state.last_action:
                print("♻️ New recycling and waste collection infrastructure is operational.")
                print("   The system is more efficient at processing and containing")
                print("   waste before it can escape into the ocean.")
                
            elif "Biodegradable Plastics" in self.state.last_action:
                print("🔬 Research into biodegradable plastics has yielded promising results.")
                print("   New materials are being tested that truly break down")
                print("   in ocean conditions, offering hope for the future.")
                
            elif "Global Plastic Treaty" in self.state.last_action:
                print("🌍 The international treaty has been signed and is being implemented.")
                print("   Nations are working together to reduce plastic production")
                print("   and pollution on a global scale.")
                
            elif "Circular Economy" in self.state.last_action:
                print("🔄 The circular economy initiative is transforming how products are designed.")
                print("   Items are now built to last longer and be easily repaired,")
                print("   reducing the need for constant replacement.")
                
            elif "Heavy Ocean Cleanup" in self.state.last_action:
                print("🚢 Heavy cleanup operations have been deployed across the ocean.")
                print("   Massive amounts of plastic debris have been removed, but")
                print("   the operations are expensive and may have disturbed some ecosystems.")
                
            elif "Subsidize Fishing Industry" in self.state.last_action:
                print("💰 Fishing industry subsidies have boosted the economy significantly.")
                print("   However, increased fishing activity has led to more gear pollution")
                print("   and some environmental concerns among the citizens.")
                
            elif "Build Waste Incineration" in self.state.last_action:
                print("🔥 Waste incineration plants have been built to burn plastic waste.")
                print("   This reduces ocean pollution but creates air quality concerns")
                print("   and some citizens are worried about the health effects.")
                
            elif "Ban Plastic Waste Exports" in self.state.last_action:
                print("🚫 The ban on plastic waste exports has been implemented.")
                print("   This prevents other countries from dumping their waste in our waters,")
                print("   but it also means we must handle all our own waste locally.")
                
            elif "Behavioral Nudge Campaign" in self.state.last_action:
                print("📢 Subtle behavioral nudges have been implemented across the cities.")
                print("   Citizens are being gently encouraged to make better choices,")
                print("   though the effects are modest without stronger structural support.")
                
            elif "Expand Fishing Fleet" in self.state.last_action:
                print("🚢 The fishing fleet has been significantly expanded.")
                print("   This brings immediate economic benefits but increases")
                print("   the risk of overfishing and gear pollution in the long term.")
                
            elif "Surface Cleanup Operations" in self.state.last_action:
                print("🧹 Surface cleanup operations have been deployed across the ocean.")
                print("   The visible pollution has been removed, improving the ocean's")
                print("   appearance, but the underlying sources of pollution remain.")
                
            elif "Recycling-Only Strategy" in self.state.last_action:
                print("♻️ A recycling-focused approach has been implemented.")
                print("   While recycling infrastructure has improved, this strategy")
                print("   doesn't address the need to reduce overall plastic production.")
                
            elif "Promote False Biodegradables" in self.state.last_action:
                print("⚠️ So-called 'biodegradable' plastics have been promoted.")
                print("   Unfortunately, these materials don't actually degrade in ocean")
                print("   conditions, leading to false environmental claims and continued pollution.")
                
            elif "Impose Fishing Quotas" in self.state.last_action:
                print("🎣 Fishing quotas have been implemented to protect fish populations.")
                print("   The ocean is showing signs of recovery, but the fishing industry")
                print("   is angry about the restrictions and public support has suffered.")
                
            elif "Emergency Ocean Tax" in self.state.last_action:
                print("💰 Heavy taxes have been imposed on polluting industries.")
                print("   This has generated significant revenue for the treasury, but")
                print("   businesses are struggling and public support has declined.")
                
            elif "Implement Austerity" in self.state.last_action:
                print("✂️ Austerity measures have been implemented to cut government spending.")
                print("   Money has been saved and yearly income increased, but public")
                print("   services have been cut and support has dropped significantly.")
                
            elif "Corporate Bailout" in self.state.last_action:
                print("🏢 Struggling industries have been bailed out with public money.")
                print("   Jobs have been preserved and public support maintained, but")
                print("   the treasury has been significantly depleted.")
                
            elif "Deploy Ocean Plastic Collectors" in self.state.last_action:
                print("🤖 Autonomous plastic collectors have been deployed across the ocean surface.")
                print("   These floating devices continuously remove plastic debris, providing")
                print("   a steady reduction in ocean toxicity while requiring minimal maintenance.")
                
            elif "Install Microplastic Filters" in self.state.last_action:
                print("🔬 Advanced microplastic filtration systems have been installed.")
                print("   Water treatment plants now catch tiny plastic particles before")
                print("   they reach the ocean, significantly reducing microplastic pollution.")
                
            elif "Deploy Ocean Restoration Technology" in self.state.last_action:
                print("🔬 Cutting-edge bioremediation technology has been deployed across the ocean.")
                print("   Advanced cleanup systems work continuously to restore ocean health,")
                print("   though the technology requires ongoing maintenance and support.")
                
            elif "Release Plastic-Eating Bacteria" in self.state.last_action:
                print("🧬 Genetically modified plastic-eating bacteria have been released.")
                print("   These microscopic organisms consume plastic waste, dramatically")
                print("   reducing ocean toxicity, though some citizens are concerned about")
                print("   the long-term ecological implications.")
                
            elif "Eastern Cities Production Agreement" in self.state.last_action:
                print("🌏 An agreement has been reached with eastern floating cities.")
                print("   They have committed to reducing their massive synthetic material")
                print("   production, which will significantly slow global pollution growth.")
                
            elif "Western Cities Waste Reform" in self.state.last_action:
                print("🌊 Western floating cities have reformed their waste management systems.")
                print("   Their excessive consumption patterns are being addressed through")
                print("   better infrastructure and citizen education programs.")
                
            elif "Southern Regions Infrastructure" in self.state.last_action:
                print("🏗️ Waste management infrastructure has been built in southern regions.")
                print("   These areas previously had high rates of mismanaged waste, but")
                print("   new systems are now properly containing and processing materials.")
                
            elif "Enforce Manufacturing Standards" in self.state.last_action:
                print("🏭 New manufacturing standards have been enforced across all producers.")
                print("   Synthetic material manufacturers must now use ocean-safe designs,")
                print("   which prevents pollution at its source but increases production costs.")
                
            elif "Habitat Restoration Project" in self.state.last_action:
                print("🐠 Marine habitat restoration projects have been launched.")
                print("   Damaged ecosystems are being rebuilt to support fish populations,")
                print("   creating healthier and more resilient ocean environments.")
                
            elif "Create Marine Protected Areas" in self.state.last_action:
                print("🛡️ Marine protected areas have been established across the ocean.")
                print("   These zones restrict fishing activities, allowing ecosystems")
                print("   to recover and fish populations to rebuild naturally.")
                
            else:
                print("📜 The previous generation's decree has had various effects on the world.")
                print("   The full impact of their decision continues to unfold.")
        else:
            print("📜 The previous generation chose to maintain the status quo.")
            print("   No major decrees were issued, and the world continued")
            print("   along its current trajectory.")
        
        print()
    
    def handle_generation_transition(self, generation: int) -> None:
        """Handle the transition to a new generation."""
        print("\n" + "=" * 80)
        print("🔄 GENERATION TRANSITION")
        print("=" * 80)
        print()
        print("The time has come for the current generation to pass into the depths.")
        print("Their 5 years of service complete, they return to the ocean's embrace.")
        print()
        print("A new generation rises from the currents, eager to continue the work")
        print("of their predecessors. The Council of Depths has chosen a new Ocean")
        print("Guardian from among the young fish-people.")
        print()
        print("The diary is passed to the new guardian, who reads the entries of")
        print("those who came before, learning from their successes and failures.")
        print()
        print("The cycle continues...")
        print()
        input("Press Enter to begin the new generation...")
    
    def process_generation(self, generation: int) -> None:
        """Process 5 years of events and decisions for a generation."""
        print(f"\n🌊 PROCESSING 5 YEARS OF EVENTS...")
        print("-" * 40)
        
        # Process one random event for the entire generation
        available_events = self.systems.get_available_events(self.events, self.state.year)
        if available_events:
            event = random.choice(available_events)
            
            if event.event_type == "interactive":
                    self.handle_interactive_event(event)
                else:
                print(f"\n📰 Generation Event: {event.name}")
                    print(f"{event.text}")
                
                # Track the event for reporting
                self.state.last_event = event.name
                self.state.last_event_choice = "Automatic Event"
                
                    self.systems.apply_effects(self.state, {
                        "money": event.effect_money,
                    "ocean_toxicity": event.effect_ocean_toxicity,
                        "fish_health": event.effect_fish,
                        "support": event.effect_support,
                        "pollution_growth": event.effect_pollution_growth
                    })
                print(f"Consequences: Treasury {event.effect_money:+d}, Ocean Toxicity {event.effect_ocean_toxicity:+d}, Marine Life {event.effect_fish:+d}, Public Trust {event.effect_support:+d}")
        else:
            print("The 5 years pass quietly, with no major events to report.")
        
        # Apply 5 years of yearly drift
        for year in range(self.config["generation_length"]):
            old_fish_health = self.state.fish_health
            old_money = self.state.money
            
            self.systems.apply_yearly_drift(self.state)
            self.state.year += 1
            
            # Show income impact from fish health changes
            income_change = self.state.money - old_money
            fish_change = self.state.fish_health - old_fish_health
            
            if fish_change < -10:
                print(f"📊 Year {self.state.year} Stats: Ocean Toxicity {self.state.ocean_toxicity}%, Fish Health {self.state.fish_health}% (-{abs(fish_change)}), Support {self.state.public_support}%, Money ${self.state.money} (+${income_change})")
                print(f"   🌊 The ocean's suffering is felt throughout our society - fewer fish means less income for all.")
            elif fish_change > 5:
                print(f"📊 Year {self.state.year} Stats: Ocean Toxicity {self.state.ocean_toxicity}%, Fish Health {self.state.fish_health}% (+{fish_change}), Support {self.state.public_support}%, Money ${self.state.money} (+${income_change})")
                print(f"   🌊 Mother ocean's recovery brings prosperity to our floating cities.")
            else:
                print(f"📊 Year {self.state.year} Stats: Ocean Toxicity {self.state.ocean_toxicity}%, Fish Health {self.state.fish_health}%, Support {self.state.public_support}%, Money ${self.state.money} (+${income_change})")
        
        # Get and display available actions for the generation
        available_actions = self.systems.get_available_actions(self.actions, self.state)
        if not available_actions:
            print("\n⚠️ No decrees can be issued during this generation.")
            input("Press Enter to continue...")
        else:
            print(f"\n⚔️ GUARDIAN'S DECISIONS FOR THIS GENERATION:")
            for i, action in enumerate(available_actions, 1):
                cost_str = f" (Cost: ${action.cost})" if action.cost > 0 else " (Free)"
                print(f"{i}. {action.name}{cost_str}")
            print(f"{len(available_actions) + 1}. Focus on maintaining the status quo")
            
            # Get player choice
            while True:
                try:
                    choice = input(f"\nChoose action (1-{len(available_actions) + 1}): ").strip()
                    choice_num = int(choice)
                    
                    if choice_num == len(available_actions) + 1:
                        print("You choose to maintain the status quo for this generation...")
                        break
                    elif 1 <= choice_num <= len(available_actions):
                        action = available_actions[choice_num - 1]
                        
                        # Apply action effects
                        self.state.money -= action.cost
                        self.systems.apply_effects(self.state, {
                            "money": action.effect_money,
                            "ocean_toxicity": action.effect_ocean_toxicity,
                            "fish_health": action.effect_fish,
                            "support": action.effect_support,
                            "pollution_growth": action.effect_pollution_growth,
                            "yearly_income": action.effect_yearly_income
                        })
                        
                        # Track the action taken and mark as used
                        self.state.last_action = action.name
                        self.state.used_actions.add(action.id)
                        
                        print(f"\n✅ Decree enacted: {action.name}")
                        print(f"Consequences: Treasury {action.effect_money:+d}, Ocean Toxicity {action.effect_ocean_toxicity:+d}, Marine Life {action.effect_fish:+d}, Public Trust {action.effect_support:+d}")
                        
                        # Store detailed consequences for next generation report
                        self.state.last_action_consequences = {
                            "money": action.effect_money,
                            "ocean_toxicity": action.effect_ocean_toxicity,
                            "fish_health": action.effect_fish,
                            "support": action.effect_support,
                            "pollution_growth": action.effect_pollution_growth,
                            "yearly_income": action.effect_yearly_income
                        }
                        break
                    else:
                        print("Invalid choice. Please try again.")
                except ValueError:
                    print("Please enter a valid number.")
    
    def play(self) -> None:
        """Main game loop."""
        print("🌊 Welcome to Planet Aqua - Stop the Trash Tide!")
        print("=" * 80)
        print("📖 THE OCEAN GUARDIAN'S DIARY")
        print("=" * 80)
        print()
        print("You have been chosen by the Council of Depths to serve as Ocean Guardian.")
        print("Each generation of fish-people lives for 5 years, and you must guide")
        print("Planet Aqua through 30 generations of challenges.")
        print()
        print("This diary chronicles your decisions and their consequences across")
        print("the ages. Each entry represents 5 years of your guardianship.")
        print()
        print("The fate of an entire world rests in your hands...")
        print()
        input("Press Enter to begin your guardianship...")
        
        generation = 0
        while True:
            # Check if we need to transition to a new generation
            if self.state.year % self.config["generation_length"] == 0 and generation > 0:
                self.handle_generation_transition(generation)
            
            # Print diary entry header
            self.print_diary_entry(generation)
            
            # Check for endings
            ending = self.systems.check_endings(self.state)
            if ending:
                print(self.systems.get_ending_narrative(ending))
                break
            
            # Process 5 years of events and decisions
            self.process_generation(generation)
            
            generation += 1
            
            # Check for endings after generation
            ending = self.systems.check_endings(self.state)
            if ending:
                print(self.systems.get_ending_narrative(ending))
                break
            
            input(f"\nPress Enter to continue to the next generation...")

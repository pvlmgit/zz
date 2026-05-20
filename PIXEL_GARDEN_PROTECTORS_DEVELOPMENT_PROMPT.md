# PIXEL GARDEN PROTECTORS - COMPLETE GAME DEVELOPMENT PROMPT

## PROJECT OVERVIEW
Create a **2D pixel art shooting game** with farming/strategy mechanics. The game blends **cute aesthetic** with **cool combat**, featuring a gardener protecting an enchanted garden from creepy-cute pests across 4 seasons.

**Target Platform:** Web-based (HTML5/Canvas or Phaser.js), Desktop (Electron), Mobile (React Native optional)
**Genre:** Action-Shooting + Tower Defense + Farming Sim Hybrid
**Target Audience:** Ages 10+, Casual to Hardcore Gamers
**Art Style:** Pixel Art (16x16 to 32x32 grid), Pastel + Neon color palette
**Tone:** Whimsical yet slightly eerie, cozy but action-packed

---

## TECHNICAL ARCHITECTURE

### Core Engine & Framework
- **Game Engine:** Phaser.js 3.x (or Godot 4.x alternative)
- **Language:** JavaScript (Web) or GDScript (Godot)
- **Graphics:** Canvas 2D or WebGL rendering
- **Audio:** Web Audio API or Howler.js
- **State Management:** Game scenes (Menu → Seasonal Intro → Planting Phase → Combat Phase → Boss Phase → Results)
- **Resolution:** 1280x720px (16:9 aspect ratio), pixel-perfect rendering
- **Frame Rate:** 60 FPS

### File Structure
```
pixel-garden-protectors/
├── src/
│   ├── main.js                    # Entry point
│   ├── config.js                  # Game config (resolution, physics, etc)
│   ├── scenes/
│   │   ├── BootScene.js           # Asset loading
│   │   ├── MenuScene.js           # Main menu & season select
│   │   ├── SeasonalIntroScene.js  # Season intro animation
│   │   ├── PlantingPhaseScene.js  # Garden grid, planting mechanics
│   │   ├── CombatPhaseScene.js    # Wave-based shooting combat
│   │   ├── BossPhaseScene.js      # Boss battle logic
│   │   ├── ResultsScene.js        # Wave/Season results
│   │   ├── GameOverScene.js       # Game end screen
│   │   └── PauseScene.js          # Pause overlay
│   ├── sprites/
│   │   ├── Player.js              # Gardener character class
│   │   ├── Enemy.js               # Base enemy class
│   │   ├── Companion.js           # Ally creature class
│   │   ├── Projectile.js          # Bullet/seed class
│   │   ├── Plant.js               # Planted garden class
│   │   ├── Boss.js                # Boss enemy subclass
│   │   └── Particle.js            # Effects & visual feedback
│   ├── managers/
│   │   ├── GameManager.js         # Game state, progression, seasons
│   │   ├── WaveManager.js         # Enemy spawning, difficulty scaling
│   │   ├── ResourceManager.js     # Seeds, water, harvested crops
│   │   ├── CompanionManager.js    # Companion selection & leveling
│   │   ├── SoundManager.js        # Audio playback
│   │   └── UIManager.js           # HUD, menus, dialogs
│   ├── systems/
│   │   ├── CombatSystem.js        # Damage, collision, hit detection
│   │   ├── PlantingSystem.js      # Grid placement, growth mechanics
│   │   ├── WeaponSystem.js        # Weapon stats, switching, upgrades
│   │   ├── ComboSystem.js         # Combo counter, multiplier logic
│   │   ├── UpgradeSystem.js       # Unlocks, perks, meta-progression
│   │   └── SaveSystem.js          # Local storage, progression saves
│   ├── utils/
│   │   ├── constants.js           # Game constants (sizes, speeds, damage)
│   │   ├── helpers.js             # Utility functions
│   │   ├── math.js                # Physics, collision, pathfinding
│   │   └── animations.js          # Tween definitions, sprite animations
│   └── assets/
│       ├── images/
│       │   ├── sprites/
│       │   │   ├── player/
│       │   │   ├── enemies/
│       │   │   ├── companions/
│       │   │   ├── plants/
│       │   │   ├── weapons/
│       │   │   ├── projectiles/
│       │   │   ├── bosses/
│       │   │   ├── particles/
│       │   │   ├── ui/
│       │   │   └── tiles/
│       │   └── backgrounds/
│       │       ├── spring/
│       │       ├── summer/
│       │       ├── fall/
│       │       └── winter/
│       ├── audio/
│       │   ├── music/
│       │   │   ├── spring_theme.ogg
│       │   │   ├── summer_theme.ogg
│       │   │   ├── fall_theme.ogg
│       │   │   ├── winter_theme.ogg
│       │   │   ├── boss_battle.ogg
│       │   │   └── menu.ogg
│       │   └── sfx/
│       │       ├── shoot.wav
│       │       ├── hit.wav
│       │       ├── plant.wav
│       │       ├── harvest.wav
│       │       ├── companion_attack.wav
│       │       ├── combo_hit.wav
│       │       ├── level_up.wav
│       │       ├── boss_spawn.wav
│       │       ├── boss_hurt.wav
│       │       ├── defeat.wav
│       │       └── victory.wav
│       └── fonts/
│           ├── pixelated-main.ttf
│           └── pixelated-bold.ttf
├── index.html                     # Main HTML entry
├── style.css                      # Global styles
├── package.json                   # Dependencies
└── README.md                      # Documentation

```

---

## GAME MECHANICS DETAILED

### 1. PLANTING PHASE (30-45 seconds)
**What Happens:**
- Player sees 8x6 grid of tilled soil (120-180 pixels per tile)
- Click empty soil to plant from available crops
- Each crop costs resources (seeds, water drops)
- Planted crops show growth animation (seed → sprout → grown)
- Harvest mature crops before wave starts

**Crops (10 Types, Growing Complexity):**
1. **Carrot** - Basic defense, blocks movement
2. **Sunflower** - Medium height, decorative wall
3. **Rose** - Thorny, damages enemies on contact
4. **Corn** - Tall cover, can be shot to trigger area damage
5. **Pumpkin** - Large, very sturdy, slow growth
6. **Vine** - Can be interacted with to swing as weapon
7. **Bamboo** - Tall, fast growth, creates corridor walls
8. **Poppy** - Blooms with stun effect (emits pollen)
9. **Nightshade** - Toxic, poisons touching enemies
10. **Moonflower** - Rare, glows in dark, heals player

**Mechanics:**
- Each crop has: Cost (seeds/water), Growth Time (3-8 seconds), Harvest Value (2-5 resources)
- Grid placement matters: Adjacent crops provide bonuses (synergies)
- Harvesting creates temporary speed boost (combo multiplier increases)
- Right-click to remove/replant crops
- Visual feedback: Soil particles when planting, glow when ready to harvest

---

### 2. COMBAT PHASE (60-90 seconds per wave)
**What Happens:**
- Background changes to combat mode (darker vignette)
- Enemies spawn in waves from screen edges
- Player switches to shooting stance with crosshair
- Combat ends when all waves defeated or player loses all lives
- Lives system: 3 lives (lose one per hit), health bar shows damage

**Player (Gardener) Stats:**
- Movement Speed: 120 pixels/second
- Rotation Speed: 8 radians/second
- Health: 100 (displays as visual heart meter)
- Lives: 3
- Starting Weapon: Seed Gun
- Equipped Companion Slot: 1/3 available

**Controls:**
- WASD or Arrow Keys: Move gardener
- Mouse: Aim (crosshair follows mouse)
- Left Click / Space: Shoot
- Number Keys (1-3): Switch weapons
- Q: Activate companion ability (cooldown: 8-15 seconds)
- E: Interact (harvest plants during combat)

**Weapon System (5 Weapon Types):**

**1. Seed Gun (Starting)**
- Fire Rate: 6 seeds/second
- Damage: 8 per seed
- Spread: 0° (straight)
- Magazine: Infinite (no reload)
- Special: Bounces off walls (max 2 bounces)
- Sound: Soft "plink" sound

**2. Thorn Spray**
- Fire Rate: 2 sprays/second
- Damage: 12 per thorn (3 thorns per spray)
- Spread: 20° cone
- Magazine: 20 shots before cooldown
- Special: Thorns stick to enemies for 1 second damage-over-time
- Sound: "Whoosh" spray sound

**3. Vine Whip**
- Fire Rate: 1 whip/0.8 seconds
- Damage: 25 (melee range, 60px)
- Spread: N/A (melee)
- Special: Can grab and pull weak enemies closer, swing to hit multiple
- Magazine: No limit (cooldown-based)
- Sound: "Crack" whip sound, satisfying impact

**4. Pollen Burst**
- Fire Rate: 0.3 bursts/second (slow, powerful)
- Damage: 40 area damage (radius: 80px)
- Spread: 360° explosion
- Magazine: 8 shots before cooldown (3 second reload)
- Special: Stuns enemies for 1 second, affects all in radius
- Sound: "Pop" explosion sound

**5. Sunbeam (Unlocked at Season 2)**
- Fire Rate: 0.5 beams/second (charge required)
- Damage: 60 per beam (starts at 30, charges up)
- Spread: 0° (laser-like)
- Magazine: Cooldown (4 seconds between shots)
- Special: Pierces through enemies, charges for extra damage
- Sound: Charging hum, then laser zap

**Weapon Switching:** Instant swap, 0.2 second animation
**Weapon Upgrades:** From seasonal loot boxes (faster fire rate, more damage, larger spread, extended range)

---

### 3. ENEMY SYSTEM

**Base Enemy Class:**
```
Enemy {
  - name (string)
  - sprite (image reference)
  - maxHealth (number)
  - currentHealth (number)
  - damage (number)
  - speed (number, pixels/second)
  - size (width, height in pixels)
  - color (primary, secondary for variety)
  - behaviors (chase, patrol, spiral attack)
  - loot (seeds, water, combo points)
  - animationSpeed (number)
}
```

**SPRING ENEMIES (Weak, Fast, Many)**

1. **Ant Worker** 
   - Health: 15 | Speed: 100 | Damage: 5 | Size: 16x16
   - Behavior: Linear dash attacks, 3 ants per swarm
   - Loot: 1 seed, 0.1 water
   - Color: Red body, black segments

2. **Gnat Swarm**
   - Health: 8 | Speed: 140 | Damage: 3 | Size: 12x12
   - Behavior: Circular flight pattern, flies in formation
   - Loot: 0.5 seed, 0.05 water
   - Color: Gray, blue-tinted wings

3. **Pill Bug**
   - Health: 20 | Speed: 60 | Damage: 8 | Size: 20x16
   - Behavior: Slow roll, curls into ball when hit (temporary armor)
   - Loot: 2 seeds, 0.15 water
   - Color: Purple segments, brown shell

4. **Aphid Cluster** (Boss of Spring)
   - Health: 100 | Speed: 80 | Damage: 12 | Size: 48x48
   - Behavior: Spawns 5 smaller aphids per 20 seconds, regenerates if not hit for 3 seconds
   - Loot: 10 seeds, 2 water, 1 unlock token
   - Color: Green body with pink spots, white spots indicate weak points

---

**SUMMER ENEMIES (Aggressive, Armored, Swarming)**

1. **Beetle Armor**
   - Health: 35 | Speed: 90 | Damage: 10 | Size: 24x24
   - Behavior: Charge attack every 3 seconds, dash forward 200px
   - Loot: 3 seeds, 0.2 water
   - Color: Shiny red carapace, gold accents
   - Weakness: Explosion/AoE damage (takes 2x from Pollen Burst)

2. **Wasp Striker**
   - Health: 25 | Speed: 130 | Damage: 15 | Size: 20x20
   - Behavior: Divebomb from top, quick stinger jabs
   - Loot: 2 seeds, 0.25 water
   - Color: Yellow and black stripes, translucent wings

3. **Grasshopper Jumper**
   - Health: 30 | Speed: 110 (jump-based) | Damage: 12 | Size: 22x28
   - Behavior: Hops in arcs, unpredictable landing spots
   - Loot: 3 seeds, 0.3 water
   - Color: Lime green, orange underside

4. **Queen Wasp** (Boss of Summer)
   - Health: 150 | Speed: 100 | Damage: 20 | Size: 64x64
   - Behavior: Hovers, summons 8 wasp soldiers, has 2 attack phases (fast swoop, then stinger strikes)
   - Loot: 15 seeds, 3 water, 1 unlock token, Queen's Crown item
   - Color: Gold and burgundy body, translucent wings with magical shimmer

---

**FALL ENEMIES (Armored, Heavy, Tanky)**

1. **Stag Beetle**
   - Health: 60 | Speed: 70 | Damage: 18 | Size: 28x32
   - Behavior: Slow methodical advance, horn bash attack
   - Loot: 4 seeds, 0.4 water
   - Color: Dark brown carapace, bronze horns
   - Weakness: Piercing weapons do 1.5x damage (Vine Whip, Sunbeam)

2. **Cicada Armor**
   - Health: 55 | Speed: 85 | Damage: 16 | Size: 26x30
   - Behavior: Invisible phases (become transparent, harder to hit), then visible attack
   - Loot: 3 seeds, 0.35 water
   - Color: Brown with iridescent wings

3. **Mantis Predator**
   - Health: 50 | Speed: 95 | Damage: 20 | Size: 30x40
   - Behavior: Methodical advance, slashing attacks with long reach (80px)
   - Loot: 5 seeds, 0.3 water
   - Color: Dark green body, pink inner arms

4. **Goliath Beetle** (Boss of Fall)
   - Health: 200 | Speed: 60 | Damage: 25 | Size: 80x80
   - Behavior: Charging attacks, ground slam (creates shockwave), spawns beetle minions
   - Loot: 20 seeds, 4 water, 1 unlock token, Goliath Shell armor (cosmetic)
   - Color: Glossy black with gold reinforcements, red undertone

---

**WINTER ENEMIES (Rare, Magical, Slow)**

1. **Frost Moth**
   - Health: 40 | Speed: 75 (slowed by environment) | Damage: 14 | Size: 24x28
   - Behavior: Drifts slowly, leaves ice trail that slows player
   - Loot: 5 seeds, 0.5 water, rare glow effect
   - Color: Icy blue body, crystalline wings

2. **Snow Beetle**
   - Health: 45 | Speed: 65 | Damage: 16 | Size: 26x26
   - Behavior: Burrowing (underground for 2 seconds), surprise attacks
   - Loot: 4 seeds, 0.45 water
   - Color: White shell, blue undertone, crystalline texture

3. **Glacial Spider**
   - Health: 50 | Speed: 80 | Damage: 18 | Size: 32x32
   - Behavior: Web-spinning (creates slow zones), fast lateral movement
   - Loot: 6 seeds, 0.4 water
   - Color: Ice white, silver markings

4. **Eternal Caterpillar** (Boss of Winter / Final Boss)
   - Health: 250 | Speed: 70 | Damage: 22 | Size: 100x40 (segmented)
   - Behavior: Multi-phase boss with 5 segments, each can be targeted separately; regenerates segments if not destroyed in order; final form transforms to butterfly
   - Loot: 30 seeds, 5 water, 1 unlock token, Crown of Seasons (final cosmetic reward)
   - Color: Gradient from icy blue to deep purple, crystalline segments

---

### 4. COMPANION SYSTEM (5 Creatures)

**Companion Base Class:**
```
Companion {
  - name (string)
  - icon (image)
  - rarity (common, rare, epic)
  - level (1-50)
  - experience (current XP)
  - maxHealth (number)
  - damage (number)
  - attackSpeed (number)
  - specialAbility (function)
  - abilityCooldown (number)
  - attackRange (number)
  - synergies (array of weapon types for bonus)
  - unlockCondition (season/boss requirement)
}
```

**1. Hedgehog (Starter)**
- Rarity: Common
- Ability: "Curled Defense" - Creates protective barrier (30px radius, reduces player damage by 50% for 4 seconds)
- Cooldown: 12 seconds
- Synergy: Bonus with Thorn Spray (+20% damage)
- Attack: Rolls at enemies, deals 12 damage per hit
- Health: 40
- Speed: 100 px/s
- Personality: Slow, adorable waddle; curls into ball animation
- Unlock: Available from start

**2. Ladybug (Spring Boss Reward)**
- Rarity: Rare
- Ability: "Blessing of Spots" - Marks all enemies for 6 seconds; marked enemies take 25% extra damage
- Cooldown: 10 seconds
- Synergy: Bonus with Seed Gun (+15% fire rate)
- Attack: Flies in circles, stings enemies for 15 damage
- Health: 35
- Speed: 140 px/s
- Personality: Bouncy flight, cheerful chirping sounds
- Unlock: Defeat Aphid Cluster (Spring Boss)

**3. Butterfly (Summer Boss Reward)**
- Rarity: Epic
- Ability: "Pollen Vortex" - Creates spinning wind that damages all enemies in 60px radius for 3 seconds (20 damage/second)
- Cooldown: 15 seconds
- Synergy: Bonus with Pollen Burst (+30% area size)
- Attack: Dash attacks, 18 damage per collision
- Health: 45
- Speed: 160 px/s
- Personality: Graceful, colorful wings change based on season; trail of sparkles
- Unlock: Defeat Queen Wasp (Summer Boss)

**4. Owl (Fall Boss Reward)**
- Rarity: Epic
- Ability: "Night Vision" - Grants player increased sight range and reveals all enemies for 8 seconds; owl dives at enemies for massive damage (35 damage)
- Cooldown: 18 seconds
- Synergy: Bonus with Vine Whip (+25% range)
- Attack: Talons slash for 20 damage, ranged screech attack (50px range)
- Health: 50
- Speed: 130 px/s
- Personality: Wise, blinking eyes; silent flight until ability triggers
- Unlock: Defeat Goliath Beetle (Fall Boss)

**5. Snow Fox (Winter Boss Reward)**
- Rarity: Legendary
- Ability: "Frozen Time" - Slows all enemies to 30% speed for 5 seconds; fox can still move at full speed
- Cooldown: 20 seconds
- Synergy: Bonus with Sunbeam (+40% damage)
- Attack: Swift dashes, leaves ice trails, 22 damage per hit
- Health: 55
- Speed: 150 px/s
- Personality: Mischievous, playful pounce; blue glowing eyes; rare aurora animation
- Unlock: Defeat Eternal Caterpillar (Winter Boss)

**Companion Leveling:**
- Gain XP from combat (10 XP per enemy killed)
- Level cap: 50
- Each level: +2 damage, +1 health, cooldown reduced by 0.2 seconds
- Every 5 levels: Unlock cosmetic skin variant

---

### 5. COMBO & SCORING SYSTEM

**Combo Counter:**
- Increases by 1 for each enemy killed within 2 seconds of last kill
- Resets to 0 if 3+ seconds pass without a kill
- Visual: Combo counter floats above player, color changes (yellow at 5x, red at 10x, purple at 20x+)

**Combo Multiplier:**
- 1-5 kills: 1.0x multiplier (no bonus)
- 6-10 kills: 1.25x multiplier (25% bonus to points & resources)
- 11-20 kills: 1.5x multiplier (50% bonus)
- 21-50 kills: 2.0x multiplier (100% bonus, double points)
- 51+ kills: 3.0x multiplier (triple points, visual effects intensify)

**Points System:**
- Each enemy killed = base points (varies by enemy type: 10-50 points)
- Bonus: Combo multiplier × base points
- Bonus: Accuracy bonus (if 80%+ of shots hit, +25%)
- Bonus: Speed kill bonus (kill within 5 seconds of spawn, +50%)
- Bonus: Headshot bonus (hit weak point, +75%)

**Season Score Calculation:**
```
Total Score = (Sum of wave scores) × Season Multiplier + Bonus Points

Where:
- Wave Score = Enemy Points × Combo Multiplier + Accuracy Bonus
- Season Multiplier = 1.0 (Spring) to 4.0 (Winter)
- Bonus Points = Perfect Health Bonus (full health = +500) + Time Bonus (fast clear = +250)
```

**Leaderboard (Local Storage):**
- Top 10 scores per season
- Lifetime high score
- Achievements unlock cosmetics

---

### 6. PROGRESSION & UPGRADES

**Season Structure:**
- 4 Seasons (Spring, Summer, Fall, Winter) = 1 complete playthrough
- Each season has 5 waves + 1 boss fight
- Season lasts ~15-20 minutes
- After Winter, loop back to Spring with increased difficulty

**Difficulty Scaling:**
- Season 1 (Spring): Base difficulty
- Season 2 (Summer): 1.2x enemy health, 1.1x enemy damage, 1.15x spawn rate
- Season 3 (Fall): 1.5x enemy health, 1.3x enemy damage, 1.3x spawn rate
- Season 4 (Winter): 2.0x enemy health, 1.5x enemy damage, 1.5x spawn rate
- New Game+ (2nd loop): 2.5x, 3.0x, 3.5x, 4.0x multipliers respectively

**Unlockable Weapons:**
- Seed Gun: Available from start
- Thorn Spray: Unlock after defeating Spring Boss
- Vine Whip: Unlock after defeating Summer Boss
- Pollen Burst: Unlock after defeating Fall Boss
- Sunbeam: Unlock after defeating Winter Boss

**Unlockable Cosmetics (Skins):**
- Player skins: Garden Witch, Farmer, Plant Druid, Botanist, Guardian of Nature
- Companion color variants: Seasonal themes (golden autumn hedgehog, snowy winter butterfly, etc.)
- Garden themes: Spring meadow, summer paradise, fall harvest, winter wonderland
- Weapon effects: Glowing seeds, crystal thorns, golden vine, starlight pollen, prismatic sunbeam

**Meta-Progression (Permanent Upgrades):**
Unlock from seasonal loot boxes (guaranteed 1 per season, 3 slots to choose from):
- Max Health +5 (stacks, max 5 total upgrades = 125 health)
- Starting Resources +5 seeds / +1 water (stacks)
- Weapon Fire Rate +10% (per weapon, can upgrade all)
- Companion Ability Cooldown -1 second (stacks, max -5 total)
- Plant Growth Speed +15% (stacks)
- Enemy Knockback +20% (stacks)
- Critical Hit Chance +5% (stacks, max 50%)
- Critical Damage +25% (stacks)

---

## ART STYLE SPECIFICATION

### Color Palette

**Primary Palette (Pastel + Neon Harmony):**
```
Pastels:
- Cream:        #FFFACD (backgrounds, soft fills)
- Light Pink:   #FFB6D9 (plant accents, UI highlights)
- Soft Blue:    #A8D8FF (water, secondary objects)
- Mint Green:   #A8FFAB (grass, spring theme)
- Peach:        #FFDAB9 (warm accents, sun)
- Lavender:     #D8B8FF (magical effects, companion auras)

Neons (for effects, UI highlights, damage numbers):
- Hot Pink:     #FF1493 (critical hits, danger)
- Cyan:         #00FFFF (combo indicators, abilities)
- Lime:         #00FF00 (healing, buffs)
- Golden:       #FFD700 (rewards, rare items)
- Purple:       #9D4EDD (rare items, epic)
```

**Seasonal Palette Shifts:**
```
SPRING:
- Background: Light cream with green grass, pastel sky
- Accent: Mint green, light pink flowers
- Enemy tint: Saturated colors (bright red ants, vivid colors)

SUMMER:
- Background: Bright golden yellow sky, vibrant green, warm peach sun
- Accent: Hot pink, cyan water
- Enemy tint: Metallic sheen, more saturated

FALL:
- Background: Orange-brown earth, amber sky, golden leaves
- Accent: Burnt orange, gold, copper
- Enemy tint: Darker browns, metallic golds

WINTER:
- Background: Icy blue, white snow, pale sky
- Accent: Light blue, purple shadows, silver
- Enemy tint: Crystalline, icy blues, translucent whites
```

### Pixel Art Grid & Sprite Sizing

**Baseline Grid:** 16x16 pixels per tile
**Scaling:** 2x or 4x for upscaling (sharp pixel look, no smoothing)

**Sprite Sizes (in 16px tiles):**
- Player (Gardener): 2x2 tiles (32x32px)
- Small enemies (Ant, Gnat): 1x1 tile (16x16px)
- Medium enemies (Beetle, Wasp): 1.5x1.5 tiles (24x24px)
- Large enemies (Mantis, Stag): 2x2 tiles (32x32px)
- Boss enemies: 4x4 to 6x6 tiles (64x64 to 96x96px)
- Companions: 1.5x1.5 tiles (24x24px)
- Plants: 1x2 tiles (16x32px, tall) to 2x2 tiles (32x32px)
- Projectiles: 0.5x0.5 tiles (8x8px) to 1x1 tile (16x16px)

### Character Design Details

#### PLAYER CHARACTER (Gardener)

**Base Design:**
- Round head, large expressive eyes (cute factor)
- Green/brown shirt with gardening patches
- Straw hat with small flower or leaf accent
- Brown pants, green boots
- Holds gun/weapon in right hand, free hand for gestures
- Proportions: Large head (1/3 of body), small limbs (chibi style)

**Animation Frames (per direction: Up, Down, Left, Right):**
1. Idle: 2 frames (breathing animation)
2. Walk: 4 frames (leg movement cycle)
3. Shoot: 2 frames (aim pose, recoil)
4. Hit/Hurt: 1 frame (flinch)
5. Crouch: 2 frames (prepare to dodge)

**Costume Skins:**
1. **Garden Witch** - Purple robes, pointed hat, stars
2. **Farmer** - Overalls, flannel shirt, farmer's hat
3. **Plant Druid** - Leaf armor, natural theme, vines
4. **Botanist** - Lab coat, goggles, scientific tools
5. **Guardian of Nature** - Ethereal, glowing, green aura

#### COMPANION CREATURES

**Hedgehog (Round, Cute, Defensive):**
- Body: Round brown/tan sphere with curved spikes
- Face: Small pink nose, tiny eyes, smile
- Animations: Walk (waddles), Curl (ball form), Attack (roll), Ability (defensive stance)
- Idle animation: Breathing, occasional sniff

**Ladybug (Symmetrical, Cheerful):**
- Body: Red carapace with 5 black spots (classic design)
- Wings: Translucent white, folded on back
- Head: Black with white eyes, happy expression
- Animations: Fly (wing flutter), Land (fold wings), Attack (sting dart), Ability (spin in place with glow)
- Idle animation: Clean antennae, happy bounce

**Butterfly (Graceful, Magical):**
- Body: Thin, elegant, pastel colors (season-dependent)
- Wings: Large, colorful, translucent with patterns
- Detail: Antennae, delicate proportions
- Animations: Fly (wing flutter, drifting), Hover, Attack (dash), Ability (vortex spin)
- Idle animation: Gentle wing flutter, trail of sparkles

**Owl (Wise, Nocturnal):**
- Body: Fluffy, round, gray-brown
- Face: Large round eyes, minimal beak, stern/wise expression
- Wings: Folded at rest, spread when flying
- Animations: Perch (sitting), Glide (diving), Attack (talon strike), Ability (night vision glow)
- Idle animation: Blinking, head tilting, hooting

**Snow Fox (Mischievous, Magical):**
- Body: Lean, fluffy, white/icy blue
- Tail: Large, fluffy, trails particles
- Eyes: Glowing blue, clever expression
- Ears: Pointed, alert
- Animations: Walk/Run (swift), Pounce (jump attack), Dash (speed boost), Ability (time slow aura)
- Idle animation: Playful pounce, tail swish, sparkles around body

---

### BACKGROUND ARTWORK

**Layout:** 1280x720px per background
**Style:** Isometric-ish view (slight angle, not fully top-down)
**Foreground, Midground, Background layers** for parallax scrolling

#### SPRING BACKGROUND
- **Color Scheme:** Mint green grass, pastel blue sky, soft white clouds
- **Elements:** Colorful wildflowers (daisies, tulips), green bushes, wooden fence in distance
- **Ground:** Green grass with lighter patches, small stones
- **Sky:** Gradient from light blue (top) to white (horizon)
- **Details:** Butterflies fluttering, birds in distance, sun with happy rays
- **Garden Grid:** 8x6 semi-transparent squares overlay for planting zones

**Parallax Layers:**
- Layer 1 (Back): Blue sky, distant mountains
- Layer 2 (Mid): Flower field, bushes
- Layer 3 (Front): Ground tile grid, fence posts

#### SUMMER BACKGROUND
- **Color Scheme:** Bright golden sky, vibrant green, warm peach accents
- **Elements:** Tall sunflowers, lush green plants, warm sun dominating the sky
- **Ground:** Rich green grass, some brown dirt patches
- **Sky:** Bright yellow-gold gradient, large warm sun, heat shimmer effect
- **Details:** Bees buzzing, dragonflies, cicada shells on ground, intense lighting
- **Garden Grid:** Same as spring (carries over)

**Parallax Layers:**
- Layer 1 (Back): Golden sky, distant heat shimmer
- Layer 2 (Mid): Sunflower field, green foliage
- Layer 3 (Front): Ground grid, garden boundaries

#### FALL BACKGROUND
- **Color Scheme:** Burnt orange, amber, copper, warm browns
- **Elements:** Orange and yellow fallen leaves, bare tree branches, autumn crops (pumpkins, corn)
- **Ground:** Brown dirt with scattered orange leaves, cracks in soil
- **Sky:** Gradient from warm orange (top) to deeper amber (horizon)
- **Details:** Falling leaves animation (slow, particle-based), bare tree silhouettes, harvest baskets
- **Garden Grid:** Same grid, autumn-colored boundaries

**Parallax Layers:**
- Layer 1 (Back): Amber sky, distant bare trees
- Layer 2 (Mid): Falling leaves, autumn foliage (sparse)
- Layer 3 (Front): Ground with leaves, harvest elements

#### WINTER BACKGROUND
- **Color Scheme:** Icy blue, white, pale purple shadows
- **Elements:** Snow-covered ground, icicle formations, frozen plants, aurora borealis (optional)
- **Ground:** White snow with blue shadows, visible ice patches, snowdrifts
- **Sky:** Pale blue to white gradient, occasional aurora shimmer
- **Details:** Snowflake particles falling, icicles hanging from garden frame, frosty crystals on plants
- **Garden Grid:** Same grid, crystalline outline effect

**Parallax Layers:**
- Layer 1 (Back): Aurora (optional), pale blue sky
- Layer 2 (Mid): Distant snow drifts, frozen landscape
- Layer 3 (Front): Ground with snow, icicles, frozen garden elements

**Background Animation Details:**
- Gentle parallax when player moves (background shifts slightly)
- Ambient particle effects (pollen spring, heat shimmer summer, falling leaves fall, snowflakes winter)
- Dynamic lighting during night phases (if applicable)
- Seasonal music syncs with background tone

---

### UI/HUD DESIGN

#### Main Menu
- **Background:** Seasonal background (currently playing season)
- **Title:** "PIXEL GARDEN PROTECTORS" in large pixel font, glowing effect
- **Buttons:** Play, Continue, Settings, Credits, Quit
- **Button Style:** Pixel-art rounded rectangles, 3D depth effect (shadow + highlight)
- **Font:** Retro pixel font (monospace, bold weight)
- **Accent Colors:** Gold highlights, shadows for depth

#### In-Game HUD (Top-Left Corner)
```
┌─────────────────────┐
│ Wave: 3 / 5         │
│ Lives: ❤️ ❤️ ❤️      │
│ Health: [████░░]    │
│ Combo: 12x          │
│ Score: 1,250 pts    │
└─────────────────────┘
```

**Health Bar:** Green fill, red background, rounded corners
**Combo Counter:** Increases in size/brightness as combo grows
**Score Display:** Gold text, updates in real-time with floating text effects

#### Weapon HUD (Top-Right Corner)
```
┌──────────────────┐
│ Seed Gun    (1)  │
│ Thorn Spray (2)  │
│ Vine Whip   (3)  │ ← Selected
│ Pollen Burst (4) │
│ Sunbeam     (5)  │
└──────────────────┘
```

**Current Weapon:** Highlighted with bright border, icon larger
**Weapon Icons:** Simplified pixel art of each weapon
**Hotkey Display:** Number in parentheses
**Fire Rate Indicator:** Optional small bar showing reload progress

#### Companion HUD (Bottom-Left Corner)
```
┌──────────────────────┐
│ Companion: Hedgehog  │
│ Level: 12            │
│ Ability: Ready (Q)   │
│ Cooldown: ████░░     │
└──────────────────────┘
```

**Companion Icon:** Large, colorful, animated
**Status Bar:** Shows cooldown visually as filling/draining bar
**Level Badge:** Gold badge with level number

#### Resources Display (Bottom-Right Corner)
```
┌──────────────────┐
│ 🌱 Seeds: 15     │
│ 💧 Water: 3.5    │
│ ⭐ Combo: 12x    │
└──────────────────┘
```

**Icons:** Simple pixel art (seed shape, water droplet, star)
**Numbers:** Large, clear font
**Color Coding:** Seeds = brown, Water = blue, Combo = gold

#### Planting Phase HUD (Entire Bottom Bar)
```
┌────────────────────────────────────────────────────┐
│ [Carrot] [Sunflower] [Rose] [Corn]...  │ Time: 30s  │
│ Cost: 1🌱 0.5💧     Held: Ready       │ Wave: 1/5  │
└────────────────────────────────────────────────────┘
```

**Crop Selection:** Icons with names, highlight currently selected
**Cost Display:** Shows resource cost before planting
**Timer:** Counts down to wave start
**Wave Counter:** Shows current wave number

#### Boss Health Bar (Center Top, When Boss Spawned)
```
┌────────────────────────────────────────────┐
│ Aphid Cluster          [██████░░░░░░░░░░] │
└────────────────────────────────────────────┘
```

**Boss Name:** Left side, bold font
**Health Bar:** Full width, gradient from green → yellow → red
**Boss Icon:** Small image left of name
**Phase Indicator:** Optional indicator showing boss phase (1/3, 2/3, etc.)

#### Floating Combat Text
- **Damage Numbers:** Red, bold, scales up then fades, moves upward
- **Healing Numbers:** Green, smaller, moves upward
- **Combo Text:** Yellow/gold, glowing effect, appears when combo increases
- **Point Text:** Gold, larger, appears on kills ("+50 pts")
- **Critical Hit Text:** Large purple "CRITICAL!" with stars

#### Pause Menu
- **Overlay:** Dark semi-transparent (30% black) covering the entire screen
- **Panel:** Centered white box with options:
  - Resume (main action)
  - Settings (audio, video, accessibility)
  - Exit to Menu
- **Styling:** Pixel art border, shadow effect for depth

---

### PARTICLE EFFECTS & ANIMATIONS

**Hit Effect (On Enemy Damage):**
- Explosion of 8-12 small particles (size: 4x4px to 8x8px)
- Color: Yellow/orange burst
- Direction: Radiating outward from hit point
- Life: 0.3 seconds
- Fade: Scales down and becomes transparent

**Critical Hit Effect:**
- Larger burst (16-20 particles, size: 6x6px to 10x10px)
- Color: Hot pink / purple
- Additional: Screen shake (2px offset)
- Sound: Higher pitched "crit" sound

**Combo Burst:**
- Ring of particles expanding outward (size starts 2x2, grows to 16x16)
- Color: Gold/yellow
- Life: 0.5 seconds
- Appears at player position, centered

**Harvest Sparkles:**
- Floating particles from harvested plant to resource counter
- Color: Green for seeds, blue for water
- Path: Curved arc toward UI
- Count: 5-8 particles per harvest

**Companion Ability Activation:**
- Screen flash (0.1s white overlay)
- Radial blast of particles from companion
- Color: Matches companion's theme color
- Count: 20-30 particles

**Plant Growth:**
- Gentle particles rising from plant during growth phase
- Color: Green, very subtle
- Life: 1-2 seconds
- Creates cozy atmosphere

**Wave Start (Screen Shake):**
- Camera shake: 4px offset for 0.3 seconds
- Fade in enemies over 0.5 seconds
- Visual rumble effect

**Victory Screen Confetti:**
- Falling particles of various shapes (squares, circles, stars)
- Colors: Seasonal colors mixed
- Life: 2 seconds
- Gentle gravity effect

---

## COMPLETE GAME LOOP FLOW

```
START
  ↓
┌─────────────────────────────────┐
│ MAIN MENU                       │
│ - Play (New Game / Continue)    │
│ - Settings                      │
│ - Leaderboard                   │
│ - Credits                       │
└─────────────────────────────────┘
  ↓
┌─────────────────────────────────┐
│ SEASON SELECT / INTRO           │
│ - Choose difficulty or continue │
│ - Seasonal intro cutscene       │
│ - Load companion selection      │
└─────────────────────────────────┘
  ↓
┌─────────────────────────────────┐
│ WAVE LOOP (5 waves per season)  │
│                                 │
│ 1. PLANTING PHASE (30-45s)      │
│    - View empty garden grid     │
│    - Click to plant crops       │
│    - Harvest mature plants      │
│    - Wave indicator shows ready │
│                                 │
│    ↓ [PREPARE] button or timer  │
│                                 │
│ 2. COMBAT PHASE (60-90s)        │
│    - Enemies spawn in waves     │
│    - Use weapons to defeat them │
│    - Manage health/lives        │
│    - Use companion ability      │
│    - Get combo multipliers      │
│                                 │
│    ↓ [Wave complete OR lose]    │
│                                 │
│ 3. RESULTS SCREEN (3s)          │
│    - Wave score display         │
│    - Resources earned           │
│    - Combo achievement shown    │
│    - Preparation for next wave  │
│                                 │
│    ↓ [NEXT] or [Game Over]      │
│                                 │
└─────────────────────────────────┘
  ↓
┌─────────────────────────────────┐
│ BOSS PHASE (Wave 5 = Boss)      │
│ - Epic intro animation          │
│ - Boss spawns with health bar   │
│ - Multi-phase combat            │
│ - Higher score potential        │
│ - Victory grants season reward  │
└─────────────────────────────────┘
  ↓
┌─────────────────────────────────┐
│ SEASON COMPLETE SCREEN          │
│ - Total score, achievements     │
│ - Reward selection (choose 1/3) │
│ - Companion level-up display    │
│ - Unlock achievement if earned  │
│                                 │
│ [Next Season] or [Main Menu]    │
└─────────────────────────────────┘
  ↓
IF (Season < 4)
  → Back to Season Select (next season)
ELSE
  → Game Complete, offer New Game+
  → Return to Main Menu
```

---

## SAVE SYSTEM & LOCAL STORAGE

**Save Data Structure:**
```json
{
  "playerName": "Player",
  "currentSeason": 1,
  "currentWave": 1,
  "totalScore": 0,
  "sessionScore": 0,
  "lives": 3,
  "health": 100,
  "resources": {
    "seeds": 20,
    "water": 3.0
  },
  "unlockedWeapons": ["Seed Gun", "Thorn Spray"],
  "unlockedCompanions": ["Hedgehog"],
  "selectedCompanion": "Hedgehog",
  "companionLevels": {
    "Hedgehog": 1,
    "Ladybug": 0,
    "Butterfly": 0,
    "Owl": 0,
    "Snow Fox": 0
  },
  "companionExp": {
    "Hedgehog": 0
  },
  "metaUpgrades": [
    "Health +5",
    "Weapon Fire Rate +10%"
  ],
  "seasonCompletions": 0,
  "leaderboard": [
    { "score": 15000, "season": 4, "date": "2024-01-15" }
  ],
  "settings": {
    "masterVolume": 0.8,
    "musicVolume": 0.7,
    "sfxVolume": 0.9,
    "fullscreen": false,
    "difficulty": "normal"
  },
  "lastPlayedDate": "2024-01-15"
}
```

**Save Locations:**
- Browser: LocalStorage (key: "pixelGardenSave")
- Alternative: IndexedDB for larger data (if needed)
- Backup: Auto-save every 30 seconds during gameplay

---

## AUDIO DESIGN

### Music Tracks (Loop-ready, 60-120 BPM)

**Spring Theme** - Cheerful, whimsical
- Instruments: Ukulele, light strings, bells
- Mood: Playful, inviting, fresh
- Tempo: 100 BPM
- Duration: 2:30 (loops seamlessly)

**Summer Theme** - Energetic, intense
- Instruments: Upbeat synth, drums, electric guitar
- Mood: Action-packed, vibrant, warm
- Tempo: 120 BPM
- Duration: 2:00 (faster loop)

**Fall Theme** - Bittersweet, mellowing
- Instruments: Acoustic guitar, woodwinds, soft strings
- Mood: Reflective, harvest vibes, transitional
- Tempo: 90 BPM
- Duration: 2:45

**Winter Theme** - Mystical, ethereal
- Instruments: Ambient synth, bell tones, icy sounds
- Mood: Magical, calm but mysterious, frosty
- Tempo: 80 BPM
- Duration: 3:00

**Boss Battle Theme** - Epic, intense
- Instruments: Full orchestra, heavy drums, driving bass
- Mood: Climactic, dangerous, memorable
- Tempo: 130 BPM
- Duration: 2:30

**Menu Theme** - Welcoming, cozy
- Instruments: Piano, light synth, nature sounds
- Mood: Inviting, nostalgic, relaxing
- Tempo: 90 BPM
- Duration: 2:00

### Sound Effects

**Weapon Sounds:**
- Seed Gun: Light "plink" + subtle recoil sound
- Thorn Spray: "Whoosh" spray sound + impact
- Vine Whip: "Crack" whip sound + impact
- Pollen Burst: "Poof" explosion sound
- Sunbeam: Charging hum + laser zap

**Combat Sounds:**
- Hit: Vary by damage (light "tap" to heavy "thunk")
- Critical Hit: Higher pitched "ding" sound
- Enemy Death: Small explosion sound (varies per enemy type)
- Damage Taken: Ouch sound, slight pitch increase for higher damage

**Game Sounds:**
- Plant: Gentle "plop" or "whoosh" planting sound
- Harvest: Coins/success "ding" sound
- Combo: "Whoosh" for each 10-combo milestone
- Level Up: Ascending note scale
- Boss Spawn: Deep dramatic hit

**UI Sounds:**
- Button Click: Soft beep, retro game feel
- Menu Open/Close: Whoosh
- Wave Complete: Ascending notes
- Season Complete: Celebratory chime

### Audio Implementation
- Use Web Audio API or Howler.js library
- Implement audio ducking (reduce music during sound effects)
- Support SFX layering (multiple sounds can play simultaneously)
- 3D positional audio (sounds louder closer to player)

---

## ACCESSIBILITY & SETTINGS

### Gameplay Accessibility
- **Colorblind Mode:** Alternate color palette (deuteranopia, protanopia, tritanopia options)
- **Text Sizing:** Options for UI text scaling (100%, 125%, 150%)
- **Font Selection:** Default vs dyslexia-friendly font (OpenDyslexic)
- **High Contrast Mode:** Enhanced border visibility, increased opacity

### Input Options
- **Keyboard Support:** Full WASD + mouse support
- **Controller Support:** Optional gamepad support (if using Phaser with Gamepad API)
- **Button Remapping:** Allow rebind all controls
- **Hold vs Toggle:** Weapon switching can be hold or toggle
- **Difficulty Settings:** Easy (more lenient), Normal, Hard, Custom

### Visual Accessibility
- **Reduce Motion:** Disable particle effects and screen shake
- **Screen Reader Support:** HTML semantic structure for menu navigation
- **Text Alternatives:** Alt text for all visual elements
- **Flash Warning:** No seizure-inducing flashing (all effects < 3 Hz)

### Subtitle & Localization
- **In-Game Text:** All dialog and UI text subtitled
- **Sound Effects:** Visual indicators for important audio cues (e.g., "Boss Spawning!" text overlay)
- **Localization:** Support for multiple languages (English primary, options for Spanish, French, German, Japanese)

---

## DEPLOYMENT & DISTRIBUTION

### Web Version
- **Framework:** Vite.js for bundling and optimization
- **Deployment:** Vercel, Netlify, or GitHub Pages
- **PWA Support:** Optional offline play capability
- **Performance:** Target < 2MB bundle size (compressed)

### Desktop Version
- **Framework:** Electron wrapper
- **Build:** Windows (.exe), macOS (.dmg), Linux (.AppImage)
- **Distribution:** GitHub Releases, itch.io

### Mobile Version (Optional Phase 2)
- **Framework:** React Native or Phaser with mobile support
- **Optimization:** Touch controls, responsive UI scaling
- **Distribution:** iOS App Store, Google Play Store

---

## DEVELOPMENT ROADMAP

### Phase 1: Core Mechanics (Weeks 1-4)
- [ ] Phaser setup, basic scene structure
- [ ] Player movement, weapon switching
- [ ] Enemy spawning, collision detection
- [ ] Planting system, grid interaction
- [ ] Wave management, basic scoring
- [ ] Main menu, pause system

### Phase 2: Polish & Content (Weeks 5-8)
- [ ] All 20 enemy types fully implemented
- [ ] All 5 weapons balanced
- [ ] 5 companion creatures with abilities
- [ ] All 4 seasonal backgrounds & music
- [ ] Boss fights (4 total)
- [ ] Upgrade/progression system
- [ ] Leaderboard, achievements

### Phase 3: Art & Sound (Weeks 9-12)
- [ ] Complete sprite sheet for all assets
- [ ] Custom pixel art for all characters
- [ ] Background parallax implementations
- [ ] Particle effects refinement
- [ ] Sound design, music composition
- [ ] UI polish, animations

### Phase 4: Testing & Optimization (Weeks 13-16)
- [ ] Playtesting, balance adjustments
- [ ] Performance optimization
- [ ] Bug fixes, QA
- [ ] Accessibility review
- [ ] Cross-browser testing
- [ ] Mobile optimization (if applicable)

### Phase 5: Launch & Post-Launch (Ongoing)
- [ ] Official launch
- [ ] Post-launch patches
- [ ] Community feedback integration
- [ ] Cosmetics/DLC planning (Phase 2)
- [ ] Potential sequel planning

---

## ESTIMATED METRICS

**Game Duration:**
- Per Season: 15-20 minutes
- Full Playthrough: 60-80 minutes
- Average Daily Session: 20-30 minutes

**Replayability:**
- 4 seasonal variations × difficulty scaling = high replay value
- Leaderboards encourage speedrunning
- Companion combinations create unique playstyles

**Monetization (Optional):**
- Free-to-play core game
- Optional cosmetic DLC (skins, garden themes, weapon effects)
- No pay-to-win mechanics

**Target Audience:**
- Casual gamers (60%)
- Indie game enthusiasts (25%)
- Speedrunners / Completionists (15%)
- Age range: 10-40+ years old

---

## CONCLUSION

**Pixel Garden Protectors** is a unique fusion of **tower defense strategy, bullet-hell action, and cozy farming**, wrapped in a charming pixel-art aesthetic. By combining cute visuals with satisfying combat mechanics, seasonal variety, and progressive unlocks, this game fills a gap in the indie gaming market.

The game is designed to be:
- **Easy to learn, hard to master**
- **Accessible to all skill levels**
- **Visually delightful and aurally pleasing**
- **Infinitely replayable through seasonal loops**
- **Emotionally engaging through companion growth**

This prompt provides a complete blueprint for development, covering mechanics, art direction, audio design, code architecture, and deployment strategy. Use it to guide your development team from conception to launch.

**Let's grow something beautiful.** 🌱🔫✨

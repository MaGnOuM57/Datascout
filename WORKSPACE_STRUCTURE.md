# Workspace Structure Overview

```
~/.openclaw/workspace/
│
├── Core Identity Files
│   ├── IDENTITY.md              # Who I am (ApporteurCash AI)
│   ├── SOUL.md                  # Personality, vibe, boundaries
│   ├── USER.md                  # About le J
│   ├── AGENTS.md                # How I operate
│   ├── TOOLS.md                 # Local tool notes
│   └── FELIX_MODE.md            # This configuration summary
│
├── Memory System (3 Layers)
│   ├── MEMORY.md                # Long-term curated insights
│   └── memory/
│       ├── YYYY-MM-DD.md        # Daily raw logs
│       ├── heartbeat-state.json # Proactive check tracking
│       └── nightly-reviews/     # Self-improvement logs
│           └── YYYY-MM-DD-review.md
│
├── Knowledge Graph (Structured)
│   └── knowledge/
│       ├── concepts/            # Core concepts, mental models
│       ├── entities/            # People, companies, tools
│       └── relationships/       # Mappings and connections
│
├── PARA System
│   ├── projects/                # Active work (has deadlines)
│   │   ├── README.md
│   │   └── apporteurcash/
│   │       ├── README.md
│   │       ├── tasks.md
│   │       ├── notes.md
│   │       └── results.md
│   ├── areas/                   # Ongoing responsibilities
│   │   └── README.md
│   ├── resources/               # Reference material
│   │   └── README.md
│   └── archives/                # Completed/inactive
│       └── README.md
│
├── Active Projects
│   └── leads/                   # Lead generation work
│       ├── ARTISANS-CIBLES-LUXEMBOURG.md
│       ├── GUIDE-PROSPECTION-ARTISANS.md
│       ├── LEAD-001-EXEMPLE.md
│       ├── lead-generator.md
│       ├── LEADS-QUALIFIES-BATCH-001.json
│       ├── proprietes-luxembourg-raw.json
│       ├── RAPPORT-AVANCEMENT-BATCH-001.md
│       └── SYNTHESE-10-LEADS.md
│
├── Reference & Guides
│   ├── HEARTBEAT.md             # Proactive check schedule
│   ├── SKILLS_REFERENCE.md      # Available skills & tools
│   └── WORKSPACE_STRUCTURE.md   # This file
│
└── System
    ├── .git/                    # Version control
    ├── .openclaw/               # OpenClaw metadata
    └── state/                   # Runtime state
```

## Navigation Tips

### Quick Access
- **Identity**: `IDENTITY.md`, `SOUL.md`, `USER.md`
- **Today's work**: `memory/$(date +%Y-%m-%d).md`
- **Long-term memory**: `MEMORY.md`
- **Current project**: `projects/apporteurcash/`
- **Lead work**: `leads/`

### File Purposes

**DO write daily**:
- `memory/YYYY-MM-DD.md` - Everything that happens

**DO update weekly/monthly**:
- `MEMORY.md` - Distilled insights and learnings
- `projects/*/tasks.md` - Task progress
- `projects/*/results.md` - Outcomes and metrics

**DO edit as needed**:
- `HEARTBEAT.md` - Adjust check frequency
- `knowledge/` - Add new concepts/entities
- `TOOLS.md` - Environment-specific notes

**DON'T edit manually** (system-managed):
- `.openclaw/` - OpenClaw internal state
- `memory/heartbeat-state.json` - Updated by automation

---

**Principle**: Everything important gets written down. Files > memory.

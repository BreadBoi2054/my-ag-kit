# AG Kit — Multi-Agent & Skill Knowledge Base

> Comprehensive agentic skill suite, multi-agent orchestration architecture, lifecycle hooks, and anti-slop frontend engineering protocols for Antigravity IDE and modern AI coding assistants.

---

## 🌟 Highlights

- **51 Specialized Skills**: Covers frontend design (anti-slop + Impeccable + Taste-Skill), creative web motion (`web-motion`), animated component registries & presets (`animated-ui-registries`), backend architectures, security audits, database modeling, editable PPTX presentation generation (`ppt-master`), and Vietnamese official administrative documentation (`vbhc-vietnamese-docx`).
- **20 Specialist Agents**: Dedicated personas with strict operational boundaries (`frontend-specialist`, `backend-specialist`, `security-auditor`, `orchestrator`, `debugger`, `devops-engineer`, etc.).
- **Automated Lifecycle Hooks & Guardrails**: System-level PreToolUse guardrails (`hooks.json`, `guard_agent_skill.py`) that strictly enforce protocol integrity before code execution.
- **Master Architecture & Catalog**: Full documentation in `ARCHITECTURE.md` explaining tier-based governance and routing mechanics.
- **Component Validation Schemas**: JSON schemas in `schemas/` supporting automated checklist verification.
- **Production-Tested Multi-Agent Coordination**: Built-in `coordinator-mode` and `parallel-agents` workflows.

---

## 📁 Repository Structure

```plaintext
my-ag-kit/
├── agent/            # 20 Specialist agent definitions (.md)
├── hooks/            # Lifecycle hooks, schemas, and contract validators
├── memory/           # Persistent cross-session memory templates (MEMORY.md)
├── rules/            # Core protocol, routing matrix, and universal rules
├── schemas/          # JSON schemas for components, manifests, and memory
├── scripts/          # Automated checklist, guardrails, & verification scripts
├── skills/           # 51 Modular skills with SKILL.md specifications
│   ├── frontend-design/        # Anti-slop UI design + Impeccable Design Director
│   ├── web-motion/             # Motion, Lenis smooth scroll, Anime.js v4 & View Transitions
│   ├── animated-ui-registries/ # React Bits, Magic UI, Skiper UI, OriginKit & Shadcn Preset
│   ├── ppt-master/             # AI-driven editable PPTX decks, templates & slides
│   ├── vbhc-vietnamese-docx/   # Nghị định 30/2020, HD 05, TT 68 administrative docs
│   ├── clean-code/             # Pragmatic, concise, non-overengineered coding standards
│   ├── coordinator-mode/       # Multi-agent parallel coordination & synthesis
│   └── ...
├── workflows/        # Predefined workflow pipelines
├── ARCHITECTURE.md   # Complete system architecture and catalog
├── hooks.json        # PreInvocation and PreToolUse guardrail configuration
└── README.md
```

---

## 🚀 Quick Setup

### Option 1: Global Setup for Antigravity IDE
Copy or clone the contents into your global Gemini config directory:
```powershell
# Windows PowerShell
Copy-Item -Path "skills", "agent", "rules", "scripts", "hooks", "schemas", "hooks.json" -Destination "C:\Users\doh52\.gemini\config\" -Recurse -Force
```

### Option 2: Project Workspace Setup
Drop into your project root under the `.agents/` folder:
```powershell
# In your project root
mkdir .agents
Copy-Item -Path "skills", "agent", "rules", "hooks", "schemas", "hooks.json" -Destination ".agents\" -Recurse -Force
```

---

## 🛡️ License

MIT License. Feel free to use, modify, and integrate into your personal AI workflows.

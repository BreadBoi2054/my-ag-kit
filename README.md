# AG Kit — Multi-Agent & Skill Knowledge Base

> Comprehensive agentic skill suite, multi-agent orchestration architecture, and anti-slop frontend engineering protocols for Antigravity IDE and modern AI coding assistants.

---

## 🌟 Highlights

- **48 Specialized Skills**: Covers frontend design (anti-slop + Impeccable + Taste-Skill), backend architectures, security audits, database modeling, and Vietnamese official administrative documentation (bhc-vietnamese-docx).
- **20 Specialist Agents**: Dedicated personas with strict operational boundaries (rontend-specialist, ackend-specialist, security-auditor, orchestrator, debugger, devops-engineer, etc.).
- **Rigorous Governance Rules**: Core protocols, intelligent request routing, universal clean-code guidelines, and automated checklist validation.
- **Production-Tested Multi-Agent Coordination**: Built-in coordinator-mode and parallel-agents workflows.

---

## 📁 Repository Structure

`
my-ag-kit/
├── agent/            # 20 Specialist agent definitions (.md)
├── rules/            # Core protocol, routing matrix, and universal rules
├── scripts/          # Automated checklist & verification scripts (checklist.py)
├── skills/           # 48 Modular skills with SKILL.md specifications
│   ├── frontend-design/      # Anti-slop UI design + Impeccable Design Director
│   ├── vbhc-vietnamese-docx/ # Nghị định 30/2020, HD 05, TT 68 administrative docs
│   ├── clean-code/           # Pragmatic, concise, non-overengineered coding standards
│   ├── coordinator-mode/     # Multi-agent parallel coordination & synthesis
│   └── ...
└── workflows/        # Predefined workflow pipelines
`

---

## 🚀 Quick Setup

### Option 1: Global Setup for Antigravity IDE
Copy or clone the contents into your global Gemini config directory:
`ash
# Windows PowerShell
Copy-Item -Path "skills", "agent", "rules", "scripts" -Destination "C:\Users\doh52\.gemini\config\" -Recurse -Force
`

### Option 2: Project Workspace Setup
Drop into your project root under the .agents/ folder:
`ash
# In your project root
mkdir .agents
Copy-Item -Path "skills", "agent", "rules" -Destination ".agents\" -Recurse -Force
`

---

## 🛡️ License

MIT License. Feel free to use, modify, and integrate into your personal AI workflows.

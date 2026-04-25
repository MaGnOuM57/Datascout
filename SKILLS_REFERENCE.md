# Skills Reference - Quick Guide

## 🎯 Available Skills

### Core Skills (built-in)

1. **healthcheck**: Host security hardening and risk-tolerance configuration
2. **node-connect**: Diagnose OpenClaw node connection and pairing failures
3. **skill-creator**: Create, edit, improve, or audit AgentSkills
4. **taskflow**: Durable flow substrate for multi-task work
5. **taskflow-inbox-triage**: Example TaskFlow pattern for inbox triage
6. **tmux**: Remote-control tmux sessions for interactive CLIs
7. **weather**: Get weather and forecasts via wttr.in or Open-Meteo

### Key Tools Available

- ✅ **read/write/edit**: File operations
- ✅ **exec**: Shell commands
- ✅ **browser**: Web automation (OpenClaw-managed or user browser)
- ✅ **web_fetch**: Lightweight page scraping
- ✅ **memory_search/get**: Semantic memory search
- ✅ **cron**: Scheduled tasks & reminders
- ✅ **sessions_spawn**: Sub-agents and ACP coding sessions
- ✅ **message**: Proactive messaging (when channels configured)
- ✅ **canvas**: Present/eval/snapshot UI
- ✅ **nodes**: Paired device control (Android/iOS/macOS)

## 🔧 Optimization Tips

### Terminal/Shell
- Use `exec` with `pty=true` for TTY-required CLIs
- Background long-running commands with `background=true`
- Use `process` to manage running sessions

### Browser Automation
- Use `profile="openclaw"` (default) for isolated browser
- Use `profile="user"` for logged-in user browser (when auth needed)
- Prefer `snapshot` + `act` for UI automation
- Use `refs="aria"` for stable element references

### Memory & Context
- Always `memory_search` before answering questions about past work
- Update `memory/YYYY-MM-DD.md` daily with raw logs
- Curate `MEMORY.md` with distilled insights (weekly/monthly)
- Use knowledge graph for structured relationships

### Sub-agents
- Use `sessions_spawn(runtime="subagent")` for complex tasks
- Use `sessions_spawn(runtime="acp")` for coding with harnesses (Codex, Cursor, etc.)
- Don't poll `subagents list` in loops - let them announce completion
- Use `thread=true` for Discord thread-bound sessions

### Proactive Work
- Configure `HEARTBEAT.md` for periodic checks
- Track state in `memory/heartbeat-state.json`
- Use `cron` for scheduled reminders (not exec sleep loops)
- Nightly self-improvement at 3 AM (Europe/Paris)

## 📚 Documentation

- **Local docs**: `/home/openclaw/.npm-global/lib/node_modules/openclaw/docs`
- **Online**: https://docs.openclaw.ai
- **Community**: https://discord.com/invite/clawd
- **Skills hub**: https://clawhub.ai

---

**Pro tip**: Read a skill's SKILL.md BEFORE using it. Skills provide detailed context and best practices.

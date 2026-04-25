# HEARTBEAT.md - Proactive Agent Checks

## 🔄 Regular Checks (rotate 2-4x daily)

### Communication & Schedule
- [ ] **Email**: Any urgent unread messages? (check every ~4-6h during daytime)
- [ ] **Calendar**: Upcoming events in next 24-48h?
- [ ] **Mentions**: Social notifications? (if configured)

### Project & Environment
- [ ] **Project Status**: Any git changes, pending work, builds to check?
- [ ] **Weather**: Relevant if le J might go out (Luxembourg weather)

### Memory Maintenance (every few days)
- [ ] **Memory Review**: Read recent daily notes, update MEMORY.md with insights
- [ ] **File Organization**: Clean up workspace, organize notes

## 🕒 Timing Rules

**Reach out when:**
- Important email or event
- Something interesting discovered
- >8h since last interaction
- Critical project update

**Stay quiet (HEARTBEAT_OK) when:**
- Late night (23:00-08:00) unless urgent
- Human clearly busy
- Nothing new since last check (<30min ago)
- Just checked same thing recently

## 📊 Tracking

State tracked in: `memory/heartbeat-state.json`

---

*Keep checks lightweight. Be helpful, not annoying. Quality over frequency.*

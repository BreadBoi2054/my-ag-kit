# -*- coding: utf-8 -*-
import sys
import json
import os
import re

def respond(decision, reason=""):
    out = {"decision": decision}
    if reason:
        out["reason"] = reason
    sys.stdout.write(json.dumps(out, ensure_ascii=False) + "\n")
    sys.stdout.flush()
    sys.exit(0)

def main():
    try:
        raw_input = sys.stdin.read()
        if not raw_input.strip():
            respond("allow")
        payload = json.loads(raw_input)
    except Exception:
        respond("allow")

    transcript_path = payload.get("transcriptPath")
    if not transcript_path or not os.path.exists(transcript_path):
        respond("allow")

    try:
        with open(transcript_path, "r", encoding="utf-8", errors="ignore") as f:
            lines = f.readlines()
    except Exception:
        respond("allow")

    last_user_idx = -1
    steps = []
    for line in lines:
        line = line.strip()
        if not line:
            continue
        try:
            step = json.loads(line)
            steps.append(step)
            if step.get("type") == "USER_INPUT" or step.get("source") == "USER_EXPLICIT":
                last_user_idx = len(steps) - 1
        except Exception:
            continue

    if last_user_idx == -1:
        current_turn_steps = steps
    else:
        current_turn_steps = steps[last_user_idx:]

    banner_found = False
    announced_skills = set()
    claims_subagent = False
    
    agent_banner_pattern = re.compile(
        r"(Applying knowledge of @|🤖\s*\*\*Applying knowledge of|@orchestrator|@frontend-specialist|@backend-specialist|@debugger|@security-auditor|@database-architect|@devops-engineer|@test-engineer|@project-planner)",
        re.IGNORECASE
    )
    skill_banner_pattern = re.compile(
        r"(?:Using skills?:\s*|skill:\s*)(@[a-zA-Z0-9_\-]+(?:\s*\+\s*@[a-zA-Z0-9_\-]+)*)",
        re.IGNORECASE
    )
    subagent_claim_pattern = re.compile(
        r"(đã gọi subagent|đã kích hoạt subagent|subagent đã|subagent id|gọi agent con|dispatch worker|đã ủy quyền cho subagent)",
        re.IGNORECASE
    )

    for step in current_turn_steps:
        content = step.get("content") or ""
        if isinstance(content, str) and content:
            if agent_banner_pattern.search(content):
                banner_found = True
            
            match = skill_banner_pattern.search(content)
            if match:
                skill_part = match.group(1)
                found = re.findall(r"@([a-zA-Z0-9_\-]+)", skill_part)
                for s in found:
                    announced_skills.add(s.lower())

            if subagent_claim_pattern.search(content):
                claims_subagent = True

    if not banner_found:
        respond(
            "deny",
            "BỊ CHẶN BỞI GUARDRAIL: Bạn chưa in banner khai báo Agent (ví dụ: '🤖 **Applying knowledge of @orchestrator...') "
            "ra màn hình trước khi thao tác file code! Quy tắc: In banner trước, sau đó mới được phép ghi file."
        )

    # Check if announced skills were read via view_file
    if announced_skills:
        viewed_files = []
        for step in steps:
            tool_calls = step.get("tool_calls") or []
            for tc in tool_calls:
                name = tc.get("name") or tc.get("tool_name")
                if name == "view_file":
                    args = tc.get("args") or {}
                    path = args.get("AbsolutePath") or ""
                    viewed_files.append(path.lower().replace("\\", "/"))

        missing_skills = []
        for skill in announced_skills:
            skill_read = False
            for vf in viewed_files:
                if f"skills/{skill}" in vf or f"skills\\{skill}" in vf or f"{skill}/skill.md" in vf:
                    skill_read = True
                    break
            if not skill_read:
                missing_skills.append(skill)

        if missing_skills:
            missing_str = ", ".join([f"@{s}" for s in missing_skills])
            respond(
                "deny",
                f"BỊ CHẶN BỞI GUARDRAIL: Bạn đã khai báo dùng skill [{missing_str}] "
                f"nhưng chưa hề gọi lệnh view_file để đọc file SKILL.md tương ứng! "
                f"Hãy dùng view_file mở file SKILL.md của skill đó ra đọc trước khi ghi/sửa file code."
            )

    # Anti-hallucination check: if agent claims subagent was called, verify tool call
    if claims_subagent:
        subagent_called = False
        for step in steps:
            tool_calls = step.get("tool_calls") or []
            for tc in tool_calls:
                name = tc.get("name") or tc.get("tool_name")
                if name in ["browser_subagent", "invoke_subagent", "spawn_subagent", "agent"]:
                    subagent_called = True
                    break
            if subagent_called:
                break
        
        if not subagent_called:
            respond(
                "deny",
                "BỊ CHẶN BỞI GUARDRAIL (ANTI-HALLUCINATION): Bạn tuyên bố 'đã gọi subagent' trong nội dung "
                "nhưng lịch sử phiên KHÔNG HỀ CÓ lệnh gọi công cụ subagent nào! "
                "Nếu môi trường không có công cụ subagent cho tác vụ này, bạn phải báo BLOCKED theo đúng quy tắc, "
                "tuyệt đối không được báo cáo giả mạo."
            )

    respond("allow")

if __name__ == "__main__":
    main()

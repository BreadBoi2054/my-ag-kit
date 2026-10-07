# -*- coding: utf-8 -*-
import sys
import json

def main():
    try:
        raw = sys.stdin.read()
        payload = json.loads(raw) if raw.strip() else {}
    except Exception:
        payload = {}
    
    inv_num = payload.get('invocationNum', 1)
    
    if inv_num == 1:
        # First invocation of the session: Session-start bootstrap instructions
        reminder_msg = (
            "[VUDOVN SESSION-START PROTOCOL]\n"
            "Đường dẫn Catalog Vudovn: C:\\Users\\doh52\\.gemini\\config\\skills\\\n"
            "Đường dẫn Gốc: c:\\Users\\doh52\\OneDrive\\Máy tính\\antigravity agent\\.agents\\ARCHITECTURE.md\n\n"
            "QUY TRÌNH BẮT BUỘC TRƯỚC NHIỆM VỤ THỰC CHẤT ĐẦU TIÊN:\n"
            "1. Kiểm tra catalog và dùng view_file (với IsSkillFile: true) để đọc SKILL.md phù hợp.\n"
            "2. Đọc hướng dẫn điều phối agent (parallel-agents/SKILL.md hoặc coordinator-mode/SKILL.md).\n"
            "3. Kiểm tra công cụ subagent: Nếu có invoke_subagent, gọi thực tế; nếu phiên chỉ có browser_subagent, báo rõ BLOCKED không có công cụ coding subagent - TUYỆT ĐỐI KHÔNG NÓI ĐÃ DÙNG NẾU CHƯA GỌI TOOL.\n"
            "4. In banner bắt buộc ở đầu phản hồi:\n"
            "   🤖 **Applying knowledge of @[agent-name]...**\n"
            "   📚 **Using skill: @[skill-name]...**\n"
            "      - Path: C:\\Users\\doh52\\.gemini\\config\\skills\\[skill-name]\\SKILL.md\n"
            "      - Reason: [Lý do áp dụng]\n"
            "5. GÁC CỔNG CƯỠNG CHẾ (PreToolUse): Mọi thao tác ghi/sửa file đều bị HỆ THỐNG CHẶN ĐỨNG nếu chưa in banner và chưa đọc SKILL.md thật!"
        )
    else:
        # Subsequent turns: concise reminder to prevent context bloat
        reminder_msg = (
            "[GUARDRAIL PROTOCOL] MANDATORY:\n"
            "1. Bắt buộc in banner Agent: 🤖 **Applying knowledge of @[agent-name]...**\n"
            "2. Nếu khai báo skill: 📚 **Using skill: @[skill-name]...** thì BẮT BUỘC phải gọi view_file đọc SKILL.md.\n"
            "3. Không tuyên bố đã dùng agent/skill nếu chưa gọi công cụ thực tế. Báo BLOCKED nếu thiếu công cụ.\n"
            "4. Thao tác ghi/sửa file sẽ bị HỆ THỐNG CHẶN CỨNG nếu vi phạm."
        )

    out = {
        'injectSteps': [
            {
                'ephemeralMessage': reminder_msg
            }
        ]
    }
    sys.stdout.write(json.dumps(out, ensure_ascii=False) + '\n')
    sys.stdout.flush()

if __name__ == '__main__':
    main()

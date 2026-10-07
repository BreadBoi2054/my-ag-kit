---
name: core-protocol
version: 2.1.0
priority: P0
trigger: always_on
---

# Core Protocol - AG Kit (Bo Skill Vudovn & Quy Chuan Thuc Thi)

> The highest-priority workspace rules. Bat buoc tuan thu vo dieu kien truoc moi hanh dong.

---

## 1. Vudovn Skill Knowledge Base & Actual Paths
- Global Skills Directory: C:\Users\doh52\.gemini\config\skills\
- Original Catalog & Architecture File: c:\Users\doh52\OneDrive\Máy tính\antigravity agent\.agents\ARCHITECTURE.md
- Global Rules Directory: C:\Users\doh52\.gemini\config\rules\
- Global Agents Directory: C:\Users\doh52\.gemini\config\agent\
- Master Scripts: C:\Users\doh52\.gemini\config\scripts\checklist.py
- Lifecycle Hooks: C:\Users\doh52\.gemini\config\hooks.json

---

## 2. QUY TRINH KHOI DONG & TRUOC NHIEM VU THUC CHAT DAU TIEN
Truoc khi thuc hien nhiem vu thuc chat dau tien moi phien lam viec:
1. Kiem tra catalog skill thuc te (tai C:\Users\doh52\.gemini\config\skills\ hoac ARCHITECTURE.md).
2. Chon va doc SKILL.md phu hop bang view_file (bat buoc cờ IsSkillFile: true).
3. Doc huong dan dieu phoi agent cua bo vudovn (parallel-agents/SKILL.md hoac coordinator-mode/SKILL.md).
4. Kiem tra kha nang subagent trong phien:
   - Neu co cong cu subagent phu hop: Thuc su goi subagent voi day du ngu canh, skill path va tieu chi hoan thanh.
   - Neu phien khong co cong cu subagent cho phan viec (vi du Antigravity IDE chi cung cap browser_subagent, khong co invoke_subagent cho coding):
     -> BẮT BUỘC bao ro BLOCKED voi phan viec giao cho subagent; TUYET DOI KHONG tu nhan hoac gia vo da goi subagent.
5. In banner theo dung huong dan goc cua bo vudovn (Xem Muc 6).

---

## 3. QUY TAC BANG CHUNG & CHINH TRUC (GROUND TRUTH EVIDENCE)
1. Khong noi "da dung skill" neu chua co thao tac goi view_file doc SKILL.md.
2. Khong noi "da dung agent" neu chua goi cong cu tao subagent thuc te.
3. Banner va loi tu bao cao KHONG DUOC tinh la bang chung thuc thi.
4. Neu khong co cong cu subagent hoac khong doc duoc skill, bao BLOCKED cung nguyen nhan; khong am tham lam thay roi tuyen bo da tuan thu.
5. Khong dung viec doc file o luot sau de chung minh cho luot truoc.
6. Chinh truc ve gioi han: Phan biet ro giua chi dan prompt (chua phai cuong che) va dieu kien duoc he thong thuc su cuong che (qua hook PreToolUse).

---

## 4. QUY TAC SU DUNG SKILL (SKILL USAGE)
1. Kiem tra catalog truoc khi lam.
2. Doc SKILL.md day du bang view_file truoc khi dung cong cu, sua file hoac tao san pham.
3. Doc tai nguyen tham chieu duoc skill yeu cau.
4. Khong bo qua skill vi nhiem vu don gian.
5. Nhac ten hoac tom tat khong tinh la da dung skill.
6. Thong bao ngan gon skill da chon, duong dan thuc te va ly do ap dung.
7. Neu khong co skill phu hop, neu ro ly do.

---

## 5. QUY TAC DIEU PHOI SUBAGENT (SUBAGENT ORCHESTRATION)
1. Kiem tra cong cu: Chi thuc hien uy quyen subagent khi runtime cung cap cong cu ho tro (vi du browser_subagent cho trinh duyet).
2. Ro rang muc tieu & ngu canh: Moi subagent phai nhan: muc tieu, du lieu dau vao, pham vi, skill path can doc va tieu chi hoan thanh.
3. Khong mac dinh ke thua context: Subagent can duoc truyen du context can thiet.
4. Tranh xung dot ghi de: Khong de nhieu agent sua cung mot file dong thoi.
5. Agent chinh chiu trach nhiem tong hop va kiem chung ket qua cuoi cung.
6. Tuyet doi khong bao cao gia ve viec da goi agent.

---

## 6. THONG BAO BANNER (MANDATORY FORMAT)
Moi khi bat dau xu ly nhiem vu ky thuat:
- 🤖 **Applying knowledge of @[agent-name]...**
- 📚 **Using skill: @[skill-name]...**
  - Path: C:\Users\doh52\.gemini\config\skills\[skill-name]\SKILL.md
  - Reason: [Ly do ap dung cu the]

---

## 7. QUY TAC THUC HIEN CONG VIEC & KIEM CHUNG
1. Lam den cung: Chu dong thuc hien den khi co ket qua kiem chung thuc te.
2. Tu quyet dinh chi tiet ky thuat thong thuong.
3. Han che hoi lap lai: Chi hoi khi thieu thong tin thiet yeu hoac danh doi lon.
4. Chay kiem tra thuc te (chay code, chay test, audit cu phap) thay vi chi nhin bang mat.
5. Phan biet minh bach trong bao cao: da thuc hien, da kiem tra, va chua xac minh / bi chan.

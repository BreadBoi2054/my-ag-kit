# Impeccable Design Refinement — The Design Director Protocol

> Extension of [frontend-design](SKILL.md) adapted from [pbakaus/impeccable](https://github.com/pbakaus/impeccable) by Paul Bakaus.
> Activates the "Design Director" feedback loop, interactive design commands, and 61 deterministic anti-slop rules.

---

## 1. TRIẾT LÝ THIẾT KẾ: DESIGN DIRECTOR LOOP

LLM có xu hướng sinh ra giao diện ở mức **"trung bình thống kê"** (statistical median): mọi thứ đều dùng bo tròn giống nhau, gradient tím-xanh, thẻ card tràn ngập, văn phong sáo rỗng.

Giao thức **Impeccable** biến Agent thành một **Giám đốc Thiết kế (Design Director)** khắt khe:
1. **Không bao giờ chấp nhận bản draft đầu tiên là bản hoàn thiện.**
2. **Tự động áp dụng 61 Deterministic Rules** (quy tắc xác định không phụ thuộc vào cảm tính của LLM).
3. **Cung cấp bộ lệnh tương tác tức thì** (`/polish`, `/quieter`, `/bolder`, `/distill`, `/audit`, `/typeset`, `/animate`).

---

## 2. BỘ LỆNH ĐIỀU HƯỚNG THIẾT KẾ (INTERACTIVE DESIGN COMMANDS)

Khi người dùng hoặc Agent gọi các lệnh này, lập tức thực thi chu trình tinh chỉnh tương ứng:

### 🔇 `/quieter` (Làm dịu & Giảm độ ồn giao diện)
*Áp dụng khi giao diện quá lòe loẹt, quá nhiều viền, shadow nổi gồ ghề, hoặc màu sắc tranh chấp.*
- **Bỏ bớt container:** Gỡ bỏ thẻ card nền nổi cho các khối thông tin thuần túy; dùng khoảng trắng (`gap-8`, `gap-12`) hoặc đường kẻ mờ (`border-t border-zinc-200/60 dark:border-zinc-800/60`) thay vì nhét mọi thứ vào card có viền và bóng.
- **Giảm tương phản viền:** Chuyển viền đặc `border-gray-300` thành viền hòa trộn `border-black/[0.06]` (light) hoặc `border-white/[0.08]` (dark).
- **Thu gọn màu sắc:** Đưa toàn bộ các màu phân tán về thang xám trung tính (Zinc/Slate/Stone); chỉ giữ lại đúng 1 điểm nhấn duy nhất cho Primary CTA.
- **Tăng khoảng thở (De-cluttering):** Tăng padding dọc giữa các section (`py-20 md:py-32`).

### ⚡ `/bolder` (Tăng cá tính & Độ sắc nét)
*Áp dụng khi giao diện nhạt nhòa, đơn điệu, phẳng lì như tài liệu Word.*
- **Kích hoạt Typographic Scale cao:** Đưa Headline Hero lên `text-5xl md:text-7xl lg:text-8xl tracking-tight font-semibold`.
- **Tạo tương phản sắc cạnh:** Dùng nền đen sâu (`bg-black` / `bg-zinc-950`) kết hợp chữ trắng ngà (`text-zinc-100`) hoặc ngược lại.
- **Bố cục bất đối xứng (Asymmetry):** Phá vỡ cấu trúc căn giữa; chuyển sang Split-screen 60/40, Hero lệch trái với khoảng trống lớn có chủ ý bên phải, hoặc Bento Grid phá cách với 1 ô tiêu điểm (Hero Cell) gấp đôi kích thước các ô khác.
- **Điểm nhấn màu đơn sắc cường độ cao:** 1 màu accent bão hòa mạnh (Electric Cobalt `#0052FF`, Emerald `#059669`, Crimson `#E11D48`, hoặc International Klein Blue) trên nền tối giản.

### 🧪 `/distill` (Chưng cất & Tinh giản tối đa)
*Áp dụng khi giao diện có quá nhiều chi tiết thừa, cấu trúc rườm rà (div-soup).*
- **Xóa bỏ các lớp lồng nhau:** Gộp các `<div>` bọc thừa; làm phẳng DOM tree.
- **Cắt giảm từ ngữ:** Rút gọn subtext hero dưới 20 từ. Cắt tiêu đề section còn dưới 6 từ.
- **Bỏ icon trang trí thừa:** Nếu icon không giúp người dùng hiểu nhanh hơn chức năng, gỡ bỏ toàn bộ icon cạnh tiêu đề.
- **Quy tụ các nút hành động (CTA Consolidation):** 1 trang chỉ có tối đa 1 Primary CTA duy nhất và 1 Secondary CTA dạng text link/ghost. Xóa các nút phụ gây nhiễu.

### ✨ `/polish` (Đánh bóng Pixel & Chi tiết Vi mô)
*Áp dụng trước khi xuất xưởng để đạt độ hoàn thiện của sản phẩm thương mại cao cấp.*
- **Cân bằng Padding trong nút:** Chiều ngang gấp 1.8 - 2.2 lần chiều dọc (ví dụ: `px-5 py-2.5` hoặc `px-6 py-3`).
- **Thống nhất độ bo góc (Border-radius consistency):**
  - Hệ thống Sharp: Toàn bộ bo góc `rounded-none` hoặc `rounded-sm`.
  - Hệ thống Soft: Nút `rounded-lg` (8px), Card `rounded-xl` (12-16px), Outer Container `rounded-2xl` (16-24px). Tuyệt đối không lẫn lộn giữa nút viên thuốc (pill) và card vuông sắc nhọn.
- **Sub-pixel font rendering:** Bắt buộc có class `antialiased` ở thẻ gốc.
- **Tactile feedback:** Nút bấm phải có phản hồi vật lý khi click: `active:scale-[0.98] transition-transform duration-100`.

### 🔍 `/audit` (Thẩm định toàn diện theo 61 Quy tắc)
*Rà soát tự động toàn bộ trang web và xuất bảng điểm đạt/chưa đạt dựa trên 61 Deterministic Rules bên dưới.*

---

## 3. BẢNG 61 DETERMINISTIC ANTI-SLOP RULES (PAUL BAKAUS SPEC)

### Nhóm 1: Typography & Hierarchy (Quy tắc 1 – 10)
1. **Rule 1 (Scale Ratio):** Sử dụng tỷ lệ phân cấp chuẩn (Major Second 1.125 hoặc Minor Third 1.2 cho dense UI; Perfect Fourth 1.333 cho marketing). Không tùy tiện dùng font-size ngẫu hứng.
2. **Rule 2 (Measure / Line Length):** Đoạn văn body text tối đa `65ch` (khoảng 60-75 ký tự một dòng). Cấm văn bản kéo dài hết chiều rộng màn hình.
3. **Rule 3 (Line-height Scaling):** Headline lớn dùng line-height chặt chẽ (`leading-[1.05]` đến `leading-tight`); Body text dùng line-height thoáng (`leading-relaxed` hoặc `1.6`).
4. **Rule 4 (No Mixed Font Families in Heading):** Không chèn 1 từ Serif ngẫu nhiên vào giữa Headline Sans-serif chỉ để "làm điệu". Muốn nhấn mạnh, hãy dùng font weight hoặc italic cùng họ font.
5. **Rule 5 (Italic Descender Clearance):** Khi dùng chữ nghiêng (italic) có các chữ cái thò đuôi (`g, j, p, q, y`), bắt buộc tăng `line-height` tối thiểu `1.1` và đệm `pb-1` để không bị cắt đuôi chữ.
6. **Rule 6 (Monospace Discipline):** Chỉ dùng Monospace cho code snippet, dữ liệu số kỹ thuật, keystroke shortcut, hoặc timestamp. Không dùng mono cho body text.
7. **Rule 7 (Font Pairing Ban):** Cấm kết hợp 2 font Sans-serif khác nhau trên cùng một trang (ví dụ vừa dùng Inter vừa dùng Roboto).
8. **Rule 8 (Uppercase Tracking):** Mọi văn bản in hoa (ALL CAPS / Eyebrow) bắt buộc phải tăng khoảng cách chữ: `tracking-wider` hoặc `tracking-[0.15em]`.
9. **Rule 9 (Subhead Word Count):** Subhead của Hero không được vượt quá 20 từ và không quá 3 dòng trên màn hình máy tính.
10. **Rule 10 (Contrast Ratios):** Chữ thông thường đạt tối thiểu 4.5:1 WCAG AA; Chữ lớn (18px+) đạt tối thiểu 3:1. Cấm chữ xám mờ trên nền trắng (`#999` trên `#fff`).

### Nhóm 2: Color, Surfaces & Contrast (Quy tắc 11 – 20)
11. **Rule 11 (Singular Accent):** Tối đa 1 màu nhấn (Accent Color) duy nhất cho toàn bộ luồng giao diện chính.
12. **Rule 12 (Purple Gradient Ban):** Cấm mặc định tạo nền màu tím neon / gradient tím-xanh kiểu "AI mặc định".
13. **Rule 13 (Neutral Harmony):** Chọn 1 thang xám duy nhất (hoặc Zinc lạnh, hoặc Slate xanh, hoặc Stone ấm). Cấm trộn lẫn xám ấm và xám lạnh trong cùng trang.
14. **Rule 14 (Pure Black Avoidance in Light Mode):** Trên nền sáng, văn bản chính dùng `#111827` (zinc-900) hoặc `#09090b`, không dùng `#000000` tuyệt đối.
15. **Rule 15 (Tinted Shadows):** Bóng đổ không được là màu đen thuần (`rgba(0,0,0,...)`), mà phải pha 2-5% sắc độ của màu nền.
16. **Rule 16 (Color Consistency Lock):** Một khi đã chọn accent (ví dụ Emerald), toàn bộ badge trạng thái chính, nút CTA, thanh tiến trình phải đồng nhất dùng Emerald.
17. **Rule 17 (Dark Mode Surface Elevation):** Dark mode không dùng bóng đổ để phân cấp. Dùng sắc độ xám nhạt dần theo độ cao: Nền `zinc-950` → Card `zinc-900` → Hover `zinc-850`.
18. **Rule 18 (Borders over Heavy Drop-shadows):** Ưu tiên dùng đường viền siêu mỏng `1px border-zinc-200/80 dark:border-zinc-800` hơn là bóng đổ đậm.
19. **Rule 19 (Form Input Contrast):** Khung input form và placeholder phải nhìn rõ ràng, vượt qua bài kiểm tra độ tương phản 3:1 so với nền form.
20. **Rule 20 (Consistent Theme Lock):** Giữ nguyên một chế độ (Toàn bộ sáng hoặc Toàn bộ tối) trong suốt quá trình cuộn trang. Cấm đổi sang nền trắng ở giữa trang nền tối.

### Nhóm 3: Layout & Whitespace (Quy tắc 21 – 30)
21. **Rule 21 (Anti-Center Bias):** Không mặc định căn giữa toàn bộ trang. Hãy căn trái nội dung văn bản và tạo điểm tựa thị giác.
22. **Rule 22 (Initial Viewport Fit):** Nội dung Hero (tiêu đề, subtext, CTA) phải nằm trọn trong màn hình đầu tiên (`min-h-[100dvh]`), không bị tràn xuống dưới ép cuộn mới thấy CTA.
23. **Rule 23 (Hero Top Padding Cap):** Khoảng cách từ thanh menu xuống nội dung Hero tối đa `pt-20` đến `pt-28`. Cấm để khoảng trống quá sâu khiến nội dung rơi xuống giữa trang.
24. **Rule 24 (Single-Line Desktop Navigation):** Thanh điều hướng trên máy tính bắt buộc phải nằm trên 1 dòng duy nhất. Nếu tràn dòng, phải thu gọn menu.
25. **Rule 25 (Nav Height Ceiling):** Chiều cao thanh menu trên desktop tối đa 72px (chuẩn 64px). Không làm menu cồng kềnh chiếm 15% chiều cao màn hình.
26. **Rule 26 (Layout Family Variety):** Mỗi kiểu bố cục (3 cột card, split-screen, bento, marquee) chỉ xuất hiện tối đa 1 lần trên 1 trang.
27. **Rule 27 (Zigzag Cap):** Cấm lặp lại bố cục "hình trái - chữ phải" rồi "chữ trái - hình phải" quá 2 lần liên tiếp.
28. **Rule 28 (Bento Cell Count Integrity):** Lưới Bento chỉ có số ô bằng đúng số lượng nội dung thực tế có sẵn. Cấm để ô trống rỗng bọc lót.
29. **Rule 29 (Eyebrow Restraint):** Tối đa 1 nhãn Eyebrow (chữ in hoa nhỏ phía trên tiêu đề) cho mỗi 3 section. Không gắn nhãn này lên mọi tiêu đề.
30. **Rule 30 (Explicit Mobile Fallback):** Mọi bố cục đa cột trên máy tính đều phải khai báo rõ ràng cách co dãn trên mobile (`grid-cols-1 md:grid-cols-3`).

### Nhóm 4: Buttons, Forms & Interactive UI (Quy tắc 31 – 40)
31. **Rule 31 (CTA Button Wrap Ban):** Văn bản trên nút bấm tuyệt đối không được gãy thành 2 dòng trên màn hình máy tính. Nút CTA tối đa 1 - 3 từ.
32. **Rule 32 (Duplicate CTA Intent Ban):** Cấm dùng nhiều từ ngữ khác nhau cho cùng một mục đích trên cùng 1 trang (ví dụ vừa "Contact us", vừa "Get in touch", vừa "Start a project"). Hãy chọn 1 nhãn duy nhất.
33. **Rule 33 (Tactile Push Feedback):** Mọi nút bấm tương tác phải có hiệu ứng `:active` thu nhỏ nhẹ (`active:scale-[0.98]`).
34. **Rule 34 (Full State Cycles):** Mọi component form/dữ liệu đều phải có đủ 4 trạng thái: Default, Loading, Empty, và Error.
35. **Rule 35 (Label Above Input):** Nhãn trường nhập liệu phải nằm ở TRÊN ô nhập, không được dùng Placeholder để thay thế cho Label.
36. **Rule 36 (Error Text Below Input):** Thông báo lỗi form nằm ngay dưới ô nhập bị lỗi với màu sắc rõ ràng và thông điệp cụ thể.
37. **Rule 37 (Focus Ring Visibility):** Phải có `focus-visible:ring-2 focus-visible:ring-offset-2` chuẩn a11y, không bao giờ dùng `outline-none` mà không có thay thế.
38. **Rule 38 (Skeleton Loaders):** Trạng thái tải (loading) phải mô phỏng hình dáng của layout sắp hiển thị, không dùng vòng xoay spinner đơn điệu giữa trang.
39. **Rule 39 (Clickable Area Sizing):** Mọi phần tử bấm được trên màn hình cảm ứng tối thiểu 44x44px.
40. **Rule 40 (Hover Cursor Logic):** Mọi phần tử có sự kiện click đều phải có `cursor-pointer`; phần tử bị disabled phải có `cursor-not-allowed opacity-50`.

### Nhóm 5: Containers, Depth & Cards (Quy tắc 41 – 48)
41. **Rule 41 (Card Container Justification):** Chỉ bọc thẻ Card khi khối đó thực sự cần click hoặc cần phân tách rõ rệt về độ cao thị giác.
42. **Rule 42 (Bento Visual Diversity):** Trong lưới Bento, tối thiểu 2 ô phải có nền khác biệt (1 ô có hình ảnh thực tế, 1 ô có màu nền nhấn). Cấm làm lưới 6 ô toàn nền trắng giống hệt nhau.
43. **Rule 43 (Glassmorphism Restraint):** Hiệu ứng kính mờ (Backdrop Blur) chỉ dùng khi có lớp nền di chuyển bên dưới (như thanh Navbar dính). Cấm gắn nền kính mờ vô tội vạ lên thẻ Card tĩnh.
44. **Rule 44 (Inner Stroke for Glass):** Khi dùng kính mờ, bắt buộc có viền trong mờ `border border-white/10` để tạo khúc xạ ánh sáng cạnh vật lý.
45. **Rule 45 (Consistent Corner Radius Scaling):** Bo góc bên trong (Inner Radius) = Bo góc bên ngoài (Outer Radius) - Padding. Cấm hiện tượng góc trong tròn hơn góc ngoài.
46. **Rule 46 (Divider Subtlety):** Đường phân cách (Divider) chỉ dùng độ mờ 5-10% (`divide-zinc-200/60 dark:divide-zinc-800/60`), không dùng đường kẻ đen đậm nét.
47. **Rule 47 (No Nested Cards):** Cấm nhét Card bên trong một Card khác trừ khi là danh sách chọn item độc lập.
48. **Rule 48 (Z-Index Hierarchy Standard):** Chuẩn hóa tầng Z-Index (Base: 0, Card Hover: 10, Sticky Nav: 40, Modal/Dialog: 50, Toast/Tooltip: 100).

### Nhóm 6: Imagery & Authenticity (Quy tắc 49 – 55)
49. **Rule 49 (Real Imagery over Div-Screenshots):** Cấm vẽ giao diện giả lập sản phẩm bằng các thẻ `<div>` lồng nhau. Hãy dùng hình chụp thật, render mockup hoặc preview component thật.
50. **Rule 50 (Social Proof Logo Purity):** Dải logo khách hàng/đối tác chỉ gồm các logo SVG đơn sắc. Không kèm chú thích ngành nghề phụ bên dưới logo.
51. **Rule 51 (Aspect Ratio Lock):** Hình ảnh trong lưới hoặc card phải dùng `aspect-video` hoặc `aspect-[4/3]` có `object-cover` để chống méo hình.
52. **Rule 52 (No Missing Image Placeholders):** Nếu chưa có hình ảnh thật, tạo vị trí rõ ràng kèm kích thước quy chuẩn, không để ảnh vỡ hoặc khung xám trơn không mục đích.
53. **Rule 53 (Accessible Alt Text):** Mọi thẻ `<img>` đều phải có thuộc tính `alt` mô tả ngữ nghĩa chính xác, không dùng `alt="image"`.
54. **Rule 54 (Single Icon Family):** Toàn trang chỉ dùng 1 bộ icon duy nhất (Phosphor, Radix, hoặc Tabler). Thống nhất độ dày nét vẽ (stroke-width: 1.5).
55. **Rule 55 (Emoji Ban in Professional UI):** Không dùng emoji làm icon đại diện cho tính năng chuyên nghiệp. Hãy dùng vector icon.

### Nhóm 7: Motion, Polish & Copywriting (Quy tắc 56 – 61)
56. **Rule 56 (Motivated Motion):** Mỗi chuyển động phải có lý do (hướng sự chú ý, phản hồi thao tác, kể chuyện). Cấm thêm animation chỉ vì "trông cho vui".
57. **Rule 57 (Spring Physics over Linear):** Sử dụng hàm chuyển động tự nhiên (Spring Physics hoặc Cubic-Bezier mượt mà `[0.16, 1, 0.3, 1]`). Tuyệt đối cấm `ease-in-out` tuyến tính chậm chạp.
58. **Rule 58 (Marquee Cap):** Dải chữ hoặc logo cuộn vô tận (Marquee) chỉ được xuất hiện tối đa 1 lần trên toàn bộ trang.
59. **Rule 59 (Prefers-Reduced-Motion):** Luôn tôn trọng tùy chọn hệ thống của người dùng bằng cách tắt hoặc tinh giản chuyển động với `useReducedMotion()`.
60. **Rule 60 (No AI Cliché Buzzwords):** Cấm tuyệt đối các từ ngữ sáo rỗng của AI: *"Elevate", "Seamless", "Unleash", "Next-gen", "Game-changing", "Delve", "Supercharge"*. Dùng câu văn cụ thể, thẳng thắn, nêu rõ giá trị sản phẩm.
61. **Rule 61 (No Fabricated Exact Metrics):** Không tự bịa ra các con số thống kê kỳ quặc như *"tăng hiệu suất 92.4%"*, *"tiết kiệm 4.7 giờ/ngày"* nếu không có dữ liệu thực tế từ brief của khách hàng.

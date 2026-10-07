---
name: vbhc-vietnamese-docx
description: Soạn thảo, định dạng và xuất file DOCX/PDF văn bản hành chính (NĐ 30/2020), Văn bản Đảng (HD 05-HD/VPTW), Văn bản Quân đội (TT 68/2024/TT-BQP), Báo cáo Đề án / Bài tập lớn APAG, và Báo cáo bài tập theo ngày / thực hành chuyên đề rút gọn. Tuân thủ 100% phong cách đen trắng công vụ, gạch đầu dòng chuẩn Việt Nam (- và +), chống đè chữ biểu đồ, tối ưu bảng biểu phân trang và khắc phục triệt để lỗi đánh số trang.
when_to_use: "Kích hoạt khi người dùng yêu cầu soạn thảo văn bản hành chính nhà nước (NĐ 30/2020), văn bản Đảng/Đoàn thể (HD 05), văn bản Quân đội (TT 68/2024), làm bài tập lớn học thuật, hoặc làm bài tập theo ngày / báo cáo thực hành chuyên đề rút gọn cho Học viện Hành chính Quốc gia (APAG) và các trường đại học."
allowed-tools: [Read, Write, Edit, Bash, Grep, Glob]
version: 1.4.0
effort: medium
---

# 📜 Soạn Thảo Văn Bản Hành Chính & Báo Cáo Học Thuật Đa Chuẩn (NĐ 30 - HD 05 - TT 68 - APAG)

> **Triết lý cốt lõi:** Tích hợp bộ quy chuẩn thể thức toàn diện của Việt Nam gồm 4 hệ thống văn bản: Hành chính Nhà nước (NĐ 30/2020/NĐ-CP); Tổ chức Đảng & Đoàn thể (HD 05-HD/VPTW); Quân đội & Quốc phòng (TT 68/2024/TT-BQP); và Báo cáo Đề án / Bài tập APAG. Định dạng 100% Đen - Trắng trang trọng cho văn bản; Gạch đầu dòng `-` và `+`; Sơ đồ kỹ thuật không đè chữ; Ảnh mô phỏng giao diện UI có màu sắc chuyên nghiệp; Tối ưu hóa bảng biểu chống tràn trang vỡ dòng; Khắc phục triệt để lỗi đánh số trang trong Word/PDF; Văn phong công vụ chính xác, loại bỏ triệt để từ ngữ sáo rỗng (Anti-AI Slop).

---

## 🎭 1. Bốn Chế Độ Soạn Thảo Chuyên Sâu (Quadruple Profiles)

Hệ thống tự động nhận diện hoặc cho phép lựa chọn 1 trong 4 chế độ:

1. **Profile `administrative-official` (Văn bản hành chính nhà nước - NĐ 30/2020/NĐ-CP)**:
   - **Áp dụng cho**: Cơ quan nhà nước, Bộ ngành, UBND, cơ quan hành chính sự nghiệp (Công văn, Tờ trình, Quyết định, Thông báo, Biên bản, Kế hoạch, Báo cáo).
   - **Thể thức**: 14 ô thành phần chuẩn mực. Bảng header không viền: Bên trái là Cơ quan ban hành + Số ký hiệu; Bên phải là Quốc hiệu (`CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM`) + Tiêu ngữ (`Độc lập - Tự do - Hạnh phúc`) có gạch chân 1/3 - 1/2 bằng graphic line. Nơi nhận không dùng ngoặc đơn.

2. **Profile `party-organization` (Văn bản Đảng & Đoàn thể - HD 05-HD/VPTW)**:
   - **Áp dụng cho**: Cơ quan Đảng, Ban Chấp hành, Chi bộ, Đảng ủy các cấp, Công đoàn, Đoàn Thanh niên.
   - **Thể thức đặc trưng**:
     * Tiêu đề góc phải: `ĐẢNG CỘNG SẢN VIỆT NAM` (In hoa, đứng, đậm).
     * Góc trái: Tên cơ quan Đảng cấp trên và Cấp ủy ban hành (In hoa, đứng).
     * Hệ thống văn loại: Nghị quyết, Chỉ thị, Quyết định của Cấp ủy, Kết luận, Báo cáo công tác Đảng, Giấy giới thiệu sinh hoạt Đảng.
     * Thẩm quyền ký: Thay mặt Ban Chấp hành (`T/M BAN CHẤP HÀNH`), `BÍ THƯ`, `PHÓ BÍ THƯ` hoặc `K/T BÍ THƯ` (Ký thay Bí thư).

3. **Profile `military-defense` (Văn bản Quân đội nhân dân Việt Nam - TT 68/2024/TT-BQP)**:
   - **Áp dụng cho**: Các đơn vị Quân đội, Bộ Chỉ huy Quân sự, Ban CHQS, Quân khu, Quân đoàn, Viện nghiên cứu quốc phòng.
   - **Thể thức đặc trưng**:
     * Thẩm quyền và chức vụ chỉ huy quân sự nghiêm ngặt: `TƯ LỆNH`, `CHỈ HUY TRƯỞNG`, `CHÍNH ỦY`, `THAM MƯU TRƯỞNG`.
     * Quản lý con dấu độ mật: Dấu khung chữ nhật in hoa đậm đỏ/đen ở góc trái trên cùng (`TUYỆT MẬT`, `TỐI MẬT`, `MẬT`) kèm số lượng bản in và phạm vi lưu hành.
     * Hệ thống văn bản tác chiến: Mệnh lệnh huấn luyện, Kế hoạch sẵn sàng chiến đấu (SSCĐ), Lệnh điều động, Báo cáo quân số - trang bị kỹ thuật.

4. **Profile `academic-coursework` (Đề án & Báo cáo học thuật APAG)**:
   - **Nhánh 4A - `academic-project` (Bài tập lớn / Đề án môn học / Khóa luận tốt nghiệp)**:
     * Đầy đủ khung viền đôi trang bìa, các trang thủ tục (Lời cảm ơn, Lời cam đoan, Danh mục từ viết tắt, Danh mục hình ảnh/bảng biểu, Mục lục tự động).
     * Phần mở đầu chuẩn 6 mục (Lý do chọn đề tài, Mục tiêu, Đối tượng & phạm vi, Phương pháp nghiên cứu, Ý nghĩa thực tiễn, Kết cấu đề tài).
     * 3 Chương nội dung hoàn chỉnh, bắt buộc có đặc tả Use Case, sơ đồ Use Case, CSDL chi tiết, Kết luận và Tài liệu tham khảo.
   - **Nhánh 4B - `daily-assignment-report` (Bài tập theo ngày / Báo cáo thực hành chuyên đề rút gọn)**:
     * **KHÔNG CẦN các phần thủ tục rườm rà**: Không trang bìa riêng, không Lời cảm ơn, không Lời cam đoan, không Danh mục từ viết tắt, không Phần mở đầu hình thức.
     * **KHÔNG CẦN VẼ USE CASE (UC)**: Trừ khi có yêu cầu thêm cụ thể từ người dùng.
     * **Header tinh gọn đầu trang 1**: Khối cơ sở đào tạo (`HỌC VIỆN HÀNH CHÍNH QUỐC GIA (APAG)` / `KHOA HỆ THỐNG THÔNG TIN QUẢN LÝ`) đặt song song Quốc hiệu hoặc thông tin học phần. Dùng đường kẻ hình học thật (`canvas.line` hoặc viền bảng Word), **tuyệt đối không dùng ký tự Unicode `─`, `━`** vì font Times New Roman bị lỗi ô vuông `□□□□`.
     * **Khối định danh sinh viên**: Tiêu đề báo cáo $\to$ Họ tên, Mã sinh viên, Lớp, Giảng viên hướng dẫn, Ngày nộp (3-4 dòng). **TUYỆT ĐỐI KHÔNG ĐÓNG KHUNG HỘP (NO BORDER BOX)**, để text tự nhiên dưới dạng bảng không viền; **CẤM DÙNG CHẤM ĐEN (`•`)**, bắt buộc dùng gạch đầu dòng ngang `- `.
     * **Đi thẳng vào nội dung kỹ thuật (Direct-to-content)**: Các mục I, II, III... trình bày trực tiếp bài toán, kiến trúc hệ thống, phân tích số liệu, luồng quy trình và Dashboard giao diện.

---

## 📑 2. Động Cơ Đánh Số Trang Tuyệt Đối (Bulletproof Page Numbering Engine)

### 2.1. Phân tích Nguyên nhân Gốc rễ Lỗi Số Trang ở các Công cụ Soạn thảo Truyền thống
Các tiện ích mở rộng macro/VSTO truyền thống trong Word thường gặp lỗi số trang bị đóng băng ở số 1, hiển thị trùng lặp, hoặc mất trắng khi chuyển trang vì 3 sai lầm kiến trúc:
1. **Xung đột kép trong Word Object Model**: Gọi đồng thời `HeaderFooter.PageNumbers.RestartNumberingAtSection = true` VÀ chèn thủ công trường `Fields.Add(Range, WdFieldType.wdFieldPage)`. Sự can thiệp kép này làm bộ nhớ đệm bố cục (Layout Cache) của Word mất đồng bộ, dẫn đến việc số trang bị kẹt ở "Trang 1".
2. **Hàm xóa dọn dẹp quét nhầm (Destructive Header Erasure)**: Dùng regex lỏng lẻo `^(Trang\s*)?\d*(\s*/\s*\d*)?$` rồi gọi `ClearHeaderFooter()`, vô tình xóa sạch mọi Header/Footer khác đang có trên tài liệu.
3. **Mất liên kết Section (Section Unlinking Failure)**: Đặt `DifferentFirstPageHeaderFooter = true` ở Section 1 nhưng không ngắt thuộc tính `LinkToPrevious = false` ở các Section tiếp theo, làm số trang bị kế thừa và ghi đè lộn xộn giữa trang bìa, mục lục và nội dung.

### 2.2. Quy trình Xử lý Số Trang Chuẩn Tuyệt đối (Word & PDF)
- **Trong file Word (.docx) qua OpenXML / python-docx**:
  ```python
  # Thiết lập Header trang đầu rỗng và đánh số trang từ trang 2 trở đi
  section = doc.sections[0]
  section.different_first_page_header_footer = True
  header = section.header
  # Đảm bảo section.first_page_header để trống hoàn toàn (Trang 1 không có số trang)
  p = header.paragraphs[0]
  p.alignment = WD_ALIGN_PARAGRAPH.CENTER
  # Chèn trực tiếp XML field mã sạch, không gọi hàm COM/VSTO chồng chéo
  fldSimple = parse_xml(r'<w:fldSimple %s w:instr="PAGE"/>' % nsdecls('w'))
  p._p.append(fldSimple)
  ```
- **Trong file PDF (ReportLab Canvas)**:
  Sử dụng mô hình **Two-Pass NumberedCanvas**: Lần chạy 1 (Pass 1) đếm và lưu tổng số trang; Lần chạy 2 (Pass 2) chỉ vẽ số trang nếu `page_num > 1` (bỏ qua trang bìa/tiêu đề), căn giữa chuẩn xác ở đỉnh đầu trang hoặc chân trang theo quy chuẩn NĐ 30.

---

## 📊 3. Bộ Tối Ưu Bảng Biểu Nâng Cao (Table Optimizer Engine)

Khi tạo bảng trong tài liệu hành chính và học thuật, bắt buộc áp dụng 4 nguyên tắc sau để bảng không bao giờ bị tràn trang vỡ layout:

1. **Phân biệt Bảng Bố cục (Layout Table) và Bảng Dữ liệu (Data Table)**:
   - *Layout Table* (Header, chữ ký, nơi nhận, thông tin sinh viên): Không viền (`None`), không lặp dòng tiêu đề, padding 0pt.
   - *Data Table* (Bảng thống kê, KPI, ma trận RACI, đặc tả CSDL): Toàn bộ viền đơn đen mỏng 0.5pt (`#000000`), nền tiêu đề xám nhẹ (`#F2F2F2`) hoặc trắng tinh.
2. **Bắt buộc Lặp lại Dòng Tiêu đề (Repeat Header Rows - `<w:tblHeader/>`)**:
   - Mọi bảng dữ liệu dài $\ge 2$ trang bắt buộc phải gán thuộc tính `tblHeader` cho hàng tiêu đề (Row 0):
     ```python
     trPr = row._tr.get_or_add_trPr()
     trPr.append(parse_xml(r'<w:tblHeader %s/>' % nsdecls('w')))
     ```
   - Đảm bảo khi bảng tràn sang trang sau, người đọc vẫn thấy rõ các cột mà không cần lật lại trang trước.
3. **Bắt buộc Chống Tách Đôi Dòng (Keep Row Together - `<w:cantSplit/>`)**:
   - Tất cả các dòng dữ liệu trong bảng phải có thuộc tính `cantSplit`:
     ```python
     trPr = row._tr.get_or_add_trPr()
     trPr.append(parse_xml(r'<w:cantSplit %s/>' % nsdecls('w')))
     ```
   - Ngăn chặn triệt để hiện tượng 1 ô dữ liệu bị xé đôi một nửa ở cuối trang này và một nửa ở đầu trang sau.
4. **Quy chuẩn Cột Số thứ tự (STT)**:
   - Cột STT luôn được cố định độ rộng từ **1.0 cm đến 1.2 cm**, căn giữa toàn bộ dữ liệu theo cả chiều ngang và chiều dọc.

---

## 🧹 4. Bộ Lọc Định Dạng & Chuẩn Hóa Văn Bản (Format Linter & Regex Sanitizer)

Trước khi xuất file, văn bản phải được quét và chuẩn hóa qua các bộ lọc tự động:

1. **Chuẩn hóa Gạch đầu dòng (List Normalizer)**:
   - Loại bỏ toàn bộ các ký tự bullet rác / ký tự lạ:
     * Regex: `r'^(\-{2,}|\-\s+\-|\*\s*\-|\+\s*\-|\*|•|o|||–|—|·)\s*'`
     * Quy đổi tự động:
       - Cấp 1 (Ý chính) $\to$ Bắt buộc dùng `- ` (gạch ngang và 1 dấu cách).
       - Cấp 2 (Ý chi tiết) $\to$ Bắt buộc dùng `+ ` (dấu cộng và 1 dấu cách).
       - Cấp 3 (Tiểu tiết) $\to$ Dùng `a)`, `b)`, `c)`.
2. **Khử Khoảng trắng thừa trước dấu câu (Punctuation Spacing)**:
   - Regex tìm kiếm: `r'\s+([.,;:!?])'` $\to$ Thay thế bằng `$1` (viết liền sau ký tự chữ, theo sau là 1 khoảng trắng).
3. **Khử Dòng trống & Ngắt trang thừa**:
   - Thay thế các đoạn ngắt dòng liên tiếp $\ge 3$ lần (`\n{3,}`) bằng 1 lần ngắt dòng duy nhất để tài liệu luôn cô đọng, chặt chẽ.
4. **Thụt đầu dòng đoạn văn chuẩn**:
   - Thụt đầu dòng dòng đầu tiên (*First Line Indent*): Cố định **1.0 cm - 1.27 cm** (tương đương 0.5 inch).

---

## 🎨 5. Quy Chuẩn Sơ Đồ & Dashboard Giao Diện (Chống Đè Chữ Tuyệt Đối)

1. **Biểu đồ tròn (Donut / Pie Chart)**:
   - **TUYỆT ĐỐI KHÔNG dùng `explode`** trên biểu đồ dạng vòng (Donut) để đảm bảo vòng tròn hoàn toàn liền mạch, ăn khớp tuyệt đối, không lệch tâm.
   - **Không in số đè lên lát cắt nhỏ ($\le 8\%$)**: Các lát cắt nhỏ phải dùng hộp Chú giải (Legend) riêng biệt đặt bên cạnh (bên phải hoặc phía dưới) để tránh hoàn toàn hiện tượng số bị che hoặc đè chữ.
   - Đặt tổng số phần trăm (`100%`) hoặc chỉ số tóm tắt vào chính giữa tâm vòng tròn một cách trang nhã.
2. **Biểu đồ mạng nhện (Radar Chart)**:
   - Giới hạn trục (`ylim`) dư $15\% - 20\%$ so với giá trị đo tối đa để đỉnh đồ thị không chạm hoặc đè lên nhãn danh mục bên ngoài.
   - Đặt nhãn có khoảng cách đệm an toàn với tiêu đề biểu đồ.
3. **Khoảng cách giữa các ô biểu đồ con (Multi-subplot spacing)**:
   - Khoảng cách ngang (`wspace`) và dọc (`hspace`) giữa các biểu đồ con trong Dashboard tối thiểu $\ge 0.40 - 0.45$.
   - Tên các danh mục trên trục Y của biểu đồ thanh ngang nằm ở cột bên phải phải được cô đọng (ví dụ: `Khối SX`, `Cty TV-A`) để nhãn không bao giờ lấn sang vùng vẽ hoặc chạm vào biểu đồ bên trái.
4. **Tỉ lệ khung hình (Aspect Ratio)**:
   - Khi nhúng ảnh biểu đồ / Dashboard vào tài liệu PDF/Word, **BẮT BUỘC giữ đúng tỉ lệ khung hình gốc** của ảnh (ví dụ tỉ lệ 13.0 : 8.2 $\to$ rộng 15.5cm thì cao 9.8cm).
   - Tuyệt đối không nén ép chiều cao làm méo hình tròn thành hình elip và chèn đè lên dòng chú thích (Caption) phía dưới.
5. **Màu sắc Dashboard Giao diện**:
   - Ảnh chụp hoặc vẽ mô phỏng UI/Dashboard: Dùng hệ màu hiện đại chuyên nghiệp (Xanh Navy `#1E3A8A`, Xanh ngọc `#0D9488`, Xanh lá `#10B981`, Cam `#F59E0B`, Xám `#64748B`) để phản ánh trực quan phần mềm thật.

---

## 📏 6. Thông Số Kỹ Thuật Canh Lề & Font Chữ Chuẩn Quốc Gia

- **Khổ giấy**: A4 Portrait (210 mm × 297 mm).
- **Font chữ**: Times New Roman 100%, bảng mã Unicode chuẩn TCVN 6909:2001.
- **Canh lề trang (Page Margins)**:
  - Lề trên (*Top*): **2.0 cm - 2.5 cm**.
  - Lề dưới (*Bottom*): **2.0 cm - 2.5 cm**.
  - Lề trái (*Left*): **3.0 cm - 3.5 cm** (chừa gáy đóng tập).
  - Lề phải (*Right*): **1.5 cm - 2.0 cm**.
- **Giãn dòng (Line Spacing)**: 1.3 - 1.5 lines, Before 0pt, After 3-6pt. Thụt đầu dòng 1.0 - 1.27cm.
- **Văn phong công vụ (Anti-AI Slop)**: Trực diện, chuẩn mực hành chính, viện dẫn căn cứ pháp luật rõ ràng, cấm tuyệt đối các cụm từ sáo rỗng AI.

"""VBHC Document Builder — Chuẩn thể thức Nghị định 30/2020/NĐ-CP, HD 05-HD/VPTW, TT 68/2024/TT-BQP.
Kết hợp giải pháp kỹ thuật OpenXML tầng thấp giải quyết triệt để các hạn chế của python-docx:
  1. Gạch chân ngắn dưới Tiêu ngữ (độ dài bằng 1/3 - 1/2) và Tên cơ quan ban hành.
  2. Bảng 2 cột header (Quốc hiệu & Cơ quan) không viền, sticky column width.
  3. Lề trang chuẩn mm: Trái 30mm, Phải 15mm, Trên 20mm, Dưới 20mm.
  4. Căn chỉnh bảng full content 165mm sát lề.
  5. Thiết lập font Times New Roman và East Asian fonts đầy đủ.
  6. Động cơ đánh số trang sạch OpenXML (Bulletproof Page Numbering) không xung đột VSTO/COM.
  7. Bộ tối ưu bảng biểu nâng cao (Table Optimizer): w:tblHeader (lặp header) và w:cantSplit (chống vỡ dòng).
  8. Bộ lọc chuẩn hóa văn bản regex (Format Linter & Sanitizer).
"""

from __future__ import annotations
import re
import sys
from docx import Document
from docx.shared import Pt, Cm, Twips, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.enum.table import WD_TABLE_ALIGNMENT, WD_ALIGN_VERTICAL
from docx.oxml import OxmlElement, parse_xml
from docx.oxml.ns import qn, nsdecls


# ============================================================
# Low-level XML Helpers
# ============================================================

def make_element(tag: str, attrs: dict | None = None) -> OxmlElement:
    """Tạo OxmlElement với namespace đúng."""
    el = OxmlElement(tag)
    if attrs:
        for k, v in attrs.items():
            el.set(qn(k), str(v))
    return el


def set_paragraph_borders(p, *, bottom=None):
    """Thêm border cho đoạn văn bản (dùng để gạch chân tiêu ngữ).
    bottom: dict {val='single', sz=6, space=1, color='000000'}
    """
    pPr = p._p.get_or_add_pPr()
    existing = pPr.find(qn('w:pBdr'))
    if existing is not None:
        pPr.remove(existing)
    pBdr = make_element('w:pBdr')
    if bottom:
        attrs = {
            'w:val': bottom.get('val', 'single'),
            'w:sz': str(bottom.get('sz', 6)),
            'w:space': str(bottom.get('space', 1)),
            'w:color': bottom.get('color', '000000'),
        }
        pBdr.append(make_element('w:bottom', attrs))
        pPr.append(pBdr)


def set_paragraph_indent(p, *, left_twips: int | None = None, right_twips: int | None = None,
                         first_line_twips: int | None = None):
    """Set căn lề đoạn văn theo đơn vị twips (1cm ≈ 567 twips, 1pt = 20 twips)."""
    pPr = p._p.get_or_add_pPr()
    ind = pPr.find(qn('w:ind'))
    if ind is None:
        ind = make_element('w:ind')
        pPr.append(ind)
    if left_twips is not None:
        ind.set(qn('w:left'), str(left_twips))
    if right_twips is not None:
        ind.set(qn('w:right'), str(right_twips))
    if first_line_twips is not None:
        ind.set(qn('w:firstLine'), str(first_line_twips))


def set_paragraph_spacing(p, *, before_pt: float = 0, after_pt: float = 0, line_spacing: float = 1.3):
    """Căn giãn dòng và giãn đoạn theo chuẩn NĐ 30."""
    pPr = p._p.get_or_add_pPr()
    spacing = pPr.find(qn('w:spacing'))
    if spacing is None:
        spacing = make_element('w:spacing')
        pPr.append(spacing)
    spacing.set(qn('w:before'), str(int(before_pt * 20)))
    spacing.set(qn('w:after'), str(int(after_pt * 20)))
    # Giãn dòng hệ số 1.3 - 1.5 line (240 twips = 1.0 line)
    spacing.set(qn('w:line'), str(int(line_spacing * 240)))
    spacing.set(qn('w:lineRule'), 'auto')


def set_run_font(run, font_name="Times New Roman", size_pt=13, bold=False, italic=False, color_rgb=(0,0,0)):
    """Áp dụng font chữ Times New Roman và cấu hình EastAsian/cs để tránh lỗi hiển thị font trên Word máy khác."""
    run.font.name = font_name
    run.font.size = Pt(size_pt)
    run.bold = bold
    run.italic = italic
    run.font.color.rgb = RGBColor(*color_rgb)
    rPr = run._r.get_or_add_rPr()
    rFonts = rPr.find(qn('w:rFonts'))
    if rFonts is None:
        rFonts = make_element('w:rFonts')
        rPr.append(rFonts)
    rFonts.set(qn('w:ascii'), font_name)
    rFonts.set(qn('w:hAnsi'), font_name)
    rFonts.set(qn('w:cs'), font_name)
    rFonts.set(qn('w:eastAsia'), font_name)


def clear_cell_margins(cell):
    """Xóa padding của cell để chữ sát mép cột bảng."""
    tcPr = cell._tc.get_or_add_tcPr()
    tcMar = make_element('w:tcMar')
    for m in ('top', 'bottom', 'left', 'right'):
        node = make_element(f'w:{m}', {'w:w': '0', 'w:type': 'dxa'})
        tcMar.append(node)
    tcPr.append(tcMar)


def remove_table_borders(table):
    """Làm cho bảng hoàn toàn không viền (borderless)."""
    tblPr = table._tbl.tblPr
    existing = tblPr.find(qn('w:tblBorders'))
    if existing is not None:
        tblPr.remove(existing)
    tblBorders = make_element('w:tblBorders')
    for border in ('top', 'left', 'bottom', 'right', 'insideH', 'insideV'):
        tblBorders.append(make_element(f'w:{border}', {'w:val': 'none'}))
    tblPr.append(tblBorders)


# ============================================================
# Advanced Engine Functions (v1.4.0)
# ============================================================

def setup_vbhc_page_numbering(doc: Document, header_or_footer: str = "header"):
    """Động cơ đánh số trang chuẩn tuyệt đối (Bulletproof Page Numbering):
    - Khắc phục triệt để lỗi phân trang: Bỏ qua Word COM Object Model, dùng trực tiếp mã trường OpenXML sạch.
    - Dùng mã trường OpenXML sạch w:fldSimple w:instr="PAGE".
    - Trang 1 không hiện số trang (different_first_page_header_footer = True).
    - Trang 2 trở đi hiển thị số trang Ả Rập, cỡ 13pt Times New Roman, căn giữa đỉnh trang (hoặc chân trang).
    """
    for section in doc.sections:
        section.different_first_page_header_footer = True
        target = section.header if header_or_footer == "header" else section.footer
        p = target.paragraphs[0] if target.paragraphs else target.add_paragraph()
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_paragraph_spacing(p, before_pt=0, after_pt=0)
        
        # Thêm field mã sạch OpenXML
        fld = parse_xml(r'<w:fldSimple %s w:instr="PAGE"/>' % nsdecls('w'))
        p._p.append(fld)
        
        # Đảm bảo run trong paragraph nhận font Times New Roman 13pt
        for r in p.runs:
            set_run_font(r, font_name="Times New Roman", size_pt=13, bold=False, color_rgb=(0, 0, 0))


def optimize_data_table(table, col_widths: list | None = None, is_header_grey: bool = True):
    """Bộ tối ưu bảng biểu nâng cao (Table Optimizer Engine):
    1. w:tblHeader: Bắt buộc lặp lại dòng tiêu đề khi bảng tràn sang trang mới.
    2. w:cantSplit: Bắt buộc chống xé đôi dữ liệu của từng dòng qua trang.
    3. Cố định độ rộng từng cột sát lề văn bản.
    4. Viền đơn đen mỏng 0.5pt, nền header F2F2F2.
    """
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    
    # 1. tblHeader cho dòng tiêu đề đầu tiên
    if len(table.rows) > 0:
        header_tr = table.rows[0]._tr.get_or_add_trPr()
        if header_tr.find(qn('w:tblHeader')) is None:
            header_tr.append(parse_xml(r'<w:tblHeader %s/>' % nsdecls('w')))

    # 2. cantSplit cho toàn bộ các dòng
    for row in table.rows:
        trPr = row._tr.get_or_add_trPr()
        if trPr.find(qn('w:cantSplit')) is None:
            trPr.append(parse_xml(r'<w:cantSplit %s/>' % nsdecls('w')))

    # 3. Format viền và nền ô
    for r_idx, row in enumerate(table.rows):
        for c_idx, cell in enumerate(row.cells):
            if col_widths and c_idx < len(col_widths):
                cell.width = col_widths[c_idx]
            cell.vertical_alignment = WD_ALIGN_VERTICAL.CENTER
            tcPr = cell._tc.get_or_add_tcPr()
            borders = parse_xml(
                f'<w:tcBorders {nsdecls("w")}>\n'
                f'  <w:top w:val="single" w:sz="4" w:space="0" w:color="000000"/>\n'
                f'  <w:left w:val="single" w:sz="4" w:space="0" w:color="000000"/>\n'
                f'  <w:bottom w:val="single" w:sz="4" w:space="0" w:color="000000"/>\n'
                f'  <w:right w:val="single" w:sz="4" w:space="0" w:color="000000"/>\n'
                f'</w:tcBorders>'
            )
            tcPr.append(borders)
            if r_idx == 0 and is_header_grey:
                shd = parse_xml(f'<w:shd {nsdecls("w")} w:fill="F2F2F2"/>')
                tcPr.append(shd)


def sanitize_vietnamese_text(text: str) -> str:
    """Bộ lọc chuẩn hóa văn bản regex (Format Linter & Sanitizer):
    1. Chuẩn hóa gạch đầu dòng: Chuyển toàn bộ bullet dị tật về -
    2. Khử khoảng trắng thừa trước dấu câu (.,;:!?)
    3. Chuẩn hóa dấu phẩy, dấu chấm
    """
    if not text:
        return ""
    # Chuyển đổi ký tự bullet lạ ở đầu dòng
    text = re.sub(r'^(\-{2,}|\-\s+\-|\*\s*\-|\+\s*\-|\*|•|o|||–|—|·)\s*', '- ', text)
    # Khử khoảng trắng trước dấu câu
    text = re.sub(r'\s+([.,;:!?])', r'\1', text)
    # Khử khoảng trắng kép
    text = re.sub(r'[ ]{2,}', ' ', text)
    return text.strip()


# ============================================================
# High-level Document Builders
# ============================================================

def create_vbhc_document() -> Document:
    """Tạo document A4 với lề chuẩn Nghị định 30/2020/NĐ-CP."""
    doc = Document()
    for section in doc.sections:
        section.page_width = Cm(21.0)
        section.page_height = Cm(29.7)
        section.top_margin = Cm(2.0)
        section.bottom_margin = Cm(2.0)
        section.left_margin = Cm(3.0)
        section.right_margin = Cm(1.5)
        section.different_first_page_header_footer = True
    return doc


def add_vbhc_header(
    doc: Document,
    co_quan_chu_quan: str,
    co_quan_ban_hanh: str,
    so_ky_hieu: str,
    dia_danh: str,
    thang: str = "10",
    nam: str = "2026",
    is_cong_van: bool = True,
    trich_yeu: str = ""
):
    """Tạo khối đầu trang gồm Quốc hiệu, Cơ quan ban hành, Số ký hiệu, Ngày tháng chuẩn NĐ 30."""
    table = doc.add_table(rows=1, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    remove_table_borders(table)

    col_left_width = Cm(7.5)
    col_right_width = Cm(9.0)

    row = table.rows[0]
    cell_left = row.cells[0]
    cell_right = row.cells[1]
    cell_left.width = col_left_width
    cell_right.width = col_right_width
    clear_cell_margins(cell_left)
    clear_cell_margins(cell_right)

    # --- CỘT TRÁI: Cơ quan ban hành ---
    p_cq1 = cell_left.paragraphs[0]
    p_cq1.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_paragraph_spacing(p_cq1, before_pt=0, after_pt=0, line_spacing=1.1)
    if co_quan_chu_quan:
        run_cq1 = p_cq1.add_run(co_quan_chu_quan.upper())
        set_run_font(run_cq1, size_pt=12, bold=False)

    p_cq2 = cell_left.add_paragraph()
    p_cq2.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_paragraph_spacing(p_cq2, before_pt=2, after_pt=2, line_spacing=1.1)
    run_cq2 = p_cq2.add_run(co_quan_ban_hanh.upper())
    set_run_font(run_cq2, size_pt=12, bold=True)
    # Đường kẻ ngắn dưới tên cơ quan (cách 2 mép 1000 twips)
    set_paragraph_borders(p_cq2, bottom={'val': 'single', 'sz': 6, 'space': 2, 'color': '000000'})
    set_paragraph_indent(p_cq2, left_twips=1000, right_twips=1000)

    p_so = cell_left.add_paragraph()
    p_so.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_paragraph_spacing(p_so, before_pt=6, after_pt=0, line_spacing=1.1)
    run_so = p_so.add_run(f"Số: {so_ky_hieu}")
    set_run_font(run_so, size_pt=12, bold=False)

    if is_cong_van and trich_yeu:
        p_ty = cell_left.add_paragraph()
        p_ty.alignment = WD_ALIGN_PARAGRAPH.CENTER
        set_paragraph_spacing(p_ty, before_pt=2, after_pt=0, line_spacing=1.1)
        run_ty = p_ty.add_run(f"V/v {trich_yeu}")
        set_run_font(run_ty, size_pt=11, italic=True)

    # --- CỘT PHẢI: Quốc hiệu, Tiêu ngữ, Ngày tháng ---
    p_qh = cell_right.paragraphs[0]
    p_qh.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_paragraph_spacing(p_qh, before_pt=0, after_pt=0, line_spacing=1.1)
    run_qh = p_qh.add_run("CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM")
    set_run_font(run_qh, size_pt=12, bold=True)

    p_tn = cell_right.add_paragraph()
    p_tn.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_paragraph_spacing(p_tn, before_pt=2, after_pt=2, line_spacing=1.1)
    run_tn = p_tn.add_run("Độc lập - Tự do - Hạnh phúc")
    set_run_font(run_tn, size_pt=13, bold=True)
    # Đường kẻ ngang nét liền dài bằng dòng chữ
    set_paragraph_borders(p_tn, bottom={'val': 'single', 'sz': 8, 'space': 2, 'color': '000000'})
    set_paragraph_indent(p_tn, left_twips=650, right_twips=650)

    p_date = cell_right.add_paragraph()
    p_date.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_paragraph_spacing(p_date, before_pt=6, after_pt=0, line_spacing=1.1)
    run_date = p_date.add_run(f"{dia_danh}, ngày        tháng {thang} năm {nam}")
    set_run_font(run_date, size_pt=13, italic=True)

    # Thêm khoảng trống sau header
    p_spacer = doc.add_paragraph()
    set_paragraph_spacing(p_spacer, before_pt=6, after_pt=6)


def add_vbhc_signature_block(
    doc: Document,
    noi_nhan_list: list[str],
    chuc_vu: str,
    ho_ten: str,
    chuc_danh_phu: str = ""
):
    """Tạo khối Nơi nhận & Chữ ký người có thẩm quyền chuẩn NĐ 30."""
    table = doc.add_table(rows=1, cols=2)
    table.alignment = WD_TABLE_ALIGNMENT.CENTER
    remove_table_borders(table)

    col_left_width = Cm(8.0)
    col_right_width = Cm(8.5)

    row = table.rows[0]
    cell_nn = row.cells[0]
    cell_sign = row.cells[1]
    cell_nn.width = col_left_width
    cell_sign.width = col_right_width
    clear_cell_margins(cell_nn)
    clear_cell_margins(cell_sign)

    # Nơi nhận (Bên trái)
    p_nn_head = cell_nn.paragraphs[0]
    set_paragraph_spacing(p_nn_head, before_pt=6, after_pt=2, line_spacing=1.0)
    run_nn_head = p_nn_head.add_run("Nơi nhận:")
    set_run_font(run_nn_head, size_pt=12, bold=True, italic=True)

    for item in noi_nhan_list:
        p_item = cell_nn.add_paragraph()
        set_paragraph_spacing(p_item, before_pt=1, after_pt=1, line_spacing=1.0)
        run_item = p_item.add_run(f"- {item};" if not item.startswith("-") else item)
        set_run_font(run_item, size_pt=11, bold=False)

    # Chữ ký (Bên phải)
    p_pos = cell_sign.paragraphs[0]
    p_pos.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_paragraph_spacing(p_pos, before_pt=6, after_pt=2, line_spacing=1.1)

    if chuc_danh_phu:
        run_cd = p_pos.add_run(f"{chuc_danh_phu.upper()}\n")
        set_run_font(run_cd, size_pt=13, bold=True)

    run_cv = p_pos.add_run(chuc_vu.upper())
    set_run_font(run_cv, size_pt=13, bold=True)

    # Khoảng cách 3-4 dòng để ký và đóng dấu
    p_space = cell_sign.add_paragraph()
    set_paragraph_spacing(p_space, before_pt=36, after_pt=0)

    p_name = cell_sign.add_paragraph()
    p_name.alignment = WD_ALIGN_PARAGRAPH.CENTER
    set_paragraph_spacing(p_name, before_pt=0, after_pt=0, line_spacing=1.1)
    run_name = p_name.add_run(ho_ten)
    set_run_font(run_name, size_pt=13, bold=True)

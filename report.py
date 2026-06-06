from fpdf import FPDF

def create_pdf(records):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, txt="Attendance Report", ln=True)

    for r in records:
        pdf.cell(200, 10, txt=str(r), ln=True)

    pdf.output("attendance_report.pdf")
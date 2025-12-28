from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def gerar_relatorio_processo(path, processo):
    c = canvas.Canvas(path, pagesize=letter)
    c.setFont("Helvetica", 12)
    c.drawString(50, 750, f"Relatório do Processo: {processo.numero}")
    c.drawString(50, 730, f"Parte: {processo.parte or '-'}")
    c.drawString(50, 710, f"Status: {processo.status}")
    c.drawString(50, 690, f"Descrição: {processo.descricao or '-'}")
    c.save()

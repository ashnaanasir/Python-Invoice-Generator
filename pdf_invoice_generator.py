"""CSC111 Winter 2021 Final Project: UK VAT Invoice Generation

Instructions
===============================

This python module contains the function that creates the pdf invoice using reportlab.

Copyright Information
===============================

This file is Copyright (c) 2021 Ayesha Nasir.
"""
from classes_data import Invoice, Vendor, Payer
from reportlab.platypus import Paragraph, Spacer, SimpleDocTemplate, Table, TableStyle
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.colors import blue, black


def create_invoice(inv: Invoice) -> None:
    """
    Generates the reportlab pdf invoice
    """
    vendor = inv.vendor
    payer = inv.payer
    service = inv.services[0]
    unit_price = inv.services[1]
    amount = inv.services[2]
    total_bt = float(inv.services[1]) * float(inv.services[2])
    vat = vendor.info['vat_rate']
    total_at = (total_bt * float(vendor.info['vat_rate'])) + total_bt

    title = f'Invoice'
    vendor_name = vendor.name
    vendor_address = vendor.address
    vendor_phone = vendor.info['phone']
    vendor_email = vendor.info['email']

    payer_name = payer.name
    payer_address = payer.address
    payer_phone = payer.info['phone']
    payer_email = payer.info['email']

    due = f'This invoice is due in: {inv.info["due"]}'

    # creating the doc structure:
    doc = SimpleDocTemplate(f'Invoices/invoice.pdf', pagesize=letter, rightMargin=72,
                            leftMargin=72, topMargin=72, bottomMargin=18,
                            title=f'Invoice for Payment',
                            author='XYZ Accountants')

    invoice_data = [
        ('Payer', 'Vendor'),
        (payer_name, vendor_name),
        (payer_address, vendor_address),
        (payer_phone, vendor_phone),
        (payer_email, vendor_email),
    ]
    t = Table(invoice_data, colWidths=4*inch)
    t.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                           ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
                           ('TEXTCOLOR', (0, 0), (1, 0), blue)
                           ]))

    sec_table = [
        ('Services Rendered', 'Unit Price', 'Amount', 'Net', 'Vat', 'Gross'),
        (service, unit_price, amount, total_bt, vat, total_at)
    ]
    s_t = Table(sec_table, colWidths=1.3*inch)
    s_t.setStyle(TableStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                             ('LINEABOVE', (0, 1), (-1, 1), 1, black)]))

    styles = getSampleStyleSheet()  # for the styles used in the document.
    story = []
    story.append(Paragraph(title, styles['Title']))
    story.append(Spacer(1, 12))
    story.append(t)
    story.append(Spacer(1, 12))
    story.append(Spacer(1, 12))
    story.append(Spacer(1, 12))
    story.append(s_t)
    story.append(Spacer(1, 12))
    story.append(Spacer(1, 12))
    story.append(Spacer(1, 12))
    story.append(Spacer(1, 12))
    story.append(Spacer(1, 12))
    story.append(Spacer(1, 12))
    story.append(Paragraph(due, styles['BodyText']))
    doc.build(story)

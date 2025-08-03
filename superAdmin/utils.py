from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from io import BytesIO
from django.core.files.base import ContentFile

def generate_id_card_pdf(id_card):
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    width, height = letter
    
    # Draw the ID card content
    c.drawString(100, height - 100, f"Name: {id_card.first_name}")
    c.drawString(100, height - 130, f"Employee ID: {id_card.id}")
    c.drawString(100, height - 160, f"Department: {id_card.last_name}")
    c.drawString(100, height - 190, f"Position: {id_card.email}")
    
    # Draw the photo
    # if id_card.user_profile:
    #     c.drawImage(id_card.user_profile, 100, height - 250, width=100, height=100)
    
    c.save()
    buffer.seek(0)
    
    return ContentFile(buffer.read(), 'id_card.pdf')

import os
from docx import Document
from io import BytesIO
from docxtpl import DocxTemplate
from datetime import datetime 
import uuid
def generate_document(template_name, contexts, output_stream):
    # Charger le modèle principal
    
    template = DocxTemplate(template_name)

    # Rendre le modèle deux fois
    doc1_stream = BytesIO()
    template.render(contexts[0])
    
    template.save(doc1_stream)
    doc1_stream.seek(0)

    doc2_stream = BytesIO()
    template.render(contexts[1])
    template.save(doc2_stream)
    doc2_stream.seek(0)

    # Fusionner les deux documents
    doc1 = Document(doc1_stream)
    doc2 = Document(doc2_stream)
    doc1.add_page_break()

    # Ajouter chaque élément du second document au premier document
    for element in doc2.element.body:
        doc1.element.body.append(element)
        
 
    # Sauvegarder le document fusionné
    doc1.save(output_stream)

    return output_stream

   
""" convertir year d'un int en lettre arabe
    ex: generate_year(2023) return "ألفان و ثلاثة و عشرون"
"""
def generate_year(year):
    arabic_numbers = {
       2023: "ألفان و ثلاثة و عشرون",
       2024: "ألفان و أربعة و عشرون",
       2025: "ألفان و خمسة و عشرون",
       2026: "ألفان و ستة و عشرون",
       2027: "ألفان و سبعة و عشرون",
       2028: "ألفان و ثمانية و عشرون",
       2029: "ألفان و تسعة و عشرون",
       2030: "ألفان و ثلاثون",
       2031: "ألفان و واحد و ثلاثون",
       2032: "ألفان و اثنان و ثلاثون",
       2033: "ألفان و ثلاثة و ثلاثون",
       2034: "ألفان و اربعة و ثلاثون",
       2035: "ألفان و خمسة و ثلاثون",
       2036: "ألفان و ستة و ثلاثون",
       2037: "ألفان و سبعة و ثلاثون",
       2038: "ألفان و ثمانية و ثلاثون",
       2039: "ألفان و تسعة و ثلاثون",
       2040: "ألفان و أربعون",
       2041: "ألفان و واحد و اربعون",
       2042: "ألفان و اثنان و اربعون",
       2043: "ألفان و ثلاثة و اربعون",
       2044: "ألفان و اربعة و اربعون",
       2045: "ألفان و خمسة و اربعون",
       2046: "ألفان و ستة و اربعون",
       2047: "ألفان و سبعة و اربعون",
       2048: "ألفان و ثمانية و اربعون",
       2049: "ألفان و تسعة و اربعون",
    }
    return arabic_numbers[year]

def generate_unique_filename(original_file_name):
        # Generate a unique file name using a timestamp and UUID
        base_name, ext = os.path.splitext(original_file_name)
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        unique_id = uuid.uuid4().hex
        unique_file_name = f"{base_name}_{timestamp}_{unique_id}{ext}"
        return unique_file_name



    


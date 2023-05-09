from docxtpl import DocxTemplate
import json

with open('data.json', 'r') as f:
  data = json.load(f)

if data['patrocinio'] and data['demandante_ci']:
  if data["fundamentacion"] and data["justificacion"]:
    context = {
      'demandante_name' : data['demandante_name'],
      'ley_infringida' : data['ley_infringida'],
    }
    doc = DocxTemplate("ai_template.docx")
    doc.render(context)
    doc.save(f"ACCEPTED_{context['demandante_name']}_generated_ai.docx")
  else:
    context = {
      'demandante_name' : data['demandante_name'],
      'ley_infringida' : data['ley_infringida'],
    }
    doc = DocxTemplate("ai_rejected_template.docx")
    doc.render(context)
    doc.save(f"REJECTED_{context['demandante_name']}_generated_ai.docx")
else:
  print("No se puede generar el AI, faltan datos")

  
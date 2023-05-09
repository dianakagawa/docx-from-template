from docxtpl import DocxTemplate
import json

with open('data.json', 'r') as f:
  data = json.load(f)

# Function for the accepted Auto Interlocutorio
def accepted_ai():
  context = {'demandante_name' : data['demandante_name'], 'ley_infringida' : data['ley_infringida']}
  doc = DocxTemplate("ai_template.docx")
  doc.render(context)
  doc.save(f"ACCEPTED_{context['demandante_name']}_generated_ai.docx")

# Function for the rejected Auto Interlocutorio
def rejected_ai():
  context = {'demandante_name' : data['demandante_name'], 'ley_infringida' : data['ley_infringida']}
  doc = DocxTemplate("ai_rejected_template.docx")
  doc.render(context)
  doc.save(f"REJECTED_{context['demandante_name']}_generated_ai.docx")

items_false = data['domicilio_real'] == False or data['ley_infringida'] == False or data['articulo_infringido'] == False or data['fundamentacion'] == False or data['justificacion'] == False
def items_not_present():
  if items_false:
    rejected_ai()
  else:
    accepted_ai()

# Check if patrocinio is true, then check if demandante_name and demandante_ci should be present. Else, abogado_name and abogado_matricula should be present.
if data['patrocinio'] == True:
  if data['demandante_name'] == False or data['demandante_ci'] == False:
    print('Error: patrocinio is true but demandante_name or demandante_ci is missing.')
  else: 
    items_not_present()
else:
  if data['abogado_name'] == False or data['abogado_matricula'] == False:
    print('Error: patrocinio is false but abogado_name or abogado_matricula is missing.')
  else:
    items_not_present()
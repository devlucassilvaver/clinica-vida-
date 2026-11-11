from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

file_path = "C:/Users/loren/OneDrive/Área de Trabalho/Anhanguera - Python/PROJETO FINAL/Projeto_Clinica_Vida_Plus_V2.pdf"

styles = getSampleStyleSheet()
story = []

# Capa
story.append(Paragraph("<b>Projeto Integrado – Plataforma de Saúde (Clínica Vida+)</b>", styles["Title"]))
story.append(Spacer(1, 40))
story.append(Paragraph("Aluno: ____________________", styles["Normal"]))
story.append(Paragraph("Curso: ____________________", styles["Normal"]))
story.append(Paragraph("Disciplina: ________________", styles["Normal"]))
story.append(Paragraph("Data: ____/____/20__", styles["Normal"]))
story.append(PageBreak())

# Introdução / Contexto
story.append(Paragraph("<b>1. Introdução / Contexto</b>", styles["Heading2"]))
story.append(Paragraph(
    "A cidade de São Lucas vem crescendo rapidamente, elevando a demanda por serviços de saúde de qualidade. "
    "A clínica Vida+ enfrentava problemas de organização: agendamentos manuais, histórico de pacientes fragmentado, erros em cobranças e relatórios. "
    "Este projeto visa desenvolver uma plataforma simples para sistema de gestão da clínica, facilitando cadastros, histórico, estatísticas e organização interna.",
    styles["BodyText"]))
story.append(Spacer(1, 12))

# Escopo e Requisitos
story.append(Paragraph("<b>2. Escopo e Requisitos do Sistema</b>", styles["Heading2"]))
story.append(Paragraph(
    "<b>Funcionalidades implementadas:</b><br/>"
    "- Cadastro de pacientes (nome, idade, telefone)<br/>"
    "- Listagem de pacientes<br/>"
    "- Busca de paciente por nome<br/>"
    "- Estatísticas básicas: total, idade média, paciente mais novo e mais velho<br/>"
    "- Menu de navegação no terminal<br/>"
    ,
    styles["BodyText"]))
story.append(Spacer(1, 12))
story.append(Paragraph(
    "<b>Funcionalidades não implementadas (limitações):</b><br/>"
    "- Cadastro de médicos<br/>"
    "- Cadastro de exames<br/>"
    "- Agendamento de consultas ou exames<br/>"
    "- Controle de horários disponíveis<br/>"
    "- Registro completo de atendimentos e histórico detalhado<br/>"
    "- Geração de relatórios mensais automatizados<br/>"
    ,
    styles["BodyText"]))
story.append(Spacer(1, 12))

# Organização no Trello
story.append(Paragraph("<b>3. Organização do Projeto (Quadro Trello)</b>", styles["Heading2"]))
story.append(Paragraph(
    "O projeto foi organizado segundo a metodologia ágil, com backlog, sprint atual, tarefas em progresso e concluídas. "
    "Abaixo, insira os prints do quadro Trello com as etiquetas coloridas indicando user stories, tarefas técnicas, testes e documentação.",
    styles["BodyText"]))
story.append(Spacer(1, 200))  # espaço em branco para colar prints
story.append(PageBreak())

# Descrição do Sistema / Código
story.append(Paragraph("<b>4. Sistema em Python — Funcionalidades e Código</b>", styles["Heading2"]))
story.append(Paragraph(
    "O sistema oferece um menu interativo no terminal com opções para cadastrar pacientes, listar pacientes, buscar por nome, "
    "ver estatísticas e sair. O código foi construído com listas e dicionários, tratamento de erros e validações básicas.",
    styles["BodyText"]))
story.append(Spacer(1, 12))
story.append(Paragraph("<i>(O código completo está anexado ou pode ser colado abaixo)</i>", styles["BodyText"]))
story.append(PageBreak())

# Manual de Uso
story.append(Paragraph("<b>5. Guia de Uso</b>", styles["Heading2"]))
story.append(Paragraph(
    "1. Salve o arquivo como, por exemplo, `clinica_vida.py`.<br/>"
    "2. Abra o terminal e execute `python clinica_vida.py`.<br/>"
    "3. Use o menu apresentado para navegar pelas opções.<br/>"
    "4. Para sair do sistema, selecione a opção “Sair”.",
    styles["BodyText"]))
story.append(Spacer(1, 12))

# Limitações e Trabalhos Futuros
story.append(Paragraph("<b>6. Limitações e Possíveis Extensões</b>", styles["Heading2"]))
story.append(Paragraph(
    "- Implementar cadastro de médicos e exames.<br/>"
    "- Permitir agendamento de consultas e exames com controle de horários.<br/>"
    "- Registrar histórico de atendimentos e evolução dos pacientes.<br/>"
    "- Gerar relatórios mensais para administração da clínica.<br/>"
    "- Criar interface gráfica ou web para facilitar uso.",
    styles["BodyText"]))
story.append(Spacer(1, 12))

# Conclusão
story.append(Paragraph("<b>7. Conclusão</b>", styles["Heading2"]))
story.append(Paragraph(
    "Este projeto atendeu aos requisitos essenciais solicitados: cadastro de pacientes, busca, listagem e estatísticas. "
    "Além disso, demonstra uma organização de projeto profissional usando metodologia ágil para planejamento e execução. "
    "O código está estruturado, validado e o relatório está pronto para futuras ampliações.",
    styles["BodyText"]))

SimpleDocTemplate(file_path, pagesize=A4).build(story)

print("PDF V2 gerado em:", file_path)

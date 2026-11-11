# 🏥 Clínica Vida+ — Sistema de Gestão de Pacientes

Sistema desenvolvido em Python como parte de um projeto acadêmico, com o objetivo de facilitar o gerenciamento de pacientes de uma clínica fictícia chamada Vida+.

A aplicação funciona via terminal e permite cadastrar, consultar e listar pacientes, além de apresentar estatísticas básicas sobre os registros.

## 📌 Funcionalidades

- **Cadastro de pacientes:** registro de nome, idade e telefone.
- **Listagem de pacientes:** visualização dos pacientes cadastrados.
- **Busca de pacientes:** pesquisa pelo nome.
- **Estatísticas:** quantidade total de pacientes, idade média, paciente mais novo e mais velho.
- **Validação de dados:** tratamento de entradas inválidas e campos obrigatórios.
- **Menu interativo:** navegação pelas funcionalidades diretamente pelo terminal.

## 🛠️ Tecnologias utilizadas

- **Python 3:** linguagem de programação utilizada no desenvolvimento.
- **ReportLab:** biblioteca utilizada para geração de documentos PDF.
- **Estruturas de dados:** listas e dicionários.
- **Git e GitHub:** controle de versão e hospedagem do código.

## 📂 Estrutura do projeto

```text
clinica-vida-plus/
│
├── clinica_vida.py
├── gerar_relatorio.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── docs/
│   └── documentacao_projeto.pdf
│
└── exercicios/
    └── fila_atendimento.py
```

## ⚙️ Como executar o projeto

### 1. Pré-requisitos

- Python 3 instalado.
- Git instalado.
- Visual Studio Code (opcional).

### 2. Clonar o repositório

```bash
git clone URL_DO_REPOSITORIO
```

Entre na pasta do projeto:

```bash
cd clinica-vida-plus
```

### 3. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 4. Executar o sistema

```bash
python clinica_vida.py
```

## 🖥️ Menu do sistema

Ao executar a aplicação, será apresentado o seguinte menu:

```text
======================================
      SISTEMA CLÍNICA VIDA+
======================================
1. Cadastrar paciente
2. Ver estatísticas
3. Buscar paciente
4. Listar todos os pacientes
5. Sair
======================================
```

O usuário pode selecionar a opção desejada e interagir com o sistema pelo terminal.

## 📊 Estrutura de dados e lógica

O sistema utiliza listas e dicionários para armazenar e organizar os dados dos pacientes durante a execução.

Também são utilizadas funções para separar as responsabilidades de cada funcionalidade, facilitando a organização e manutenção do código.

O exercício complementar de fila de atendimento demonstra o conceito FIFO (*First In, First Out*), no qual o primeiro paciente a entrar na fila é o primeiro a ser atendido.

## ⚠️ Limitações e melhorias futuras

O projeto possui funcionalidades básicas de gerenciamento de pacientes. Algumas possibilidades de evolução são:

- Implementar cadastro de médicos e exames.
- Desenvolver um módulo de agendamento de consultas.
- Implementar persistência de dados utilizando banco de dados.
- Criar histórico de atendimentos dos pacientes.
- Desenvolver relatórios administrativos automatizados.
- Criar uma interface gráfica ou aplicação web.

## 📄 Documentação

A documentação acadêmica completa do projeto está disponível na pasta `docs/`, contendo contexto, escopo, requisitos, funcionalidades, limitações e conclusão.

## 🎯 Objetivo acadêmico

Este projeto foi desenvolvido como atividade acadêmica do curso de Análise e Desenvolvimento de Sistemas (ADS), com o propósito de aplicar conceitos fundamentais de lógica de programação, estruturas de dados, modularização e desenvolvimento de aplicações em Python.

---

**Desenvolvido como projeto acadêmico — Clínica Vida+**
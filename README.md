
# 🤖 Chatbot - Pizzaria Tech

## 📄 Descrição do Projeto
Este projeto é um **Chatbot de Atendimento para uma Pizzaria**, desenvolvido 100% em Python puro, sem uso de frameworks ou bibliotecas externas. O sistema simula um atendimento básico, com funcionalidades como:

- Realizar pedidos de pizza
- Consultar perguntas frequentes (FAQ)
- Gerar registros dos atendimentos e dos pedidos
- Armazenar logs das conversas

O objetivo é aplicar conceitos de programação estruturada, manipulação de arquivos e organização de código.

## 👨‍🏫 Informações Acadêmicas
- **Disciplina:** Programação em Python
- **Professor:** Jeofton
- **Alunos:** 
  - Izaiais Terto
  - Pedro Michael
  - José Felipe

## 🗂️ Estrutura de Pastas
```
chatbot/
├── dados/
│   ├── faq.txt           # Base de perguntas frequentes
│   ├── logs.txt          # Logs das conversas realizadas
│   └── registros.txt     # Histórico dos pedidos feitos
├── main.py               # Arquivo principal do sistema
├── chatbot.py            # Controle do fluxo do chatbot
├── database.py           # Controle de dados e persistência
├── utils.py              # Funções auxiliares (limpar tela, datas, formatação)
└── README.md             # Documentação do projeto
```

## 🚀 Funcionalidades

- 💬 **Iniciar Atendimento:**  
  - Permite que o usuário faça pedidos de pizza ou consulte perguntas frequentes.

- 🍕 **Fazer Pedido:**  
  - O cliente escolhe um sabor de pizza e o pedido é registrado com nome e horário.

- ❓ **FAQ - Perguntas Frequentes:**  
  - Responde perguntas previamente cadastradas no arquivo `faq.txt`.

- 📄 **Sobre a Empresa:**  
  - Exibe informações gerais da pizzaria.

- 📝 **Logs e Registros:**  
  - Todos os atendimentos e pedidos são salvos nos arquivos `logs.txt` e `registros.txt`.

## 🔧 Como Executar

1. **Pré-requisitos:**  
   - Ter Python instalado na máquina (versão 3 ou superior).

2. **Executar o sistema:**  
   - Navegue até a pasta do projeto no terminal.
   - Execute o comando:
   ```bash
   python main.py
   ```

## 🗃️ Dados Placeholder
O sistema já acompanha alguns dados simulados, como:

- FAQ pré-cadastrado com perguntas comuns.
- Logs e registros de exemplos de atendimentos anteriores.

## 💻 Divisão das Tarefas

| Integrante      | Responsável por                                  |
|-----------------|---------------------------------------------------|
| Izaiais Terto   | Estrutura dos arquivos, manipulação de dados     |
| Pedro Michael   | Desenvolvimento do chatbot e regras de atendimento|
| José Felipe     | Implementação de utilitários e sistema principal |

## 🏁 Conclusão
Este projeto foi desenvolvido com o objetivo de consolidar os conhecimentos adquiridos na disciplina, aplicando lógica de programação, modularização e persistência de dados em arquivos texto, sem o uso de frameworks externos.
